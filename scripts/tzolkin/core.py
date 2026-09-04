# -*- coding: utf-8 -*-
"""
Núcleo do Sincronário — Cosba
FONTE ÚNICA da matemática e das tabelas do Tzolkin (Dreamspell / Lei do Tempo).

Este módulo não contém texto de leitura. Só estrutura e cálculo.
Todo texto vive em textos.py; toda montagem de mensagem vive em mensagens.py.

Convenção de Famílias Terrestres: cânone José Argüelles (agrupamento de 5 em 5).
Decidido em 03/09/2026. Ver docstring de FAMILIAS.
"""

import datetime

# ==========================================================
# ÂNCORA E CÁLCULO DO KIN
# ==========================================================

ANCHOR_DATE = datetime.date(1987, 7, 26)   # Convergência Harmônica
ANCHOR_KIN = 34                            # Mago Galáctico Branco


def _is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _feb29_count(d: datetime.date) -> int:
    """Quantos 29 de fevereiro já ocorreram até a data d, incluindo o próprio dia.

    Incluir o próprio dia é o que faz o 29/02 carregar o Kin do dia 28 —
    o Dreamspell não conta o bissexto, então a contagem trava nele, não no 01/03.
    """
    n = d.year - 1
    count = n // 4 - n // 100 + n // 400
    if _is_leap(d.year) and (d.month > 2 or (d.month == 2 and d.day == 29)):
        count += 1
    return count


def calculate_kin(target: datetime.date) -> int:
    """Kin (1 a 260) de qualquer data. O(1), funciona pra frente e pra trás."""
    delta_days = (target - ANCHOR_DATE).days
    delta_leaps = _feb29_count(target) - _feb29_count(ANCHOR_DATE)
    effective = delta_days - delta_leaps
    return ((ANCHOR_KIN - 1 + effective) % 260) + 1


def seal_of(kin: int) -> int:
    return ((kin - 1) % 20) + 1


def tone_of(kin: int) -> int:
    return ((kin - 1) % 13) + 1


def kin_from(seal: int, tone: int) -> int:
    """Único Kin de 1 a 260 com esse selo e esse tom."""
    for k in range(1, 261):
        if seal_of(k) == seal and tone_of(k) == tone:
            return k
    raise ValueError("combinação selo/tom inválida")


# ==========================================================
# OS 20 SELOS SOLARES — estrutura
# ==========================================================
# acao / poder / essencia = os verbos canônicos DO SELO
# (não confundir com a ação do clã: Inicia/Refina/Transforma/Amadurece)

SELOS = {
    1:  {'nome': 'Dragão',            'maia': 'Imix',    'cla': 'Vermelho', 'acao': 'nutrir',      'poder': 'nascimento',      'essencia': 'ser'},
    2:  {'nome': 'Vento',             'maia': 'Ik',      'cla': 'Branco',   'acao': 'comunicar',   'poder': 'espírito',        'essencia': 'alento'},
    3:  {'nome': 'Noite',             'maia': 'Akbal',   'cla': 'Azul',     'acao': 'sonhar',      'poder': 'abundância',      'essencia': 'intuição'},
    4:  {'nome': 'Semente',           'maia': 'Kan',     'cla': 'Amarelo',  'acao': 'focalizar',   'poder': 'florescimento',   'essencia': 'percepção'},
    5:  {'nome': 'Serpente',          'maia': 'Chicchan','cla': 'Vermelho', 'acao': 'sobreviver',  'poder': 'força vital',     'essencia': 'instinto'},
    6:  {'nome': 'Enlaçador',         'maia': 'Cimi',    'cla': 'Branco',   'acao': 'igualar',     'poder': 'morte',           'essencia': 'oportunidade'},
    7:  {'nome': 'Mão',               'maia': 'Manik',   'cla': 'Azul',     'acao': 'conhecer',    'poder': 'realização',      'essencia': 'cura'},
    8:  {'nome': 'Estrela',           'maia': 'Lamat',   'cla': 'Amarelo',  'acao': 'embelezar',   'poder': 'elegância',       'essencia': 'arte'},
    9:  {'nome': 'Lua',               'maia': 'Muluc',   'cla': 'Vermelho', 'acao': 'purificar',   'poder': 'água universal',  'essencia': 'fluxo'},
    10: {'nome': 'Cão',               'maia': 'Oc',      'cla': 'Branco',   'acao': 'amar',        'poder': 'coração',         'essencia': 'lealdade'},
    11: {'nome': 'Macaco',            'maia': 'Chuen',   'cla': 'Azul',     'acao': 'brincar',     'poder': 'magia',           'essencia': 'ilusão'},
    12: {'nome': 'Humano',            'maia': 'Eb',      'cla': 'Amarelo',  'acao': 'influenciar', 'poder': 'livre-arbítrio',  'essencia': 'sabedoria'},
    13: {'nome': 'Caminhante do Céu', 'maia': 'Ben',     'cla': 'Vermelho', 'acao': 'explorar',    'poder': 'espaço',          'essencia': 'vigilância'},
    14: {'nome': 'Mago',              'maia': 'Ix',      'cla': 'Branco',   'acao': 'encantar',    'poder': 'atemporalidade',  'essencia': 'receptividade'},
    15: {'nome': 'Águia',             'maia': 'Men',     'cla': 'Azul',     'acao': 'criar',       'poder': 'visão',           'essencia': 'mente'},
    16: {'nome': 'Guerreiro',         'maia': 'Cib',     'cla': 'Amarelo',  'acao': 'questionar',  'poder': 'inteligência',    'essencia': 'coragem'},
    17: {'nome': 'Terra',             'maia': 'Caban',   'cla': 'Vermelho', 'acao': 'evoluir',     'poder': 'navegação',       'essencia': 'sincronicidade'},
    18: {'nome': 'Espelho',           'maia': 'Etznab',  'cla': 'Branco',   'acao': 'refletir',    'poder': 'infinito',        'essencia': 'ordem'},
    19: {'nome': 'Tormenta',          'maia': 'Cauac',   'cla': 'Azul',     'acao': 'catalisar',   'poder': 'autogeração',     'essencia': 'energia'},
    20: {'nome': 'Sol',               'maia': 'Ahau',    'cla': 'Amarelo',  'acao': 'iluminar',    'poder': 'fogo universal',  'essencia': 'vida'},
}

# Nome completo do selo, com a cor no lugar certo do gênero
SELO_NOME_COMPLETO = {
    1: 'Dragão Vermelho', 2: 'Vento Branco', 3: 'Noite Azul', 4: 'Semente Amarela',
    5: 'Serpente Vermelha', 6: 'Enlaçador de Mundos Branco', 7: 'Mão Azul', 8: 'Estrela Amarela',
    9: 'Lua Vermelha', 10: 'Cão Branco', 11: 'Macaco Azul', 12: 'Humano Amarelo',
    13: 'Caminhante do Céu Vermelho', 14: 'Mago Branco', 15: 'Águia Azul', 16: 'Guerreiro Amarelo',
    17: 'Terra Vermelha', 18: 'Espelho Branco', 19: 'Tormenta Azul', 20: 'Sol Amarelo',
}

# Gênero do selo, para o tom concordar no nome do Kin.
# Sem isto sai "Estrela Galáctico Amarela" em vez de "Estrela Galáctica Amarela".
_SELO_FEMININO = {3, 4, 5, 7, 8, 9, 15, 17, 19}

# Tons que flexionam: (masculino, feminino). Os demais são invariáveis.
_TOM_FEMININO = {
    1: 'Magnética', 3: 'Elétrica', 5: 'Harmônica', 6: 'Rítmica',
    8: 'Galáctica', 10: 'Planetária', 13: 'Cósmica',
}


def nome_do_tom(tone: int, seal: int) -> str:
    if seal in _SELO_FEMININO and tone in _TOM_FEMININO:
        return _TOM_FEMININO[tone]
    return TONS[tone][0]


def artigo_do_selo(seal: int) -> str:
    """'da' ou 'do', para 'Onda da Semente' e não 'Onda do Semente'."""
    return 'da' if seal in _SELO_FEMININO else 'do'


def nome_do_kin(kin: int) -> str:
    s, t = seal_of(kin), tone_of(kin)
    partes = SELO_NOME_COMPLETO[s].split()
    cor = partes[-1]
    base = ' '.join(partes[:-1])
    return f"{base} {nome_do_tom(t, s)} {cor}"


# (infinitivo, direção, território, 3ª pessoa — para "o time que inicia")
CLAS = {
    'Vermelho': ('Iniciar', 'Leste',  'Corpo e matéria', 'inicia'),
    'Branco':   ('Refinar', 'Norte',  'Mente e espírito', 'refina'),
    'Azul':     ('Transformar', 'Oeste', 'Emoção e alquimia', 'transforma'),
    'Amarelo':  ('Amadurecer', 'Sul',  'Espírito e colheita', 'amadurece'),
}

# ==========================================================
# OS 13 TONS GALÁCTICOS
# ==========================================================
# (nome, poder, acao, essencia, totem, pergunta)

TONS = {
    1:  ('Magnético',     'Unificar',      'Atrair',      'Propósito',    'Morcego 🦇',   'Qual é o meu propósito?'),
    2:  ('Lunar',         'Polarizar',     'Estabilizar', 'Desafio',      'Escorpião 🦂', 'Qual é o meu desafio?'),
    3:  ('Elétrico',      'Ativar',        'Vincular',    'Serviço',      'Veado 🦌',     'Como posso servir melhor?'),
    4:  ('Autoexistente', 'Definir',       'Medir',       'Forma',        'Coruja 🦉',    'Qual é a forma da minha ação?'),
    5:  ('Harmônico',     'Potencializar', 'Comandar',    'Radiação',     'Pavão 🦚',     'Como reúno meus recursos?'),
    6:  ('Rítmico',       'Organizar',     'Equilibrar',  'Igualdade',    'Lagarto 🦎',   'Como me organizo com equilíbrio?'),
    7:  ('Ressonante',    'Canalizar',     'Inspirar',    'Sintonização', 'Macaco 🐒',    'Como sintonizo com a Fonte?'),
    8:  ('Galáctico',     'Harmonizar',    'Modelar',     'Integridade',  'Falcão 🦅',    'Eu vivo aquilo em que acredito?'),
    9:  ('Solar',         'Pulsar',        'Realizar',    'Intenção',     'Jaguar 🐆',    'Como realizo minha intenção?'),
    10: ('Planetário',    'Aperfeiçoar',   'Produzir',    'Manifestação', 'Cão 🐕',       'Como manifesto frutos concretos?'),
    11: ('Espectral',     'Dissolver',     'Libertar',    'Liberação',    'Serpente 🐍',  'Como solto o que já cumpriu seu papel?'),
    12: ('Cristal',       'Dedicar',       'Cooperar',    'Cooperação',   'Coelho 🐇',    'Como coopero com tudo o que vive?'),
    13: ('Cósmico',       'Perseverar',    'Transcender', 'Presença',     'Tartaruga 🐢', 'Como expando minha presença?'),
}

# ==========================================================
# FAMÍLIAS TERRESTRES — CÂNONE ARGÜELLES
# ==========================================================
# As Famílias Terrestres são, por definição, o agrupamento dos selos DE 5 EM 5.
# Fórmula: indice = (selo - 1) % 5
#
#   Polar   {1, 6, 11, 16}  → Coronário   → Polo Norte
#   Cardeal {2, 7, 12, 17}  → Laríngeo    → Zona Temperada Norte
#   Central {3, 8, 13, 18}  → Cardíaco    → Equador
#   Sinal   {4, 9, 14, 19}  → Plexo Solar → Zona Temperada Sul
#   Portal  {5, 10, 15, 20} → Raiz        → Polo Sul
#
# NOTA HISTÓRICA: até 03/09/2026 o bot usava {1,5,10,15}/{9,14,19,20}, que não é
# agrupamento de 5 em 5 e portanto não correspondia a nenhuma tradição. 15 dos 20
# selos recebiam o chakra errado. Corrigido aqui. Se algum dia o método Cosba
# adotar convenção própria, muda-se ESTA tabela e só ela.

_FAMILIA_ORDEM = ['Polar', 'Cardeal', 'Central', 'Sinal', 'Portal']

FAMILIAS = {
    'Polar':   {'chakra': 'Coronário',   'holon': 'Polo Norte',            'funcao': 'Recebe a informação e barra o excesso'},
    'Cardeal': {'chakra': 'Laríngeo',    'holon': 'Zona Temperada Norte',  'funcao': 'Transmite a voz e expressa a palavra'},
    'Central': {'chakra': 'Cardíaco',    'holon': 'Equador',               'funcao': 'Transmuta e faz a alquimia do coração'},
    'Sinal':   {'chakra': 'Plexo Solar', 'holon': 'Zona Temperada Sul',    'funcao': 'Revela o mistério e sinaliza a sabedoria'},
    'Portal':  {'chakra': 'Raiz',        'holon': 'Polo Sul',              'funcao': 'Abre os portais do tempo e anima a vida'},
}


def familia_de(seal: int):
    nome = _FAMILIA_ORDEM[(seal - 1) % 5]
    dados = dict(FAMILIAS[nome])
    dados['nome'] = nome
    return dados


# ==========================================================
# HUNAB KU 21 — OS 21 ARQUÉTIPOS GALÁCTICOS
# ==========================================================
# A atualização pós-2010 da Lei do Tempo (Stephanie South / Foundation for the
# Law of Time): os 20 selos ganham um 21º arquétipo central, o Hunab Ku, e se
# organizam em 5 Cortes Cósmicas. É a camada arquetípica — o "quem" por trás do
# selo. Fonte: conteudo-autoral/atualizacoes-profundidade-tzolkin-hunab-ku-21.md
#
# (arquétipo, corte, atributo psíquico transmitido)

HUNAB_KU_21 = {
    1:  ('A Força Primordial',   'Conhecimento', 'a memória cósmica do ser e a nutrição original'),
    2:  ('O Sumo Sacerdote',     'Conhecimento', 'a comunicação do espírito e o sopro divino'),
    3:  ('O Sonhador',           'Conhecimento', 'a abundância intuitiva e a visão dos mundos sutis'),
    4:  ('O Inocente',           'Conhecimento', 'o florescimento do alvo e a pureza do potencial'),
    5:  ('O Iniciado',           'Conhecimento', 'a força vital, a kundalini e a regeneração'),
    6:  ('O Hierofante',         'Amor',         'a arte do desapego e as pontes entre mundos'),
    7:  ('O Avatar',             'Amor',         'a realização concreta e a ação que cura'),
    8:  ('O Artista',            'Amor',         'a harmonia da proporção e a elegância viva'),
    9:  ('A Curandeira',         'Amor',         'a purificação das águas e a cura emocional'),
    10: ('O Compassivo',         'Amor',         'o amor incondicional e a abertura do coração'),
    11: ('O Mágico',             'Profecia',     'a alquimia do humor e a quebra de ilusões'),
    12: ('O Sábio',              'Profecia',     'o livre-arbítrio e a sabedoria terrena'),
    13: ('O Profeta',            'Profecia',     'a exploração do espaço e a vigília dimensional'),
    14: ('O Mago do Infinito',   'Profecia',     'a atemporalidade, o silêncio da mente e o agora'),
    15: ('O Vidente',            'Profecia',     'a mente superior e a visão de longo alcance'),
    16: ('O Descobridor',        'Inteligência', 'a coragem de questionar e a inteligência destemida'),
    17: ('O Navegador',          'Inteligência', 'a sincronicidade e a evolução junto com a Terra'),
    18: ('O Yogi',               'Inteligência', 'o discernimento límpido e a verdade sem enfeite'),
    19: ('O Mudador de Mundos',  'Inteligência', 'a autogeração de energia e a catarse que transmuta'),
    20: ('O Iluminado',          'Inteligência', 'o fogo universal, a maestria e a vida plena'),
    21: ('O Magus do Infinito',  'Central',      'a unidade suprema que governa todo movimento e medida'),
}

CORTES = {
    'Conhecimento': ('Leste', 'onde a consciência entra e aprende', 'do'),
    'Amor':         ('Norte', 'onde a consciência se abre e acolhe', 'do'),
    'Profecia':     ('Oeste', 'onde a consciência enxerga e antecipa', 'da'),
    'Inteligência': ('Sul',   'onde a consciência amadurece e decide', 'da'),
    'Central':      ('Centro', 'a fonte de onde tudo parte', ''),
}


def arquetipo_de(seal: int) -> dict:
    nome, corte, atributo = HUNAB_KU_21[seal]
    direcao, sentido, artigo = CORTES[corte]
    rotulo = f'Corte {artigo} {corte}'.replace('  ', ' ').strip()
    return {'nome': nome, 'corte': corte, 'atributo': atributo,
            'direcao': direcao, 'sentido': sentido, 'rotulo': rotulo}


# ==========================================================
# ONDAS ENCANTADAS, CASTELOS, CÉLULAS, PORTAIS
# ==========================================================

ONDAS = [
    (1, 'Dragão Vermelho', 'Iniciação e confiança primordial'),
    (14, 'Mago Branco', 'Atemporalidade e presença pura'),
    (27, 'Mão Azul', 'Cura e realização na matéria'),
    (40, 'Sol Amarelo', 'Iluminação e fogo universal'),
    (53, 'Caminhante do Céu Vermelho', 'Exploração e quebra de limites'),
    (66, 'Enlaçador de Mundos Branco', 'Desapego e morte sagrada'),
    (79, 'Tormenta Azul', 'Autogeração e catarse construtiva'),
    (92, 'Humano Amarelo', 'Livre-arbítrio e sabedoria vivida'),
    (105, 'Serpente Vermelha', 'Força vital e regeneração'),
    (118, 'Espelho Branco', 'Verdade nua e discernimento'),
    (131, 'Macaco Azul', 'Magia da ilusão e leveza lúcida'),
    (144, 'Semente Amarela', 'Foco e florescimento do potencial'),
    (157, 'Terra Vermelha', 'Navegação e sincronicidade com Gaia'),
    (170, 'Cão Branco', 'Amor incondicional e lealdade'),
    (183, 'Noite Azul', 'Intuição e abundância invisível'),
    (196, 'Guerreiro Amarelo', 'Inteligência e coragem ética'),
    (209, 'Lua Vermelha', 'Purificação e fluxo universal'),
    (222, 'Vento Branco', 'Comunicação e espírito'),
    (235, 'Águia Azul', 'Visão panorâmica e mente superior'),
    (248, 'Estrela Amarela', 'Arte, elegância e harmonia'),
]

CASTELOS = {
    1: ('Castelo Vermelho do Leste', 'do Nascimento', 'Fundar as bases: lançar projetos e dar o primeiro passo.'),
    2: ('Castelo Branco do Norte', 'da Purificação', 'Refinar a mente, desapegar do que não serve, perdoar.'),
    3: ('Castelo Azul do Oeste', 'da Transformação', 'O coração alquímico: transmutar dores e quebrar padrões.'),
    4: ('Castelo Amarelo do Sul', 'do Florescimento', 'Colher os frutos e ancorar a sabedoria com maturidade.'),
    5: ('Castelo Verde Central', 'da Matriz', 'Sintetizar a jornada, partilhar e preparar o próximo ciclo.'),
}

CELULAS = {
    1: ('Entrada', 'Informar a matriz'),
    2: ('Armazém', 'Lembrar a verdade'),
    3: ('Processo', 'Formular a visão'),
    4: ('Saída', 'Expressar o florescimento'),
}

# 52 Portais de Ativação Galáctica
PAGS = frozenset({
    1, 20, 22, 39, 43, 50, 51, 58, 64, 69, 72, 77, 85, 88, 93, 96,
    106, 107, 108, 109, 110, 111, 112, 113, 114, 115,
    146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
    165, 168, 173, 176, 184, 189, 192, 197, 203, 208, 211, 218, 222, 239, 241, 260,
})

# Pulsares dimensionais
PULSARES = {
    1: ('Pulsar do Tempo', '4ª dimensão', (1, 5, 9, 13)),
    2: ('Pulsar dos Sentidos', '1ª dimensão', (2, 6, 10)),
    3: ('Pulsar da Mente', '2ª dimensão', (3, 7, 11)),
    4: ('Pulsar da Forma', '3ª dimensão', (4, 8, 12)),
}

_PULSAR_POR_TOM = {t: p for p, (_, _, tons) in PULSARES.items() for t in tons}


# ==========================================================
# ORÁCULO DAS 5 FORÇAS
# ==========================================================

def _selo_analogo(s: int) -> int:
    if s <= 18:
        return 19 - s
    return 20 if s == 19 else 19


def _selo_antipoda(s: int) -> int:
    return ((s + 9) % 20) + 1


_GUIA_SHIFT = {1: 0, 6: 0, 11: 0, 2: 12, 7: 12, 12: 12,
               3: 4, 8: 4, 13: 4, 4: 16, 9: 16, 5: 8, 10: 8}


def _selo_guia(s: int, t: int) -> int:
    return ((s - 1 + _GUIA_SHIFT[t]) % 20) + 1


def oracle(kin: int) -> dict:
    """Cruz de 5 forças. Retorna só números de Kin — texto é responsabilidade de mensagens.py."""
    s, t = seal_of(kin), tone_of(kin)
    guia = kin_from(_selo_guia(s, t), t)
    analogo = kin_from(_selo_analogo(s), t)
    antipoda = kin_from(_selo_antipoda(s), t)
    oculto = 261 - kin
    quinta = ((kin + guia + analogo + antipoda + oculto - 1) % 260) + 1
    return {'destino': kin, 'guia': guia, 'analogo': analogo,
            'antipoda': antipoda, 'oculto': oculto, 'quinta': quinta}


def relacao_com(kin_referencia: int, kin_alvo: int):
    """Como kin_alvo se relaciona com kin_referencia. Devolve a chave ou None.

    É o cruzamento que transforma broadcast em leitura: 'hoje é o seu antípoda'.
    """
    o = oracle(kin_referencia)
    for chave in ('destino', 'guia', 'analogo', 'antipoda', 'oculto', 'quinta'):
        if o[chave] == kin_alvo:
            return chave
    if seal_of(kin_referencia) == seal_of(kin_alvo):
        return 'mesmo_selo'
    if tone_of(kin_referencia) == tone_of(kin_alvo):
        return 'mesmo_tom'
    return None


# ==========================================================
# SINCRONÁRIO DAS 13 LUAS
# ==========================================================

LUAS = [
    ('Magnética do Morcego', 'Unificar o propósito'),
    ('Lunar do Escorpião', 'Identificar o desafio'),
    ('Elétrica do Veado', 'Ativar o serviço'),
    ('Autoexistente da Coruja', 'Definir a forma'),
    ('Harmônica do Pavão', 'Potencializar o comando'),
    ('Rítmica do Lagarto', 'Organizar o equilíbrio'),
    ('Ressonante do Macaco', 'Canalizar a inspiração'),
    ('Galáctica do Falcão', 'Harmonizar a integridade'),
    ('Solar do Jaguar', 'Pulsar a intenção'),
    ('Planetária do Cão', 'Aperfeiçoar a manifestação'),
    ('Espectral da Serpente', 'Dissolver o apego'),
    ('Cristal do Coelho', 'Dedicar a cooperação'),
    ('Cósmica da Tartaruga', 'Perseverar a presença'),
]

PLASMAS = [
    ('Dali', 'Coronário', 'Alinhar com a Fonte'),
    ('Seli', 'Raiz', 'Aterrar a força física'),
    ('Gamma', 'Terceiro Olho', 'Pacificar a mente'),
    ('Kali', 'Sexual', 'Catalisar a criação'),
    ('Alfa', 'Laríngeo', 'Liberar a palavra'),
    ('Limi', 'Plexo Solar', 'Purificar a vontade'),
    ('Silio', 'Cardíaco', 'Descarregar a tensão'),
]


def moon_info(d: datetime.date) -> dict:
    """Posição no calendário de 13 luas. Ano começa em 26/07."""
    if d.month == 7 and d.day == 25:
        return {'fora_do_tempo': True, 'lua': 'Dia Fora do Tempo',
                'acao': 'Celebrar a paz e a arte', 'dia_da_lua': 0,
                'plasma': ('Silio', 'Cardíaco', 'Descarregar a tensão'), 'heptada': 52}

    inicio_ano = datetime.date(d.year, 7, 26)
    if d < inicio_ano:
        inicio_ano = datetime.date(d.year - 1, 7, 26)

    # O 29/02 também não é contado no calendário de 13 luas: sem esta correção
    # a contagem da lua desanda em 1 dia depois de todo bissexto.
    desde = (d - inicio_ano).days - (_feb29_count(d) - _feb29_count(inicio_ano))
    lua_num = min(desde // 28 + 1, 13)
    dia_da_lua = desde % 28 + 1
    return {
        'fora_do_tempo': False,
        'lua_num': lua_num,
        'lua': f'Lua {LUAS[lua_num - 1][0]}',
        'acao': LUAS[lua_num - 1][1],
        'dia_da_lua': dia_da_lua,
        'plasma': PLASMAS[(dia_da_lua - 1) % 7],
        'heptada': desde // 7 + 1,
    }


# ==========================================================
# AGREGADOR
# ==========================================================

def kin_data(kin: int) -> dict:
    """Tudo que se sabe estruturalmente sobre um Kin. Sem uma linha de texto de leitura."""
    s_num, t_num = seal_of(kin), tone_of(kin)
    selo = SELOS[s_num]
    tom = TONS[t_num]

    onda_idx = max(i for i, (inicio, _, _) in enumerate(ONDAS) if inicio <= kin)
    onda_inicio, onda_nome, onda_tema = ONDAS[onda_idx]

    castelo_num = (kin - 1) // 52 + 1
    celula_num = (s_num - 1) // 5 + 1
    pulsar_num = _PULSAR_POR_TOM[t_num]

    return {
        'kin': kin,
        'selo_num': s_num,
        'tom_num': t_num,
        'selo': selo,
        'selo_nome': SELO_NOME_COMPLETO[s_num],
        'tom': tom,
        'cla': selo['cla'],
        'cla_info': CLAS[selo['cla']],
        'nome': nome_do_kin(kin),
        'familia': familia_de(s_num),
        'onda': {'inicio': onda_inicio, 'nome': onda_nome, 'tema': onda_tema,
                 'degrau': kin - onda_inicio + 1,
                 'artigo': artigo_do_selo(seal_of(onda_inicio))},
        'castelo': {'num': castelo_num, 'nome': CASTELOS[castelo_num][0],
                    'corte': CASTELOS[castelo_num][1], 'missao': CASTELOS[castelo_num][2],
                    'dia': (kin - 1) % 52 + 1},
        'celula': {'num': celula_num, 'nome': CELULAS[celula_num][0], 'funcao': CELULAS[celula_num][1]},
        'arquetipo': arquetipo_de(s_num),
        'pulsar': {'num': pulsar_num, 'nome': PULSARES[pulsar_num][0], 'dimensao': PULSARES[pulsar_num][1]},
        'is_pag': kin in PAGS,
        'is_coluna_mistica': 121 <= kin <= 140,
        'is_ponto_zero': kin in (130, 131),
        'harmonica': (kin - 1) // 4 + 1,
    }


def kin_do_dia(d: datetime.date = None) -> dict:
    d = d or datetime.date.today()
    dados = kin_data(calculate_kin(d))
    dados['data'] = d
    dados['lua'] = moon_info(d)
    return dados


# ==========================================================
# O DECRETO — a fórmula tradicional do Dreamspell
# ==========================================================
# Estrutura canônica de 5 versos:
#   Eu {verbo do tom} a fim de {ação do selo}
#   {gerúndio do tom} {essência do selo}
#   Selo {processo} {poder do selo}
#   Com o tom {n} {nome} {qualidade do tom}
#   Guia-me o poder {do selo-guia}
#
# O processo do 3º verso vai em blocos de 5 selos, e é onde o texto gerado
# em 2025 errava: dizia "armazém da atemporalidade" para o Mago, que é o
# selo 14 e portanto está no bloco do PROCESSO, não do armazém.

_PROCESSO = ('a entrada', 'o armazém', 'o processo', 'a produção')

# 1ª pessoa do singular do verbo do tom
_DECRETO_VERBO = {
    1: 'Unifico', 2: 'Polarizo', 3: 'Ativo', 4: 'Defino', 5: 'Potencializo',
    6: 'Organizo', 7: 'Canalizo', 8: 'Harmonizo', 9: 'Pulso', 10: 'Aperfeiçoo',
    11: 'Dissolvo', 12: 'Dedico', 13: 'Persevero',
}

# Gerúndio canônico. Não é derivado do verbo da tabela TONS de propósito:
# "Cooperando a receptividade" não existe em português — o cânone usa
# "Universalizando", que é transitivo e fecha o verso.
_DECRETO_GERUNDIO = {
    1: 'Atraindo', 2: 'Estabilizando', 3: 'Vinculando', 4: 'Medindo',
    5: 'Comandando', 6: 'Equilibrando', 7: 'Inspirando', 8: 'Modelando',
    9: 'Realizando', 10: 'Produzindo', 11: 'Libertando', 12: 'Universalizando',
    13: 'Transcendendo',
}

# Gênero dos substantivos, para o artigo sair certo em todos os 260 kins.
_ART_ESSENCIA = {
    1: 'o', 2: 'o', 3: 'a', 4: 'a', 5: 'o', 6: 'a', 7: 'a', 8: 'a', 9: 'o',
    10: 'a', 11: 'a', 12: 'a', 13: 'a', 14: 'a', 15: 'a', 16: 'a', 17: 'a',
    18: 'a', 19: 'a', 20: 'a',
}
_ART_PODER = {
    1: 'do', 2: 'do', 3: 'da', 4: 'do', 5: 'da', 6: 'da', 7: 'da', 8: 'da',
    9: 'da', 10: 'do', 11: 'da', 12: 'do', 13: 'do', 14: 'da', 15: 'da',
    16: 'da', 17: 'da', 18: 'do', 19: 'da', 20: 'do',
}
_ART_QUALIDADE = {
    1: 'do', 2: 'do', 3: 'do', 4: 'da', 5: 'da', 6: 'da', 7: 'da', 8: 'da',
    9: 'da', 10: 'da', 11: 'da', 12: 'da', 13: 'da',
}


def decreto(kin: int) -> str:
    """Os 5 versos do Kin, com concordância conferida nos 260."""
    s, t = seal_of(kin), tone_of(kin)
    selo, tom = SELOS[s], TONS[t]
    guia_s = seal_of(oracle(kin)['guia'])
    if guia_s == s:
        verso5 = 'Guia-me o meu próprio poder, duplicado.'
    else:
        verso5 = f"Guia-me o poder {_ART_PODER[guia_s]} {SELOS[guia_s]['poder']}."
    return (f"{_DECRETO_VERBO[t]} a fim de {selo['acao']},\n"
            f"{_DECRETO_GERUNDIO[t]} {_ART_ESSENCIA[s]} {selo['essencia']}.\n"
            f"Selo {_PROCESSO[(s - 1) // 5]} {_ART_PODER[s]} {selo['poder']}\n"
            f"com o tom {t} {tom[0].lower()} {_ART_QUALIDADE[t]} {tom[3].lower()}.\n"
            f"{verso5}")
