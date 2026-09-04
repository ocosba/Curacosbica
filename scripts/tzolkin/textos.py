# -*- coding: utf-8 -*-
"""
Camada ACESSÍVEL — o texto que vai para grupo de WhatsApp.

Regra de ouro deste arquivo: uma pessoa que nunca ouviu falar de Kin
tem que entender TUDO sem precisar de glossário. Zero jargão.

Nada aqui usa as palavras: selo solar, tom galáctico, oráculo, antípoda,
quinta força, PAG, coluna mística, decreto, portal, harmônica, hólon.
Esses termos existem — mas moram em textos_profundos.py, na aula do Leo.

Cada selo tem 8 campos, e cada um é usado numa posição diferente da leitura:
  frase  → manchete do dia quando este selo rege
  flui   → o que anda fácil
  trava  → onde a pessoa tropeça
  acao   → a única coisa a fazer (80/20: uma, não sete)
  guia   → usado quando este selo é o guia do dia
  apoio  → usado quando este selo é o aliado do dia
  tira   → usado quando este selo é o desafio. É O GANCHO DE CAPTAÇÃO:
           é a linha em que a pessoa se reconhece e manda mensagem.
  dom    → usado quando este selo é o dom escondido
"""

ACESSIVEL = {
    1: {
        'frase': 'Dia de começar algo — e de se deixar cuidar.',
        'flui': 'começar do zero, acolher, cuidar de quem precisa',
        'trava': 'achar que precisa dar conta de tudo sozinho',
        'acao': 'comece uma coisa nova hoje. Pequena, mas comece',
        'guia': 'quando travar, cuide da base — comida, água, sono. O resto vem depois',
        'apoio': 'você tem chão firme. Pode confiar que a vida sustenta',
        'tira': 'gente carente, que puxa você pra dentro do problema dela',
        'dom': 'você já foi sustentado em coisa muito pior do que essa',
    },
    2: {
        'frase': 'Dia de falar o que está engasgado.',
        'flui': 'falar com clareza, escrever, gravar, escutar de verdade',
        'trava': 'falar demais sem dizer nada — ou engolir e ficar remoendo',
        'acao': 'diga hoje aquela frase que você vem adiando',
        'guia': 'respire antes de responder. A resposta melhora sozinha',
        'apoio': 'as palavras saem fáceis. Aproveite',
        'tira': 'gente que fala muito e não escuta nada',
        'dom': 'você sabe traduzir o difícil em simples',
    },
    3: {
        'frase': 'Dia de silêncio, não de decisão.',
        'flui': 'intuição, ideia que aparece sozinha, descanso que rende',
        'trava': 'medo de faltar — e a decisão tomada por esse medo',
        'acao': 'não decida nada grande hoje. Deixe decantar até amanhã',
        'guia': 'a resposta não vem da lógica. Vem do silêncio',
        'apoio': 'tem mais recurso disponível do que você está enxergando',
        'tira': 'gente que enche o ambiente de barulho e urgência',
        'dom': 'você enxerga saída onde os outros só veem parede',
    },
    4: {
        'frase': 'Dia de fazer uma coisa só, bem feita.',
        'flui': 'foco, paciência, cuidado com o detalhe',
        'trava': 'querer que fique perfeito antes de mostrar',
        'acao': 'termine uma coisa que já está quase pronta',
        'guia': 'corte o que não é essencial e vá direto no alvo',
        'apoio': 'você tem paciência de sobra. O processo anda sozinho',
        'tira': 'gente que atropela processo e quer tudo pra ontem',
        'dom': 'você tem talento guardado que ainda não colocou pra fora',
    },
    5: {
        'frase': 'Dia de escutar o corpo antes da cabeça.',
        'flui': 'energia física, instinto certeiro, vontade de se mexer',
        'trava': 'reagir no impulso e depois ter que consertar',
        'acao': 'mexa o corpo hoje — caminhada, alongamento, o que der',
        'guia': 'se o corpo travou, isso é resposta. Escute antes de forçar',
        'apoio': 'sua energia física está do seu lado',
        'tira': 'gente que mexe no seu território ou no seu tempo sem pedir',
        'dom': 'seu corpo sabe o que fazer quando a cabeça não sabe',
    },
    6: {
        'frase': 'Dia de soltar o que já acabou.',
        'flui': 'encerrar ciclo, perdoar, dar adeus sem drama',
        'trava': 'segurar o que já morreu porque dói admitir',
        'acao': 'encerre uma pendência hoje. Mande a mensagem, cancele, feche',
        'guia': 'pergunte o que já acabou e você ainda está segurando',
        'apoio': 'soltar é mais leve do que parece',
        'tira': 'gente que não deixa nada morrer e revive tudo',
        'dom': 'você atravessa perda sem se perder',
    },
    7: {
        'frase': 'Dia de terminar, não de começar.',
        'flui': 'fechar tarefa, cuidar de alguém, resolver com as mãos',
        'trava': 'pegar mais uma coisa quando já tem cinco abertas',
        'acao': 'feche uma coisa que está aberta há tempo demais',
        'guia': 'a resposta está no que você faz, não no que você pensa',
        'apoio': 'você consegue fechar o que está aberto. Escolha o que mais pesa',
        'tira': 'gente que promete e não entrega',
        'dom': 'você acalma os outros só de estar presente',
    },
    8: {
        'frase': 'Dia de deixar bonito o que já existe.',
        'flui': 'acabamento, bom gosto, cuidado com a forma',
        'trava': 'refazer o detalhe pra sempre e nunca entregar',
        'acao': 'dê o acabamento em algo e entregue hoje',
        'guia': 'se está feio ou bagunçado, arrumar isso já destrava',
        'apoio': 'seu senso do que fica bom está afiado',
        'tira': 'gente relaxada com o próprio trabalho',
        'dom': 'você enxerga beleza onde ninguém tinha visto',
    },
    9: {
        'frase': 'Dia de deixar sair o que precisa sair.',
        'flui': 'emoção que flui, choro que alivia, limpeza',
        'trava': 'segurar o sentimento pra não incomodar ninguém',
        'acao': 'beba mais água e deixe a emoção passar sem julgar',
        'guia': 'o que está incomodando quer ser sentido, não resolvido',
        'apoio': 'você é mais sensível que a média — isso é informação, não fraqueza',
        'tira': 'gente fria, que trata sentimento como frescura',
        'dom': 'você sente o clima de um lugar antes de entender por quê',
    },
    10: {
        'frase': 'Dia de estar perto de quem importa.',
        'flui': 'lealdade, afeto simples, proteger os seus',
        'trava': 'dar demais pra quem não retribui',
        'acao': 'procure alguém que você ama e diga por quê',
        'guia': 'pergunte por quem você está fazendo isso',
        'apoio': 'seu coração está aberto. Use isso com quem merece',
        'tira': 'gente desleal, que some quando aperta',
        'dom': 'sua lealdade é rara e as pessoas sentem isso',
    },
    11: {
        'frase': 'Dia de levar menos a sério.',
        'flui': 'humor, criatividade, sair do roteiro',
        'trava': 'virar piada pra não ter que sentir',
        'acao': 'faça algo hoje só porque é divertido',
        'guia': 'se está pesado demais, você comprou uma ilusão em algum lugar',
        'apoio': 'a leveza abre porta que a força não abre',
        'tira': 'gente rígida, séria demais, sem humor nenhum',
        'dom': 'você desmonta situação travada só mudando o tom',
    },
    12: {
        'frase': 'Dia de escolher, não de aceitar.',
        'flui': 'decidir com maturidade, influenciar pelo exemplo',
        'trava': 'deixar os outros decidirem por você e reclamar depois',
        'acao': 'tome hoje uma decisão que você vem empurrando',
        'guia': 'pergunte o que você quer, não o que esperam de você',
        'apoio': 'seu bom senso está apurado. Confie nele',
        'tira': 'gente que decide por você sem perguntar',
        'dom': 'as pessoas mudam de ideia quando escutam você',
    },
    13: {
        'frase': 'Dia de sair da bolha.',
        'flui': 'explorar, conhecer gente nova, mudar de ambiente',
        'trava': 'ficar preso na rotina achando que não tem escolha',
        'acao': 'mude uma coisa no seu trajeto de hoje. Qualquer uma',
        'guia': 'se travou, o problema é o lugar, não você',
        'apoio': 'uma porta se abre quando você se mexe',
        'tira': 'gente que quer te prender no lugar de sempre',
        'dom': 'você transita entre mundos diferentes e se adapta',
    },
    14: {
        'frase': 'Dia de estar presente, não de correr.',
        'flui': 'presença, escuta profunda, ambiente que se organiza sozinho',
        'trava': 'querer controlar o tempo e o resultado',
        'acao': 'faça uma coisa hoje sem olhar o relógio',
        'guia': 'pare de empurrar. Fique quieto e veja o que aparece',
        'apoio': 'sua presença já faz metade do trabalho',
        'tira': 'gente apressada, que cobra prazo o tempo inteiro',
        'dom': 'você muda o clima de um lugar só de entrar nele',
    },
    15: {
        'frase': 'Dia de olhar de longe, não de mexer no detalhe.',
        'flui': 'visão de conjunto, planejar, enxergar o que vem',
        'trava': 'ficar na cabeça e não descer pra ação',
        'acao': 'pare vinte minutos e olhe o quadro inteiro antes de agir',
        'guia': 'suba um degrau e olhe o todo antes de decidir',
        'apoio': 'você enxerga longe. Anote o que vier',
        'tira': 'gente perdida no detalhe, que não vê o todo',
        'dom': 'você vê o que ainda não aconteceu',
    },
    16: {
        'frase': 'Dia de perguntar o que ninguém quer perguntar.',
        'flui': 'coragem, encarar a conversa difícil, questionar',
        'trava': 'engolir por medo do conflito',
        'acao': 'faça hoje a pergunta que você tem medo de fazer',
        'guia': 'a saída está na pergunta que você vem evitando',
        'apoio': 'você tem coragem sobrando. Use bem',
        'tira': 'gente que foge de conversa direta',
        'dom': 'você não se abala no conflito quando ele é necessário',
    },
    17: {
        'frase': 'Dia de prestar atenção nos sinais.',
        'flui': 'coincidência útil, encontro na hora certa, alinhamento',
        'trava': 'forçar caminho que a vida já está fechando',
        'acao': 'repare no que se repetir hoje. Isso é informação',
        'guia': 'se está dando errado demais, o caminho não é esse',
        'apoio': 'a vida está abrindo porta. Você só precisa reparar',
        'tira': 'gente que atropela sinal e força tudo no braço',
        'dom': 'você percebe a direção certa antes da lógica confirmar',
    },
    18: {
        'frase': 'Dia de encarar a verdade sem enfeite.',
        'flui': 'clareza, honestidade, arrumar o que está bagunçado',
        'trava': 'dureza consigo mesmo, cobrança que não ajuda em nada',
        'acao': 'arrume um espaço físico hoje. A cabeça segue atrás',
        'guia': 'o que te incomoda no outro é o que você ainda não olhou em você',
        'apoio': 'a verdade está acessível. Não fuja dela',
        'tira': 'gente falsa, que diz uma coisa e faz outra',
        'dom': 'você enxerga através das máscaras',
    },
    19: {
        'frase': 'Dia de mudança brusca. Deixe acontecer.',
        'flui': 'energia alta, mudança rápida, transformação',
        'trava': 'querer segurar no lugar o que já está mudando',
        'acao': 'se algo desabar hoje, não remende. Deixe cair',
        'guia': 'a crise de hoje é a limpeza que você mesmo pediu',
        'apoio': 'você gera a própria energia. Não depende de ninguém',
        'tira': 'gente que joga o caos dela em cima de você',
        'dom': 'você se reinventa mais rápido do que imagina',
    },
    20: {
        'frase': 'Dia de aparecer inteiro.',
        'flui': 'clareza, generosidade, presença que aquece',
        'trava': 'querer ser o centro — ou se apagar pra não incomodar',
        'acao': 'apareça hoje. Publique, fale, mostre o que você faz',
        'guia': 'seja o exemplo em vez de dar o conselho',
        'apoio': 'você tem calor de sobra. Aqueça alguém',
        'tira': 'gente que precisa ser o centro de tudo',
        'dom': 'sua presença ilumina sem você fazer esforço',
    },
}

# ==========================================================
# OS 13 TONS, EM LINGUAGEM DE GENTE
# ==========================================================
# 'ritmo'  = o que o dia pede
# 'peso'   = dia de alavancagem? (marca os dias de virada, conforme
#            as aplicações estratégicas: 1 atrai, 5 comanda, 10 colhe, 13 solta)

TONS_ACESSIVEL = {
    1:  {'ritmo': 'Primeiro dia de um ciclo de 13. Hoje se planta a intenção.', 'peso': 'Bom dia para começar e para chamar atenção.'},
    2:  {'ritmo': 'Dia de ver o obstáculo. Não é problema — é informação.', 'peso': None},
    3:  {'ritmo': 'Dia de colocar em movimento e envolver gente.', 'peso': None},
    4:  {'ritmo': 'Dia de dar forma: estruturar, medir, organizar.', 'peso': None},
    5:  {'ritmo': 'Dia de reunir o que você tem e assumir o comando.', 'peso': 'Bom dia para liderar e para se posicionar.'},
    6:  {'ritmo': 'Dia de equilibrar e organizar a rotina.', 'peso': None},
    7:  {'ritmo': 'Dia de sintonizar: escutar mais do que agir.', 'peso': None},
    8:  {'ritmo': 'Dia de checar se você vive aquilo que fala.', 'peso': None},
    9:  {'ritmo': 'Dia de realizar de verdade. Ação concreta.', 'peso': None},
    10: {'ritmo': 'Dia de colher. O resultado do ciclo aparece agora.', 'peso': 'Bom dia para fechar negócio e para cobrar.'},
    11: {'ritmo': 'Dia de soltar. Não force nada.', 'peso': None},
    12: {'ritmo': 'Dia de cooperar e dividir com os outros.', 'peso': 'Bom dia para acordo e para parceria.'},
    13: {'ritmo': 'Último dia do ciclo. Feche, celebre e descanse.', 'peso': 'Bom dia para encerrar e para descansar.'},
}

# Onde o ciclo de 13 dias está — usado na linha da onda
FASE_DA_ONDA = {
    'inicio': 'fase de plantar a intenção',
    'forma': 'fase de dar forma, ainda não de colher',
    'fluxo': 'fase de execução, com o motor já ligado',
    'colheita': 'fase de colher e universalizar',
    'fechamento': 'fecho do ciclo — hora de soltar',
}


def fase_do_degrau(degrau: int) -> str:
    if degrau <= 3:
        return FASE_DA_ONDA['inicio']
    if degrau <= 6:
        return FASE_DA_ONDA['forma']
    if degrau <= 9:
        return FASE_DA_ONDA['fluxo']
    if degrau <= 12:
        return FASE_DA_ONDA['colheita']
    return FASE_DA_ONDA['fechamento']


# ==========================================================
# COMO O DIA CONVERSA COM O KIN DA PESSOA
# ==========================================================
# Usado quando se conhece a data de nascimento (/meukin e a aula do Leo).
# É o que transforma broadcast em leitura.

RELACAO = {
    'destino': 'Hoje é o SEU dia — a energia de hoje é a mesma com que você nasceu. Acontece 1 vez a cada 260 dias. Aproveite.',
    'guia': 'Hoje o dia trabalha a favor da sua direção natural. Bom dia para decidir.',
    'analogo': 'Hoje o dia te apoia. Empurre o que estava travado — vai render mais que o normal.',
    'antipoda': 'Hoje o dia te desafia. Não é um dia ruim: é um dia de treino. Repare no que te irritar.',
    'oculto': 'Hoje aparece o seu lado escondido. Coisa que você não usa sempre fica disponível.',
    'quinta': 'Hoje o dia soma com tudo o que você é. Dia de síntese.',
    'mesmo_selo': 'Hoje carrega o mesmo arquétipo do seu nascimento, em outro ritmo. Familiar.',
    'mesmo_tom': 'Hoje pulsa no mesmo ritmo do seu nascimento. O andamento do dia é o seu.',
    # As cinco de baixo entraram em 04/09/2026. Em 03/09 o relacao_com passou a
    # reconhecer também o SELO de cada força, não só o Kin exato — e a aula, que
    # lê esta tabela direto, quebrava com KeyError em 60 dos 260 dias do ciclo.
    # Kin exato bate 1 vez em 260; o selo da força bate 13 vezes.
    'selo_guia': 'Hoje o arquétipo que guia o seu mapa está regendo o dia. Bom dia para decidir e para virar chave.',
    'selo_analogo': 'Hoje o dia cai no arquétipo que te apoia. O custo de mover é menor: empurre o que estava travado.',
    'selo_antipoda': 'Hoje o dia cai no arquétipo que mais te tira do sério. Dia de treino — repare no que te irritar.',
    'selo_oculto': 'Hoje o arquétipo do seu dom escondido está no ar. Capacidade que você não usa sempre fica à mão.',
    'selo_quinta': 'Hoje o dia cai na soma das suas cinco forças. Ponta solta tende a se encaixar.',
}

# A frase de identidade de cada selo — usada no mapa pessoal, onde não se fala
# do "dia" e sim de quem a pessoa é.
NATAL = {
    1:  'Você veio para começar coisas e para cuidar.',
    2:  'Você veio para falar o que precisa ser dito.',
    3:  'Você veio para sonhar e enxergar no escuro.',
    4:  'Você veio para fazer bem feito, no tempo certo.',
    5:  'Você veio com o corpo e o instinto como bússola.',
    6:  'Você veio para atravessar fins e recomeços.',
    7:  'Você veio para terminar e para curar com as mãos.',
    8:  'Você veio para deixar o mundo mais bonito.',
    9:  'Você veio para sentir e para deixar fluir.',
    10: 'Você veio para amar com lealdade.',
    11: 'Você veio para trazer leveza onde tudo pesa.',
    12: 'Você veio para escolher e para influenciar pelo exemplo.',
    13: 'Você veio para explorar e para não caber em caixa.',
    14: 'Você veio para estar presente e encantar sem esforço.',
    15: 'Você veio para enxergar longe.',
    16: 'Você veio para perguntar o que ninguém pergunta.',
    17: 'Você veio para navegar pelos sinais.',
    18: 'Você veio para refletir a verdade sem enfeite.',
    19: 'Você veio para transformar e mover o que está parado.',
    20: 'Você veio para iluminar sendo quem você é.',
}

# O que cada tom faz, já conjugado — evita "Você definir forma".
TOM_FRASE = {
    1:  'unifica o propósito',
    2:  'polariza o desafio',
    3:  'ativa o serviço',
    4:  'define a forma',
    5:  'potencializa o comando',
    6:  'organiza o equilíbrio',
    7:  'canaliza a sintonia',
    8:  'harmoniza a integridade',
    9:  'pulsa a intenção',
    10: 'aperfeiçoa a manifestação',
    11: 'dissolve o apego',
    12: 'dedica a cooperação',
    13: 'perdura na presença',
}

# ==========================================================
# GLOSSÁRIO — O TERMO E A TRADUÇÃO, NA MESMA LINHA
# ==========================================================
# A mensagem pública usa os termos técnicos DE PROPÓSITO, para a pessoa ir se
# familiarizando. Mas nenhum termo aparece sozinho: sempre vem com a explicação
# curta e com a origem. É assim que iniciante vira estudante e especialista
# continua achando o texto sério.

GLOSSARIO = {
    'kin': 'Kin é o "dia" no calendário maia de 260 dias. São 260 combinações possíveis, e cada uma se repete a cada 260 dias.',
    'selo': 'O Selo Solar é o arquétipo do dia — 20 no total. Diz QUAL é a energia.',
    'tom': 'O Tom Galáctico é o ritmo — 13 no total. Diz COMO essa energia se move.',
    'assinatura': 'Selo + Tom formam a Assinatura Galáctica: os 20 arquétipos vezes os 13 ritmos dão os 260 Kins.',
    'onda': 'A Onda Encantada é um ciclo de 13 dias com começo, meio e fim. São 20 ondas que cobrem os 260 dias.',
    'castelo': 'Os Castelos são 5 blocos de 52 dias que dividem o ciclo de 260. Cada um tem uma tarefa maior.',
    'oraculo': 'O Oráculo são 4 forças que cercam o dia — como um mapa de bússola. Vem da matemática do Tzolkin, não de adivinhação.',
    'guia': 'O Guia é para onde a energia do dia aponta quando você trava.',
    'analogo': 'O Análogo é a força que apoia — o que anda fácil hoje.',
    'antipoda': 'O Antípoda é a força que desafia — o que tira você do sério. É o mais útil dos quatro.',
    'oculto': 'O Oculto é o recurso escondido — o que você tem e não costuma usar.',
    'quinta': 'A Quinta Força é a soma das outras: a síntese do dia.',
    'familia': 'A Família Terrestre agrupa os selos de 5 em 5 e liga cada um a um centro do corpo. É a ponte entre o dia e a sua biologia.',
    'pag': 'Portal de Ativação Galáctica: 52 dias do ciclo em que a matriz "abre". Dias de sincronicidade mais forte.',
    'coluna': 'A Coluna Mística são os Kins 121 a 140, a coluna central do tabuleiro. Dias de silêncio e recolhimento.',
    'arquetipo': 'O Hunab Ku 21 é a atualização de 2010 do sistema: cada selo ganha um arquétipo e entra numa das 4 Cortes Cósmicas.',
    'cla': 'As 4 cores são os clãs: Vermelho inicia, Branco refina, Azul transforma, Amarelo amadurece.',
}

# ==========================================================
# OS 13 DEGRAUS DA ONDA ENCANTADA, DESTRINCHADOS
# ==========================================================
# Cada Onda é uma jornada de 13 etapas. Quem nasce num degrau carrega o papel
# daquele degrau na resolução do propósito de toda a onda.

DEGRAUS = {
    1:  ('O PROPÓSITO',     'Por que essa jornada existe. Aqui o tema é atraído e nomeado.'),
    2:  ('O DESAFIO',       'Aparece o obstáculo. A função é enxergar o que vai atrapalhar — não resolver ainda.'),
    3:  ('O SERVIÇO',       'A energia entra em movimento e envolve outras pessoas.'),
    4:  ('A FORMA',         'Define-se o método: como isso vai ser feito na prática.'),
    5:  ('O COMANDO',       'Reúnem-se os recursos e alguém assume o leme.'),
    6:  ('O EQUILÍBRIO',    'Organiza-se o ritmo para o processo não quebrar no meio.'),
    7:  ('A SINTONIA',      'O centro exato da onda. Hora de escutar e corrigir a rota.'),
    8:  ('A INTEGRIDADE',   'Prova de coerência: viver aquilo que se prega.'),
    9:  ('A INTENÇÃO',      'A ação concreta. Aqui se realiza de verdade.'),
    10: ('A MANIFESTAÇÃO',  'O resultado aparece no mundo físico. Colheita.'),
    11: ('A LIBERAÇÃO',     'Solta-se o que sobrou do processo. Desapego.'),
    12: ('A COOPERAÇÃO',    'Divide-se com os outros. O aprendizado vira coletivo.'),
    13: ('A PRESENÇA',      'Fecha-se o ciclo. Celebração, síntese e voo para a próxima onda.'),
}

# ==========================================================
# A PONTE COM A TERAPIA — OS QUATRO CORPOS
# ==========================================================
# É o que conecta o Kin diário ao trabalho clínico do Leo. A Família Terrestre
# aponta um centro no corpo; o centro aponta um corpo do método Cosba.
# Sem isso o Kin fica sendo horóscopo. Com isso, vira leitura de campo.

CHAKRA_CORPO = {
    'Coronário':   ('espiritual', 'conexão, sentido, propósito — quando desalinha, dá desconexão e vazio'),
    'Laríngeo':    ('mental',     'expressão e verdade — quando desalinha, dá garganta travada e conversa engolida'),
    'Cardíaco':    ('emocional',  'vínculo e afeto — quando desalinha, dá aperto no peito e dificuldade de receber'),
    'Plexo Solar': ('emocional',  'poder pessoal e limite — quando desalinha, dá digestão ruim e dificuldade de dizer não'),
    'Raiz':        ('físico',     'segurança e matéria — quando desalinha, dá insegurança, cansaço e aperto financeiro'),
}

# ==========================================================
# ASSINATURA E CHAMADA
# ==========================================================

# Duas linhas: nome com o @ junto, e o que é feito. Aparece igual no Kin do dia
# e no mapa — é o que a pessoa guarda quando encaminha a mensagem pra outra, e
# é por onde chega gente nova pro Instagram.
#
# O @ vai puro, por decisão do Leo em 04/09/2026, ciente de que arroba não vira
# link clicável nem no WhatsApp nem no Telegram (o ponto invalida o nome de
# usuário). Vale mais a assinatura curta do que o toque de dedo.
ASSINATURA = '*Leonardo @o.cosba*\n_Terapeuta multidimensional_'
CHAMADA = 'Quer saber o seu? Me manda sua data de nascimento.'

# Fronteira honesta: usada no fim de toda leitura pessoal.
# Existe para não prometer o que o bot não entrega.
FRONTEIRA = (
    'Isso aqui é um retrato de fora, feito só com a sua data. '
    'É verdadeiro, mas é a superfície. A leitura de verdade vem da conversa.'
)


# ==========================================================
# OS 4 PULSARES — a etiqueta do dia
# ==========================================================
# O pulsar vem do TOM, então muda todo dia e fecha um compasso de 4 batidas
# dentro da onda de 13. Serve para uma coisa só: dizer a CATEGORIA do dia
# numa linha, antes de qualquer detalhe. Quem lê rápido no grupo já sai com
# algo; quem acompanha um mês percebe o ritmo sozinho.
#
# Só no Kin do dia. No mapa pessoal viraria mais um rótulo — já tem clã,
# arquétipo, corte, totem e família.

PULSAR_DIA = {
    1: ('Dia de intenção',
        'é aqui que o ciclo é lançado, comandado e cumprido. Bom para decidir e para ir.'),
    2: ('Dia de sentir',
        'o obstáculo, a rotina e o resultado aparecem pelo que se percebe, não pelo que se pensa.'),
    3: ('Dia de mente',
        'serve para conectar, escutar e soltar. Não é dia de fechar contrato.'),
    4: ('Dia de forma',
        'estruturar, medir, alinhar conduta e dividir com os outros. O que se faz hoje ganha contorno.'),
}


# ==========================================================
# O CORPO NO DIA — a prática regida pelo TOM
# ==========================================================
# Medido em 04/09/2026, em 60 dias seguidos de leitura: o bloco do corpo do
# diário tinha só 5 textos distintos, porque CORPO_FAMILIA é indexada pela
# família terrestre — (selo - 1) % 5 — e o selo anda de 1 em 1 por dia. O bloco
# voltava IGUAL a cada 5 dias, 73 vezes por ano, ocupando 17% da mensagem. Era
# o texto mais previsível do diário.
#
# A família define a REGIÃO, e isso é cânone: não muda. O que passou a variar é
# a prática. Como o tom gira em 13 e a região em 5, o bloco só se repete
# inteiro a cada 65 dias.
#
# Uma frase por tom. Concreta, para fazer hoje, sem jargão — a regra do arquivo.

CORPO_DO_TOM = {
    1:  'Comece o dia pelo corpo, antes do celular: de pé, respirando, sentindo o peso nos pés. O resto se organiza a partir daí.',
    2:  'Alongue os dois lados e repare em qual deles trava mais. O lado duro está segurando o que a sua cabeça ainda não decidiu.',
    3:  'Não se exercite sozinho hoje. Chame alguém, entre num grupo, vá até onde tem gente — o corpo responde melhor acompanhado.',
    4:  'Repare na postura três vezes ao longo do dia e corrija. Pé no chão, coluna longa, mandíbula solta — a forma organiza o resto.',
    5:  'Ocupe espaço com o corpo: ombros abertos, peito livre, queixo no lugar. Encolher hoje custa mais caro do que nos outros dias.',
    6:  'Repita hoje, no mesmo horário, o cuidado que você costuma pular: a água, o intervalo, a hora de deitar. Constância vale mais que intensidade.',
    7:  'Reserve cinco minutos em silêncio, sem tela, só escutando a respiração. O corpo tem um recado hoje, e ele fala baixo.',
    8:  'Confira se o corpo está fazendo o que a boca prometeu. Onde tem incoerência tem tensão — e ela aparece antes de você admitir.',
    9:  'Coloque o corpo em ação de verdade: suor, esforço, movimento que cansa. Hoje a intenção só desce se passar pela musculatura.',
    10: 'Dê ao corpo alguma coisa visível para produzir: lave, guarde, conserte, cozinhe. O cansaço bom vem de ver resultado, não de esforço solto.',
    11: 'Sacuda o corpo por um minuto, de pé, sem coreografia. Tremer solto descarrega o que a conversa não resolveu.',
    12: 'Procure contato: abraço, mão no ombro, andar lado a lado. O corpo regula melhor perto de outro corpo do que sozinho.',
    13: 'Fique parado cinco minutos sem fazer nada, sentado, respirando. Não é preguiça: hoje a presença é o exercício.',
}
