# -*- coding: utf-8 -*-
"""
O ORÁCULO e a ONDA, com peso.

Correção de rumo de 03/09/2026: a versão anterior tinha moldura longa
explicando o sistema e uma frase curta sobre a pessoa. Invertido aqui —
a moldura some, o conteúdo de cada força cresce.

Modelo é o texto da Lilli:
    "O seu Guia é um Portal Galáctico aberto. A sua intuição mais pura fala
     através da voz, da comunicação autêntica e da respiração. Nunca engula
     o que você precisa expressar para evitar conflito."

Duas a três frases por posição. A primeira nomeia, a segunda instrui.
"""

# ==========================================================
# AS 4 FORÇAS — o que dizer quando cada selo cai em cada posição
# ==========================================================

ORACULO = {
    1: {
        'guia': 'A sua direção vem do cuidado com a base. Quando estiver perdido, não busque estratégia: cuide do sono, da comida e do corpo primeiro — a clareza volta por aí, sempre.',
        'apoio': 'Você tem chão embaixo dos pés mesmo quando não sente. A vida já te sustentou em situações piores do que a de agora, e vai sustentar de novo.',
        'desafio': 'Gente carente que te puxa para dentro do problema dela vai te tirar do sério. O treino é acolher sem carregar — você pode escutar sem assumir o peso.',
        'oculto': 'Nas horas de aperto, desperta em você uma capacidade de nutrir e recomeçar do zero que surpreende até você mesmo.',
    },
    2: {
        'guia': 'A sua intuição fala pela voz e pela respiração. Nunca engula o que precisa dizer para evitar conflito: quando você fala a verdade com firmeza e doçura, o ambiente se reorganiza e a sua mente clareia na hora.',
        'apoio': 'As palavras vêm fáceis para você. Use isso — escreva, grave, converse: o que você não resolve pensando, resolve falando.',
        'desafio': 'Gente que fala muito e não escuta nada vai te esgotar. O treino é não competir por espaço: diga o essencial uma vez e deixe o silêncio trabalhar.',
        'oculto': 'Você tem o dom escondido de traduzir o complexo em simples. Quando aperta, essa clareza aparece e desarma a confusão dos outros.',
    },
    3: {
        'guia': 'A sua melhor decisão nunca vem na correria. Pare, recolha-se, durma sobre o assunto — a resposta chega pela intuição no silêncio, não pela análise na pressa.',
        'apoio': 'Existe mais recurso disponível para você do que os seus olhos mostram agora. A abundância trabalha primeiro no invisível.',
        'desafio': 'Ambiente barulhento e gente com urgência artificial vão te desestabilizar. O treino é não deixar a pressa dos outros virar a sua.',
        'oculto': 'Quando tudo parece beco sem saída, desperta em você uma visão noturna que enxerga a porta onde os outros só viam parede.',
    },
    4: {
        'guia': 'A sua direção está em cortar o supérfluo. Quando travar, não faça mais coisas: escolha a única que importa e vá nela até o fim.',
        'apoio': 'Você tem paciência orgânica, e ela é rara. O que você planta com cuidado amadurece — mesmo quando parece que nada está acontecendo.',
        'desafio': 'Gente que atropela processo e quer tudo para ontem vai te tirar do eixo. O treino é sustentar o seu tempo sem se justificar.',
        'oculto': 'Você tem talento guardado que ainda não colocou para fora. Sob pressão, ele aparece e você descobre que sempre esteve ali.',
    },
    5: {
        'guia': 'O seu corpo decide antes da sua cabeça, e acerta. Quando estiver confuso, repare no que o corpo faz: ele já sabe a resposta que a mente ainda discute.',
        'apoio': 'A sua vitalidade está do seu lado. Você regenera rápido — depois do esgotamento, volta mais inteiro do que a maioria.',
        'desafio': 'Quem mexe no seu território, no seu tempo ou no seu corpo sem pedir vai despertar o seu pior. O treino é colocar limite antes de explodir, não depois.',
        'oculto': 'Nas horas críticas, o instinto assume e você faz exatamente o que precisa ser feito, sem pensar. É o seu recurso mais confiável.',
    },
    6: {
        'guia': 'A sua direção aparece quando você pergunta o que já acabou e você ainda segura. Encerrar é o movimento que destrava a sua vida — sempre foi.',
        'apoio': 'Você atravessa perdas e transições sem se perder. Onde os outros desmoronam, você faz a ponte e segue.',
        'desafio': 'Gente que não deixa nada morrer, que revive tudo e não fecha ciclo, vai te sufocar. O treino é não segurar a mão de quem não quer atravessar.',
        'oculto': 'Quando você finalmente solta, aparece uma leveza e uma sorte que parecem vir do nada. Não vêm: é o espaço que você abriu.',
    },
    7: {
        'guia': 'A sua resposta está no que você faz, não no que você pensa. Quando travar, pare de analisar e execute a menor coisa possível — o caminho aparece na ação.',
        'apoio': 'Você tem inteligência nas mãos e capacidade de fechar o que está aberto. Nada te organiza mais do que concluir uma coisa.',
        'desafio': 'Gente que promete e não entrega vai te consumir. O treino é parar de compensar a falha do outro fazendo por ele.',
        'oculto': 'Você acalma as pessoas só de estar presente, sem fazer nada. É um poder que você usa sem perceber e subestima demais.',
    },
    8: {
        'guia': 'Quando algo estiver travado, olhe para a forma: arrumar o que está feio ou bagunçado destrava mais do que qualquer esforço mental.',
        'apoio': 'O seu senso do que fica bom é afiado e as pessoas confiam nele. Isso abre portas que o currículo não abre.',
        'desafio': 'Gente relaxada com o próprio trabalho, que entrega qualquer coisa, vai te irritar profundamente. O treino é elevar o padrão sem virar julgamento.',
        'oculto': 'Você enxerga beleza onde ninguém viu e transforma o comum em digno. Nas crises, é isso que devolve sentido ao seu dia.',
    },
    9: {
        'guia': 'O que está te incomodando quer ser sentido, não resolvido. Quando travar, pare de buscar solução e deixe a emoção passar por você — a clareza vem depois.',
        'apoio': 'A sua sensibilidade é ferramenta, não fraqueza. Você lê ambiente e pessoa antes de qualquer palavra ser dita.',
        'desafio': 'Gente fria, que trata sentimento como frescura, vai te machucar mais do que devia. O treino é não pedir validação de quem não tem a mesma língua.',
        'oculto': 'Quando você deixa sair o que estava represado, vem junto uma limpeza que resolve coisas que pareciam sem saída.',
    },
    10: {
        'guia': 'Quando estiver perdido, pergunte por quem você está fazendo isso. A sua bússola é o vínculo — se não tem ninguém do outro lado, o caminho está errado.',
        'apoio': 'O seu coração aberto é o seu maior patrimônio. As pessoas confiam em você de um jeito que não conseguem explicar.',
        'desafio': 'Gente desleal, que some quando aperta, vai te ferir de um jeito que você demora a superar. O treino é investir a sua lealdade em quem retribui.',
        'oculto': 'A sua constância afetiva é rara. Nos momentos de colapso, é ela que segura você e todo mundo à sua volta.',
    },
    11: {
        'guia': 'Se está pesado demais, você comprou uma ilusão em algum lugar. Quando travar, procure onde a solenidade se instalou — e desmonte com humor.',
        'apoio': 'A leveza abre porta que a força não abre. Você desarma situação travada só mudando o tom da conversa.',
        'desafio': 'Gente rígida, séria demais, sem humor nenhum, vai te asfixiar. O treino é não virar palhaço para agradar nem endurecer para ser levado a sério.',
        'oculto': 'A sua criatividade aparece justamente quando você para de tentar. É no ócio e na brincadeira que a solução chega.',
    },
    12: {
        'guia': 'A sua direção está na pergunta: o que EU quero, e não o que esperam de mim. Toda vez que você responde isso com honestidade, o caminho abre.',
        'apoio': 'O seu discernimento é apurado e as pessoas mudam de ideia quando escutam você. Influência pelo exemplo é a sua moeda.',
        'desafio': 'Gente que decide por você sem perguntar vai acumular uma revolta silenciosa. O treino é falar na hora, não depois.',
        'oculto': 'Você tem uma sabedoria prática que só aparece quando alguém precisa de verdade. Nessas horas, você sabe exatamente o que dizer.',
    },
    13: {
        'guia': 'Se travou, o problema é o lugar, não você. Mude o ambiente, o trajeto, o cenário — o seu sistema destrava pelo movimento, não pela insistência.',
        'apoio': 'Você tem sede de horizonte e isso te leva longe. Ambiente novo, gente nova e aprendizado novo te enchem de energia.',
        'desafio': 'Gente que quer te prender no lugar de sempre vai te sufocar. O treino é distinguir compromisso de prisão — os dois se parecem quando você está cansado.',
        'oculto': 'Você transita entre mundos muito diferentes sem perder a essência. É uma adaptabilidade que quase ninguém tem.',
    },
    14: {
        'guia': 'Pare de empurrar. Quando travar, fique quieto e presente — o campo se reorganiza sozinho, e a saída aparece sem você forçar.',
        'apoio': 'A sua presença já faz metade do trabalho. Você muda o clima de um lugar só de entrar nele.',
        'desafio': 'Gente apressada, que cobra prazo o tempo inteiro, vai te desestabilizar. O treino é não deixar a urgência do outro sequestrar o seu ritmo.',
        'oculto': 'Quando você solta o resultado de verdade, as coisas se resolvem rápido demais para ser coincidência.',
    },
    15: {
        'guia': 'Suba um degrau antes de decidir. Quando travar, o problema quase nunca é falta de esforço — é falta de altitude para ver o quadro inteiro.',
        'apoio': 'Você enxerga longe e antecipa cenário. Nas crises você fica mais frio e mais estratégico, não menos.',
        'desafio': 'Gente perdida no detalhe, que não vê o todo, vai te esgotar. O treino é traduzir a sua visão em passo pequeno, em vez de esperar que entendam.',
        'oculto': 'Você vê o que ainda não aconteceu. Confiar nessa antecipação, em vez de duvidar dela, é o que destrava a sua vida.',
    },
    16: {
        'guia': 'A saída está na pergunta que você vem evitando. Quando travar, faça a pergunta desconfortável — é sempre ela que destranca a porta.',
        'apoio': 'Você tem coragem para a conversa difícil. Onde os outros recuam, você encara — e é isso que resolve.',
        'desafio': 'Gente que foge de conversa direta vai te deixar furioso. O treino é não transformar a busca por clareza em interrogatório.',
        'oculto': 'A sua integridade sustenta você quando tudo desmorona. Você não se dobra, e essa firmeza é o seu chão.',
    },
    17: {
        'guia': 'Se está dando errado demais, o caminho não é esse. Quando travar, releia os sinais em vez de aumentar o esforço — a vida está te redirecionando.',
        'apoio': 'A sincronicidade trabalha a seu favor. Você encontra a pessoa certa na hora certa com uma frequência que não é coincidência.',
        'desafio': 'Gente que atropela sinal e força tudo no braço vai te desgastar. O treino é não entrar no ritmo de quem empurra a realidade.',
        'oculto': 'Você percebe a direção certa antes da lógica confirmar. Quando confia nisso, acerta quase sempre.',
    },
    18: {
        'guia': 'O que te incomoda no outro é o que você ainda não olhou em você. Quando travar, vire o espelho — a resposta está do seu lado, e você sabe disso.',
        'apoio': 'Você enxerga através das máscaras. Essa clareza te poupa de muita gente e de muita cilada.',
        'desafio': 'Gente falsa, que diz uma coisa e faz outra, vai te tirar completamente do sério. O treino é não gastar a sua verdade tentando desmascarar quem não quer ver.',
        'oculto': 'Quando você dirige a mesma honestidade para dentro com carinho, e não com lâmina, uma paz muito grande se instala.',
    },
    19: {
        'guia': 'A crise não é castigo, é a limpeza que você mesmo pediu. Quando travar, não remende: deixe cair o que já estava rachado.',
        'apoio': 'Você gera a própria energia e não depende de ninguém para recomeçar. Isso te dá uma liberdade que poucos têm.',
        'desafio': 'Gente que joga o caos dela em cima de você vai te consumir. O treino é distinguir a sua tempestade da tempestade dos outros.',
        'oculto': 'Você se reinventa mais rápido do que imagina. Depois do desabamento, em pouco tempo você está de pé — e melhor.',
    },
    20: {
        'guia': 'Seja o exemplo em vez de dar o conselho. Quando travar, pare de explicar e simplesmente faça — as pessoas seguem o que você é, não o que você diz.',
        'apoio': 'A sua presença aquece e as pessoas se sentem melhores perto de você. Isso abre porta em qualquer lugar.',
        'desafio': 'Gente que precisa ser o centro de tudo vai te esvaziar. O treino é brilhar sem disputar e sem se apagar.',
        'oculto': 'Você ilumina sem esforço nenhum. Quando para de tentar merecer, descobre que já era suficiente.',
    },
}

# ==========================================================
# A ONDA — narrativa, não lista
# ==========================================================
# Antes eu listava os 13 degraus com nome e Kin, o que ficou longo e não dizia
# nada. Os textos bons do Leo faziam diferente: um parágrafo sobre o que a onda
# representa, e depois "o seu papel na história". Voltando a esse formato.
#
# (o que a onda representa, a tensão que ela carrega)

ONDA_NARRATIVA = {
    1: ('O Dragão é o útero de tudo — a confiança primordial de que a vida sustenta quem nasce.',
         'Mas confiar não basta: alguém precisa ter a coragem de dar o primeiro passo sem garantia.'),
    2: ('O Vento é o sopro da verdade, a palavra que reorganiza o ambiente.',
         'Mas falar não é o mesmo que ser ouvido: alguém precisa dizer no tempo e no tom certos.'),
    3: ('A Noite é o sonho e a abundância que se formam no invisível, antes de aparecer.',
         'Mas sonho precisa de chão: alguém precisa trazer a visão para a matéria.'),
    4: ('A Semente é o potencial puro, a promessa do que ainda pode florescer.',
         'Mas semente jogada no asfalto morre: alguém precisa preparar a terra e proteger o processo.'),
    5: ('A Serpente é a inteligência do corpo, o instinto que sabe antes da mente.',
         'Mas instinto sem consciência vira reação: alguém precisa dar direção à força vital.'),
    6: ('O Enlaçador é a arte de encerrar com dignidade e atravessar para o novo.',
         'Mas soltar dói: alguém precisa transformar a perda em passagem, e não em vazio.'),
    7: ('A Mão é a cura que acontece pelo fazer, não pelo falar.',
         'Mas realizar cansa: alguém precisa saber terminar sem carregar o mundo nas costas.'),
    8: ('A Estrela é a harmonia e a beleza que elevam o padrão de tudo à volta.',
         'Mas beleza pode virar vaidade: alguém precisa embelezar servindo, e não impressionando.'),
    9: ('A Lua é a água que move e purifica o que estava represado.',
         'Mas emoção que só flui não constrói: alguém precisa dar forma ao que foi sentido.'),
    10: ('O Cão é o amor incondicional e a lealdade que não negocia.',
         'Mas amar sem limite adoece: alguém precisa ser leal também a si mesmo.'),
    11: ('O Macaco é a magia que desmonta o peso do mundo pelo riso.',
         'Mas leveza pode virar escape: alguém precisa rir sem deixar de sentir.'),
    12: ('O Humano é o livre-arbítrio, o poder de escolher em vez de aceitar.',
         'Mas escolher exige maturidade: alguém precisa decidir sem terceirizar a responsabilidade.'),
    13: ('O Caminhante é o explorador que atravessa fronteiras e não cabe em caixa nenhuma.',
         'Mas explorar pode virar fuga: alguém precisa ter coragem de também ficar.'),
    14: ('O Mago é a presença pura, o poder de parar o tempo e deixar o campo se organizar.',
         'Mas presença sem ação vira espera: alguém precisa transformar o silêncio em movimento.'),
    15: ('A Águia é a visão de altitude, que enxerga o jogo inteiro de cima.',
         'Mas visão sem descida é só paisagem: alguém precisa transformar a vista em passo concreto.'),
    16: ('O Guerreiro é a coragem de questionar tudo o que se acomodou.',
         'Mas a espada precisa de direção: alguém precisa questionar sem virar a lâmina contra si.'),
    17: ('A Terra é a navegação pelos sinais, a evolução em sintonia com o tempo natural.',
         'Mas seguir sinal exige entrega: alguém precisa confiar na rota sem exigir garantia.'),
    18: ('O Espelho é a verdade nua, que corta as ilusões e as máscaras do ego.',
         'Mas a verdade só liberta quando alguém tem a coragem prática de soltar as falsas seguranças.'),
    19: ('A Tormenta é a força que derruba o que estava podre para que algo verdadeiro nasça.',
         'Mas o caos por si só não constrói: alguém precisa reconstruir depois que a poeira baixa.'),
    20: ('O Sol é o fogo da maturidade, a luz de quem já não precisa provar nada.',
         'Mas iluminar consome: alguém precisa aprender a aquecer sem se queimar.'),
}

# O papel de cada degrau, em uma linha — para compor a frase do papel na história
PAPEL_DO_DEGRAU = {
    1:  'é quem abre a jornada e ancora o propósito de todos os outros',
    2:  'é quem enxerga o obstáculo antes de todo mundo e nomeia o que vai atrapalhar',
    3:  'é quem coloca a coisa em movimento e envolve as pessoas certas',
    4:  'é quem dá forma prática ao que era só ideia, e define como vai ser feito',
    5:  'é quem reúne os recursos e assume o comando quando ninguém assume',
    6:  'é quem organiza o ritmo para que o processo não quebre no meio do caminho',
    7:  'é quem escuta e corrige a rota no ponto exato do meio da jornada',
    8:  'é quem prova, pelo próprio exemplo, a coerência que a jornada exige',
    9:  'é quem realiza de verdade, tirando do papel o que os outros só planejaram',
    10: 'é quem faz o resultado aparecer no mundo físico, onde todos possam ver',
    11: 'é quem solta o que sobrou e liberta a jornada do próprio processo',
    12: 'é quem divide com os outros e transforma o aprendizado em coisa coletiva',
    13: 'é quem fecha o ciclo, colhe o sentido e prepara o voo para a próxima jornada',
}


# ==========================================================
# O TOM DENTRO DE CADA FORÇA
# ==========================================================
# Achado da rodada 4 (03/09/2026): três Mãos com tons diferentes — Simon (9),
# Stephanie (4) e Dani (5) — tinham de 46% a 58% das linhas do mapa IDÊNTICAS.
# Motivo: quase tudo no oráculo deriva do SELO, e o selo das cinco forças é o
# mesmo para quem nasce sob o mesmo selo, independente do tom.
#
# Mas o TOM de cada força muda: guia, análogo e antípoda carregam o tom natal;
# o oculto carrega o tom espelho (14 - t); a quinta tem tom próprio. Ou seja,
# as cinco forças divergem no tom mesmo quando o selo é igual.
#
# Esta tabela usa exatamente isso. Cada força ganha uma linha final calibrada
# pelo tom DAQUELE kin — o que faz duas pessoas do mesmo selo lerem cinco
# parágrafos diferentes onde antes liam cinco iguais.
#
# Regra de escrita: nenhuma frase repete a abertura de outra dentro do mesmo
# bloco, e nenhuma usa "O treino é" — construção que já vive nos textos de selo
# da posição antípoda, e que apareceria duas vezes seguidas.

TOM_NA_FORCA = {
    'guia': {
        1:  'A direção chega como atração, não como plano: você percebe para onde ir pelo que te puxa. Se nada te puxa, ainda não é hora.',
        2:  'Você só enxerga o caminho depois de bater no obstáculo. Não é falha de método — é o seu jeito: o "não" te mostra o "sim".',
        3:  'A sua clareza aparece falando com alguém. Sozinho na cabeça você roda em círculo; em voz alta, o caminho aparece na primeira conversa.',
        4:  'Direção, para você, é decisão escrita. Enquanto a escolha não tiver prazo, tamanho e primeiro passo, ela ainda não foi tomada.',
        5:  'Você decide bem quando assume o comando e para de consultar. Não é arrogância: a sua bússola trava quando você terceiriza a escolha.',
        6:  'Nenhum insight vai te dar a resposta — a repetição vai. Volte à mesma pergunta em dias diferentes e ela se firma sozinha.',
        7:  'A sua bússola é o corpo antes da lógica. Se a ideia é boa mas o peito fecha, confie no peito: ele lê o que você ainda não formulou.',
        8:  'Uma escolha só é certa se você conseguiria explicá-la sem se envergonhar. Coerência é o seu instrumento de navegação.',
        9:  'Você não decide pensando, decide fazendo. Dê um passo pequeno e irreversível e a direção inteira se revela no movimento.',
        10: 'Escolha olhando o resultado final: o que você quer ter pronto daqui a um ano. Depois caminhe de trás para frente até hoje.',
        11: 'O caminho se ilumina quando você tira da mesa a opção que já estava morta. Descartar, para você, é decidir.',
        12: 'A escolha que serve só a você costuma ser a errada, e você sente isso rápido. Decida pensando em quem vai ser afetado.',
        13: 'O seu norte se confirma no prazo longo. Não force resposta hoje: sustente a pergunta e veja o que continua verdadeiro em três meses.',
    },
    'analogo': {
        1:  'O apoio chega por atração, não por pedido. Diga em voz alta o que você está construindo e as pessoas certas aparecem sozinhas.',
        2:  'Você se fortalece no par. Uma pessoa só, que te encara de igual para igual, vale mais que uma rede inteira de contatos mornos.',
        3:  'A sua força volta quando você se mexe e junta gente. Isolamento te apaga rápido — não é frescura, é fisiologia.',
        4:  'O que te sustenta é ter estrutura. Uma agenda clara e um lugar organizado te devolvem mais energia que qualquer conversa motivacional.',
        5:  'A sua energia se reúne quando você ocupa o centro. Sendo ponto de referência de um grupo, mesmo pequeno, você se abastece.',
        6:  'O seu aliado é a rotina. Sono, comida e horário fazem por você o que nenhum esforço extraordinário faz.',
        7:  'Você se recupera no silêncio e na escuta. Música, natureza, água, mato: é ali que o seu tanque enche de novo.',
        8:  'Coerência te abastece. Qualquer desalinho entre o que você vive e o que você acredita drena mais do que trabalho pesado.',
        9:  'Ver a coisa acontecendo é o que te dá gás. Uma entrega real por semana te recarrega mais do que uma semana inteira de descanso.',
        10: 'Terminar te abastece. Um ciclo fechado, por menor que seja, te devolve mais do que dez começados ao mesmo tempo.',
        11: 'Soltar é o que te reabastece. Cada vez que você abre mão de algo pesado, volta uma energia que você achava perdida.',
        12: 'O que é feito junto rende mais e cansa menos. Rede não é muleta para você — é combustível, e você funciona pior sem ela.',
        13: 'A sua base é o tempo. Você não é de arranque: é de constância longa, e a sua força aparece na segunda metade da caminhada.',
    },
    'antipoda': {
        1:  'O atrito vem de quem disputa o mesmo lugar que você. Você não precisa vencer ninguém para existir — sair da disputa já é a vitória.',
        2:  'A discussão é a sua armadilha. Você entra para provar o ponto e sai esvaziado; sair antes de ganhar vale mais do que ter razão.',
        3:  'Lentidão alheia te irrita mais do que você admite. Esperar o outro no tempo dele é a sua lição mais difícil, e a mais necessária.',
        4:  'O que não tem contorno te desmonta: reunião sem pauta, combinado sem prazo, conversa que não fecha. Peça a definição em vez de adivinhar.',
        5:  'Você perde a linha quando te desautorizam na frente de alguém. Quem tem lugar não precisa defendê-lo — e lembrar disso te poupa metade dos atritos.',
        6:  'O imprevisto que atropela a sua rotina é o que mais te desregula. Deixe folga na agenda: o inesperado precisa caber, porque ele vem.',
        7:  'Você absorve o estado de quem está por perto, inclusive o mau humor que não é seu. Distinguir o que é seu do que é da sala te poupa metade dos desgastes.',
        8:  'A incoerência dos outros é o que mais te ferve por dentro. Escolha onde cobrar: nem toda hipocrisia do mundo é sua para corrigir.',
        9:  'A sua paciência acaba com quem fala muito e faz pouco. Parar de puxar quem não quer andar não é abandono, por mais que pareça.',
        10: 'O pendente dos outros vira peso seu e te consome por dentro. Deixe apodrecer o que não é sua tarefa — ninguém morre disso.',
        11: 'Você trava com quem tenta te controlar, mesmo com a melhor das intenções. Dizer não na hora custa menos do que sumir depois.',
        12: 'Ficar de fora te machuca mais do que você mostra. Peça o seu lugar em voz alta em vez de esperar que alguém perceba.',
        13: 'Cobrança de resposta imediata te desmonta. "Eu te respondo amanhã" é uma frase inteira: você não fica devendo nada dizendo isso.',
    },
    'oculto': {
        1:  'Esse dom te transforma em ponto de encontro: as pessoas certas se juntam em volta de você sem que você chame ninguém.',
        2:  'Sob oscilação você fica estranhamente estável. É uma firmeza que você nem reivindica, porque não percebe que está usando ela.',
        3:  'Você se mexe primeiro, sem discutir, e o seu movimento tira o grupo inteiro do lugar. Arrancar é o seu dom guardado.',
        4:  'A sua cabeça fica cirúrgica: enxerga a estrutura do problema num instante e desenha a saída em três passos claros.',
        5:  'Sem cargo e sem convite, as pessoas passam a olhar para você — e você dá conta. A autoridade aparece pronta, do nada.',
        6:  'A lista, a divisão das tarefas, o horário: você organiza sem pensar, e a ordem que você cria acalma o ambiente inteiro.',
        7:  'A resposta chega inteira no instante em que você para de forçar. É o seu recurso mais estranho e o mais confiável que você tem.',
        8:  'Você diz a frase exata que ninguém teve coragem de dizer, e o problema muda de tamanho na mesma hora.',
        9:  'A energia que faltava chega toda de uma vez, e você faz num dia o que vinha arrastando por meses.',
        10: 'Por mais travado que você estivesse, o trabalho sai pronto e bem feito. Entregar é o seu talento escondido.',
        11: 'Você abre mão do que estava segurando com unha e dente — e é exatamente aí que a vida se reorganiza sozinha.',
        12: 'Você pede ajuda e ela vem. É o dom que você mais subestima: as pessoas aparecem por você mais do que você imagina.',
        13: 'Você não resolve, não conserta e não foge: você fica. E esse ficar cura mais do que qualquer solução que alguém traga.',
    },
    'quinta': {
        1:  'Tudo se alinha quando existe uma intenção só, clara, à frente de tudo. Duas metas grandes ao mesmo tempo e o seu eixo se perde.',
        2:  'Você fica inteiro quando aceita a tensão entre dois lados seus. Não precisa escolher um: precisa parar de fingir que só existe um.',
        3:  'As peças se encaixam quando você está em movimento e com gente junto. Parado e sozinho, elas se soltam de novo.',
        4:  'Forma é o seu eixo. Quando a sua vida ganha rotina, contorno e limite claro, o resto para de sangrar energia.',
        5:  'A sua vida se estabiliza no dia em que você assume o próprio comando. Não é liderar os outros: é parar de esperar permissão.',
        6:  'Nada te centra mais do que fazer as mesmas poucas coisas nos mesmos horários. O ritmo é o seu chão.',
        7:  'Você fica em pé quando reserva um tempo diário sem produzir nada — e é justamente o primeiro tempo que você corta.',
        8:  'A coerência é o que te sustenta. No dia em que a agenda bate com os valores, o cansaço some sem você mudar mais nada.',
        9:  'Realizar te estabiliza. Não é hiperatividade: a sua vida só faz sentido quando a intenção vira coisa existente no mundo.',
        10: 'Terminar e mostrar o resultado, mesmo pequeno, te recoloca no lugar mais rápido do que qualquer descanso.',
        11: 'Esvaziar é o que te organiza: menos compromisso, menos objeto, menos vínculo morto. É assim que você respira.',
        12: 'Você se encontra quando o que é seu passa a servir mais gente — e se perde quando fica só seu.',
        13: 'A sua paz é feita de tempo. Nada seu amadurece rápido, e você fica em paz no dia em que para de exigir que amadureça.',
    },
}
