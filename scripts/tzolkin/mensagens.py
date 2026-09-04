# -*- coding: utf-8 -*-
"""
As três leituras.

Correção de rumo de 03/09/2026 (segunda rodada): a versão anterior virou aula
sobre o sistema em vez de leitura sobre a pessoa. Cortado daqui:

  - "a atualização de 2010 do sistema, em que cada Selo encarna uma figura..."
  - "O Tom é o ritmo. São 13, e o seu diz como você opera."
  - "Os 20 Selos se agrupam de 5 em 5 nas Famílias Terrestres..."
  - a lista dos 13 degraus com nome e Kin, que era longa e não dizia nada

Princípio que ficou: **se o título já explica, não repita embaixo.** O termo
aparece como aposto curto dentro da própria frase, e a pessoa entende pelo
contexto. Quem quiser a teoria vai atrás por conta.

Formatação enxuta para WhatsApp: poucas divisórias, sem saltos duplos de
parágrafo. Alvo — Kin do dia ~2.500 e mapa ~6.000 caracteres.
"""

import datetime

from . import ano as mod_ano
from . import core
from . import textos as T
from . import textos_mapa as M
from . import textos_oraculo as O
from .textos_profundos import PROFUNDO, TONS_PROFUNDO, TOTENS

LINHA = '━━━━━━━━━━━━━━━'

# Marca curta de um ano futuro. Só aparece quando diz algo: ano sem relação
# com o mapa natal não recebe rótulo nenhum, em vez de "de território novo".
ROTULO_CURTO = {
    'destino': '👑 seu Retorno Galáctico',
    'guia': '🧭 ano da sua bússola',
    'analogo': '🤝 ano de apoio',
    'antipoda': '🛡️ ano de desafio',
    'oculto': '💎 ano do dom escondido',
    'quinta': '👑 ano de síntese',
    'selo_guia': '🧭 no selo da sua bússola',
    'selo_analogo': '🤝 no selo do seu aliado',
    'selo_antipoda': '🛡️ no selo do seu treino',
    'selo_oculto': '💎 no selo do seu dom escondido',
    'selo_quinta': '👑 no selo da sua síntese',
    'mesmo_selo': '🔁 seu arquétipo volta',
    'mesmo_tom': '🎵 seu ritmo volta',
    None: None,
}

# Quando o ano cai numa das forças do mapa, o oráculo já descreveu esse
# arquétipo alguns parágrafos acima. Em vez de repetir a armadilha como se
# fosse notícia, o texto nomeia o encontro — que é o que torna o ano especial.
FORCA_DO_ANO = {
    'guia': 'da sua *Bússola de Decisão*', 'selo_guia': 'da sua *Bússola de Decisão*',
    'analogo': 'do seu *Aliado Natural*', 'selo_analogo': 'do seu *Aliado Natural*',
    'antipoda': 'do seu *Mestre de Atrito*', 'selo_antipoda': 'do seu *Mestre de Atrito*',
    'oculto': 'do seu *Tesouro Secreto*', 'selo_oculto': 'do seu *Tesouro Secreto*',
    'quinta': 'do seu *Vórtice Integrador*', 'selo_quinta': 'do seu *Vórtice Integrador*',
}


def _limpa(texto: str) -> str:
    if texto.count('*') % 2:
        texto = texto.replace('*', '')
    if texto.count('_') % 2:
        texto = texto.replace('_', '')
    return texto


def _mai(t: str) -> str:
    return t[:1].upper() + t[1:] if t else t


def _marcos(kd: dict, natal: bool = False) -> str:
    linhas = []
    # Os 260 dias se dividem em 52 portais e 208 dias comuns. As duas metades
    # ganham a mesma régua: uma linha, sem afirmar nada sobre o corpo de quem
    # lê. "Sensível" e "estável" são tendências do campo, não diagnóstico.
    if kd['is_pag']:
        linhas.append('🌀 ' + ('*Você nasceu num Portal de Ativação Galáctica* — '
                               if natal else '*Hoje é Portal de Ativação Galáctica* — ')
                      + 'um dos 52 dias em que a matriz abre. Campo mais sensível: '
                        'coincidência e intensidade aparecem mais.')
    elif natal:
        linhas.append('🌀 *Fora dos portais* — você nasceu num dos 208 dias de '
                      'frequência mais estável. Menos intensidade de campo, mais constância.')
    if kd['is_ponto_zero']:
        linhas.append('✨ *Ponto zero* — o centro exato do tabuleiro de 260 dias.')
    elif kd['is_coluna_mistica']:
        linhas.append('🌌 ' + ('*Você nasceu na Coluna Mística* — ' if natal
                               else '*Coluna Mística* — ')
                      + 'a coluna central do tabuleiro. Território de silêncio e canal aberto.')
    return '\n'.join(linhas)


def _atemporal(texto: str) -> str:
    """As 20 mensagens de antípoda foram escritas para a aula diária e dizem
    'o treino de hoje é'. No mapa de nascimento isso é uma força de vida
    inteira, não uma tarefa do dia."""
    return texto.replace('o treino de hoje é', 'o treino de uma vida é')


def _bussola(kin: int, natal: bool = False) -> str:
    """As 5 forças em dois níveis.

    Gramática fixa do texto, decidida em 03/09/2026: a linha em _itálico_ diz o
    que o arquétipo é para qualquer pessoa; a linha seguinte diz o que ele faz
    na vida de quem está lendo. Quem acompanha aprende o alfabeto dos 20 selos
    lendo o próprio mapa, e fica claro que a leitura sai de um sistema — não de
    um palpite sobre a vida de alguém que eu nunca vi.

    Um selo só é apresentado uma vez por bússola: se a Quinta Força repete um
    selo que já apareceu, ela entra direto na leitura.

    No mapa (natal=True) cada força fecha com o ⚡: a mesma posição calibrada
    pelo TOM daquele kin. É o que separa dois mapas do mesmo selo — o selo das
    cinco forças é idêntico para todo mundo que nasce sob ele, mas o tom não:
    guia, análogo e antípoda carregam o tom natal, o oculto carrega 14 - t e a
    quinta tem tom próprio. Sem esta linha, duas pessoas do mesmo selo leem
    cinco parágrafos iguais.
    """
    o = core.oracle(kin)
    linhas, ja_vistos = [], set()
    for chave, campo, msg in (('guia', 'guia', 'guia_msg'),
                              ('analogo', 'apoio', 'analogo_msg'),
                              ('antipoda', 'desafio', 'antipoda_msg'),
                              ('oculto', 'oculto', 'oculto_msg')):
        k = o[chave]
        s = core.seal_of(k)
        emoji, nome, _ = M.ORACULO_NOMES[chave]
        pag = ' 🌀' if k in core.PAGS else ''
        ja_vistos.add(s)
        # No mapa a força é permanente, não a energia de um dia: entra também a
        # camada profunda, que diz o que o arquétipo faz na vida inteira.
        fundo = f"\n↳ {_atemporal(PROFUNDO[s][msg])}" if natal else ''
        tom = f"\n⚡ {O.TOM_NA_FORCA[chave][core.tone_of(k)]}" if natal else ''
        linhas.append(f"{emoji} *{nome}* — {core.nome_do_kin(k)}{pag}\n"
                      f"_{O.ONDA_NARRATIVA[s][0]}_\n"
                      f"{O.ORACULO[s][campo]}{fundo}{tom}")
    k = o['quinta']
    s_q = core.seal_of(k)
    arquetipo = '' if s_q in ja_vistos else f"_{O.ONDA_NARRATIVA[s_q][0]}_\n"
    fundo_q = f"\n↳ {_atemporal(PROFUNDO[s_q]['quinta_msg'])}" if natal else ''
    tom_q = f"\n⚡ {O.TOM_NA_FORCA['quinta'][core.tone_of(k)]}" if natal else ''
    linhas.append(f"👑 *O Vórtice Integrador* — {core.nome_do_kin(k)}\n"
                  f"{arquetipo}"
                  f"A soma das cinco forças ativa {M.SUPERPODER[s_q][0].lower()}.{fundo_q}{tom_q}")
    return '\n\n'.join(linhas)


def _corpo(kd: dict, natal: bool = False) -> str:
    """No mapa o corpo é retrato de vida inteira; no dia é bilhete.

    Medido em 04/09/2026, em 60 dias seguidos: o bloco do diário tinha só 5
    textos distintos, porque CORPO_FAMILIA é indexada pela família terrestre —
    (selo - 1) % 5 — e o selo anda de 1 em 1 por dia. Voltava idêntico a cada
    5 dias, 73 vezes por ano, ocupando 17% da mensagem. Pior: os sintomas são
    escritos como padrão de vida ("o cansaço que o sono não resolve"), que é
    registro de mapa, não de dia — o bloco do mapa tinha sido reaproveitado.

    No diário sobram duas linhas: a região, que é fato do dia e repete com
    razão, e uma prática regida pelo TOM. Região gira em 5, tom em 13: o bloco
    só se repete inteiro a cada 65 dias.
    """
    regiao, orgaos, sintomas, higiene = M.CORPO_FAMILIA[kd['familia']['nome']]
    if not natal:
        return (f"Hoje a energia pega no *{regiao}* — {orgaos}.\n"
                f"🧘 {T.CORPO_DO_TOM[kd['tom_num']]}")
    return (f"A sua energia ancora no *{regiao}* — {orgaos}.\n\n"
            'Quando você segura o que precisa sair, é aqui que aperta:\n'
            + '\n'.join(f'• {s}' for s in sintomas)
            + f"\n\n🧘 {higiene}")


# ==========================================================
# ESTRUTURA A — KIN DO DIA
# ==========================================================

def kin_do_dia(data: datetime.date = None, rotulo: str = 'KIN DO DIA') -> str:
    kd = core.kin_do_dia(data or datetime.date.today())
    d = kd['data']
    s_num, t_num = kd['selo_num'], kd['tom_num']
    ac = T.ACESSIVEL[s_num]
    onda = kd['onda']
    degrau = onda['degrau']
    lua = kd['lua']

    marcos = _marcos(kd)
    bloco_marcos = f'\n{marcos}\n' if marcos else ''
    rotulo_pulsar, texto_pulsar = T.PULSAR_DIA[kd['pulsar']['num']]
    peso = T.TONS_ACESSIVEL[t_num]['peso']
    linha_peso = f'\n⚡ {peso}' if peso else ''

    msg = f"""☀️ *{rotulo} — {d:%d/%m/%Y}*
*KIN {kd['kin']:03d} — {kd['nome'].upper()}*
🏛️ {kd['arquetipo']['nome']} | 🌙 {lua['lua']}, dia {lua['dia_da_lua']}/28
⚡ *{rotulo_pulsar}* — {texto_pulsar}

*{ac['frase']}*
{bloco_marcos}
☀️ *A ENERGIA DE HOJE*
*{core.SELO_NOME_COMPLETO[s_num]}* ({kd['selo']['maia']})
_{O.ONDA_NARRATIVA[s_num][0]}_
{PROFUNDO[s_num]['descricao']} — o poder de {kd['selo']['acao']}, a essência de {kd['selo']['essencia']}. É a força que rege o dia inteiro.

⚡ *Tom {t_num}, {core.nome_do_tom(t_num, s_num)}*
_{TONS_PROFUNDO[t_num]}_
Na prática: o dia que {T.TOM_FRASE[t_num]}. {T.TONS_ACESSIVEL[t_num]['ritmo']}{linha_peso}

🟢 *Flui:* {ac['flui']}
🔴 *Trava — {M.ARMADILHA[s_num][0]}:* {ac['trava']}

🗺️ *AS 5 FORÇAS DE HOJE*

{_bussola(kd['kin'])}

🌊 *A ONDA — DIA {degrau} DE 13*
Onda {onda['artigo']} {onda['nome']}
_{O.ONDA_NARRATIVA[core.seal_of(onda['inicio'])][0]}_
Hoje é o degrau {degrau}: *{T.DEGRAUS[degrau][0]}*. {T.DEGRAUS[degrau][1]}

🫀 *O CORPO HOJE*
{_corpo(kd)}

👉 *A AÇÃO DE HOJE:* {_mai(ac['acao'])}.
🪞 *Para se perguntar:* _{kd['tom'][5]}_

📩 Se bateu com o seu momento, me conta. E se quiser o seu mapa, manda a sua data de nascimento.

✨ {T.ASSINATURA}"""
    return _limpa(msg)


# ==========================================================
# ESTRUTURA C — O CICLO ANUAL
# ==========================================================

def bloco_do_ano(nascimento: datetime.date, hoje: datetime.date = None) -> str:
    c = mod_ano.ciclo_anual(nascimento, hoje, adiante=2)
    atual = c['anos'][0]
    kd = atual['dados']
    s_num = kd['selo_num']
    titulo, texto = mod_ano.LEITURA_DA_RELACAO[atual['relacao']]
    quad_nome, quad_corte, quad_ini, quad_fim, _ = c['quadrante']

    # A virada do ano galáctico acontece no aniversário, não em 1º de janeiro.
    # Quando ela está perto, é a informação mais acionável da leitura inteira:
    # a pessoa está fechando um ciclo de 365 dias e não sabe disso.
    prox = c['anos'][1]
    dias_para_virar = (prox['inicio'] - (hoje or datetime.date.today())).days
    if 0 <= dias_para_virar <= 30:
        quando = ('*amanhã*' if dias_para_virar == 1
                  else '*hoje*' if dias_para_virar == 0
                  else f"em *{dias_para_virar} dias*")
        aviso = ('\n⏳ *Você está fechando esse ciclo.* '
                 f"O seu ano galáctico vira {quando} ({prox['inicio']:%d/%m}), quando você "
                 f"entra no Kin {prox['kin']:03d}, {prox['dados']['nome']}. "
                 'O que não for encerrado agora atravessa junto.\n')
    else:
        aviso = ''

    # O ano tem selo E tom, e o tom nunca era dito. É ele que explica COMO o
    # ano funciona: o mesmo arquétipo num tom 2 e num tom 10 pede coisas
    # opostas. Sem isso o bloco do ano ficava só com metade da informação.
    t_ano = kd['tom_num']
    # O ano quase sempre cai sobre uma das 5 forças do mapa. Nomear o encontro
    # transforma o que seria repetição — o oráculo já descreveu esse arquétipo
    # — na informação mais valiosa do bloco.
    forca = FORCA_DO_ANO.get(atual['relacao'])
    linha_forca = (f"🔗 É o selo {forca} — o ano inteiro dentro de uma força "
                   f"que já é sua.\n\n" if forca else '')
    corpo_do_ano = (f"_{O.ONDA_NARRATIVA[s_num][0]}_\n"
                    f"{M.ARQUETIPO_PRATICA[s_num]}\n\n"
                    f"{linha_forca}"
                    f"⚡ *O ritmo do ano — Tom {t_ano}, "
                    f"{core.nome_do_tom(t_ano, s_num)}*\n"
                    f"_{TONS_PROFUNDO[t_ano]}_\n"
                    f"Na prática: é um ano que {T.TOM_FRASE[t_ano]}, "
                    f"{M.TOM_MODO[t_ano]}.\n\n"
                    f"🟢 *A luz do ano:* {T.ACESSIVEL[s_num]['flui']}\n"
                    f"🔴 *A armadilha — {M.ARMADILHA[s_num][0]}:* {T.ACESSIVEL[s_num]['trava']}\n"
                    f"🔑 *A virada do ano:* {M.CHAVE[s_num]}")

    # Quando o selo do ano é o mesmo do nascimento, o arquétipo e a chave de
    # ouro sairiam idênticos aos do item 2 deste mapa. Em vez de repetir, o
    # bloco nomeia o retorno — que é justamente o que torna esse ano diferente.
    if s_num == core.seal_of(c['natal']):
        corpo_do_ano = (f"🔁 *É o seu próprio selo que rege o ano.* Tudo que você leu no seu "
                        f"superpoder e na sua armadilha volta com força dobrada, e agora no "
                        f"Tom {t_ano} — {core.nome_do_tom(t_ano, s_num)}, que pede "
                        f"{M.TOM_MODO[t_ano]}.\n\n"
                        f"_{TONS_PROFUNDO[t_ano]}_\n"
                        f"Não é ano de aprender coisa nova sobre você. É ano de fazer o que "
                        f"você já sabe, num nível que antes não dava.")

    # O ano seguinte ganha leitura de verdade, não só uma linha: é a emenda que
    # a pessoa mais quer ver, e ela chega logo ali.
    seg = c['anos'][1]
    s_seg = seg['dados']['selo_num']
    marca_seg = f" — {ROTULO_CURTO[seg['relacao']]}" if ROTULO_CURTO.get(seg['relacao']) else ''
    # O arquétipo em prática fica só no item 1 e no ano corrente. Aqui ele era
    # a terceira aparição da mesma forma de frase dentro de uma leitura só —
    # o que mais fazia o mapa soar gerado quando se lia dois seguidos.
    bloco_seguinte = (f"*O PRÓXIMO — {seg['idade']} anos, a partir de {seg['inicio']:%d/%m/%Y}*\n"
                      f"🏛️ *Kin {seg['kin']:03d} — {seg['dados']['nome']}*{marca_seg}\n"
                      f"_{O.ONDA_NARRATIVA[s_seg][0]}_\n\n"
                      f"🟢 *A luz:* {T.ACESSIVEL[s_seg]['flui']}\n"
                      f"🔴 *A armadilha — {M.ARMADILHA[s_seg][0]}:* {T.ACESSIVEL[s_seg]['trava']}\n"
                      f"🔑 {M.CHAVE[s_seg]}")

    # Entrar ou sair de um castelo de 13 anos é a informação mais acionável do
    # bloco, e antes o leitor tinha que descobrir sozinho comparando a idade
    # com o intervalo impresso ao lado.
    if atual['idade'] == quad_fim:
        borda_castelo = (' *É o seu último ano nele* — o que não for lapidado agora '
                         'atravessa para o próximo castelo.')
    elif atual['idade'] == quad_ini:
        borda_castelo = ' *Você acabou de entrar nele* — os 13 anos começam agora.'
    else:
        borda_castelo = ''

    ter = c['anos'][2]
    frase_ter = T.ACESSIVEL[ter['dados']['selo_num']]['frase'].replace('Dia de', 'ano de')
    marca_ter = f" — {ROTULO_CURTO[ter['relacao']]}" if ROTULO_CURTO.get(ter['relacao']) else ''
    bloco_terceiro = (f"*E depois — {ter['idade']} anos ({ter['inicio']:%d/%m/%Y})*\n"
                      f"Kin {ter['kin']:03d}, {ter['dados']['nome']}{marca_ter}. "
                      f"{_mai(frase_ter)}")

    return f"""🔑 *{titulo}*
{texto}
{aviso}
*O ANO CORRENTE — {atual['idade']} anos*, de {atual['inicio']:%d/%m/%Y} a {atual['fim']:%d/%m/%Y}
🏛️ *Kin {atual['kin']:03d} — {kd['nome']}*
{corpo_do_ano}

{bloco_seguinte}

{bloco_terceiro}

_{mod_ano.REGRA_DO_CICLO}_

🏰 *{quad_nome}* — dos {quad_ini} aos {quad_fim} anos. Você está no ano *{atual['idade']} de 52* dessa volta.{borda_castelo}
👑 Aos *{c['idade_retorno']} anos*, em {c['data_retorno']:%d/%m/%Y}, você volta ao Kin {c['natal']:03d} do seu nascimento. Faltam {c['faltam_para_retorno']} anos."""


# ==========================================================
# ESTRUTURA B — O MAPA PESSOAL
# ==========================================================

def mapa_pessoal(nascimento: datetime.date, nome: str = 'Você',
                 hoje: datetime.date = None) -> list:
    """Devolve DUAS peças, cada uma fechando sozinha.

    Peça 1 — quem você é: kin, selo, superpoder, armadilha, ritmo, bússola, enredo.
    Peça 2 — o seu momento: o ano, o corpo, as diretrizes, o fechamento.

    Decisão de 03/09/2026: em vez de deixar o Telegram cortar um texto de 7 mil
    caracteres numa junta qualquer, a quebra virou editorial.
    """
    hoje = hoje or datetime.date.today()
    kin = core.calculate_kin(nascimento)
    kd = core.kin_data(kin)
    s_num, t_num = kd['selo_num'], kd['tom_num']
    arq, onda = kd['arquetipo'], kd['onda']
    degrau = onda['degrau']
    totem = TOTENS[t_num]
    o = core.oracle(kin)

    nome_super, texto_super = M.SUPERPODER[s_num]
    nome_super_min = nome_super[0].lower() + nome_super[1:]
    # Itálico verso a verso: nem o WhatsApp nem o Telegram sustentam um par de
    # sublinhados atravessando quebra de linha.
    decreto = '\n'.join(f'_{v}_' for v in core.decreto(kin).split('\n'))
    nome_arm, texto_arm = M.ARMADILHA[s_num]
    d_carreira, d_relacoes, d_cuidado = M.DIRETRIZES[s_num]

    marcos = _marcos(kd, natal=True)
    bloco_marcos = f'\n{marcos}\n' if marcos else ''

    # Portais dentro do oráculo
    pags = [o[c] for c in ('guia', 'analogo', 'antipoda', 'oculto') if o[c] in core.PAGS]
    bloco_pag = ''
    if pags:
        nomes = ', '.join(core.nome_do_kin(k) for k in pags)
        qtd = f'{len(pags)} Portais' if len(pags) > 1 else '1 Portal'
        bloco_pag = (f"\n🌀 *Alta voltagem:* {qtd} de Ativação Galáctica dentro do seu oráculo "
                     f"({nomes}). Ambiente e timing pesam mais no seu caso — "
                     f"silêncio e natureza não são luxo, são higiene.\n")

    # A onda como narrativa, não como lista
    selo_onda = core.seal_of(onda['inicio'])
    o_representa, o_tensao = O.ONDA_NARRATIVA[selo_onda]
    papel = O.PAPEL_DO_DEGRAU[degrau]

    parte1 = f"""Fala {nome}! ✨

Mapeei a sua Assinatura Galáctica a partir da sua data ({nascimento:%d/%m/%Y}) — o seu Kin de nascimento no calendário maia de 260 dias.

🏛️ *SEU KIN: {kin:03d} — {kd['nome'].upper()}*
🎨 Clã {kd['cla']} — você é do time que {kd['cla_info'][3]}
{bloco_marcos}
_"{M.MANIFESTO[s_num]}"_

☀️ *1. O SEU SELO: {core.SELO_NOME_COMPLETO[s_num].upper()}* ({kd['selo']['maia']})
_{O.ONDA_NARRATIVA[s_num][0]} O poder de {kd['selo']['acao']}, a essência de {kd['selo']['essencia']}._

Nos 21 arquétipos ele é *{arq['nome']}*, na {arq['rotulo']}. {M.ARQUETIPO_PRATICA[s_num]}

⭐ *2. O SEU SUPERPODER: {nome_super.upper()}*
{texto_super}

*⚠️ A SUA ARMADILHA: {nome_arm.upper()}*
{texto_arm}

*🔑 A CHAVE DE OURO*
{M.CHAVE[s_num]}

⚡ *3. O SEU RITMO: TOM {t_num}, {core.nome_do_tom(t_num, s_num).upper()}*
_{TONS_PROFUNDO[t_num]}_

Na sua vida: você é quem {T.TOM_FRASE[t_num]}, e forçar outro andamento te desgasta.
A pergunta que guia a sua vida: _"{kd['tom'][5]}"_

*Totem {totem[0]}* — {totem[1]}
{totem[2]}

*🔮 A ALQUIMIA DOS DOIS*
O seu selo te dá {nome_super_min}. O seu tom pede que você exerça isso {M.TOM_MODO[t_num]}.
Selo e tom se cruzam de 260 jeitos. O {kin:03d} é o seu.

🌊 *4. O ENREDO DA SUA VIDA*
Você nasceu no degrau *{degrau} de 13* da Onda {onda['artigo']} {onda['nome']} — e é daí que vem o seu Tom {t_num}: na onda, o degrau e o tom são o mesmo número.

_{o_representa} {o_tensao}_

*O seu papel nessa história:* dentro dessa jornada, você {papel}. Você não precisa resolver a onda inteira — precisa cumprir bem o seu passo dela.

*✨ O SEU DECRETO DE PODER*
A fórmula tradicional do seu Kin. Diga em voz alta, de manhã, sem pressa.

{decreto}

Esse é o retrato de quem você é. Na sequência, a sua rota: as forças que te movem, o ano que você está vivendo e o que o seu corpo faz quando isso desalinha. 👇"""

    parte2 = f"""*{nome.upper()} — A SUA ROTA* 🧭

🗺️ *5. AS SUAS 5 FORÇAS*

{_bussola(kin, natal=True)}
{bloco_pag}
🗓️ *6. O ANO QUE VOCÊ ESTÁ VIVENDO*

{bloco_do_ano(nascimento, hoje)}

🎯 *7. TRÊS DIRETRIZES*
*Carreira e dinheiro:* {d_carreira}

*Relações:* {d_relacoes}

*Autocuidado:* {d_cuidado}

🫀 *8. O SEU CORPO E O PONTO DE ALERTA*
{_corpo(kd, natal=True)}

🪞 *A pergunta que você carrega:* _{PROFUNDO[s_num]['auto_investigacao']}_

✨ {T.ASSINATURA}"""
    return [_limpa(parte1), _limpa(parte2)]


# ==========================================================
# A AULA — estudo do Leo, profundidade total
# ==========================================================

def aula_diaria(data: datetime.date = None, kin_natal: int = 194) -> str:
    """O estudo do dia — e a matéria-prima do conteúdo do dia.

    Reescrita em 04/09/2026. A versão anterior tinha ficado parada no dia em
    que foi escrita: de 13 tabelas de texto do sistema, usava UMA. Faltava o
    decreto (que estava no mapa e não na leitura mais profunda — invertido),
    o TOM_NA_FORCA, o CORPO_DO_TOM, a gramática de dois níveis, o pulsar. E
    ainda usava as barras ━━━ que saíram de todo o resto.

    Mas o problema maior não era o que faltava: era o formato. Despejar sete
    seções todo dia é dicionário, não estudo. Duas mudanças estruturais:

    1. A ORDEM VIRA CAMINHO. Quem é o dia (selo e tom) → o que ele pede do
       corpo → como ele conversa com as outras forças → onde ele está no tempo
       maior → o que fazer. Cada seção monta em cima da anterior.

    2. A AULA TERMINA EM CONTEÚDO. É o Princípio das Duas Saídas do método:
       profundidade para o Leo, destilada para o vídeo. As quatro últimas
       linhas são o roteiro do dia, montado do material acessível que já
       existe. Estudar deixa de competir com produzir.
    """
    from .textos_profundos import TONS_PROFUNDO
    kd = core.kin_do_dia(data or datetime.date.today())
    d = kd['data']
    s_num, t_num = kd['selo_num'], kd['tom_num']
    p = PROFUNDO[s_num]
    ac = T.ACESSIVEL[s_num]
    arq, onda, castelo, celula = kd['arquetipo'], kd['onda'], kd['castelo'], kd['celula']
    lua, fam, pulsar = kd['lua'], kd['familia'], kd['pulsar']
    o = core.oracle(kd['kin'])
    totem = TOTENS[t_num]
    degrau = onda['degrau']
    # Itálico linha a linha: no Telegram o _ não atravessa quebra de linha.
    decreto_fmt = chr(10).join(f'_{linha}_' for linha in core.decreto(kd['kin']).splitlines())
    rotulo_pulsar, texto_pulsar = T.PULSAR_DIA[pulsar['num']]
    # Dia comum não tem marco nenhum: sem isto sobra linha em branco no topo.
    marcos = _marcos(kd)
    marcos = marcos + chr(10) if marcos else ''

    rel = core.relacao_com(kin_natal, kd['kin'])
    linha_natal = T.RELACAO[rel] if rel else 'Dia neutro em relação ao seu Kin natal.'

    # As 5 forças em três camadas: o arquétipo (igual para todos), o que a
    # posição faz numa vida, e o tom daquele kin. É a mesma gramática do mapa.
    forcas = []
    for rotulo, chave, campo in [
        ('Guia', 'guia', 'guia_msg'), ('Análogo', 'analogo', 'analogo_msg'),
        ('Antípoda', 'antipoda', 'antipoda_msg'), ('Oculto', 'oculto', 'oculto_msg'),
        ('Quinta Força', 'quinta', 'quinta_msg'),
    ]:
        k = o[chave]
        s_f, t_f = core.seal_of(k), core.tone_of(k)
        pag = ' 🌀' if k in core.PAGS else ''
        forcas.append(f"*{rotulo}* — Kin {k:03d}, {core.nome_do_kin(k)}{pag}\n"
                      f"_{O.ONDA_NARRATIVA[s_f][0]}_\n"
                      f"{PROFUNDO[s_f][campo]}\n"
                      f"⚡ {O.TOM_NA_FORCA[chave][t_f]}")

    return _limpa(f"""📚 *AULA DO TZOLKIN — {d:%d/%m/%Y}*
*KIN {kd['kin']:03d} — {kd['nome'].upper()}*
🏛️ {arq['nome']}, {arq['rotulo']} | Harmônica {kd['harmonica']} | Célula {celula['num']}, {celula['nome']}
⚡ *{pulsar['nome']}* ({pulsar['dimensao']}) — *{rotulo_pulsar}:* {texto_pulsar}
{marcos}
🎯 *PARA VOCÊ HOJE* — Kin natal {kin_natal:03d}, {core.nome_do_kin(kin_natal)}
{linha_natal}

☀️ *1. O SELO — quem é o dia*
*{core.SELO_NOME_COMPLETO[s_num]}* ({kd['selo']['maia']})
_{O.ONDA_NARRATIVA[s_num][0]}_
{p['descricao']}.
{p['corpo']}

⚡ *2. O TOM — em que velocidade*
*Tom {t_num}, {core.nome_do_tom(t_num, s_num)}*
{TONS_PROFUNDO[t_num]}

🐆 *Totem {totem[0]}* — {totem[1]}
{totem[2]}

🔮 *A alquimia dos dois*
O selo dá {M.SUPERPODER[s_num][0].lower()}. O tom pede que isso seja exercido {M.TOM_MODO[t_num]}.

🫀 *3. O CORPO — onde o dia aterrissa*
Família *{fam['nome']}* → centro *{fam['chakra']}* → {fam['holon']}
🔻 *Contração:* {p['somat_contracao']}
🔺 *Expansão:* {p['somat_expansao']}
🧘 *Higiene do selo:* {p['somat_higiene']}
🧘 *Prática do tom:* {T.CORPO_DO_TOM[t_num]}

🌗 *4. LUZ, SOMBRA E CHAVE*
🟢 {p['luz']}
🔴 {p['sombra']}
🏷️ Armadilha: *{M.ARMADILHA[s_num][0]}*
🔑 _{p['chave']}_

🗺️ *5. O ORÁCULO DAS 5 FORÇAS*

""" + '\n\n'.join(forcas) + f"""

🌊 *6. O DIA NO TEMPO MAIOR*
Onda {onda['artigo']} *{onda['nome']}* — degrau {degrau}/13
_{O.ONDA_NARRATIVA[core.seal_of(onda['inicio'])][0]}_
*{T.DEGRAUS[degrau][0]}*. {T.DEGRAUS[degrau][1]}

🏰 *{castelo['nome']}* — Corte {castelo['corte']}, dia {castelo['dia']}/52
{castelo['missao']}
🔲 Célula {celula['num']}, *{celula['nome']}*: {celula['funcao'].lower()}.

🌙 *7. AS 13 LUAS E O PLASMA*
{lua['lua']} — {lua['acao'].lower()} | dia {lua['dia_da_lua']}/28, heptada {lua['heptada']}/52
Plasma *{lua['plasma'][0]}* no centro {lua['plasma'][1]}: {lua['plasma'][2].lower()}. Respire 4-4-4.

✨ *8. O DECRETO DO DIA*
{decreto_fmt}

🎯 *9. APLICAÇÃO*
💼 {p['dir_trabalho']}
💬 {p['dir_relacoes']}
🪞 _{p['auto_investigacao']}_

📣 *DESTILADA — o roteiro de hoje*
_As quatro linhas abaixo já estão no tom de vídeo. É só falar._

{ac['frase']}
Flui: {ac['flui']}. Trava: {ac['trava']}.
{_mai(ac['acao'])}.
A pergunta do dia: {kd['tom'][5].lower()}""")


# ==========================================================
# ESTRUTURA D — O DIA PESSOAL (produto de assinatura)
# ==========================================================

def dia_pessoal(nascimento: datetime.date, nome: str = '',
                data: datetime.date = None) -> str:
    """O Kin do dia lido contra o mapa de quem recebe.

    A diferença entre isto e o kin_do_dia é a diferença entre o que se dá e o
    que se cobra. O diário coletivo é igual para todo mundo; este cruza os 260
    dias do ciclo com os 260 Kins natais possíveis — 67.600 leituras, nenhuma
    repetida no ano.

    Quatro eixos, três deles falando todo dia (ver a nota em textos.py sobre
    os 168 dias sem relação):

        relação  → a manchete, quando existe
        ritmo    → a manchete, quando não existe
        corpo    → sempre: o centro do dia contra o centro natal
        ano      → sempre: onde a pessoa está no próprio ciclo

    Curto de propósito. O valor aqui é precisão, não volume: quem assina quer
    saber o que fazer com o dia antes do café, não ler uma apostila.
    """
    hoje = data or datetime.date.today()
    natal = core.calculate_kin(nascimento)
    kd = core.kin_do_dia(hoje)
    s_dia, t_dia = kd['selo_num'], kd['tom_num']
    s_nat, t_nat = core.seal_of(natal), core.tone_of(natal)
    fam_dia = kd['familia']['nome']
    fam_nat = core.kin_do_dia(nascimento)['familia']['nome']

    # --- manchete -------------------------------------------------------
    rel = core.relacao_com(natal, kd['kin'])
    titulo = corpo_manchete = None
    if rel and rel in T.DIA_PESSOAL:
        titulo, corpo_manchete = T.DIA_PESSOAL[rel]

    # --- corpo ----------------------------------------------------------
    centro_dia = kd['familia']['chakra']
    centro_nat = core.kin_do_dia(nascimento)['familia']['chakra']
    if fam_dia == fam_nat:
        corpo = T.CORPO_DOBRADO.format(centro=centro_dia)
    else:
        corpo = T.CORPO_CRUZADO.format(centro_dia=centro_dia, centro_seu=centro_nat)

    # --- o chamado do dia -----------------------------------------------
    # Aqui ficava CORPO_DO_TOM, que é exatamente a mesma linha do diário aberto:
    # o assinante recebia a mesma instrução duas vezes na mesma manhã. No lugar,
    # o superpoder DELE cruzado com o modo de HOJE — a fórmula da alquimia do
    # mapa aplicada ao dia. Muda a cada 13 dias e nenhum não-assinante vê.
    superpoder = M.SUPERPODER[s_nat][0]
    for artigo in ('O ', 'A ', 'Os ', 'As '):
        if superpoder.startswith(artigo):
            superpoder = superpoder[len(artigo):]
            break
    chamado = f"Hoje o seu *{superpoder}* opera {M.TOM_MODO[t_dia]}"
    chamado = chamado.rstrip('.') + '.'

    # --- o ano ----------------------------------------------------------
    # Este bloco é o coração do produto pago, e na primeira versão era UMA
    # linha. Medido: nos 168 dias sem relação, só 4 das 21 linhas eram da
    # pessoa — o resto duplicava o diário grátis que ela já recebe. O ciclo
    # anual é o oposto disso: muda com a idade E com o Kin natal, então dois
    # assinantes nunca leem a mesma coisa aqui.
    c = mod_ano.ciclo_anual(nascimento, hoje, adiante=1)
    atual, prox = c['anos'][0], c['anos'][1]
    dias_virar = (prox['inicio'] - hoje).days
    dia_do_ano = (hoje - atual['inicio']).days + 1
    quad_nome, quad_corte, quad_ini, quad_fim, quad_missao = c['quadrante']

    ano_linhas = [f"Ano {atual['idade']} → {atual['idade'] + 1}, dia *{dia_do_ano}* de 365."]
    # O Kin regente do ano é o mesmo por 365 dias. Repetido toda manhã vira
    # ruído — apareceu 22 vezes em 60 dias no roast. Entra na primeira semana
    # do ciclo, e depois só quando carrega rótulo (aí ele diz algo).
    if dia_do_ano <= 7 or ROTULO_CURTO.get(atual['relacao']):
        ano_linhas.append(f"Regido por *{core.nome_do_kin(atual['kin'])}*"
                          + (f" — {ROTULO_CURTO[atual['relacao']]}."
                             if ROTULO_CURTO.get(atual['relacao']) else '.'))
    forca = FORCA_DO_ANO.get(atual['relacao'])
    if forca:
        ano_linhas.append(f"O ano inteiro está rodando dentro {forca}.")
    # O castelo de vida é fato de 13 anos: repetido todo dia vira ruído. Só
    # entra no dia da virada do ano e na primeira semana de cada ciclo anual,
    # que é quando ele diz alguma coisa.
    if dia_do_ano == 1:
        # Uma vez por ano, no dia da virada. Com "<= 7" ele saía três vezes na
        # mesma semana, idêntico — pior do que sair uma vez só.
        ano_linhas.append(f"🏰 *{quad_nome}*, {quad_corte} ({quad_ini}–{quad_fim} anos): "
                          f"{quad_missao}")
    if c['faltam_para_retorno'] <= 3:
        ano_linhas.append(f"👑 Faltam *{c['faltam_para_retorno']} anos* para o seu Retorno "
                          f"Galáctico, aos {c['idade_retorno']}.")
    if hoje == atual['inicio']:
        # O dia da virada. A checagem antiga só olhava o ano SEGUINTE, então no
        # próprio aniversário galáctico dias_virar dava 365 e a leitura não
        # dizia nada — justamente no dia mais importante do ciclo pessoal.
        ano_linhas.insert(0, T.ANIVERSARIO_GALACTICO + '\n')
    elif dias_virar <= 30:
        ano_linhas.append(f"🎂 Faltam *{dias_virar} dias* para o seu aniversário galáctico — "
                          f"o ano vira em {prox['inicio']:%d/%m}, sob "
                          f"*{core.nome_do_kin(prox['kin'])}*.")

    tratamento = f"{nome.split()[0]}, " if nome else ''

    # DIA GRANDE OU DIA COMUM.
    # Dos 260 dias do ciclo, ~92 tocam o mapa da pessoa de alguma forma. Nos
    # outros 168 não há o que anunciar, e insistir seria inventar. Se toda
    # manhã grita, nenhuma manhã é ouvida — então o dia comum vem curto e o dia
    # grande vem inteiro. Quem assina aprende a confiar no volume da mensagem.
    # PAG de fora de propósito: portal é evento COLETIVO, já anunciado no diário
    # aberto, e são 52 por ciclo. Incluí-lo levava os dias grandes a 51% — metade
    # do ano "especial" não é especial. Sem ele fica em ~35%, um dia em cada três.
    grande = bool(rel) or hoje == atual['inicio'] or dias_virar <= 30

    cabeca = (f"☀️ *O SEU DIA — {hoje:%d/%m/%Y}*\n"
              f"{tratamento}Kin natal *{natal:03d} — {core.nome_do_kin(natal)}*\n"
              f"Hoje o campo é *Kin {kd['kin']:03d} — {kd['nome']}*"
              f"{' 🌀' if kd['is_pag'] else ''}")

    # A VÉSPERA. O que faltava para isto ser assinatura e não uma sequência de
    # bilhetes soltos: cada manhã aponta para a próxima que importa. Puro
    # cálculo, nenhum texto novo — e é o que faz a pessoa continuar amanhã.
    aviso = ''
    for salto in range(1, 22):
        futuro = hoje + datetime.timedelta(days=salto)
        r_fut = core.relacao_com(natal, core.calculate_kin(futuro))
        if r_fut in T.DIA_CURTO:
            quando = 'Amanhã' if salto == 1 else f'Daqui a *{salto} dias*'
            aviso = f"\n⏭️ {quando}: {T.DIA_CURTO[r_fut]}."
            break

    if not grande:
        # Dia comum: quatro linhas. Sem manchete, sem moldura, sem explicação
        # repetida. O contraste de ritmo só entra quando é notícia de verdade.
        return _limpa(f"""{cabeca}
_{O.ONDA_NARRATIVA[s_dia][0]}_

🫀 {corpo}
👉 {chamado}
🗓️ Dia *{dia_do_ano}* dos 365 do seu ano.{aviso}

✨ {T.ASSINATURA}""")

    # O arquétipo do dia, o flui/trava e a ação NÃO entram aqui: são idênticos
    # ao diário aberto. Quem assina recebe o que é dela, não o mesmo texto duas
    # vezes.
    # Dia grande. A manchete existe só aqui — nos dias comuns não há o que
    # anunciar, e anunciar assim mesmo é o que gastava a atenção da pessoa.
    manchete = f"\n🎯 *{titulo}*\n{corpo_manchete}\n" if titulo else ''
    # O ritmo só aparece quando é notícia: no dia em que o tom do dia é o seu,
    # o próprio DIA_PESSOAL já diz. Aqui entra o contraste, em UMA linha, e só
    # quando o dia grande veio da virada do ano (senão a manchete já basta).
    ritmo = ('\n⚡ ' + T.RITMO_CONTRASTE.format(modo_dia=M.TOM_MODO[t_dia]) + '\n'
             if not titulo else '')
    return _limpa(f"""{cabeca}
_{O.ONDA_NARRATIVA[s_dia][0]}_
{manchete}{ritmo}
🫀 {corpo}
👉 {chamado}

🗓️ *O SEU ANO*
""" + '\n'.join(ano_linhas) + f"""{aviso}

✨ {T.ASSINATURA}""")
