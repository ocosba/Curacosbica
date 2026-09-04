# -*- coding: utf-8 -*-
"""
ESTRUTURA C — o ciclo anual.

O bloco que faltava em todos os textos de referência. Nenhum deles dizia a
coisa mais útil que existe sobre um ano de vida: **como o Kin do ano se
relaciona com o Kin de nascimento da pessoa.**

Exemplo real: Fabio, Kin 136 (Guerreiro). Aos 46 anos ele está sob o Kin 26,
Enlaçador — que é exatamente o Mestre de Atrito dele. Um ano inteiro habitando
o próprio antípoda. O texto entregue não disse isso, e era a leitura mais forte
possível daquele mapa.

A regularidade que sustenta tudo (e que também não estava escrita em lugar nenhum):
    365 - 260 = 105 kins de avanço por ano
    105 mod 13 = 1   → o TOM avança 1 a cada aniversário
    105 mod 20 = 5   → o SELO avança 5 a cada aniversário
Logo: o selo volta a cada 4 anos, com um tom mais maduro; e em 52 anos
(4 x 13) tom e selo fecham juntos, de volta ao Kin de nascimento.
"""

import datetime

from . import core


def _aniversario(nascimento: datetime.date, ano: int) -> datetime.date:
    try:
        return nascimento.replace(year=ano)
    except ValueError:          # 29/02 em ano comum
        return datetime.date(ano, 2, 28)


def ciclo_anual(nascimento: datetime.date, hoje: datetime.date = None,
                adiante: int = 2) -> dict:
    """Ano corrente + os próximos, com a relação de cada um com o Kin natal."""
    hoje = hoje or datetime.date.today()
    natal = core.calculate_kin(nascimento)

    # Aniversário vigente: o último que já passou
    ano_base = hoje.year if (hoje.month, hoje.day) >= (nascimento.month, nascimento.day) \
        else hoje.year - 1
    inicio = _aniversario(nascimento, ano_base)
    idade = ano_base - nascimento.year

    anos = []
    for passo in range(0, adiante + 1):
        ini = _aniversario(nascimento, ano_base + passo)
        fim = _aniversario(nascimento, ano_base + passo + 1) - datetime.timedelta(days=1)
        k = core.calculate_kin(ini)
        anos.append({
            'idade': idade + passo,
            'inicio': ini,
            'fim': fim,
            'kin': k,
            'dados': core.kin_data(k),
            'relacao': core.relacao_com(natal, k),
            'corrente': passo == 0,
        })

    # O Retorno Galáctico: aos 52 anos o Kin natal volta exato
    ciclo = idade // 52
    idade_retorno = (ciclo + 1) * 52
    data_retorno = _aniversario(nascimento, nascimento.year + idade_retorno)

    return {
        'natal': natal,
        'idade': idade,
        'inicio_ciclo': inicio,
        'anos': anos,
        'faltam_para_retorno': idade_retorno - idade,
        'idade_retorno': idade_retorno,
        'data_retorno': data_retorno,
        'quadrante': _quadrante(idade % 52),
    }


def _quadrante(idade_no_ciclo: int) -> tuple:
    """Os 52 anos divididos nos 4 castelos da vida."""
    if idade_no_ciclo < 13:
        return ('Castelo Vermelho do Leste', 'do Nascimento', 0, 12,
                'Fundar as bases: descobrir quem se é, formar a identidade e a estrutura.')
    if idade_no_ciclo < 26:
        return ('Castelo Branco do Norte', 'da Purificação', 13, 25,
                'Depurar: quebrar ilusões, lapidar a identidade e aprender pelo atrito.')
    if idade_no_ciclo < 39:
        return ('Castelo Azul do Oeste', 'da Transformação', 26, 38,
                'Transmutar: alianças, carreira, obra no mundo e as grandes viradas.')
    return ('Castelo Amarelo do Sul', 'do Florescimento', 39, 51,
            'Colher: maturidade, maestria e transmissão do que se aprendeu.')


# A leitura mais forte do bloco: o que significa viver um ano regido por
# cada posição do próprio oráculo.
LEITURA_DA_RELACAO = {
    'destino': (
        'ANO DE RETORNO AO SEU KIN',
        'A energia deste ano é a mesma do seu nascimento. Acontece uma vez a cada 52 anos: '
        'não é ano de aprender coisa nova, é o ano de ser com maestria aquilo que você já é.'
    ),
    'guia': (
        'ANO REGIDO PELA SUA BÚSSOLA',
        'O ano inteiro joga a favor da sua direção natural. É um dos melhores ciclos da vida '
        'para tomar decisões grandes.'
    ),
    'analogo': (
        'ANO DE APOIO',
        'O ano é regido pelo seu aliado — menos atrito e mais fluência. Aproveite para destravar '
        'o que estava parado: o custo de mover é menor agora.'
    ),
    'antipoda': (
        'ANO DE DESAFIO',
        'O ano é regido exatamente pelo que mais te tira do sério. Não é azar: é o ciclo em que '
        'a vida te dá a lição que você vem adiando. Quem entende, atravessa e sai maior.'
    ),
    'oculto': (
        'ANO DO TESOURO ESCONDIDO',
        'O ano ativa o seu dom adormecido, aquele que só aparece quando você solta o controle. '
        'Capacidades que você nem sabia que tinha ficam disponíveis.'
    ),
    'quinta': (
        'ANO DE SÍNTESE',
        'O ano soma todas as suas forças. As pontas soltas dos últimos anos tendem a se encaixar.'
    ),
    # Kin exato é raro; o selo da força é 13 vezes mais provável. Estas cinco
    # entradas existem para o ano nunca mais ser chamado de "território novo"
    # quando ele cai justamente sobre uma das forças do mapa da pessoa.
    'selo_guia': (
        'ANO NA DIREÇÃO DA SUA BÚSSOLA',
        'O ano é regido pelo mesmo arquétipo que guia o seu mapa. A direção que você já conhece '
        'fica ativa o ciclo inteiro: é o melhor ano para decidir e para virar a chave.'
    ),
    'selo_analogo': (
        'ANO NO SEU ALIADO',
        'O ano cai sobre o arquétipo que te apoia. Você vai passar 365 dias dentro de uma força '
        'que já trabalha a seu favor — o custo de mover é menor agora do que costuma ser.'
    ),
    'selo_antipoda': (
        'ANO NO SEU TREINO',
        'O ano é regido pelo arquétipo que mais te tira do sério. Não é azar: é o ciclo em que '
        'a lição que você vem adiando fica em cima da mesa todo dia. Quem atravessa, sai maior.'
    ),
    'selo_oculto': (
        'ANO DO DOM QUE DORME',
        'O ano ativa o arquétipo do seu dom escondido, aquele que só aparece quando você solta '
        'o controle. Capacidades que você nem sabia que tinha ficam à mão.'
    ),
    'selo_quinta': (
        'ANO DE SÍNTESE',
        'O ano cai sobre a soma das suas cinco forças. As pontas soltas dos últimos ciclos '
        'tendem a se encaixar.'
    ),
    'mesmo_selo': (
        'ANO DO SEU PRÓPRIO ARQUÉTIPO',
        'O mesmo arquétipo do seu nascimento volta, num ritmo mais maduro. Acontece a cada quatro '
        'anos: você não está aprendendo algo novo, está sendo convocado a viver quem você é num '
        'nível mais alto.'
    ),
    'mesmo_tom': (
        'ANO NO SEU PRÓPRIO RITMO',
        'O tema é outro, mas a cadência é a sua. Tende a ser um ano em que você se sente no seu tempo.'
    ),
    None: (
        'ANO DE TERRITÓRIO NOVO',
        'O ano traz uma energia que não está no seu mapa. É aprendizado por fora — e é aí que a sua '
        'caixa de ferramentas cresce.'
    ),
}


REGRA_DO_CICLO = (
    'Todo aniversário o seu ritmo avança uma casa e o seu arquétipo, cinco. '
    'Por isso o arquétipo volta a cada 4 anos, mais maduro — e aos 52 os dois fecham juntos.'
)
