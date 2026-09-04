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
    'mesmo_selo': '🔁 seu arquétipo volta',
    'mesmo_tom': '🎵 seu ritmo volta',
    None: None,
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
        linhas.append(f"{emoji} *{nome}* — {core.nome_do_kin(k)}{pag}\n"
                      f"_{O.ONDA_NARRATIVA[s][0]}_\n"
                      f"{O.ORACULO[s][campo]}{fundo}")
    k = o['quinta']
    s_q = core.seal_of(k)
    arquetipo = '' if s_q in ja_vistos else f"_{O.ONDA_NARRATIVA[s_q][0]}_\n"
    fundo_q = f"\n↳ {_atemporal(PROFUNDO[s_q]['quinta_msg'])}" if natal else ''
    linhas.append(f"👑 *O Vórtice Integrador* — {core.nome_do_kin(k)}\n"
                  f"{arquetipo}"
                  f"A soma das cinco forças ativa {M.SUPERPODER[s_q][0].lower()}: "
                  f"{T.ACESSIVEL[s_q]['flui']}.{fundo_q}")
    return '\n\n'.join(linhas)


def _corpo(kd: dict, natal: bool = False) -> str:
    regiao, orgaos, sintomas, higiene = M.CORPO_FAMILIA[kd['familia']['nome']]
    abre = ('A sua energia ancora no' if natal else 'A energia de hoje pega no')
    aviso = ('Quando você segura o que precisa sair, é aqui que aperta:'
             if natal else 'Se o dia apertar, é aqui que você sente:')
    return (f"{abre} *{regiao}* — {orgaos}.\n\n{aviso}\n"
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
*A ENERGIA DE HOJE*
☀️ *{core.SELO_NOME_COMPLETO[s_num]}* ({kd['selo']['maia']})
_{O.ONDA_NARRATIVA[s_num][0]}_
{PROFUNDO[s_num]['descricao']} — o poder de {kd['selo']['acao']}, a essência de {kd['selo']['essencia']}. É a força que rege o dia inteiro.

⚡ *Tom {t_num}, {core.nome_do_tom(t_num, s_num)}*
_{TONS_PROFUNDO[t_num]}_
Na prática: o dia que {T.TOM_FRASE[t_num]}. {T.TONS_ACESSIVEL[t_num]['ritmo']}{linha_peso}

🟢 *Flui:* {ac['flui']}
🔴 *Trava — {M.ARMADILHA[s_num][0]}:* {ac['trava']}

*A BÚSSOLA DE HOJE*
{_bussola(kd['kin'])}

*A ONDA — DIA {degrau} DE 13*
🌊 Onda {onda['artigo']} {onda['nome']}
_{O.ONDA_NARRATIVA[core.seal_of(onda['inicio'])][0]}_
Hoje é o degrau {degrau}: *{T.DEGRAUS[degrau][0]}*. {T.DEGRAUS[degrau][1]}

*O CORPO HOJE*
{_corpo(kd)}

👉 *A AÇÃO DE HOJE:* {_mai(ac['acao'])}.
🪞 *Para se perguntar:* _{kd['tom'][5]}_

✨ *{T.ASSINATURA}*
Se bateu com o seu momento, me conta. E se quiser o seu mapa, manda a sua data de nascimento. 📩"""
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
    corpo_do_ano = (f"_{O.ONDA_NARRATIVA[s_num][0]}_\n"
                    f"{M.ARQUETIPO_PRATICA[s_num]}\n\n"
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
    bloco_seguinte = (f"*O PRÓXIMO — {seg['idade']} anos, a partir de {seg['inicio']:%d/%m/%Y}*\n"
                      f"🏛️ *Kin {seg['kin']:03d} — {seg['dados']['nome']}*{marca_seg}\n"
                      f"_{O.ONDA_NARRATIVA[s_seg][0]}_\n"
                      f"{M.ARQUETIPO_PRATICA[s_seg]}\n\n"
                      f"🟢 *A luz:* {T.ACESSIVEL[s_seg]['flui']}\n"
                      f"🔴 *A armadilha — {M.ARMADILHA[s_seg][0]}:* {T.ACESSIVEL[s_seg]['trava']}")

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

🏰 *{quad_nome}* — dos {quad_ini} aos {quad_fim} anos. Você está no ano *{atual['idade']} de 52* dessa volta.
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
        bloco_pag = (f"\n⚡ *Alta voltagem:* {qtd} de Ativação Galáctica dentro do seu oráculo "
                     f"({nomes}). Isso deixa o seu mapa mais sensível a ambiente e a timing — "
                     f"silêncio e natureza não são luxo pra você, são higiene.\n")

    # A onda como narrativa, não como lista
    selo_onda = core.seal_of(onda['inicio'])
    o_representa, o_tensao = O.ONDA_NARRATIVA[selo_onda]
    papel = O.PAPEL_DO_DEGRAU[degrau]

    parte1 = f"""Fala {nome}! ✨

Mapeei a sua Assinatura Galáctica a partir da sua data ({nascimento:%d/%m/%Y}) — o seu Kin de nascimento no calendário maia de 260 dias.

🏛️ *SEU KIN: {kin:03d} — {kd['nome'].upper()}*
🎨 Clã {kd['cla']} — você é do time que {kd['cla_info'][3]}
🏛️ Arquétipo: *{arq['nome']}*
{bloco_marcos}
_"{M.MANIFESTO[s_num]}"_

*1. O SEU SELO: {core.SELO_NOME_COMPLETO[s_num].upper()}* ({kd['selo']['maia']})
_{O.ONDA_NARRATIVA[s_num][0]} O poder de {kd['selo']['acao']}, a essência de {kd['selo']['essencia']}._
{PROFUNDO[s_num]['descricao']} — esse campo é o mesmo para todo mundo que nasce sob esse selo. O que muda é o que você faz com ele.

No mapa dos 21 arquétipos, ele aparece como *{arq['nome']}*, na {arq['rotulo']}. {M.ARQUETIPO_PRATICA[s_num]}

*2. O SEU SUPERPODER: {nome_super.upper()}*
{texto_super}

*⚠️ A SUA ARMADILHA: {nome_arm.upper()}*
{texto_arm}

*🔑 A CHAVE DE OURO*
{M.CHAVE[s_num]}

*3. O SEU RITMO: TOM {t_num}, {core.nome_do_tom(t_num, s_num).upper()}*
_{TONS_PROFUNDO[t_num]}_
Dos 13 tons, é o {t_num}º — a velocidade em que a sua energia trabalha melhor.

Na sua vida: você é quem {T.TOM_FRASE[t_num]}, e forçar outro andamento te desgasta.
A pergunta que guia a sua vida: _"{kd['tom'][5]}"_

*Totem {totem[0]}* — {totem[1]}
{totem[2]}

*🔮 A ALQUIMIA DOS DOIS*
O seu selo te dá {nome_super_min}. O seu tom pede que você exerça isso {M.TOM_MODO[t_num]}.
É esse cruzamento — e não o selo sozinho — que faz o seu Kin ser o {kin:03d} e não outro. Selo e tom se combinam de 260 jeitos: esse é o seu.

*4. O ENREDO DA SUA VIDA*
🌊 Você nasceu no degrau *{degrau} de 13* da Onda {onda['artigo']} {onda['nome']}.

_{o_representa} {o_tensao}_

*O seu papel nessa história:* dentro dessa jornada, você {papel}. Você não precisa resolver a onda inteira — precisa cumprir bem o seu passo dela.

*✨ O SEU DECRETO DE PODER*
A fórmula tradicional do seu Kin. Diga em voz alta, de manhã, sem pressa.

{decreto}

Esse é o retrato de quem você é. Na sequência, a sua rota: as forças que te movem, o ano que você está vivendo e o que o seu corpo faz quando isso desalinha. 👇"""

    parte2 = f"""*{nome.upper()} — A SUA ROTA* 🧭

*5. A SUA BÚSSOLA DE 5 FORÇAS*
{_bussola(kin, natal=True)}
{bloco_pag}
*6. O ANO QUE VOCÊ ESTÁ VIVENDO*

{bloco_do_ano(nascimento, hoje)}

*7. TRÊS DIRETRIZES*
*Carreira e dinheiro:* {d_carreira}
*Relações:* {d_relacoes}
*Autocuidado:* {d_cuidado}

*8. O SEU CORPO E O PONTO DE ALERTA*
{_corpo(kd, natal=True)}

🪞 *A pergunta que você carrega:* _{PROFUNDO[s_num]['auto_investigacao']}_

Lê com calma e me conta: o que mais ressoou? Se algum ponto do corpo bateu, me diz qual — é sempre por aí que a conversa fica boa. 📩

Isso aqui é o que a sua data conta. O mapa de verdade a gente monta junto, com a sua história dentro. ✨

*{T.ASSINATURA}*"""
    return [_limpa(parte1), _limpa(parte2)]


# ==========================================================
# A AULA — estudo do Leo, profundidade total
# ==========================================================

def aula_diaria(data: datetime.date = None, kin_natal: int = 194) -> str:
    from .textos_profundos import TONS_PROFUNDO
    kd = core.kin_do_dia(data or datetime.date.today())
    d = kd['data']
    s_num, t_num = kd['selo_num'], kd['tom_num']
    p = PROFUNDO[s_num]
    arq, onda, castelo, celula = kd['arquetipo'], kd['onda'], kd['castelo'], kd['celula']
    lua = kd['lua']
    o = core.oracle(kd['kin'])
    totem = TOTENS[t_num]
    fam = kd['familia']

    rel = core.relacao_com(kin_natal, kd['kin'])
    linha_natal = T.RELACAO[rel] if rel else 'Dia neutro em relação ao seu Kin natal.'

    forcas = []
    for rotulo, chave, campo in [
        ('Guia', 'guia', 'guia_msg'), ('Análogo', 'analogo', 'analogo_msg'),
        ('Antípoda', 'antipoda', 'antipoda_msg'), ('Oculto', 'oculto', 'oculto_msg'),
        ('Quinta Força', 'quinta', 'quinta_msg'),
    ]:
        k = o[chave]
        pag = ' 🌀' if k in core.PAGS else ''
        forcas.append(f"*{rotulo}* — Kin {k:03d}, {core.nome_do_kin(k)}{pag}\n"
                      f"{PROFUNDO[core.seal_of(k)][campo]}")

    marcos = _marcos(kd)

    return _limpa(f"""📚 *AULA DO TZOLKIN — {d:%d/%m/%Y}*
*KIN {kd['kin']:03d} — {kd['nome'].upper()}*
Harmônica {kd['harmonica']} | Célula {celula['num']} ({celula['nome']}) | {kd['pulsar']['nome']}, {kd['pulsar']['dimensao']}
{marcos}

*PARA VOCÊ HOJE (Kin natal {kin_natal:03d})*
{linha_natal}

{LINHA}

*1. SELO E TOM*
☀️ *{core.SELO_NOME_COMPLETO[s_num]}* ({kd['selo']['maia']}) — {arq['nome']}, {arq['rotulo']}
{p['descricao']}.
{p['corpo']}

⚡ *Tom {t_num}, {core.nome_do_tom(t_num, s_num)}*
{TONS_PROFUNDO[t_num]}

🐆 *{totem[0]}* — {totem[1]}
{totem[2]}

{LINHA}

*2. LUZ, SOMBRA E CHAVE*
🟢 {p['luz']}
🔴 {p['sombra']}
🔑 _{p['chave']}_
🏷️ Armadilha: *{M.ARMADILHA[s_num][0]}*

{LINHA}

*3. LEITURA SOMÁTICA*
Família *{fam['nome']}* → centro *{fam['chakra']}* → {fam['holon']}
🔻 *Contração:* {p['somat_contracao']}
🔺 *Expansão:* {p['somat_expansao']}
🧘 *Higiene:* {p['somat_higiene']}

{LINHA}

*4. O ORÁCULO DAS 5 FORÇAS*

""" + '\n\n'.join(forcas) + f"""

{LINHA}

*5. ONDA E CASTELO*
🌊 Onda {onda['artigo']} *{onda['nome']}* — degrau {onda['degrau']}/13: {T.DEGRAUS[onda['degrau']][0]}
{T.DEGRAUS[onda['degrau']][1]}

🏰 *{castelo['nome']}* — Corte {castelo['corte']}, dia {castelo['dia']}/52
{castelo['missao']}
🔲 Célula {celula['num']}, *{celula['nome']}*: {celula['funcao'].lower()}.

{LINHA}

*6. 13 LUAS E PLASMA*
🌙 {lua['lua']} — {lua['acao'].lower()} | dia {lua['dia_da_lua']}/28, heptada {lua['heptada']}/52
Plasma *{lua['plasma'][0]}* no centro {lua['plasma'][1]}: {lua['plasma'][2].lower()}. Respire 4-4-4.

{LINHA}

*7. APLICAÇÃO*
💼 {p['dir_trabalho']}
💬 {p['dir_relacoes']}
🪞 _{p['auto_investigacao']}_""")
