# -*- coding: utf-8 -*-
"""
Material do MAPA PESSOAL — escrito à mão, na régua do conselho.

Substitui o texto que o Antigravity gerava por concatenação de template
("A união do Estrela com o Tom Galáctico convida você a ancorar elegância
através da postura de modelar") — frase que se via a costura e que nenhum
dos textos bons do Leo tinha.

Regras que valem para cada linha daqui:
  1. Nenhum termo aparece sozinho — vem sempre com o que ele é.
  2. Todo termo tem que virar leitura SOBRE A PESSOA, ou é cortado.
  3. A armadilha ganha nome próprio. É o que faz a pessoa se reconhecer.
  4. O corpo é sempre órgão e sintoma nomeado, nunca "desequilíbrio energético".
  5. Português correto. Concordância conferida selo a selo.
"""

# ==========================================================
# A FRASE-MANIFESTO — o momento de arrepio
# ==========================================================
# Primeira pessoa, presente. Substitui o decreto mecânico no texto público.
# Padrão: "Eu sou [imagem]. Através de [3 recursos], eu [verbo do selo] e [efeito]."

MANIFESTO = {
    1:  'Eu sou o útero onde a vida começa. Através da memória ancestral, do cuidado e da confiança primordial, eu nutro o que nasce e sustento quem ainda não aprendeu a se sustentar.',
    2:  'Eu sou o sopro que carrega a verdade. Através da palavra consciente, da respiração e da escuta inteira, eu digo o que precisa ser dito e devolvo espírito às conversas.',
    3:  'Eu sou o silêncio fértil onde a abundância se forma. Através da intuição, do sonho e da quietude, eu enxergo no escuro e trago à luz o que ainda não tinha nome.',
    4:  'Eu sou o potencial que sabe esperar a hora. Através do foco, da paciência e da confiança no tempo, eu planto com precisão e faço florescer o que os outros desistiram de regar.',
    5:  'Eu sou a força vital que atravessa o corpo. Através do instinto, da vitalidade e da coragem de sobreviver, eu sinto antes de pensar e devolvo vida ao que estava adormecido.',
    6:  'Eu sou a ponte viva entre o que se encerra e o que nasce. Através do desapego, da palavra clara e da força da intenção, eu igualo as relações e abro portais onde havia apenas um fim.',
    7:  'Eu sou a força que transforma o caos em obra viva. Através da sabedoria das mãos, da intuição e da coragem do coração, eu realizo a cura e dou forma ao que parecia impossível.',
    8:  'Eu sou a harmonia que revela a beleza escondida. Através do senso de proporção, do cuidado com a forma e do brilho sem arrogância, eu embelezo o que toco e elevo o padrão à minha volta.',
    9:  'Eu sou a água que move o que ficou parado. Através da sensibilidade, do fluxo e da coragem de sentir, eu purifico memórias e devolvo movimento ao que estava represado.',
    10: 'Eu sou a lealdade que não abandona. Através do amor incondicional, da presença fiel e da proteção dos meus, eu sustento os vínculos e lembro as pessoas de que elas importam.',
    11: 'Eu sou a magia que desmonta a ilusão pelo riso. Através do humor sagrado, da espontaneidade e da leveza lúcida, eu quebro o peso do mundo e devolvo o encanto ao cotidiano.',
    12: 'Eu sou o livre-arbítrio que escolhe com consciência. Através do discernimento, da sabedoria vivida e do respeito ao caminho do outro, eu influencio pelo exemplo e devolvo a cada um o próprio poder.',
    13: 'Eu sou o explorador que não cabe em caixa nenhuma. Através da coragem de atravessar, da vigilância desperta e da sede de horizonte, eu rompo limites e abro espaço onde havia parede.',
    14: 'Eu sou a presença que não precisa de pressa. Através do silêncio da mente, da receptividade e do encanto do agora, eu suspendo o tempo e deixo o campo se organizar sozinho.',
    15: 'Eu sou a visão que enxerga o jogo inteiro. Através da mente superior, do voo alto e da estratégia serena, eu vejo o que ainda não aconteceu e traço a rota antes da tempestade.',
    16: 'Eu sou a coragem que faz a pergunta que ninguém faz. Através da inteligência destemida, da integridade e do questionamento lúcido, eu corto o dogma e defendo o que é justo.',
    17: 'Eu sou a navegação que segue os sinais. Através da sincronicidade, da escuta da Terra e da confiança no tempo natural, eu evoluo junto com o caminho e encontro a direção sem forçar.',
    18: 'Eu sou a verdade sem enfeite. Através do discernimento, da ordem e da coragem de olhar o que é, eu reflito o real e liberto quem está pronto para se ver.',
    19: 'Eu sou a tempestade que limpa e regenera. Através da autogeração, da catarse e da coragem de deixar cair, eu transformo o que travou e gero a energia da minha própria mudança.',
    20: 'Eu sou o fogo que ilumina sem consumir. Através da clareza, da generosidade e da maestria de ser inteiro, eu aqueço quem chega perto e mostro o caminho apenas sendo quem sou.',
}

# ==========================================================
# SUPERPODER — o que a pessoa faz melhor que quase todo mundo
# ==========================================================
# Modelo dos textos bons do Leo: contrasta com o que "a maioria" faz.

SUPERPODER = {
    1:  ('O Berço que Sustenta',
         'Você nasceu com a capacidade de fazer o outro se sentir seguro perto de você. Enquanto a maioria das pessoas oferece conselho, você oferece presença — e é isso que efetivamente acalma. Você começa coisas do zero sem precisar de garantia de que vai dar certo, porque confia no processo de gestação.'),
    2:  ('O Tradutor do Invisível',
         'Você tem o dom raro de pegar o que é sutil, confuso ou grande demais e dizer em palavras que qualquer um entende. Enquanto muitos falam para provar que sabem, você fala para que o outro compreenda — e o ambiente se reorganiza quando você diz a verdade com firmeza e doçura.'),
    3:  ('O Visionário do Escuro',
         'Você enxerga possibilidade onde os outros só veem beco sem saída. Sua inteligência não trabalha na pressa: ela trabalha no silêncio, e as melhores respostas chegam quando você para. Você percebe a abundância antes dela aparecer no plano físico.'),
    4:  ('O Cultivador de Precisão',
         'Você tem paciência orgânica e mira cirúrgica. Enquanto a maioria se dispersa em dez frentes, você reconhece o alvo certo e cuida dele até florescer. Você enxerga potencial adormecido nas pessoas e nos projetos — e sabe exatamente o que falta para germinar.'),
    5:  ('O Instinto que Não Erra',
         'Seu corpo sabe antes da sua cabeça. Você entra num lugar e sente na hora se algo está certo ou errado, e quase sempre acerta. Enquanto muitos precisam analisar, você tem uma leitura visceral imediata — e uma vitalidade que regenera rápido depois do esgotamento.'),
    6:  ('O Construtor de Pontes',
         'Você tem faro ímpar para oportunidades e conexões. Enquanto a maioria enxerga coisas isoladas, você olha um cenário e percebe imediatamente quem precisa se conectar com quem, qual ideia precisa destravar e qual ciclo precisa ser concluído para a vida fluir. Você sabe que uma fase nova só nasce quando a anterior é honrada e encerrada.'),
    7:  ('O Realizador Prático',
         'Você tem inteligência nas mãos e na mente executiva: o dom de fazer acontecer, organizar o caos e dar forma tangível ao que era só ideia. Enquanto muitos ficam paralisados na teoria, você olha um problema e enxerga na hora o passo a passo para resolvê-lo.'),
    8:  ('O Elevador de Padrão',
         'Você tem senso estético apurado e percebe desarmonia antes de todo mundo. Onde os outros veem "está bom", você vê o que falta para ficar certo. Sua presença eleva o padrão de um ambiente, de um trabalho ou de uma relação sem você precisar cobrar nada.'),
    9:  ('O Leitor de Campo',
         'Você sente o clima de um lugar e o estado de uma pessoa antes de qualquer palavra ser dita. Enquanto muitos precisam de explicação, você já captou. Essa sensibilidade é sua ferramenta de trabalho — e, quando não é cuidada, vira sobrecarga.'),
    10: ('A Lealdade que Ancora',
         'Você ama de um jeito que as pessoas conseguem sentir e confiar. Enquanto muitos vínculos são de conveniência, os seus são de verdade — e isso é raro o bastante para ser o seu maior patrimônio. Você protege os seus com uma constância que não depende de humor.'),
    11: ('O Desarmador de Peso',
         'Você tem a habilidade de mudar o clima de uma situação travada só pelo tom. Onde há solenidade desnecessária, medo ou rigidez, você entra com leveza e desmonta. Sua criatividade nasce exatamente do não levar tudo tão a sério.'),
    12: ('O Discernidor',
         'Você tem uma clareza rara sobre o que é seu e o que é do outro. Enquanto muitos se afogam no problema alheio, você consegue enxergar a fronteira. E quando você fala com convicção, as pessoas realmente mudam de ideia — porque você influencia pelo exemplo, não pela pressão.'),
    13: ('O Atravessador de Mundos',
         'Você transita entre ambientes, culturas e realidades completamente distintas sem perder a sua essência. Onde a maioria precisa de território conhecido para funcionar, você funciona melhor no território novo. Sua vigilância desperta enxerga o que ainda vai acontecer.'),
    14: ('O Magnetismo da Presença',
         'Você muda o ambiente só de entrar nele, sem fazer esforço nenhum. Enquanto muitos tentam convencer, você simplesmente está — e as coisas se reorganizam à sua volta. Sua receptividade lê o campo inteiro sem precisar perguntar nada.'),
    15: ('A Visão de Altitude',
         'Você enxerga o jogo inteiro de cima enquanto os outros ainda discutem uma peça. Sua mente naturalmente antecipa cenários, e nas crises acontece o contrário do esperado: você fica mais frio e mais estratégico, não menos.'),
    16: ('A Coragem Lúcida',
         'Você faz a pergunta que trava a sala — e é essa pergunta que destrava o problema. Enquanto a maioria aceita o que foi dito, você investiga até a raiz. Sua integridade não é postura: você realmente não consegue defender o que acha errado.'),
    17: ('O Navegador de Sinais',
         'Você percebe a direção certa antes da lógica confirmar. Coincidências úteis acontecem à sua volta com frequência que não é coincidência. Você evolui pelo caminho, não apesar dele — e sabe reconhecer quando a vida está fechando uma porta a seu favor.'),
    18: ('O Espelho Limpo',
         'Você enxerga através das máscaras e das justificativas, inclusive das suas. Onde os outros se conformam com a versão bonita, você quer a verdade — e sua presença faz as pessoas se verem sem que você precise apontar nada.'),
    19: ('O Regenerador',
         'Você se reinventa mais rápido do que qualquer pessoa à sua volta. Onde muitos levam anos para se recuperar de um colapso, você usa o colapso como combustível. Você gera a própria energia e não depende de ninguém para recomeçar.'),
    20: ('O Fogo que Aquece',
         'Você ilumina um ambiente pelo simples fato de estar inteiro nele. As pessoas se sentem melhores perto de você e nem sabem explicar por quê. Sua generosidade não é estratégia — é temperatura natural, e é isso que faz as pessoas confiarem.'),
}

# ==========================================================
# A ARMADILHA — com nome próprio
# ==========================================================
# O conselho foi unânime: dar NOME à sabotagem é o que faz a pessoa se
# reconhecer. "O Complexo de Salvador" funcionou melhor que qualquer
# descrição genérica de sombra.

ARMADILHA = {
    1:  ('O Peso do Provedor Solitário',
         'Você acredita, sem nunca ter dito isso em voz alta, que precisa dar conta de tudo sozinho para merecer cuidado. Então você acolhe todo mundo e não pede nada — e vai acumulando um cansaço que ninguém enxerga, porque você não deixa ninguém ver.'),
    2:  ('A Verdade Engolida',
         'Você percebe o que precisa ser dito e segura para não criar conflito ou não magoar. O problema é que a verdade não some quando é engolida: ela desce, vira remoendo mental e cobra no corpo. E depois sai de uma vez, em hora ruim.'),
    3:  ('O Medo da Falta',
         'No fundo você teme que não vá dar — dinheiro, tempo, amor, o que for. E esse medo toma decisões por você: você aceita menos do que merece, guarda em vez de investir, e se isola quando devia pedir ajuda. A escassez que você teme costuma ser a que você mesmo cria.'),
    4:  ('O Perfeccionismo que Não Entrega',
         'Você segura o trabalho pronto porque "ainda falta um detalhe". Falta sempre. Enquanto isso a oportunidade passa, e você fica com a sensação de que não fez nada — quando na verdade você fez tudo e não mostrou. Procrastinação disfarçada de excelência.'),
    5:  ('O Bote Precipitado',
         'Sua intensidade é sua força, mas quando o instinto dispara sem filtro você reage antes de entender — e depois passa dias consertando o que a reação quebrou. O mesmo corpo que te dá a leitura certa também te dá o impulso errado.'),
    6:  ('O Apego ao que Já Acabou',
         'Você mantém situações desgastadas vivas por pena, culpa ou medo de magoar. Quando você hesita em encerrar relações, projetos ou hábitos que já cumpriram o ciclo, acumula um peso invisível: o corpo cansa, a energia estagna, e você carrega responsabilidades que não são suas.'),
    7:  ('O Complexo de Salvador',
         'Você quer resolver a vida de todo mundo e esquece das próprias necessidades. Quando tenta salvar quem não pediu ajuda — ou quem não quer mudar — você acumula um cansaço absurdo, sobrecarga física e uma sensação surda de desvalorização.'),
    8:  ('A Vaidade do Detalhe',
         'Você refina, refina, e no meio do caminho o refino vira sobre você e não sobre a obra. Aí entra o julgamento — do trabalho dos outros, do seu próprio — e a busca de harmonia vira exigência. O que era cuidado com a forma vira medo de não ser suficiente.'),
    9:  ('A Emoção Represada',
         'Você sente tudo e mostra pouco, para não incomodar e para não parecer frágil. Só que emoção segurada não evapora: ela empoça. E o que devia ter saído em uma conversa sai depois em explosão, em adoecimento ou em uma tristeza sem motivo aparente.'),
    10: ('A Lealdade Mal Investida',
         'Você é fiel a quem já provou não ser fiel a você. Continua dando presença, tempo e cuidado para relações que só drenam — porque desistir parece traição. Mas lealdade a quem não retribui não é amor: é hábito, e está te custando caro.'),
    11: ('A Piada que Esconde a Dor',
         'Você usa o humor para não ter que sentir. Quando a conversa fica séria demais ou chega perto de algo verdadeiro, você faz a graça e desvia. Funciona — e é justamente por funcionar que você nunca chega no fundo do que está doendo.'),
    12: ('A Escolha Terceirizada',
         'Você deixa os outros decidirem por você — por gentileza, por evitar atrito, por não querer decepcionar — e depois carrega a frustração de uma vida que você não escolheu. Cada decisão que você não toma vira uma decisão tomada por outra pessoa.'),
    13: ('A Fuga Disfarçada de Liberdade',
         'Quando aperta, você se move: muda de cidade, de projeto, de relação. Às vezes isso é coragem legítima. Às vezes é fuga com nome bonito. A diferença é honesta e só você sabe: você está indo em direção a algo, ou está saindo de algo que precisaria ser encarado?'),
    14: ('O Controle Disfarçado de Presença',
         'Você diz que está no fluxo, mas por dentro está segurando o resultado com as duas mãos. A presença vira postura, a receptividade vira espera ansiosa. E o corpo denuncia: você está parado por fora e correndo por dentro.'),
    15: ('A Torre de Marfim',
         'Você enxerga longe e não desce para agir. Vê o plano inteiro, antecipa os cenários, entende tudo — e não executa. A visão vira substituto da ação, e você fica com a frustração de saber exatamente o que fazer e não estar fazendo.'),
    16: ('A Guerra Mental',
         'Você transforma a vida numa batalha interna de dúvidas e autocrítica: "e se der errado?", "será que sou capaz?". A mesma coragem que questiona o mundo se vira contra você — e a espada que devia cortar o dogma passa a cortar você mesmo.'),
    17: ('A Força Contra a Corrente',
         'Você insiste num caminho que a vida já está fechando. Os sinais aparecem — atrasos, portas que não abrem, corpo pedindo pausa — e você aumenta o esforço em vez de reler o mapa. Persistência é virtude sua; teimosia é a versão dela que te machuca.'),
    18: ('A Lâmina Voltada para Dentro',
         'Sua clareza é cirúrgica, e quando ela aponta para você vira crueldade. Você se cobra por padrões que jamais exigiria de outra pessoa e chama isso de honestidade. Verdade sem compaixão não liberta — só machuca com precisão.'),
    19: ('O Caos Como Identidade',
         'Você se acostumou a funcionar na urgência, e quando a vida acalma você sente falta. Aí, sem perceber, cria a próxima tempestade. Você é capaz de estabilidade — só não aprendeu ainda que estabilidade não é o mesmo que estagnação.'),
    20: ('O Brilho que Precisa de Plateia',
         'De um lado, a necessidade de ser o centro; do outro, o oposto exato: se apagar para não incomodar ninguém. Os dois vêm da mesma raiz — brilho medido pelo olhar do outro. E enquanto estiver medido assim, nunca é suficiente.'),
}

# ==========================================================
# A CHAVE DE OURO — a virada
# ==========================================================

CHAVE = {
    1:  'Você não precisa provar que merece cuidado. Deixar alguém cuidar de você é o começo de tudo, não a recompensa do fim.',
    2:  'A palavra guardada apodrece; a palavra dita no tempo certo cura. Fale antes de virar peso.',
    3:  'A abundância se forma no invisível antes de aparecer. Confiar no vazio fértil é diferente de esperar sem fazer nada.',
    4:  'A semente não floresce por ser perfeita, mas por ser plantada. Entregue em 90% — o resto se ajusta no mundo real.',
    5:  'Seu instinto acerta. Seu impulso, nem sempre. Entre a leitura e a reação, cabe uma respiração — e é ela que muda tudo.',
    6:  'Desapegar não é perder: é abrir espaço. Toda vez que você coloca um ponto final honesto no que expirou, uma porta melhor se abre à sua frente.',
    7:  'Cuidar de você não é egoísmo — é o seu primeiro ato de realização. Seu copo precisa estar cheio para sustentar sua força.',
    8:  'Beleza feita para impressionar cansa. Beleza feita para honrar o que é sustenta. Refine pela obra, nunca pelo julgamento.',
    9:  'Sentir não é fraqueza, é informação. O que você deixa passar por você não te derruba — o que você segura, sim.',
    10: 'Amar não obriga a ficar. Lealdade verdadeira inclui lealdade a você mesmo.',
    11: 'A leveza é sagrada quando liberta, não quando esconde. Você pode rir e sentir a mesma coisa, na mesma hora.',
    12: 'Escolher errado ainda é escolher. Uma decisão sua imperfeita vale mais que uma vida inteira decidida por outros.',
    13: 'Liberdade de verdade é poder ficar. Se você só sabe partir, o horizonte virou prisão de outro formato.',
    14: 'Presença não é ficar parado esperando: é soltar o resultado. No instante em que você larga, o campo se move.',
    15: 'Visão sem pé no chão é só paisagem. Desça um degrau e faça a coisa pequena e concreta que está na sua frente.',
    16: 'O verdadeiro guerreiro luta consigo primeiro. Vire a espada para o dogma, nunca para você.',
    17: 'Quando tudo trava ao mesmo tempo, não é castigo — é correção de rota. Reler o mapa é mais inteligente que forçar a porta.',
    18: 'A mesma verdade que corta também acolhe, dependendo de como é dita. Comece dizendo a verdade com carinho para você mesmo.',
    19: 'Você não precisa de crise para se mover. A mesma força que reconstrói depois do desabamento também constrói na calmaria.',
    20: 'Luz que precisa de plateia é fogueira; luz que existe por si é sol. Você já é o suficiente antes de qualquer reconhecimento.',
}

# ==========================================================
# O CORPO — por FAMÍLIA TERRESTRE (cânone Argüelles)
# ==========================================================
# Decisão de 03/09/2026, caminho A: a Família define o centro, e o centro
# define os órgãos. Os textos entregues antes usavam a convenção rodada
# (Mão dava Cardíaco); no cânone, Mão é Cardeal e dá Laríngeo.
#
# (região, órgãos, [3 sintomas nomeados], higiene diária)

CORPO_FAMILIA = {
    'Polar': (
        'Centro do Alto da Cabeça (Coronário)',
        'topo do crânio, sistema nervoso central, ciclo do sono',
        ['a cabeça que pesa e aperta no fim do dia, sempre no mesmo ponto',
         'o corpo exausto na cama e a cabeça que continua trabalhando',
         'estar na sala com todo mundo e sentir que você não está ali'],
        'Reduza estímulo: tela desligada uma hora antes de dormir, luz baixa à noite '
        'e cinco minutos de silêncio real ao acordar, antes de pegar o celular.'
    ),
    'Cardeal': (
        'Centro da Garganta (Laríngeo)',
        'garganta, tireoide, cordas vocais, cervical, mandíbula',
        ['a garganta que fecha na hora exata em que você ia falar',
         'o pescoço e os ombros duros de segurar o que não foi dito',
         'a mandíbula travada, apertada sem você perceber'],
        'Beba água morna em goles lentos com a intenção de soltar a garganta, '
        'solte o ar pela boca com som ao final do dia, e nunca vá dormir com '
        'conversa importante engasgada. Falar com calma cura o seu corpo.'
    ),
    'Central': (
        'Centro do Peito (Cardíaco)',
        'coração, pulmões, caixa torácica, ombros e região entre as escápulas',
        ['o aperto no peito quando o assunto é vínculo ou cobrança',
         'a respiração curta, que fica em cima e nunca chega no fundo',
         'os ombros enrolados pra frente, como quem protege o meio do peito'],
        'Respire abrindo a caixa torácica várias vezes ao dia, alongue a frente dos '
        'ombros contra o batente da porta, e treine receber alguma coisa sem retribuir na hora.'
    ),
    'Sinal': (
        'Centro do Estômago (Plexo Solar)',
        'estômago, diafragma, fígado, vesícula e digestão',
        ['a decisão difícil que você sente na boca do estômago antes de pensar nela',
         'o aperto que vem antes da conversa em que você precisa se impor',
         'o "não" engolido que fica pesando ali por dias'],
        'Coma devagar e sem tela, respire fundo pelo diafragma antes de qualquer '
        'refeição, e diga um "não" pequeno de vez em quando só para o corpo lembrar que é possível.'
    ),
    'Portal': (
        'Centro da Base (Raiz)',
        'lombar, quadril, pernas, intestino e suprarrenais',
        ['a lombar que avisa quando a segurança material aperta',
         'o cansaço que o sono não resolve, como bateria que não recarrega',
         'as pernas pesadas e o corpo lento nas fases de insegurança'],
        'Pise descalço na terra ou na grama por cinco minutos, coma comida de verdade '
        'e quente, e não deixe pendência material pequena envelhecer aberta.'
    ),
}

# ==========================================================
# O ORÁCULO — nomes memoráveis
# ==========================================================
# Guia/Análogo/Antípoda/Oculto seco não gruda. Os textos bons do Leo usavam
# nomes que a pessoa lembra depois. (emoji, nome, o que a posição é)

ORACULO_NOMES = {
    'guia':     ('🧭', 'A Bússola de Decisão', 'para onde você deve olhar quando estiver confuso ou travado'),
    'analogo':  ('🤝', 'O Aliado Natural', 'a energia com que você se sente em casa, e que te sustenta sem esforço'),
    'antipoda': ('🛡️', 'O Mestre de Atrito', 'o que mais te tira do sério — e por isso mesmo, a sua maior lição'),
    'oculto':   ('💎', 'O Tesouro Secreto', 'o poder que só aparece quando você solta o controle ou quando aperta de verdade'),
    'quinta':   ('👑', 'O Vórtice Integrador', 'a soma das cinco forças: onde a sua vida encontra estabilidade'),
}

# ==========================================================
# O ARQUÉTIPO NA PRÁTICA — Hunab Ku 21
# ==========================================================
# O conselho pegou: "Corte Cósmica: Corte da Inteligência (Sul)" apareceu sem
# nenhuma explicação. Aqui cada arquétipo ganha o "o que isso significa na prática".

ARQUETIPO_PRATICA = {
    1:  'Você é a consciência que sustenta o começo das coisas. Onde você está, as pessoas se sentem seguras para nascer de novo — num projeto, numa fase, numa versão nova delas mesmas.',
    2:  'Você é a consciência que carrega a mensagem. Sua função é dizer aquilo que o grupo não está conseguindo formular, e é por isso que sua palavra pesa mais do que você imagina.',
    3:  'Você é a consciência que acessa o que ainda não se manifestou. Sua função é sonhar antes, no sentido literal: enxergar a possibilidade enquanto ela ainda é invisível para os outros.',
    4:  'Você é a consciência que reconhece o potencial. Sua função é ver a árvore dentro da semente — em pessoas, em ideias, em projetos que ninguém mais aposta.',
    5:  'Você é a consciência que habita o corpo por inteiro. Sua função é lembrar aos outros que existe uma inteligência abaixo do pensamento, e que ela raramente erra.',
    6:  'Você é a consciência que faz a ponte entre realidades. Você transita por ambientes completamente distintos sem perder a essência, harmoniza conflitos e aproxima quem estava distante — porque sabe que, na alma, todos são iguais.',
    7:  'Você é a consciência que desce à matéria para realizar. Não se contenta em filosofar: sua função é pegar os recursos do mundo, consertar o que está falho e materializar o que era só visão.',
    8:  'Você é a consciência que traz a proporção. Sua função é lembrar que a forma importa — que o modo como algo é feito e apresentado faz parte da verdade daquilo.',
    9:  'Você é a consciência que purifica. Sua função é ser o lugar onde as emoções travadas de um sistema — família, equipe, relação — finalmente encontram vazão.',
    10: 'Você é a consciência que ama sem condição. Sua função é ser prova viva de que existe vínculo que não se compra e não se negocia.',
    11: 'Você é a consciência que desmonta a ilusão. Sua função é mostrar, pelo riso e não pelo sermão, que boa parte do que as pessoas levam a sério é convenção.',
    12: 'Você é a consciência que escolhe. Sua função é encarnar o livre-arbítrio: mostrar que existe escolha mesmo onde parecia só haver destino.',
    13: 'Você é a consciência que atravessa fronteiras. Sua função é ir onde os outros não vão e voltar com notícia do que existe do outro lado.',
    14: 'Você é a consciência que suspende o tempo. Sua função é ser o ponto de calma num sistema acelerado — e é impressionante o quanto isso reorganiza tudo à sua volta.',
    15: 'Você é a consciência que vê de cima. Sua função é a metavisão: enxergar o padrão inteiro enquanto os outros ainda estão dentro dele.',
    16: 'Você é a consciência que questiona. Sua função é ser a pergunta viva num ambiente que se acomodou — e é por isso que sua presença incomoda antes de libertar.',
    17: 'Você é a consciência que navega com a Terra. Sua função é ler os sinais e mostrar que existe uma ordem operando, mesmo quando parece caos.',
    18: 'Você é a consciência que reflete sem distorção. Sua função é ser o espelho limpo: as pessoas se veem de verdade perto de você, e nem sempre agradecem na hora.',
    19: 'Você é a consciência que catalisa a mudança. Sua função é ser o agente da transformação necessária — inclusive quando ela chega em forma de colapso.',
    20: 'Você é a consciência que ilumina inteira. Sua função é ser exemplo vivo de que dá para ser maduro, generoso e verdadeiro ao mesmo tempo.',
    21: 'Você é a fonte de onde todo movimento parte.',
}

# ==========================================================
# AS 3 DIRETRIZES — carreira, relações, autocuidado
# ==========================================================

DIRETRIZES = {
    1:  ('Posicione-se como quem começa e sustenta. Seu valor está em tirar projeto do papel e criar ambiente seguro para o time — não em executar sozinho até o fim.',
         'Peça ajuda uma vez esta semana, mesmo sem precisar. É treino: você precisa provar a si mesmo que pedir não te torna um peso.',
         'Cuide da base biológica primeiro — comida de verdade, água, sono e pés no chão. Sua energia mental depende disso mais do que a da média das pessoas.'),
    2:  ('Seu produto é a tradução. Empacote o que você sabe explicar: aula, texto, áudio, consultoria. As pessoas pagam pela clareza que você entrega.',
         'Diga a coisa difícil dentro de 24 horas. O custo de segurar é sempre maior do que o de falar com cuidado.',
         'Respire com consciência todo dia e proteja a garganta e a voz. Cante, faça som, solte o ar. Seu canal precisa estar aberto.'),
    3:  ('Não decida na pressa nem sob pressão. Negocie prazo para dormir sobre as decisões importantes — sua melhor resposta vem depois do silêncio.',
         'Diga o que você precisa antes de acumular. Quem convive com você não adivinha o que se passa aí dentro.',
         'Proteja o seu sono e o seu recolhimento. Penumbra, telas desligadas cedo, tempo sozinho sem culpa: isso não é luxo, é manutenção.'),
    4:  ('Entregue em noventa por cento. Combine data de entrega com alguém para não ficar refém do próprio detalhe.',
         'Reconheça em voz alta o potencial que você vê nas pessoas. É um dom seu e muda a vida de quem escuta.',
         'Uma tarefa por vez, com as notificações fechadas. Sua energia se dispersa mais rápido que a dos outros quando você fragmenta.'),
    5:  ('Trabalhe onde o corpo participa. Você rende no que é presencial, prático e vivo — e definha em rotina abstrata e imóvel.',
         'Respire antes de responder no calor. Sua leitura está certa; é o tempo da reação que precisa de ajuste.',
         'Movimente o corpo diariamente, sem negociação. Sua energia represada vira irritação ou adoecimento — não existe terceira via.'),
    6:  ('Posicione-se como quem constrói pontes e resolve impasses. Seu maior valor está em conectar pessoas, mediar acordos e fechar ciclos pendentes.',
         'Pratique o desapego com carinho. Encerrar um ciclo desgastado não é falta de amor: é maturidade para libertar os dois lados.',
         'Faça uma limpeza física por semana — armário, arquivo, agenda. Seu corpo responde direto ao que você está segurando sem precisar.'),
    7:  ('Empacote seu conhecimento em processos fechados, com começo, meio e fim. As pessoas pagam pelo seu dom de trazer ordem ao caos delas.',
         'Demita-se do cargo de salvador. Confie na capacidade dos outros de resolverem os próprios problemas — e aprenda a receber cuidado.',
         'Reserve quinze minutos diários para fazer algo com as mãos sem cobrança de produtividade: planta, cozinha, desenho. Isso desliga o ruído mental.'),
    8:  ('Cobre pelo padrão que você entrega, não pelas horas. Seu diferencial é o acabamento, e acabamento tem preço próprio.',
         'Elogie com especificidade. Você enxerga qualidades que a pessoa não vê em si — dizer isso é um presente que só você sabe dar.',
         'Cerque-se de beleza no cotidiano: a mesa arrumada, a luz certa, a música. Não é frescura; é regulação do seu sistema nervoso.'),
    9:  ('Trabalhe em ciclos, não em linha reta. Você tem fases de muita entrega e fases de recolhimento — planeje contando com as duas.',
         'Diga o que está sentindo enquanto ainda é pequeno. O que você guarda por educação volta triplicado depois.',
         'Água em todos os sentidos: beba mais, tome banho demorado, chore quando precisar. Você limpa o sistema pela água.'),
    10: ('Construa negócio sobre relação de longo prazo. Sua vantagem não é a venda rápida: é o cliente que fica dez anos.',
         'Revise onde a sua lealdade está sendo investida. Fidelidade a quem não retribui não é virtude — é hábito caro.',
         'Contato afetivo diário, sem pauta e sem resolver nada. Abraço, animal, presença. É assim que você recarrega.'),
    11: ('Use o humor como ferramenta profissional. Você desarma sala travada e ensina o que é difícil pela leveza — isso tem valor de mercado.',
         'Deixe uma conversa séria chegar até o fim sem fazer a piada de escape. Uma por semana já muda muita coisa.',
         'Brinque de verdade, sem produtividade. Você adoece quando tudo vira obrigação.'),
    12: ('Cobre pelo discernimento, não pela execução. Seu valor está em ajudar o outro a enxergar a escolha que ele não estava vendo.',
         'Respeite o livre-arbítrio alheio — inclusive o de errar. Deixe cada um aprender pelas próprias escolhas para não drenar sua energia.',
         'Tome uma decisão adiada por semana. Cada pendência aberta consome energia sua em segundo plano.'),
    13: ('Monte trabalho com movimento e variedade. Rotina rígida em ambiente fechado te sufoca e derruba seu rendimento.',
         'Antes de partir, pergunte com honestidade: estou indo em direção a algo, ou saindo de algo? A resposta muda tudo.',
         'Ar livre e horizonte, semanalmente. Sua alma precisa de espaço aberto para reciclar a energia.'),
    14: ('Venda presença, não volume. Você entrega mais em uma hora inteira de atenção do que a maioria em um mês de agenda cheia.',
         'Solte o resultado das relações. Sua ansiedade por controle é sentida pelo outro mesmo quando você não diz nada.',
         'Silêncio sem produtividade todo dia. Nada de podcast, nada de "aproveitar o tempo". Só ficar.'),
    15: ('Ofereça visão estratégica, não execução. Você é caro na função de enxergar o quadro inteiro e barato na de tocar o detalhe.',
         'Desça da análise para o encontro. As pessoas querem você presente, não avaliando a situação de cima.',
         'Faça uma ação pequena e concreta por dia, com as mãos. É o que traz você de volta ao corpo.'),
    16: ('Posicione-se como quem questiona o que ninguém questiona. Consultoria, auditoria, diagnóstico: sua pergunta é o produto.',
         'Tenha as conversas difíceis com amor. Fale com clareza e escute com honestidade, sem levantar a espada da defesa.',
         'Descarregue a mente no papel toda noite. Sua ruminação não para sozinha — precisa de saída física.'),
    17: ('Alinhe as decisões grandes com o timing, não com o calendário. Quando trava demais, é rota errada, não falta de esforço.',
         'Observe o que se repete nas suas relações. O padrão que volta é o mapa, não o azar.',
         'Contato com terra e natureza toda semana. É literal: seu sistema se recalibra no chão.'),
    18: ('Trabalhe onde a clareza é o valor: revisão, diagnóstico, organização, mediação. Você vê o que os outros não conseguem admitir.',
         'Diga a verdade com carinho — começando pela que você diz a si mesmo. Precisão sem compaixão afasta as pessoas.',
         'Organize um espaço físico por semana. A sua cabeça segue o ambiente, sempre nessa ordem.'),
    19: ('Assuma projetos de virada e reconstrução. Você é excelente onde há crise e entediado onde está tudo estável.',
         'Avise as pessoas antes da sua tempestade. Sua intensidade é legítima, mas quem convive precisa de aviso.',
         'Gaste a energia no corpo antes que ela vire caos na vida. Exercício intenso não é opção para você.'),
    20: ('Apareça. Publique, ensine, mostre o trabalho. Seu maior gargalo de negócio é a visibilidade, não a competência.',
         'Aqueça sem se consumir. Dar demais para ser querido cansa você e infantiliza o outro.',
         'Sol de manhã, todo dia que der. E algo que seja só seu, que ninguém veja e ninguém elogie.'),
}


# ==========================================================
# A ALQUIMIA: o que o Tom faz com o Selo
# ==========================================================
# Recuperado do texto de referência de 2025 ("A Alquimia da Sua Identidade"),
# que era a melhor ideia daquela versão: descrever o Selo, descrever o Tom e
# nunca dizer o que a COMBINAÇÃO dos dois produz deixa a leitura pela metade.
# Aqui a frase é escrita, não costurada por template — o texto antigo saía
# como "manifestar receptividade através da postura de cooperar".
#
# Uso: "O seu selo te dá {superpoder}. O seu tom pede que você exerça isso
#       {TOM_MODO[tom]}."

TOM_MODO = {
    1:  'atraindo os outros para aquilo que você começa, em vez de empurrar ninguém',
    2:  'encarando o obstáculo de frente — é no atrito que você encontra a sua medida',
    3:  'em movimento e com gente junto, nunca sozinho na sala',
    4:  'dando forma concreta e mensurável, senão não sai do lugar',
    5:  'assumindo o comando, sem esperar autorização de ninguém',
    6:  'no ritmo da rotina, com constância valendo mais que intensidade',
    7:  'escutando antes de agir, sintonizando em vez de forçar',
    8:  'com coerência inteira entre o que você diz e o que você faz',
    9:  'realizando de verdade, colocando a intenção no mundo e não só na cabeça',
    10: 'levando até o acabamento — você não entrega rascunho e não se contenta com meio',
    11: 'soltando o controle e deixando cair o que já não serve',
    12: 'dedicando à coletividade: o que é seu só se completa quando vira de todos',
    13: 'sustentando presença ao longo do tempo, sem pressa de provar nada',
}
