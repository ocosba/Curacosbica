# -*- coding: utf-8 -*-
"""
Bot do Sincronário — Cosba
Transporte e comandos. Toda a leitura vem de tzolkin/mensagens.py.

COMANDOS PÚBLICOS (4)
  /hoje /ontem /amanha        → Kin do dia, leitura completa
  /kin DD/MM/AAAA [Nome]      → assinatura galáctica de uma data de nascimento
  /parar                      → cancela o envio automático
  /ajuda

COMANDO PRIVADO (só ADMIN_CHAT_ID)
  /estudo [DD/MM/AAAA]        → a aula diária, profundidade total
  /disparo                    → força o envio para os inscritos

SEGURANÇA
  - Token só por variável de ambiente. Sem fallback: sem token, não sobe.
  - /disparo e /estudo exigem ADMIN_CHAT_ID. Antes, qualquer pessoa que
    descobrisse o bot podia disparar mensagem para a lista inteira.
  - Inscritos persistem em TELEGRAM_SUBSCRIBERS (ambiente) + arquivo local.
    Em nuvem com disco efêmero, o ambiente é a fonte que sobrevive ao deploy.
"""

import datetime
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import http.server
import socketserver

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tzolkin import mensagens, core

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BRT = datetime.timezone(datetime.timedelta(hours=-3))
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'telegram_config.json')
HORA_DISPARO = int(os.environ.get('DISPATCH_HOUR', '6'))
MINUTO_DISPARO = int(os.environ.get('DISPATCH_MINUTE', '0'))
KIN_NATAL_LEO = int(os.environ.get('KIN_NATAL', '194'))

RE_DATA = re.compile(r'(\d{1,2})[/\-.](\d{1,2})[/\-.](\d{4})')

# ==========================================================
# VERSÃO — para saber qual código está no ar sem ter que adivinhar
# ==========================================================
# Em 04/09/2026 o disparo das 6h chegou no formato antigo enquanto o GitHub já
# tinha o novo há cinco commits, e a única forma de descobrir isso foi comparar
# o texto da mensagem com o histórico do git. Não de novo.
#
# VERSAO_TEXTO sobe à mão quando a FORMA da leitura muda. O commit vem sozinho.
# Os dois aparecem no /ajuda, no health check e no log de boot.
VERSAO_TEXTO = '2.1'


def commit_no_ar() -> str:
    """Hash curto do commit que está rodando, ou de onde der para descobrir."""
    c = (os.environ.get('RENDER_GIT_COMMIT')
         or os.environ.get('SOURCE_COMMIT')
         or os.environ.get('HEROKU_SLUG_COMMIT')
         or '').strip()
    if not c:
        # Local: lê direto do .git, sem depender do git estar no PATH.
        try:
            raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            with open(os.path.join(raiz, '.git', 'HEAD'), encoding='utf-8') as f:
                head = f.read().strip()
            if head.startswith('ref: '):
                with open(os.path.join(raiz, '.git', head[5:]), encoding='utf-8') as f:
                    c = f.read().strip()
            else:
                c = head
        except Exception:
            return 'desconhecido'
    return c[:7]


def versao() -> str:
    return f'v{VERSAO_TEXTO} · {commit_no_ar()}'


def agora_brt():
    return datetime.datetime.now(BRT)


# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

def carrega_env():
    """Lê o .env da raiz do projeto. Variável de ambiente real sempre tem prioridade,
    para a nuvem (Render) não ser sobrescrita por um .env que subiu sem querer."""
    caminho = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    if not os.path.exists(caminho):
        return
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if not linha or linha.startswith('#') or '=' not in linha:
                    continue
                chave, valor = linha.split('=', 1)
                chave, valor = chave.strip(), valor.strip().strip('"').strip("'")
                if chave and valor and chave not in os.environ:
                    os.environ[chave] = valor
    except Exception as e:
        print(f'[AVISO] não consegui ler o .env: {e}', flush=True)


def carrega_token() -> str:
    token = os.environ.get('TELEGRAM_BOT_TOKEN', '').strip()
    if not token:
        print('\n[ERRO] TELEGRAM_BOT_TOKEN não está definido.\n'
              '  O bot não sobe sem ele — de propósito. Token nunca fica no código.\n'
              '  Local: coloque TELEGRAM_BOT_TOKEN=... no arquivo .env\n'
              '  Nuvem: defina a variável de ambiente no painel do serviço.\n', flush=True)
        sys.exit(1)
    return token


def admin_id() -> str:
    return os.environ.get('ADMIN_CHAT_ID', '').strip()


def eh_admin(chat_id) -> bool:
    a = admin_id()
    return bool(a) and str(chat_id).strip() == a


def carrega_inscritos() -> list:
    inscritos = []
    do_ambiente = os.environ.get('TELEGRAM_SUBSCRIBERS', '').strip()
    if do_ambiente:
        inscritos = [s.strip() for s in do_ambiente.split(',') if s.strip()]
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                for s in json.load(f).get('subscribers', []):
                    s = str(s).strip()
                    if s and s not in inscritos:
                        inscritos.append(s)
        except Exception as e:
            print(f'[AVISO] não consegui ler {CONFIG_FILE}: {e}', flush=True)
    return inscritos


def salva_inscritos(inscritos: list):
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump({'subscribers': inscritos}, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f'[AVISO] não consegui salvar inscritos: {e}', flush=True)


# ==========================================================
# TELEGRAM
# ==========================================================

def _quebra(texto: str, limite: int = 4000) -> list:
    """Quebra entre SEÇÕES, nunca no meio de uma.

    Toda seção começa com um parágrafo em negrito (`*O SEU RITMO*`, `*5. ...*`).
    Agrupar por esse marcador antes de empacotar evita o que acontecia antes:
    a mensagem racharded no meio do decreto ou no meio da bússola.

    Só desce para o corte por parágrafo quando uma seção sozinha já passa do
    limite — aí não há junta melhor disponível.
    """
    if len(texto) <= limite:
        return [texto]

    # 1. parágrafos → seções
    secoes = []
    for parte in texto.split('\n\n'):
        if parte.lstrip().startswith('*') or not secoes:
            secoes.append(parte)
        else:
            secoes[-1] += '\n\n' + parte

    # 2. seções → blocos
    blocos, atual = [], ''
    for secao in secoes:
        candidato = (atual + '\n\n' + secao) if atual else secao
        if len(candidato) <= limite:
            atual = candidato
            continue
        if atual:
            blocos.append(atual)
            atual = ''
        if len(secao) <= limite:
            atual = secao
            continue
        # seção maior que o limite: não há junta boa, corta por parágrafo
        for paragrafo in secao.split('\n\n'):
            cand = (atual + '\n\n' + paragrafo) if atual else paragrafo
            if len(cand) > limite and atual:
                blocos.append(atual)
                atual = paragrafo
            else:
                atual = cand
    if atual:
        blocos.append(atual)
    return blocos


def envia(token: str, chat_id: str, texto, tentativas: int = 3, formatado: bool = False):
    """`texto` pode ser uma string ou uma lista de peças (ver mensagens.mapa_pessoal).

    `formatado=False` é o padrão porque as leituras existem para serem copiadas
    daqui e coladas no WhatsApp. Se o Telegram renderizar o Markdown, o texto
    copiado chega no WhatsApp sem os asteriscos e sem negrito nenhum. Mandando
    cru, o que você vê é exatamente o que o WhatsApp vai renderizar.

    `formatado=True` só para o que se lê dentro do próprio Telegram: /ajuda,
    avisos do bot e a aula do Leo.
    """
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    pecas = texto if isinstance(texto, list) else [texto]
    blocos = [b for p in pecas for b in _quebra(p)]
    for bloco in blocos:
        for tentativa in range(tentativas):
            payload = {'chat_id': chat_id, 'text': bloco}
            if formatado:
                payload['parse_mode'] = 'Markdown'
            req = urllib.request.Request(
                url, data=urllib.parse.urlencode(payload).encode('utf-8'))
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    json.loads(r.read().decode('utf-8'))
                break
            except urllib.error.HTTPError as e:
                corpo = e.read().decode('utf-8', errors='replace')
                if e.code == 429:
                    espera = 2 ** tentativa
                    print(f'[AVISO] limite do Telegram, aguardando {espera}s', flush=True)
                    time.sleep(espera)
                    continue
                # Markdown quebrado: reenvia sem formatação em vez de perder a mensagem
                print(f'[AVISO] Telegram {e.code}: {corpo[:200]} — reenviando sem formatação',
                      flush=True)
                req2 = urllib.request.Request(
                    url, data=urllib.parse.urlencode(
                        {'chat_id': chat_id, 'text': bloco}).encode('utf-8'))
                try:
                    with urllib.request.urlopen(req2, timeout=30):
                        pass
                except Exception as e2:
                    print(f'[ERRO] falhou de vez para {chat_id}: {e2}', flush=True)
                break
            except Exception as e:
                print(f'[ERRO] envio para {chat_id}: {e}', flush=True)
                break
        time.sleep(0.4)


def busca_updates(token: str, offset=None):
    url = f'https://api.telegram.org/bot{token}/getUpdates?timeout=20'
    if offset:
        url += f'&offset={offset}'
    try:
        with urllib.request.urlopen(urllib.request.Request(url), timeout=30) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f'[AVISO] getUpdates: {e}', flush=True)
        return {'ok': False, 'result': []}


# ==========================================================
# COMANDOS
# ==========================================================

AJUDA = f"""📖 *SINCRONÁRIO GALÁCTICO*

O calendário maia de 260 dias, em português claro. Cada dia é um Kin: um arquétipo cruzado com um ritmo. São 20 arquétipos e 13 ritmos — a conta fecha em 260 dias, que depois recomeçam.

*O DIA*
*/hoje* — a leitura completa de hoje
*/ontem* — a de ontem
*/amanha* — a de amanhã

*O SEU MAPA*
Me manda a sua *data de nascimento*, só isso, sem comando nenhum:
_04/09/2003_

Com nome, se quiser que eu chame você por ele:
*/kin* _04/09/2003 Stephanie_

O mapa chega em duas partes: *quem você é* e *a sua rota* — o ano que você está vivendo, o corpo e por onde ir.

*O RESTO*
*/parar* — cancela o envio das manhãs
*/ajuda* — esta mensagem

⏰ O Kin do dia chega toda manhã às {HORA_DISPARO:02d}:{MINUTO_DISPARO:02d}.

Uma coisa que costuma estranhar: as leituras chegam com os asteriscos à mostra, de propósito. É assim que você copia daqui e cola no WhatsApp já com o negrito certo.

✨ *Leonardo Cosba*
_Terapeuta multidimensional_
📲 @o.cosba · instagram.com/o.cosba

Se alguma leitura bater com o seu momento, me conta.

_{versao()}_"""

BOAS_VINDAS = """✨ *Bem-vindo ao Sincronário Galáctico!*

Toda manhã chega aqui a leitura do dia pelo calendário maia de 260 dias — com os termos explicados, sem precisar saber nada antes.

Quer o seu mapa? Me manda a sua *data de nascimento* (assim: _04/09/2003_).
*/ajuda* mostra o resto.

Segue a leitura de hoje 👇"""


def le_data_e_nome(texto: str):
    m = RE_DATA.search(texto)
    if not m:
        return None, None
    try:
        d = datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    except ValueError:
        return None, None
    nome = (texto[:m.start()] + texto[m.end():]).strip() or 'Você'
    return d, nome


def dispara_diario(token: str, inscritos: list, dia: datetime.date):
    print(f'\n📢 Disparo do Kin {core.calculate_kin(dia):03d} '
          f'({dia:%d/%m/%Y}) para {len(inscritos)} inscritos', flush=True)
    texto = mensagens.kin_do_dia(dia)
    entregues = 0
    for chat_id in inscritos:
        try:
            envia(token, chat_id, texto)
            entregues += 1
        except Exception as e:
            print(f'   ✗ {chat_id}: {e}', flush=True)
        time.sleep(0.6)
    print(f'📢 Entregues {entregues}/{len(inscritos)}\n', flush=True)
    return entregues


def processa(token: str, chat_id: str, texto: str, nome_usuario: str = ''):
    hoje = agora_brt().date()
    partes = texto.strip().split()
    if not partes:
        return
    cmd = partes[0].lower().split('@')[0]
    args = ' '.join(partes[1:])
    chat_id = str(chat_id).strip()

    inscritos = carrega_inscritos()
    if chat_id not in inscritos:
        inscritos.append(chat_id)
        salva_inscritos(inscritos)
        print(f'Novo inscrito: {chat_id} ({nome_usuario})', flush=True)

    if cmd in ('/start', '/inicio'):
        envia(token, chat_id, BOAS_VINDAS, formatado=True)
        envia(token, chat_id, mensagens.kin_do_dia(hoje))

    elif cmd in ('/hoje', 'hoje'):
        envia(token, chat_id, mensagens.kin_do_dia(hoje))

    elif cmd in ('/ontem', 'ontem'):
        envia(token, chat_id, mensagens.kin_do_dia(
            hoje - datetime.timedelta(days=1), rotulo='KIN DE ONTEM'))

    elif cmd in ('/amanha', 'amanhã', 'amanha'):
        envia(token, chat_id, mensagens.kin_do_dia(
            hoje + datetime.timedelta(days=1), rotulo='KIN DE AMANHÃ'))

    elif cmd in ('/kin', '/mapa', '/calcular'):
        d, nome = le_data_e_nome(args)
        if d:
            envia(token, chat_id, mensagens.mapa_pessoal(d, nome, hoje))
        else:
            envia(token, chat_id,
                  '⚠️ Não consegui ler essa data. Me manda assim:\n'
                  '*/kin 04/09/2003 Stephanie*\n\n'
                  'Ou só a data, sem comando nenhum: _04/09/2003_', formatado=True)

    elif cmd in ('/parar', '/desinscrever', '/cancelar'):
        if chat_id in inscritos:
            inscritos.remove(chat_id)
            salva_inscritos(inscritos)
        envia(token, chat_id,
              '🔕 Envio automático cancelado. Você ainda pode pedir */hoje* quando quiser, '
              'e mandar uma data de nascimento a hora que for.', formatado=True)

    elif cmd in ('/estudo', '/aula'):
        if not eh_admin(chat_id):
            envia(token, chat_id, 'Esse comando é privado. Digite */ajuda* para ver o que tem.',
                  formatado=True)
            return
        d, _ = le_data_e_nome(args)
        envia(token, chat_id, mensagens.aula_diaria(d or hoje, kin_natal=KIN_NATAL_LEO),
              formatado=True)

    elif cmd in ('/disparo', '/broadcast'):
        if not eh_admin(chat_id):
            envia(token, chat_id, 'Esse comando é privado. Digite */ajuda* para ver o que tem.',
                  formatado=True)
            return
        envia(token, chat_id, '⏳ Disparando...')
        n = dispara_diario(token, inscritos, hoje)
        envia(token, chat_id, f'✅ Entregue para {n} de {len(inscritos)}.')

    elif cmd in ('/ajuda', '/help', 'ajuda'):
        envia(token, chat_id, AJUDA, formatado=True)

    else:
        # Data solta, sem comando: trata como pedido de mapa. É o caminho natural
        # de quem chegou pelo grupo e mandou a data de nascimento.
        d, nome = le_data_e_nome(texto)
        if d:
            envia(token, chat_id, mensagens.mapa_pessoal(d, nome, hoje))
        else:
            envia(token, chat_id,
                  'Não entendi 😊\n\n'
                  '• */hoje* — a leitura do dia\n'
                  '• uma *data de nascimento* (_04/09/2003_) — o mapa dessa pessoa\n'
                  '• */ajuda* — tudo que dá pra fazer aqui', formatado=True)


# ==========================================================
# AGENDADOR E SAÚDE
# ==========================================================

def agendador(token: str):
    ultimo = None
    print(f'⏰ Agendador ativo para {HORA_DISPARO:02d}:{MINUTO_DISPARO:02d} BRT', flush=True)
    while True:
        try:
            agora = agora_brt()
            hoje = agora.date()
            # Recuperação: se o processo subiu depois da hora e ainda não disparou
            # hoje, dispara assim mesmo. Antes, um restart às 07:05 pulava o dia.
            passou_da_hora = (agora.hour > HORA_DISPARO or
                              (agora.hour == HORA_DISPARO and agora.minute >= MINUTO_DISPARO))
            if passou_da_hora and ultimo != hoje:
                inscritos = carrega_inscritos()
                if inscritos:
                    dispara_diario(token, inscritos, hoje)
                ultimo = hoje
            time.sleep(30)
        except Exception as e:
            print(f'[AVISO] agendador: {e}', flush=True)
            time.sleep(60)


class Saude(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        hoje = agora_brt().date()
        corpo = json.dumps({
            'status': 'online',
            'servico': 'Sincronario Cosba',
            # Estes dois dizem QUAL codigo esta no ar. Basta abrir a URL do
            # servico no navegador para saber, sem esperar o disparo das 6h.
            'versao_texto': VERSAO_TEXTO,
            'commit': commit_no_ar(),
            'hoje': hoje.strftime('%d/%m/%Y'),
            'kin': core.calculate_kin(hoje),
            'disparo': f'{HORA_DISPARO:02d}:{MINUTO_DISPARO:02d} BRT',
            'inscritos': len(carrega_inscritos()),
        }, ensure_ascii=False, indent=2).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def log_message(self, *a):
        pass


def servidor_saude(porta: int):
    try:
        class Reusa(socketserver.TCPServer):
            allow_reuse_address = True
        print(f'🌐 Health check na porta {porta}', flush=True)
        Reusa(('', porta), Saude).serve_forever()
    except Exception as e:
        print(f'[AVISO] health check: {e}', flush=True)


# ==========================================================
# MAIN
# ==========================================================

def main():
    carrega_env()
    token = carrega_token()
    inscritos = carrega_inscritos()

    print('=' * 56, flush=True)
    print('🌀 SINCRONÁRIO CÓSBICO', flush=True)
    print(f'   Versão: {versao()}', flush=True)
    print(f'   Inscritos: {len(inscritos)}', flush=True)
    print(f'   Admin: {"configurado" if admin_id() else "NÃO CONFIGURADO — /estudo e /disparo bloqueados"}',
          flush=True)
    hoje = agora_brt().date()
    print(f'   Hoje: Kin {core.calculate_kin(hoje):03d} — {core.nome_do_kin(core.calculate_kin(hoje))}',
          flush=True)
    print('=' * 56, flush=True)

    threading.Thread(target=agendador, args=(token,), daemon=True).start()

    porta = os.environ.get('PORT')
    if porta:
        threading.Thread(target=servidor_saude, args=(int(porta),), daemon=True).start()

    offset = None
    print('🤖 Ouvindo...', flush=True)
    while True:
        try:
            updates = busca_updates(token, offset)
            for u in updates.get('result', []):
                offset = u['update_id'] + 1
                msg = u.get('message', {})
                chat = msg.get('chat', {})
                if chat.get('id') and msg.get('text'):
                    print(f'📩 {chat.get("first_name", "?")}: {msg["text"][:60]}', flush=True)
                    try:
                        processa(token, str(chat['id']), msg['text'], chat.get('first_name', ''))
                    except Exception as e:
                        print(f'[ERRO] ao processar: {e}', flush=True)
            time.sleep(1)
        except KeyboardInterrupt:
            print('\nEncerrando.', flush=True)
            break
        except Exception as e:
            print(f'[AVISO] laço principal: {e}', flush=True)
            time.sleep(3)


if __name__ == '__main__':
    main()
