"""
Telegram Kin Bot — Sincronário Galáctico Cósbico (EDIÇÃO ESCOLA VIVA DA LEI DO TEMPO)
Motor de Ensino Diário, Diagnóstico Arquetípico e Tradução Energética 13:20
Substitui qualquer aplicativo de consulta com máxima profundidade pedagógica e ancoragem somática.
Formatação 100% Humana, Sem Formatação de IA (#, ---, -), Calibrado para 1 Bolha Única (< 3.600 caracteres).
"""

import datetime
import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==========================================
# 1. MATRIZ SAGRADA DOS 20 SELOS SOLARES
# ==========================================

SEALS = {
    1: {
        'nome': 'Dragão Vermelho', 'maia': 'Imix', 'acao': 'Inicia', 'poder': 'Nutrição', 'essencia': 'Ser',
        'arquetipo': 'A Força Primordial / Mãe Cósmica',
        'cor': 'Vermelho', 'direcao': 'Leste (Iniciação / Entrada da Vida)',
        'corpo': '🟥 CORPO FÍSICO — Ancoragem Biológica, Nutrição Celular e Sistema Nervoso',
        'celula': 'Célula 1 — Entrada (Informar a Matriz)',
        'corte': 'Corte do Conhecimento (Leste)',
        'descricao': 'Útero da criação, confiança primordial, nutrição do ser e resgate da memória ancestral',
        'luz': 'Capacidade de gerar novos projetos, acolher incondicionalmente e confiar no fluxo da vida. Hoje é dia de INICIAR com confiança primordial.',
        'sombra': 'Sentimento crônico de desamparo, carência afetiva e desconfiança na existência. Vigie o controle por medo de abandono.',
        'chave': 'Você é nutrido pela própria existência. Confie no fluxo e permita-se receber.',
        'somat_contracao': 'Ativação de desamparo no sistema simpático: nó no estômago, sensação de vazio visceral ou compulsão por comer rápido sem mastigar.',
        'somat_expansao': 'Segurança biológica de base (vagal ventral): diafragma solto, calor no baixo ventre e sensação de estar seguro na própria pele.',
        'somat_higiene': 'Coma comida viva e densa. Beba água morna. Aterre a planta dos pés no chão e faça 5 minutos de respiração abdominal lenta.',
        'dir_trabalho': 'Plante a semente de algo novo com fé e coragem. Escreva a intenção central do seu próximo projeto em 1 frase clara.',
        'dir_relacoes': 'Pratique acolhimento. Ofereça presença a quem precisa ser ouvido sem julgamento. Prepare um alimento com afeto.',
        'auto_investigacao': 'Onde eu ainda sinto que preciso lutar sozinho para merecer cuidado? O que acontece no meu corpo se eu confiar que a vida me sustenta hoje?',
        'guia_msg': 'O Farol Guia aponta para a nutrição original: pare de buscar validação fora e cuide da sua base biológica e emocional antes de qualquer movimento.',
        'analogo_msg': 'O Aliado de Apoio entrega vitalidade telúrica: garante calma nas vísceras e estabilidade corporal para sustentar o ritmo do dia.',
        'antipoda_msg': 'O Mestre do Desafio provoca a dor da carência ou a sensação de abandono: o treino de hoje é ser seu próprio refúgio e parar de mendigar afeto.',
        'oculto_msg': 'O Tesouro Oculto desperta a memória de que a vida sempre te sustentou nas travessias mais difíceis, liberando a paz de soltar o controle.',
        'quinta_msg': 'A Quinta Força sintetiza a Força Primordial: o poder soberano de gestar, acolher e alimentar a si mesmo e aos seus com dignidade.',
        'leo_cura_steph': 'Leo ancora a presença acolhedora da Mãe Cósmica: desacelera a mente dela, cuida da alimentação e lembra que ela não precisa carregar tudo sozinha.',
        'steph_cura_leo': 'Stephanie puxa Leo para o chão com cuidado prático: garante que o ninho esteja nutrido, organiza as refeições e traz aconchego para o corpo.',
        'cura_casal': 'Nutrir o ninho com comida caseira, toques de afeto e conversas serenas sobre o futuro. Cuidem do corpo um do outro sem pressa.'
    },
    2: {
        'nome': 'Vento Branco', 'maia': 'Ik', 'acao': 'Refina', 'poder': 'Comunicação', 'essencia': 'Espírito',
        'arquetipo': 'O Sumo Sacerdote / Sopro Divino',
        'cor': 'Branco', 'direcao': 'Norte (Refinamento / Mente e Espírito)',
        'corpo': '⬜ CORPO MENTAL — Clareza Verbal, Discernimento e Purificação de Diálogos Internos',
        'celula': 'Célula 2 — Armazém (Lembrar a Verdade)',
        'corte': 'Corte do Conhecimento (Leste)',
        'descricao': 'Transmissão da verdade, palavra consciente, respiração vital (Prana) e escuta do espírito',
        'luz': 'Clareza verbal, capacidade de inspirar com palavras e canal aberto para mensagens sutis. Hoje é dia de FALAR SUA VERDADE com amor.',
        'sombra': 'Falatório superficial, manipulação verbal ou medo de se expressar. Vigie palavras jogadas sem consciência.',
        'chave': 'A palavra é sopro divino. Antes de falar, respire. Antes de reagir, escute.',
        'somat_contracao': 'Contração laríngea e aperto no peito: sensação de garganta travada por engolir a própria verdade ou hiperventilação superficial.',
        'somat_expansao': 'Canal aéreo desobstruído: respiração ampla que chega aos pulmões profundos, voz ressonante e maxilar completamente destravado.',
        'somat_higiene': 'Pratique 5 minutos de respiração 4-7-8 (inspira em 4, segura em 7, solta em 8). Solte o ar com som de alívio.',
        'dir_trabalho': 'Comunique com clareza. Escreva a mensagem, grave o áudio, faça a reunião. A palavra consciente move montanhas.',
        'dir_relacoes': 'Diga o que precisa ser dito com firmeza e doçura. Ouça sem preparar resposta. A escuta atenta é a forma mais alta do Vento.',
        'auto_investigacao': 'Qual verdade eu estou engolindo por covardia ou conveniência? O que meu silêncio complacente está custando para a minha paz?',
        'guia_msg': 'O Farol Guia convoca você a alinhar a fala ao Espírito: não gaste palavras à toa e fale apenas aquilo que edifica e liberta.',
        'analogo_msg': 'O Aliado de Apoio abre canais de diálogo e sintonia fina, tornando sua expressão magnética, fluida e compreendida por todos.',
        'antipoda_msg': 'O Mestre do Desafio traz tagarelice mental e o medo do julgamento: o treino de hoje é domar a mente e falar com coragem cirúrgica.',
        'oculto_msg': 'O Tesouro Oculto é o sopro vital silencioso que restaura sua clareza instantaneamente quando você para e respira com presença.',
        'quinta_msg': 'A Quinta Força ativa o Mensageiro Cósmico: a capacidade de traduzir visões profundas em linguagem simples, poética e transformadora.',
        'leo_cura_steph': 'Leo abre espaço seguro de escuta para Stephanie: faz perguntas gentis que ajudam ela a verbalizar o que está engasgado no peito.',
        'steph_cura_leo': 'Stephanie organiza a comunicação de Leo: ajuda-o a traduzir conceitos cósmicos em linguagem humana, simples e acionável.',
        'cura_casal': 'Conversar com transparência absoluta e escuta profunda. Perguntem: "O que você precisa que eu escute hoje?" — e escutem em silêncio.'
    },
    3: {
        'nome': 'Noite Azul', 'maia': 'Akbal', 'acao': 'Transforma', 'poder': 'Sonho', 'essencia': 'Intuição / Abundância',
        'arquetipo': 'O Sonhador Místico / Guardião do Silêncio',
        'cor': 'Azul', 'direcao': 'Oeste (Transformação / Alquimia das Águas)',
        'corpo': '🟦 CORPO EMOCIONAL — Intuição Profunda, Inconsciente, Sombra e Matriz dos Sonhos',
        'celula': 'Célula 3 — Processo (Formular a Visão)',
        'corte': 'Corte do Conhecimento (Leste)',
        'descricao': 'Quietude fértil, intuição profunda, visão dos sonhos lúcidos e matriz da abundância invisível',
        'luz': 'Intuição aguçada, conexão com o subconsciente e capacidade de materializar sonhos. Hoje é dia de CONFIAR NA INTUIÇÃO silenciosa.',
        'sombra': 'Medo do escuro interior, sensação de escassez, isolamento depressivo e fuga da própria sombra.',
        'chave': 'A verdadeira abundância mora no invisível antes de se materializar. Confie no vazio fértil.',
        'somat_contracao': 'Sensação de peso ocular, aperto no plexo por medo de escassez ou insônia agitada por pensamentos ruminantes.',
        'somat_expansao': 'Sensação de recolhimento acolhedor: desaceleração profunda dos batimentos cardíacos, relaxamento ocular e sono reparador.',
        'somat_higiene': 'Desligue todas as telas 1 hora antes de dormir. Fique na penumbra. Coloque uma música suave e deixe o subconsciente decantar.',
        'dir_trabalho': 'Silêncio criativo. Não force decisões no atropelo. Deixe as ideias germinarem. A solução virá da intuição.',
        'dir_relacoes': 'Fiquem em silêncio juntos — sem celular, sem cobranças. Deixem o campo harmonizar sozinho na presença.',
        'auto_investigacao': 'Qual medo na minha sombra ainda dita minhas decisões por escassez? O que é a verdadeira abundância para mim hoje?',
        'guia_msg': 'O Farol Guia direciona você a buscar as respostas na quietude interior: a lógica do mundo não resolve o que só a intuição decifra.',
        'analogo_msg': 'O Aliado de Apoio traz sonhos reveladores e a certeza visceral de que a abundância já está operando nos bastidores invisíveis.',
        'antipoda_msg': 'O Mestre do Desafio ativa o pavor da falta e do escuro: o treino de hoje é olhar para a própria sombra sem desespero e acolhê-la.',
        'oculto_msg': 'O Tesouro Oculto é a visão noturna da alma: enxergar saídas luminosas exatamente onde a mente racional só via beco sem saída.',
        'quinta_msg': 'A Quinta Força ativa o Místico Lúcido: o poder de sonhar a realidade com tanta convicção que o mundo material se alinha à visão.',
        'leo_cura_steph': 'Leo ensina Stephanie a descansar no silêncio fértil: retira o celular dela à noite, apaga as luzes e cria um santuário para ela relaxar.',
        'steph_cura_leo': 'Stephanie ancora os sonhos de Leo na matéria: ajuda-o a estruturar prazos e ações concretas para que as visões ganhem corpo.',
        'cura_casal': 'Cultivar o silêncio compartilhado. Desliguem as telas cedo, fiquem abraçados na penumbra e deixem a mente desacelerar por completo.'
    },
    4: {
        'nome': 'Semente Amarela', 'maia': 'Kan', 'acao': 'Amadurece', 'poder': 'Foco / Atenção', 'essencia': 'Florescimento',
        'arquetipo': 'O Inocente / Visionário do Alvo',
        'cor': 'Amarelo', 'direcao': 'Sul (Amadurecimento / Florescimento e Fogo)',
        'corpo': '🟨 CORPO ESPIRITUAL — Foco Cósmico, Potencial Genético e Paciência Orgânica',
        'celula': 'Célula 4 — Saída (Expressar o Florescimento)',
        'corte': 'Corte do Conhecimento (Leste)',
        'descricao': 'Potencial latente, precisão do foco, respeito aos ciclos orgânicos e paciência para germinar',
        'luz': 'Paciência, determinação, foco cirúrgico e capacidade de fazer florescer talentos ocultos. Hoje é dia de PLANTAR COM PRECISÃO.',
        'sombra': 'Rigidez perfeccionista, medo de errar e hesitação em germinar. Vigie a procrastinação disfarçada de perfeccionismo.',
        'chave': 'A semente não tem pressa. Ela confia no tempo. Plante com fé e solte o controle do resultado.',
        'somat_contracao': 'Tensão muscular nas têmporas e rigidez na mandíbula por hiperfoco ansioso e medo de errar a execução.',
        'somat_expansao': 'Tônus de concentração serena: coluna ereta sem rigidez, respiração ritmada e presença focada em uma única ação de cada vez.',
        'somat_higiene': 'Elimine todas as abas abertas e notificações. Beba água fresca em goles lentos para hidratar as células.',
        'dir_trabalho': 'Foco absoluto em 1 única tarefa de alto valor. Nada de multitarefa dispersa. Plante e cuide com atenção total.',
        'dir_relacoes': 'Reconheça o potencial latente no outro. Elogie com especificidade algo que a pessoa ainda não vê em si mesma.',
        'auto_investigacao': 'Qual semente eu plantei mas vivo desenterrando por ansiedade e desconfiança? O que eu preciso deixar maturar em silêncio?',
        'guia_msg': 'O Farol Guia aponta para a seleção do essencial: corte os galhos secos da rotina e direcione toda a sua energia para o alvo prioritário.',
        'analogo_msg': 'O Aliado de Apoio entrega paciência orgânica: sustenta a disciplina diária sem o desgaste do perfeccionismo doentio.',
        'antipoda_msg': 'O Mestre do Desafio dispara a pressa e a autocrítica paralisante: o treino de hoje é dar o passo imperfeito em vez de esperar o cenário ideal.',
        'oculto_msg': 'O Tesouro Oculto desperta talentos adormecidos no seu DNA: recursos que você nem lembrava que tinha desabrocham sob pressão.',
        'quinta_msg': 'A Quinta Força ativa o Mestre do Alvo: a mente cirúrgica que reconhece o momento exato de germinar e manifestar resultados sólidos.',
        'leo_cura_steph': 'Leo ensina Stephanie a ter paciência com o próprio ritmo: tira a cobrança de velocidade da cabeça dela e celebra os pequenos avanços.',
        'steph_cura_leo': 'Stephanie cobra o foco de Leo: puxa a atenção dele para uma entrega prioritária de cada vez, impedindo aberturas dispersas.',
        'cura_casal': 'Alinhar o foco conjunto. Escrevam num papel a única meta importante do ciclo e cuidem dela com carinho e disciplina diária.'
    },
    5: {
        'nome': 'Serpente Vermelha', 'maia': 'Chicchan', 'acao': 'Inicia', 'poder': 'Sobrevivência / Instinto', 'essencia': 'Força Vital',
        'arquetipo': 'O Iniciado Serpente / Mestre da Kundalini',
        'cor': 'Vermelho', 'direcao': 'Leste (Iniciação / Entrada da Vida)',
        'corpo': '🟥 CORPO FÍSICO — Kundalini, Sistema Nervoso Autônomo, Descarga Somática e Vigor',
        'celula': 'Célula 1 — Entrada (Informar a Matriz)',
        'corte': 'Corte do Conhecimento (Leste)',
        'descricao': 'Inteligência visceral do corpo físico, sexualidade sagrada, regeneração celular e vigor vital',
        'luz': 'Vigor físico explosivo, intuição corporal precisa, magnetismo natural e recuperação rápida. Hoje é dia de HONRAR O CORPO.',
        'sombra': 'Apego a instintos de sobrevivência, reatividade cega ou apatia física. Vigie a impulsividade defensiva.',
        'chave': 'O corpo é o seu templo e o seu primeiro oráculo. Escute a sabedoria visceral antes de racionalizar.',
        'somat_contracao': 'Reatividade simpática de luta/fuga: contração da fáscia lombar, ombros encolhidos e pulso acelerado por alerta de perigo imaginário.',
        'somat_expansao': 'Fluidez neuromuscular: pelve relaxada, calor distribuído nos membros, vitalidade desperta e sensação de prontidão sem tensão.',
        'somat_higiene': 'Treino de força, corrida ou caminhada rápida para queimar o cortisol. Depois, banho quente alongando a cadeia posterior.',
        'dir_trabalho': 'Ação física e energia alta. Use a vitalidade para tarefas que exigem presença corporal, vigor e entrega intensa.',
        'dir_relacoes': 'Respeite o espaço visceral do outro. Toque com afeto. A intimidade hoje pede autenticidade e presença sincera.',
        'auto_investigacao': 'O que o meu corpo está me dizendo através das minhas contrações musculares? Onde eu ignorei meus limites biológicos recentemente?',
        'guia_msg': 'O Farol Guia convoca você a confiar na resposta visceral do corpo: se o estômago contrai, recue; se o peito expande, avance.',
        'analogo_msg': 'O Aliado de Apoio injeta vitalidade biológica e magnetismo pessoal para você trabalhar e se posicionar sem fadiga.',
        'antipoda_msg': 'O Mestre do Desafio ativa a reatividade irracional: o treino de hoje é não morder a isca de provocações e respirar antes de reagir.',
        'oculto_msg': 'O Tesouro Oculto é o poder de trocar de pele: regenerar a saúde e o ânimo após fases de esgotamento com velocidade surpreendente.',
        'quinta_msg': 'A Quinta Força ativa o Mestre da Kundalini: a união sagrada entre a inteligência dos instintos terrestres e a lucidez espiritual.',
        'leo_cura_steph': 'Leo traz calma para o sistema nervoso simpático de Stephanie: ajuda-a a soltar a guarda, respirar fundo e relaxar a musculatura.',
        'steph_cura_leo': 'Stephanie puxa Leo para o movimento físico: lembra-o de treinar, beber água, sair da cadeira e honrar o corpo.',
        'cura_casal': 'Conectar pela linguagem do corpo e do toque. Massagem nos pés, carinho na nuca ou simplesmente se abraçar respirando juntos.'
    },
    6: {
        'nome': 'Enlaçador de Mundos Branco', 'maia': 'Cimi', 'acao': 'Refina', 'poder': 'Igualar / Pontes', 'essencia': 'Morte / Oportunidade',
        'arquetipo': 'O Hierofante / Diplomata Cósmico',
        'cor': 'Branco', 'direcao': 'Norte (Refinamento / Mente e Espírito)',
        'corpo': '⬜ CORPO MENTAL — Desapego Lúcido, Fim de Projeções do Ego e Luto Sagrado',
        'celula': 'Célula 2 — Armazém (Lembrar a Verdade)',
        'corte': 'Corte do Amor (Norte)',
        'descricao': 'Desapego consciente, encerramento sagrado de ciclos, transcendência e conexão entre mundos',
        'luz': 'Facilidade para perdoar e soltar o passado, serenidade diante de finais e habilidade diplomática. Hoje é dia de SOLTAR com paz.',
        'sombra': 'Apego possessivo, medo da perda e teimosia em manter o que já morreu. Vigie o controle obsessivo.',
        'chave': 'Toda morte é uma ponte para um renascimento. Solte o que já cumpriu sua função com gratidão.',
        'somat_contracao': 'Sensação de aperto no peito e peso nas costas por carregar fardos de relações ou projetos do passado que já terminaram.',
        'somat_expansao': 'Leveza profunda no tronco: expiração completa com sensação de esvaziamento e paz com os desfechos da vida.',
        'somat_higiene': 'Limpeza do espaço físico: jogue fora papéis velhos, doe o que não usa e tome um banho com intenção consciente de descarrego.',
        'dir_trabalho': 'Encerre ciclos e limpe a mesa. Delete arquivos inúteis, cancele compromissos drenantes e finalize pendências.',
        'dir_relacoes': 'Perdoe uma mágoa antiga em silêncio. Solte a expectativa de que o outro mude. Aceite o presente como ele é.',
        'auto_investigacao': 'Qual ciclo, apego ou crença antiga já morreu e eu continuo tentando manter vivo por medo do vazio? Como posso soltar isso hoje?',
        'guia_msg': 'O Farol Guia aponta para a elegância de soltar: perdoe, feche portas desgastadas e abra caminho para que novas pontes surjam.',
        'analogo_msg': 'O Aliado de Apoio traz diplomacia e poder de conciliação, permitindo acordos justos e transições de ciclo sem conflito.',
        'antipoda_msg': 'O Mestre do Desafio cutuca o medo da perda e a carência de controle: o treino de hoje é abrir as mãos e confiar no novo ciclo.',
        'oculto_msg': 'O Tesouro Oculto é a capacidade de enxergar oportunidades de ouro exatamente onde a maioria só vê crise, perda e fim de linha.',
        'quinta_msg': 'A Quinta Força ativa o Construtor de Pontes: a sabedoria de unir realidades diferentes e transitar com leveza entre o terreno e o sutil.',
        'leo_cura_steph': 'Leo ensina Stephanie a soltar o controle e confiar nos ciclos: ajuda-a a perdoar imprevistos e lembrar que nem tudo depende dela.',
        'steph_cura_leo': 'Stephanie ajuda Leo a fechar ciclos práticos: cobranças pendentes, contratos e decisões adiadas, limpando a mesa dele.',
        'cura_casal': 'Liberar mágoas passadas e pesos acumulados. Façam uma limpeza simbólica na casa, doem o que não usam e celebrem a leveza.'
    },
    7: {
        'nome': 'Mão Azul', 'maia': 'Manik', 'acao': 'Transforma', 'poder': 'Conhecer / Realização', 'essencia': 'Cura',
        'arquetipo': 'O Avatar / Construtor da Realidade',
        'cor': 'Azul', 'direcao': 'Oeste (Transformação / Alquimia das Águas)',
        'corpo': '🟦 CORPO EMOCIONAL — Cura pelas Mãos, Conclusão de Feridas Abertas e Auto-acolhimento',
        'celula': 'Célula 3 — Processo (Formular a Visão)',
        'corte': 'Corte do Amor (Norte)',
        'descricao': 'Cura pelas mãos, inteligência prática executiva, conclusão de tarefas e ancoragem da obra na matéria',
        'luz': 'Eficiência, dom de cura pelas mãos, concretização de projetos e resolução prática. Hoje é dia de CONCLUIR e CONSTRUIR.',
        'sombra': 'Complexo de salvador, perfeccionismo e burnout por carregar o fardo dos outros. Vigie a compulsão de resolver tudo.',
        'chave': 'Você cura o mundo curando a si mesmo primeiro. Termine o que começou e descanse sem culpa.',
        'somat_contracao': 'Tensão aguda nos punhos, antebraços e trapézios por sobrecarga de trabalho e postura de "carregar tudo nas costas".',
        'somat_expansao': 'Mãos quentes, palmas relaxadas e respiração tranquila de dever cumprido ao fechar um ciclo aberto de entrega.',
        'somat_higiene': 'Lave as mãos com água fria e sabão esfregando com intenção de descarrego. Alongue punhos e dedos.',
        'dir_trabalho': 'Conclua tarefas. Feche processos abertos, entregue o que está pendente, coloque a mão na massa com método e finalização.',
        'dir_relacoes': 'Ofereça ajuda prática — não apenas conselhos teóricos. Cozinhe, organize, conserte algo. A Mão serve pela ação.',
        'auto_investigacao': 'Onde eu estou me sobrecarregando tentando salvar ou consertar a vida dos outros? Qual tarefa aberta está roubando a minha paz?',
        'guia_msg': 'O Farol Guia direciona você a finalizar pendências: termine o que começou para estancar o vazamento de energia mental.',
        'analogo_msg': 'O Aliado de Apoio entrega inteligência técnica e destreza manual para descomplicar problemas difíceis com soluções simples.',
        'antipoda_msg': 'O Mestre do Desafio ativa o complexo de salvador e a ilusão de que só você sabe fazer: o treino de hoje é delegar e cuidar de si.',
        'oculto_msg': 'O Tesouro Oculto é a energia curativa que emana da sua presença quando você atua com intenção pura e método organizado.',
        'quinta_msg': 'A Quinta Força ativa o Realizador Sagrado: a capacidade de transformar conhecimento teórico em obras sólidas e curativas na matéria.',
        'leo_cura_steph': 'Leo lembra Stephanie de que ela já fez o suficiente: tira ela do modo tarefeira, cuida das mãos cansadas dela e acolhe o descanso.',
        'steph_cura_leo': 'Stephanie ancora a visão de Leo: ajuda a estruturar métodos práticos, organizar prioridades e materializar ideias no mundo real.',
        'cura_casal': 'Construir algo juntos com as mãos. Montem um projeto, arrumem a sala, cozinhem juntos e sintam o prazer da realização compartilhada.'
    },
    8: {
        'nome': 'Estrela Amarela', 'maia': 'Lamat', 'acao': 'Amadurece', 'poder': 'Embelezar / Arte', 'essencia': 'Elegância',
        'arquetipo': 'O Artista Cósmico / Harmonizador',
        'cor': 'Amarelo', 'direcao': 'Sul (Amadurecimento / Florescimento e Fogo)',
        'corpo': '🟨 CORPO ESPIRITUAL — Harmonia Áurica, Proporção Áurea e Alinhamento Estético',
        'celula': 'Célula 4 — Saída (Expressar o Florescimento)',
        'corte': 'Corte do Amor (Norte)',
        'descricao': 'Proporção áurea, harmonia estética, elegância nas atitudes e brilho pessoal sem arrogância',
        'luz': 'Senso estético refinado, capacidade de harmonizar ambientes e relações, brilho autêntico. Hoje é dia de EMBELEZAR.',
        'sombra': 'Vaidade excessiva, julgamento estético e superficialidade disfarçada de refinamento. Vigie a arrogância sutil.',
        'chave': 'A verdadeira elegância é a harmonia entre o que você sente e o que você expressa.',
        'somat_contracao': 'Rigidez na expressão facial e autocrítica ácida diante de imperfeições no espelho ou no ambiente.',
        'somat_expansao': 'Harmonia áurica: sensação de leveza estética no peito, postura ereta e fluidez suave nos movimentos corporais.',
        'somat_higiene': 'Vista uma roupa que honre seu valor. Arrume o seu ambiente de trabalho. Coloque beleza no que seus olhos enxergam.',
        'dir_trabalho': 'Refine a forma. Melhore o design, a apresentação visual e a estética do seu trabalho. A beleza atrai respeito.',
        'dir_relacoes': 'Elogie a beleza no outro — uma virtude, um gesto, uma gentileza. A Estrela reconhece o brilho de quem está ao lado.',
        'auto_investigacao': 'Como posso trazer mais harmonia e beleza para a minha rotina sem me perder na armadilha do perfeccionismo e da vaidade?',
        'guia_msg': 'O Farol Guia aponta para a proporção áurea: equilibre as atitudes, transforme o atrito em harmonia e mantenha a elegância sob pressão.',
        'analogo_msg': 'O Aliado de Apoio traz charme, magnetismo e bom gosto natural, facilitando negociações e encantando quem ouve você.',
        'antipoda_msg': 'O Mestre do Desafio dispara a intolerância com o caos e a arrogância estética: o treino de hoje é amar a beleza crua da vida.',
        'oculto_msg': 'O Tesouro Oculto é o seu brilho autêntico e despretensioso: quando você é você mesmo sem tentar impressionar, sua presença ilumina.',
        'quinta_msg': 'A Quinta Força ativa o Artista Cósmico: a maestria de viver o Tempo como Arte, tornando cada ação e conversa uma obra harmônica.',
        'leo_cura_steph': 'Leo reconhece e celebra a beleza de Stephanie: elogia os detalhes, traz doçura poética e dissolve tensões com carinho.',
        'steph_cura_leo': 'Stephanie traz harmonia e elegância para o espaço de Leo: organiza o ambiente dele e inspira-o a se apresentar impecavelmente.',
        'cura_casal': 'Criar um clima romântico e belo. Coloquem uma música suave, acendam uma vela, vistam-se com carinho e celebrem estarem juntos.'
    },
    9: {
        'nome': 'Lua Vermelha', 'maia': 'Muluc', 'acao': 'Inicia', 'poder': 'Purificar / Fluxo', 'essencia': 'Água Universal',
        'arquetipo': 'A Sacerdotisa da Água / Farol da Consciência',
        'cor': 'Vermelho', 'direcao': 'Leste (Iniciação / Entrada da Vida)',
        'corpo': '🟥 CORPO FÍSICO — Drenagem Linfática, Fluidez Celular e Liberação Emocional Somática',
        'celula': 'Célula 1 — Entrada (Informar a Matriz)',
        'corte': 'Corte do Amor (Norte)',
        'descricao': 'Fluidez emocional, purificação de memórias, lembrança de quem você é e respeito às marés da vida',
        'luz': 'Fluidez emocional saudável, purificação de memórias tóxicas e lembrança de quem você é. Hoje é dia de PURIFICAR e FLUIR.',
        'sombra': 'Represamento emocional, rigidez diante de mudanças e vitimismo. Vigie a resistência ao fluxo natural.',
        'chave': 'Deixe a água correr. A emoção que flui purifica; a emoção represada adoece.',
        'somat_contracao': 'Retenção hídrica, nó na garganta por choro reprimido e peso no baixo ventre por apego a mágoas antigas.',
        'somat_expansao': 'Liberação das águas internas: alívio após o choro consciente, drenagem celular e sensação de frescor no corpo.',
        'somat_higiene': 'Beba 2 litros de água pura. Tome um banho demorado deixando a água cair no topo da cabeça descarregando tudo.',
        'dir_trabalho': 'Limpe a fila emocional. Resolva pendências que envolvem sentimentos engasgados. Responda com verdade e perdoe.',
        'dir_relacoes': 'Permita-se expressar vulnerabilidade. A vulnerabilidade autêntica é a ponte mais sólida entre dois corações.',
        'auto_investigacao': 'Qual emoção eu estou represando por orgulho ou medo de parecer vulnerável? O que acontece no meu corpo se eu simplesmente deixar fluir?',
        'guia_msg': 'O Farol Guia convoca você a purificar intenções e deixar as águas correrem: não segure o fluxo dos sentimentos nem force diques.',
        'analogo_msg': 'O Aliado de Apoio confere sensibilidade e compaixão natural para acolher os sentimentos alheios com respeito e empatia.',
        'antipoda_msg': 'O Mestre do Desafio ativa tempestades emocionais e vitimismo: o treino de hoje é ser o leito firme do rio por onde a água passa.',
        'oculto_msg': 'O Tesouro Oculto é a regeneração através da entrega: a capacidade de se purificar em 10 minutos de recolhimento sincero.',
        'quinta_msg': 'A Quinta Força ativa a Sacerdotisa da Água: a consciência que limpa resíduos do passado e sustenta a memória da verdade pura.',
        'leo_cura_steph': 'Leo oferece o colo seguro para as águas de Stephanie transbordarem: acolhe o desabafo dela sem tentar impor soluções lógicas.',
        'steph_cura_leo': 'Stephanie lembra Leo de hidratar o corpo e descarregar a sobrecarga mental na água: prepara um banho quente para ele relaxar.',
        'cura_casal': 'Lavar as feridas em conjunto. Tomem um banho relaxante juntos ou lavem os pés um do outro em silêncio, deixando a água limpar o cansaço.'
    },
    10: {
        'nome': 'Cachorro Branco', 'maia': 'Oc', 'acao': 'Refina', 'poder': 'Amar / Lealdade', 'essencia': 'Coração',
        'arquetipo': 'O Compassivo / Guardião do Amor',
        'cor': 'Branco', 'direcao': 'Norte (Refinamento / Mente e Espírito)',
        'corpo': '⬜ CORPO MENTAL — Superação de Julgamentos Punitivos e Pacificação da Mente Crítica',
        'celula': 'Célula 2 — Armazém (Lembrar a Verdade)',
        'corte': 'Corte do Amor (Norte)',
        'descricao': 'Amor sem cobranças, lealdade à própria essência e aos parceiros de jornada, abertura do chakra cardíaco',
        'luz': 'Amor incondicional genuíno, lealdade inabalável e capacidade de amar sem cobranças. Hoje é dia de ABRIR O CORAÇÃO.',
        'sombra': 'Carência afetiva, dependência emocional e lealdade cega a quem não merece. Vigie o medo de amar.',
        'chave': 'O amor verdadeiro não exige reciprocidade imediata. Ele existe porque você escolhe amar.',
        'somat_contracao': 'Sensação de armadura no peito, respiração curta no tórax e contração defensiva por medo de rejeição ou traição.',
        'somat_expansao': 'Calor radiante no centro do peito: batimentos cardíacos coerentes, sensação de pertencimento e acolhimento incondicional.',
        'somat_higiene': 'Coloque a palma da mão no centro do peito e respire fundo 7 vezes sentindo o calor e o ritmo do seu próprio coração.',
        'dir_trabalho': 'Sirva com o coração. Faça o trabalho com amor genuíno, não só por obrigação. A qualidade reflete o coração.',
        'dir_relacoes': 'Diga "eu te amo" olhando nos olhos. Pratique atos de afeto concretos: mensagens de carinho e escuta sem pressa.',
        'auto_investigacao': 'Onde eu estou cobrando amor e lealdade do outro em vez de ser a minha própria fonte de acolhimento e respeito próprio?',
        'guia_msg': 'O Farol Guia aponta para a lealdade incondicional aos seus valores e aos seus parceiros: sirva com o coração sem se trair.',
        'analogo_msg': 'O Aliado de Apoio abre portas através do companheirismo e da empatia, gerando confiança instantânea nos ambientes.',
        'antipoda_msg': 'O Mestre do Desafio ativa a carência e o medo do abandono: o treino de hoje é estabelecer limites dignos e amar sem dependência.',
        'oculto_msg': 'O Tesouro Oculto é a coragem mansa do perdão: restaurar pontes e dissolver ressentimentos com um simples abraço sincero.',
        'quinta_msg': 'A Quinta Força ativa o Guardião do Amor: a autoridade compassiva que pacifica conflitos e traz harmonia para o clã.',
        'leo_cura_steph': 'Leo valida o valor inestimável de Stephanie: elogia a lealdade dela, abraça-a no peito e faz ela se sentir amada.',
        'steph_cura_leo': 'Stephanie ancora o amor protetor para Leo: cria um refúgio acolhedor onde ele pode ser frágil e descansar no ninho.',
        'cura_casal': 'Olhar nos olhos por 3 minutos em silêncio absoluto. Depois, declarem o compromisso de lealdade e amor que une a aliança de vocês no ponto zero.'
    },
    11: {
        'nome': 'Macaco Azul', 'maia': 'Chuen', 'acao': 'Transforma', 'poder': 'Brincar / Magia', 'essencia': 'Ilusão',
        'arquetipo': 'O Mágico / Alquimista Brincalhão',
        'cor': 'Azul', 'direcao': 'Oeste (Transformação / Alquimia das Águas)',
        'corpo': '🟦 CORPO EMOCIONAL — Criança Interior, Desmonte da Rigidez e Alquimia do Humor',
        'celula': 'Célula 3 — Processo (Formular a Visão)',
        'corte': 'Corte da Profecia (Oeste)',
        'descricao': 'Desconstrução da rigidez pelo humor, criatividade genial, quebra de ilusões e leveza lúcida',
        'luz': 'Genialidade criativa, humor inteligente, capacidade de desconstruir o pesado com leveza. Hoje é dia de BRINCAR.',
        'sombra': 'Irresponsabilidade, sarcasmo destrutivo e fuga pela piada para não encarar a dor. Vigie a evasão.',
        'chave': 'O humor sagrado dissolve o medo. Ria de si mesmo com carinho e a ilusão perde o poder.',
        'somat_contracao': 'Mandíbula travada em sisudez rígida, testa franzida e sensação de peso insuportável por se levar a sério demais.',
        'somat_expansao': 'Soltura muscular espontânea: riso no ventre, olhos brilhantes e flexibilidade ágil nas articulações.',
        'somat_higiene': 'Pule, balance os braços soltos, faça caretas no espelho e ria de si mesmo. O movimento lúdico quebra a couraça muscular.',
        'dir_trabalho': 'Criatividade solta. Brainstorm sem censura, ideias ousadas, testes rápidos. O melhor trabalho nasce brincando.',
        'dir_relacoes': 'Riam juntos. Contem piadas, relembrem memórias leves, dancem na cozinha. A leveza cura mais que mil discursos.',
        'auto_investigacao': 'Onde eu estou me levando a sério demais e criando um drama desnecessário? Como a minha criança interior resolveria isso com leveza?',
        'guia_msg': 'O Farol Guia convoca você a desmontar a rigidez do ego: enxergue o jogo cósmico da vida e use a criatividade como chave mestra.',
        'analogo_msg': 'O Aliado de Apoio traz inventividade e quebra de padrões obsoletos, desarmando o peso de reuniões e processos engessados.',
        'antipoda_msg': 'O Mestre do Desafio dispara a solenidade doentia ou a ironia defensiva: o treino de hoje é usar o humor para libertar, nunca para ferir.',
        'oculto_msg': 'O Tesouro Oculto é o estalo de genialidade da criança: descobrir a solução exata para um problema enquanto você relaxa e brinca.',
        'quinta_msg': 'A Quinta Força ativa o Alquimista da Realidade: o mestre que desmascara ilusões sociais e devolve a magia e o encantamento ao cotidiano.',
        'leo_cura_steph': 'Leo tira Stephanie do estresse com brincadeiras: faz cócegas, dança de forma boba e quebra a rigidez do dia dela em segundos.',
        'steph_cura_leo': 'Stephanie traz leveza prática para as teorias de Leo: lembra-o de que a vida é simples, puxa-o para rir e descontrair.',
        'cura_casal': 'Fazer algo completamente descompromissado juntos. Joguem um jogo leve, assistam uma comédia, comam pipoca e dêem risadas.'
    },
    12: {
        'nome': 'Humano Amarelo', 'maia': 'Eb', 'acao': 'Amadurece', 'poder': 'Influenciar / Livre-Arbítrio', 'essencia': 'Sabedoria',
        'arquetipo': 'O Sábio da Terra / Cálice Sagrado',
        'cor': 'Amarelo', 'direcao': 'Sul (Amadurecimento / Florescimento e Fogo)',
        'corpo': '🟨 CORPO ESPIRITUAL — Autorresponsabilidade, Sabedoria Vivida e Saída do Vitimismo',
        'celula': 'Célula 4 — Saída (Expressar o Florescimento)',
        'corte': 'Corte da Profecia (Oeste)',
        'descricao': 'Responsabilidade pelas próprias escolhas, respeito ao livre-arbítrio alheio e sabedoria colhida na vivência',
        'luz': 'Maturidade ética, sabedoria prática colhida na vivência e respeito genuíno ao livre-arbítrio. Hoje é dia de ESCOLHER COM SABEDORIA.',
        'sombra': 'Arrogância intelectual, manipulação das escolhas alheias ou vitimismo. Vigie a terceirização de culpa.',
        'chave': 'Cada escolha que você faz é uma oração viva. Escolha com consciência e arque com as consequências em paz.',
        'somat_contracao': 'Sensação de paralisia na tomada de decisão, peso na cabeça por excesso de racionalização e terceirização de culpa.',
        'somat_expansao': 'Espinha dorsal alinhada, presença centrada e sensação de soberania calma sobre os próprios passos e escolhas.',
        'somat_higiene': 'Sente-se com a coluna reta em uma cadeira firme. Sinta os ísquios apoiados. Respire fundo e tome a decisão pendente.',
        'dir_trabalho': 'Decisões estratégicas. Avalie com bom senso e tome a decisão adiada. O livre-arbítrio é o seu poder na matéria.',
        'dir_relacoes': 'Respeite o livre-arbítrio do outro. Não tente moldar ninguém. Ofereça a sua perspectiva e solte o controle.',
        'auto_investigacao': 'Qual decisão crucial eu continuo adiando e terceirizando para as circunstâncias? O que eu escolho assumir 100% hoje?',
        'guia_msg': 'O Farol Guia aponta para a sabedoria das escolhas conscientes: assuma a rédea do seu destino e aja com ética irrepreensível.',
        'analogo_msg': 'O Aliado de Apoio confere bom senso e discernimento prático para guiar pessoas e projetos com maturidade e firmeza.',
        'antipoda_msg': 'O Mestre do Desafio cutuca a tentação de se fazer de vítima ou culpar terceiros: o treino de hoje é assumir a responsabilidade total.',
        'oculto_msg': 'O Tesouro Oculto é a sabedoria colhida nas cicatrizes antigas: seus erros passados se convertem na sua bússola mais precisa.',
        'quinta_msg': 'A Quinta Força ativa o Sábio da Terra: o ser humano que alcançou a maestria de viver em harmonia com sua verdade mais profunda.',
        'leo_cura_steph': 'Leo apoia as escolhas soberanas de Stephanie: dá espaço para ela decidir o que quer sem tentar tutelar os passos dela.',
        'steph_cura_leo': 'Stephanie traz bom senso humano para as decisões de Leo: ajuda-o a filtrar o que é prioridade prática e o que é devaneio.',
        'cura_casal': 'Tomar decisões importantes em harmonia. Sentem-se para alinhar as escolhas da semana com respeito ao espaço de cada um.'
    },
    13: {
        'nome': 'Caminhante do Céu Vermelho', 'maia': 'Ben', 'acao': 'Inicia', 'poder': 'Explorar / Espaço', 'essencia': 'Vigilância',
        'arquetipo': 'O Profeta / Peregrino das Estrelas',
        'cor': 'Vermelho', 'direcao': 'Leste (Iniciação / Entrada da Vida)',
        'corpo': '🟥 CORPO FÍSICO — Exploração de Novos Ambientes, Quebra de Inércia e Aterramento',
        'celula': 'Célula 1 — Entrada (Informar a Matriz)',
        'corte': 'Corte da Profecia (Oeste)',
        'descricao': 'Rompimento de limites e fronteiras, coragem de desbravar o desconhecido e travessia de limiares',
        'luz': 'Coragem de explorar o desconhecido, espírito inovador e capacidade de romper limites autoimpostos. Hoje é dia de EXPANDIR.',
        'sombra': 'Inquietude crônica, fuga geográfica dos problemas e superficialidade. Vigie a dispersão.',
        'chave': 'O verdadeiro espaço a explorar está dentro de você. A maior aventura é a jornada interior ancorada no presente.',
        'somat_contracao': 'Inquietação nas pernas (síndrome das pernas inquietas), respiração superficial e ansiedade de querer estar em outro lugar.',
        'somat_expansao': 'Sensação de espaço interno ampliado: pulmões cheios, pés firmes e olhar aberto para novos horizontes sem medo.',
        'somat_higiene': 'Caminhe ao ar livre mudando de rota. Observe o céu e o horizonte por 10 minutos para expandir o campo visual.',
        'dir_trabalho': 'Explore possibilidades. Pesquise novas referências, estude novos temas, faça contatos fora da sua bolha.',
        'dir_relacoes': 'Surpreenda com algo inédito. Um convite diferente, um passeio novo, uma conversa sobre horizontes futuros.',
        'auto_investigacao': 'Qual fronteira ou medo imaginário está aprisionando o meu crescimento? O que há do outro lado desse limite se eu der o passo?',
        'guia_msg': 'O Farol Guia desafia você a romper barreiras conhecidas: pise no desconhecido com vigilância lúcida e coragem pioneira.',
        'analogo_msg': 'O Aliado de Apoio traz adaptabilidade e mente investigativa, facilitando a navegação em cenários inéditos e mutáveis.',
        'antipoda_msg': 'O Mestre do Desafio ativa a claustrofobia e a vontade de fugir das obrigações: o treino de hoje é habitar o presente antes de partir.',
        'oculto_msg': 'O Tesouro Oculto é a certeza visceral de que você tem proteção em qualquer travessia: seu centro espiritual é a sua casa.',
        'quinta_msg': 'A Quinta Força ativa o Guardião de Limiares: o pioneiro que abre caminhos onde não havia estrada e guia os outros com segurança.',
        'leo_cura_steph': 'Leo expande os horizontes de Stephanie: apresenta ideias novas e inspiradoras, tirando ela da mesmice do cotidiano.',
        'steph_cura_leo': 'Stephanie organiza as explorações de Leo: garante que os voos dele tenham base segura, rotina e estrutura estável.',
        'cura_casal': 'Sair da rotina juntos. Visitem um lugar diferente, façam uma caminhada por ruas inéditas e sintam o frescor da novidade.'
    },
    14: {
        'nome': 'Mago Branco', 'maia': 'Ix', 'acao': 'Refina', 'poder': 'Encantar / Atemporalidade', 'essencia': 'Receptividade',
        'arquetipo': 'O Mago do Infinito / Xamã do Coração',
        'cor': 'Branco', 'direcao': 'Norte (Refinamento / Mente e Espírito)',
        'corpo': '⬜ CORPO MENTAL — Silenciamento da Mente Racional, Presença Pura e Foco no Agora',
        'celula': 'Célula 2 — Armazém (Lembrar a Verdade)',
        'corte': 'Corte da Profecia (Oeste)',
        'descricao': 'Magia da presença pura, silenciamento da mente racional, visão atemporal e receptividade sagrada',
        'luz': 'Presença magnética que encanta sem esforço, clareza intuitiva e capacidade de habitar o Agora. Hoje é dia de SER PRESENÇA.',
        'sombra': 'Fuga para abstração etérea, manipulação e recusa de habitar a matéria. Vigie a procrastinação disfarçada.',
        'chave': 'A magia não mora no futuro nem no passado. Ela pulsa neste exato momento. Habite o Agora.',
        'somat_contracao': 'Dissociação corporal: sensação de estar "fora do corpo", cabeça fervendo de ideias e perda de contato com a matéria.',
        'somat_expansao': 'Presença pura ancorada: batimento cardíaco lento, olhar magnético sereno e relaxamento profundo no momento presente.',
        'somat_higiene': 'Feche os olhos por 10 minutos em silêncio absoluto. Apenas observe a respiração sem interferir. Sinta a pele.',
        'dir_trabalho': 'Presença pura. Faça menos tarefas, mas com atenção total. Uma de cada vez com o coração. A magia está no foco.',
        'dir_relacoes': 'Esteja 100% presente com quem está ao seu lado. Sem telas, sem pressa. A sua presença é o maior presente.',
        'auto_investigacao': 'Onde eu estou fugindo do momento presente com ansiedade do futuro ou culpa do passado? O que é real e sagrado AGORA?',
        'guia_msg': 'O Farol Guia convoca você a silenciar o ruído e agir a partir da presença pura: a verdadeira magia acontece sem força bruta.',
        'analogo_msg': 'O Aliado de Apoio permite captar nuances sutis e criar conexões magnéticas pela simples qualidade da sua escuta e presença.',
        'antipoda_msg': 'O Mestre do Desafio dispara a fuga para abstrações teóricas e a hesitação de agir: o treino de hoje é materializar no chão.',
        'oculto_msg': 'O Tesouro Oculto é o silêncio interior que transmuta o caos: fechar os olhos no olho do furacão e restaurar a ordem no campo.',
        'quinta_msg': 'A Quinta Força ativa o Mago do Infinito: a consciência atemporal que sabe que todo o poder de criação reside no eterno Agora.',
        'leo_cura_steph': 'Leo ancora o campo de atemporalidade para Stephanie: silencia as urgências da mente dela com um olhar calmo e um abraço que para o tempo.',
        'steph_cura_leo': 'Stephanie traz Leo do etéreo para o físico: toca a pele dele, beija-o com ternura e lembra-o de habitar o corpo humano.',
        'cura_casal': 'Meditar juntos em silêncio de mãos dadas por 10 minutos. Deixem o tempo linear sumir e sintam a eternidade pulsando no peito.'
    },
    15: {
        'nome': 'Águia Azul', 'maia': 'Men', 'acao': 'Transforma', 'poder': 'Criar / Mente', 'essencia': 'Visão',
        'arquetipo': 'O Vidente Cósmico / Arquiteto Planetário',
        'cor': 'Azul', 'direcao': 'Oeste (Transformação / Alquimia das Águas)',
        'corpo': '🟦 CORPO EMOCIONAL — Metavisão das Dores, Quebra de Apego a Conflitos Locais e Criação',
        'celula': 'Célula 3 — Processo (Formular a Visão)',
        'corte': 'Corte da Profecia (Oeste)',
        'descricao': 'Visão panorâmica de longo alcance, metavisão estratégica, criação pela mente superior e compaixão',
        'luz': 'Visão de águia sobre a própria vida, capacidade estratégica e compaixão lúcida. Hoje é dia de VER DE CIMA.',
        'sombra': 'Frieza analítica, arrogância intelectual e distanciamento emocional. Vigie a desconexão do coração.',
        'chave': 'A visão sem compaixão é tirania. Veja o todo, mas nunca perca de vista o coração de cada detalhe.',
        'somat_contracao': 'Fadiga ocular intensa por telas, rigidez na base do crânio e distanciamento emocional gélido.',
        'somat_expansao': 'Visão periférica ampla: relaxamento dos globos oculares, mente lúcida e coração aberto para acolher o cenário.',
        'somat_higiene': 'Olhe para o ponto mais distante do horizonte por 5 minutos sem piscar com pressa. Descanse os olhos na luz natural.',
        'dir_trabalho': 'Planejamento estratégico. Suba o drone mental e olhe o projeto de cima. Trace o mapa dos próximos passos com clareza.',
        'dir_relacoes': 'Olhe as relações com metavisão — compreenda o contexto amplo de cada pessoa sem se prender a picuinhas.',
        'auto_investigacao': 'Se eu olhasse para os meus dilemas atuais daqui a 10 anos, o que pareceria pequeno demais para roubar a minha paz hoje?',
        'guia_msg': 'O Farol Guia convoca você a subir o drone da consciência: tome decisões com visão estratégica de longo alcance aliada à compaixão.',
        'analogo_msg': 'O Aliado de Apoio garante clareza intelectual e criatividade refinada para desenhar soluções muito antes dos outros.',
        'antipoda_msg': 'O Mestre do Desafio dispara a frieza crítica e o pessimismo analítico: o treino de hoje é usar a mente para edificar e acolher.',
        'oculto_msg': 'O Tesouro Oculto é o poder de materializar visões: quando sua mente se alinha a um propósito nobre, os recursos aparecem.',
        'quinta_msg': 'A Quinta Força ativa o Vidente Planetário: a mente que enxerga o plano maior da evolução e ajuda a arquitetar novas realidades.',
        'leo_cura_steph': 'Leo eleva a perspectiva de Stephanie: ajuda-a a ver o quadro maior dos negócios quando ela se afoga nos micro-detalhes.',
        'steph_cura_leo': 'Stephanie valida a visão de Leo: transforma os voos mentais dele em cronogramas tangíveis, metas e passos executáveis.',
        'cura_casal': 'Olhar para a vida do alto. Sentem-se para desenhar o plano dos próximos meses com entusiasmo, clareza e cumplicidade.'
    },
    16: {
        'nome': 'Guerreiro Amarelo', 'maia': 'Cib', 'acao': 'Amadurece', 'poder': 'Questionar / Inteligência', 'essencia': 'Coragem',
        'arquetipo': 'O Descobridor / Guardião da Verdade',
        'cor': 'Amarelo', 'direcao': 'Sul (Amadurecimento / Florescimento e Fogo)',
        'corpo': '🟨 CORPO ESPIRITUAL — Espada da Verdade, Desarme de Ilusões e Coragem Ética',
        'celula': 'Célula 4 — Saída (Expressar o Florescimento)',
        'corte': 'Corte da Inteligência (Sul)',
        'descricao': 'Questionamento lúcido que não aceita dogmas, inteligência focada, coragem moral e integridade',
        'luz': 'Inteligência prática destemida, coragem de questionar e integridade ética inabalável. Hoje é dia de QUESTIONAR com coragem.',
        'sombra': 'Combatividade destrutiva, teimosia e beligerância disfarçada de justiça. Vigie a agressividade intelectual.',
        'chave': 'O verdadeiro guerreiro luta consigo mesmo primeiro. A maior batalha é a da autenticidade.',
        'somat_contracao': 'Tensão na armadura peitoral, punhos cerrados e postura combativa de quem espera ser atacado a qualquer instante.',
        'somat_expansao': 'Tônus de coragem mansa: peito aberto sem armaduras, olhar firme e sereno, e passos determinados sem agressividade.',
        'somat_higiene': 'Treino de alta intensidade (musculação ou corrida) para canalizar a energia marcial. Depois, relaxamento e respiração.',
        'dir_trabalho': 'Questionamento estratégico. Desafie pressupostos, questione processos obsoletos e pergunte "por quê?" até a raiz.',
        'dir_relacoes': 'Tenha conversas difíceis com amor. Fale com clareza e escute com honestidade, sem levantar a espada da defesa.',
        'auto_investigacao': 'Qual mentira conveniente eu estou contando para mim mesmo? Qual pergunta corajosa eu venho evitando me fazer?',
        'guia_msg': 'O Farol Guia aponta para a coragem moral: questione as convenções, defenda o que é justo e aja com integridade inegociável.',
        'analogo_msg': 'O Aliado de Apoio confere firmeza de caráter e inteligência tática para vencer resistências sem precisar gritar.',
        'antipoda_msg': 'O Mestre do Desafio ativa a beligerância cega e a desconfiança paranoica: o treino de hoje é abaixar o escudo e confiar na verdade.',
        'oculto_msg': 'O Tesouro Oculto é a força serena que desce do centro do peito: permanecer inabalável diante de ameaças e pressões externas.',
        'quinta_msg': 'A Quinta Força ativa o Guardião da Verdade: o investigador lúcido que dissipa a mentira e restabelece a ordem com firmeza.',
        'leo_cura_steph': 'Leo protege a paz de Stephanie: coloca limites firmes contra demandas externas abusivas e defende o tempo sagrado dela.',
        'steph_cura_leo': 'Stephanie estimula a coragem de Leo: incentiva-o a se posicionar publicamente, gravar seus vídeos e vencer hesitações.',
        'cura_casal': 'Blindar a aliança. Conversem sobre o que precisa ser protegido de interferências e reafirmem o pacto de integridade e coragem.'
    },
    17: {
        'nome': 'Terra Vermelha', 'maia': 'Caban', 'acao': 'Inicia', 'poder': 'Evoluir / Sincronicidade', 'essencia': 'Navegação',
        'arquetipo': 'O Navegador Cósmico / Sismógrafo de Gaia',
        'cor': 'Vermelho', 'direcao': 'Leste (Iniciação / Entrada da Vida)',
        'corpo': '🟥 CORPO FÍSICO — Conexão com Gaia, Sincronização Biológica e Ritmo Natural',
        'celula': 'Célula 1 — Entrada (Informar a Matriz)',
        'corte': 'Corte da Inteligência (Sul)',
        'descricao': 'Leitura dos sinais e sincronicidades, alinhamento com a ordem cósmica e aterramento profundo em Gaia',
        'luz': 'Leitura natural das sincronicidades, aterramento e conexão visceral com a Terra. Hoje é dia de LER OS SINAIS.',
        'sombra': 'Insensibilidade aos sinais, desconexão da natureza ou superstição obsessiva. Vigie a perda do bom senso.',
        'chave': 'A Terra fala para quem pisa descalço. Ouça com os pés, não com a mente ansiosa.',
        'somat_contracao': 'Tontura, mente aérea descolada da realidade e perda de estabilidade gravitacional nos pés.',
        'somat_expansao': 'Enraizamento telúrico: pés firmes no chão, coluna estável como uma montanha e sincronização com os ritmos da Terra.',
        'somat_higiene': 'Pise descalço na terra ou grama por 10 minutos. Sinta a gravidade puxando as tensões mentais para o centro da Terra.',
        'dir_trabalho': 'Alinhe-se com o fluxo. Observe os sinais do dia — convites, mensagens inesperadas, padrões. O rumo se revela.',
        'dir_relacoes': 'Pise na terra juntos. Um momento na natureza recalibra qualquer relação com a harmonia primordial da vida.',
        'auto_investigacao': 'Quais sincronicidades e sinais a vida colocou no meu caminho recentemente? O que eles estão apontando para o meu próximo passo?',
        'guia_msg': 'O Farol Guia direciona você a navegar pelos sinais sutis da vida: pare de remar contra a maré e sincronize seus passos com Gaia.',
        'analogo_msg': 'O Aliado de Apoio traz estabilidade geológica e paciência cósmica para construir alicerces inabaláveis na matéria.',
        'antipoda_msg': 'O Mestre do Desafio dispara a sobrecarga sensorial e o medo do futuro: o treino de hoje é fincar raízes e viver o ritmo do dia.',
        'oculto_msg': 'O Tesouro Oculto é a inteligência gravitacional da Terra: o magnetismo que reabastece seu corpo no momento em que você pisa no chão.',
        'quinta_msg': 'A Quinta Força ativa o Navegador Cósmico: a consciência que lê as correntes do tempo e sempre conduz com segurança ao destino certo.',
        'leo_cura_steph': 'Leo ensina Stephanie a ler os sinais sincrônicos nos dias difíceis: mostra que nada é por acaso e traz paz para as incertezas.',
        'steph_cura_leo': 'Stephanie aterra Leo no chão firme da realidade: ajuda-o a organizar finanças, rotina e casa com a estabilidade da Terra.',
        'cura_casal': 'Ir para a natureza juntos. Caminhem descalços na grama, respirem ar puro e sintam a sincronização magnética com o planeta.'
    },
    18: {
        'nome': 'Espelho Branco', 'maia': 'Etznab', 'acao': 'Refina', 'poder': 'Refletir / Ordem', 'essencia': 'Infinito / Verdade',
        'arquetipo': 'O Yogi / Lâmina da Verdade',
        'cor': 'Branco', 'direcao': 'Norte (Refinamento / Mente e Espírito)',
        'corpo': '⬜ CORPO MENTAL — Fim de Projeções do Ego, Autocrítica Consciente e Ordem Sagrada',
        'celula': 'Célula 2 — Armazém (Lembrar a Verdade)',
        'corte': 'Corte da Inteligência (Sul)',
        'descricao': 'Verdade sem distorções do ego, clareza impecável, lâmina de corte de ilusões e ordem sagrada',
        'luz': 'Discernimento cristalino, capacidade de ver a verdade sem filtros e coragem de se enxergar. Hoje é dia de VER COM CLAREZA.',
        'sombra': 'Autocrítica paralisante, julgamento implacável e perfeccionismo cruel. Vigie a auto-flagelação.',
        'chave': 'O espelho não mente, mas também não julga. Olhe-se com compaixão impecável.',
        'somat_contracao': 'Contração aguda na nuca e ombros travados por julgamento impiedoso de si mesmo e autocrítica corrosiva.',
        'somat_expansao': 'Claridade mental translúcida: relaxamento facial total, respiração límpida e cessação de todo diálogo interno acusador.',
        'somat_higiene': 'Olhe nos seus próprios olhos no espelho por 3 minutos em silêncio absoluto. Respire fundo e diga: "Eu acolho quem eu sou hoje."',
        'dir_trabalho': 'Audite com verdade. Revise números, processos e entregas com honestidade cirúrgica. Elimine o que não funciona.',
        'dir_relacoes': 'Perceba o que te irrita no outro: muitas vezes é o espelho do que precisa ser acolhido em você. Auto-observação.',
        'auto_investigacao': 'O que eu estou projetando com tanta raiva ou frustração nos outros que é, na verdade, um reflexo do que recuso acolher em mim?',
        'guia_msg': 'O Farol Guia aponta para a ordem sagrada: use a lâmina do discernimento para cortar ilusões e veja as coisas como realmente são.',
        'analogo_msg': 'O Aliado de Apoio entrega sobriedade e justiça impecável para avaliar situações sem se deixar contaminar por reações emocionais.',
        'antipoda_msg': 'O Mestre do Desafio ativa a autocrítica impiedosa e o tribunal do ego: o treino de hoje é usar a verdade para curar, nunca para punir.',
        'oculto_msg': 'O Tesouro Oculto é a meditação do ponto zero: o silêncio absoluto que reina no centro do seu ser além de todas as ilusões.',
        'quinta_msg': 'A Quinta Força ativa o Mestre da Ordem Sagrada: a mente límpida que reflete a verdade divina e dissipa qualquer engano pela presença.',
        'leo_cura_steph': 'Leo reflete para Stephanie a grandeza incondicional dela: atua como espelho de ouro que mostra quem ela é, dissolvendo a autocrítica.',
        'steph_cura_leo': 'Stephanie reflete para Leo a verdade com amor: dá feedbacks práticos e honestos sobre o trabalho dele para lapidar a obra.',
        'cura_casal': 'Ser espelho amoroso um do outro. Perguntem: "O que eu reflito em você hoje?" — escutem sem defesas e evoluam juntos.'
    },
    19: {
        'nome': 'Tormenta Azul', 'maia': 'Cauac', 'acao': 'Transforma', 'poder': 'Catalisar / Autogeração', 'essencia': 'Energia',
        'arquetipo': 'O Mudador de Mundos / Mestre do Raio',
        'cor': 'Azul', 'direcao': 'Oeste (Transformação / Alquimia das Águas)',
        'corpo': '🟦 CORPO EMOCIONAL — Catarse Construtiva, Autotransmutação e Quebra de Estagnação',
        'celula': 'Célula 3 — Processo (Formular a Visão)',
        'corte': 'Corte da Inteligência (Sul)',
        'descricao': 'Autotransmutação radical, energia pura de renovação, quebra de estagnação e catarse construtiva',
        'luz': 'Energia explosiva de renovação, capacidade de catalisar mudanças profundas em si e no ambiente. Hoje é dia de MUDAR.',
        'sombra': 'Caos descontrolado, mudança compulsiva e drama destrutivo. Vigie o vício na instabilidade.',
        'chave': 'A tormenta limpa o céu. Deixe o raio agir e confie que depois vem a calmaria restauradora.',
        'somat_contracao': 'Voltagem elétrica represada no corpo: tremores sutis, agitação motora e sensação de que vai explodir de pressão.',
        'somat_expansao': 'Catarse descarregada: sensação de purificação eletromagnética, corpo leve após a tempestade e serenidade no centro do peito.',
        'somat_higiene': 'Treino de força explosivo ou dança vigorosa para descarregar a alta voltagem. Depois, banho gelado ou alternado.',
        'dir_trabalho': 'Catalise mudanças. Quebre velhos padrões, mude fluxos, reestruture o que está estagnado. Revolução construtiva.',
        'dir_relacoes': 'Permita que as relações evoluam. Não tente manter o outro preso a versões antigas. Deixe a renovação agir.',
        'auto_investigacao': 'Qual estrutura obsoleta na minha vida precisa ser destruída pelo raio da transformação para que a minha verdade possa respirar?',
        'guia_msg': 'O Farol Guia convoca você a autogerar energia e quebrar a casca velha: não tema a crise, ela é o motor do seu próximo nível.',
        'analogo_msg': 'O Aliado de Apoio acelera transformações que levariam anos, destravando a evolução com altíssima potência transformadora.',
        'antipoda_msg': 'O Mestre do Desafio cutuca o apego a dramas e o medo do caos: o treino de hoje é ser o olho sereno no centro do furacão.',
        'oculto_msg': 'O Tesouro Oculto é a capacidade de renascer das cinzas com o dobro de vigor e clareza após as tempestades mais duras.',
        'quinta_msg': 'A Quinta Força ativa o Mudador de Mundos: o catalisador que transforma estagnação em movimento vivo por onde quer que passe.',
        'leo_cura_steph': 'Leo é o olho sereno do furacão para Stephanie: quando tudo ao redor parece caótico, ele sustenta o centro em paz e acalma tudo.',
        'steph_cura_leo': 'Stephanie canaliza a tormenta criativa de Leo em ações produtivas: direciona a alta voltagem dele para entregas rentáveis.',
        'cura_casal': 'Transmutar juntos o que estava travado. Façam uma grande mudança no ambiente, iniciem um novo hábito e usem o raio para crescer.'
    },
    20: {
        'nome': 'Sol Amarelo', 'maia': 'Ahau', 'acao': 'Amadurece', 'poder': 'Iluminar / Fogo Universal', 'essencia': 'Vida',
        'arquetipo': 'O Iluminado / Consciência Crística',
        'cor': 'Amarelo', 'direcao': 'Sul (Amadurecimento / Florescimento e Fogo)',
        'corpo': '🟨 CORPO ESPIRITUAL — Selagem Áurica, Maestria Solar e Amor Incondicional Pleno',
        'celula': 'Célula 4 — Saída (Expressar o Florescimento)',
        'corte': 'Corte da Inteligência (Sul)',
        'descricao': 'Amor incondicional, iluminação da verdade, vida plena, sabedoria viva e autoridade benevolente',
        'luz': 'Iluminação interior, autoridade benevolente e capacidade de irradiar amor universal. Hoje é dia de BRILHAR com autenticidade.',
        'sombra': 'Megalomania espiritual, complexo de guru e arrogância de quem se acha superior. Vigie o ego espiritual.',
        'chave': 'O sol não precisa provar que brilha. Ele apenas é. Brilhe sem precisar de plateia.',
        'somat_contracao': 'Tensão no plexo solar por necessidade de validação externa ou frustração por não ser reconhecido e aplaudido.',
        'somat_expansao': 'Calor solar irradiando do coração para todo o corpo: respiração plena, olhar caloroso e serenidade soberana.',
        'somat_higiene': 'Tome 15 minutos de sol da manhã na pele. Sinta a luz ativando a produção de vitamina D e a vitalidade mitocondrial.',
        'dir_trabalho': 'Irradie maestria. Compartilhe o seu melhor trabalho, ensine, lidere com generosidade. Sua presença clareia o caminho.',
        'dir_relacoes': 'Seja a luz acolhedora do ambiente sem ofuscar ninguém. Pratique generosidade silenciosa e amor sem cobranças.',
        'auto_investigacao': 'Como posso compartilhar a minha sabedoria e luz hoje por pura generosidade com a vida, sem depender de aplausos ou validação?',
        'guia_msg': 'O Farol Guia aponta para a consciência da unidade: viva com nobreza e irradie clareza e calor para todos sem distinção.',
        'analogo_msg': 'O Aliado de Apoio entrega autoridade benevolente e presença acolhedora, inspirando confiança e respeito espontâneo.',
        'antipoda_msg': 'O Mestre do Desafio cutuca o orgulho do ego e o complexo de superioridade: o treino de hoje é brilhar com humildade sagrada.',
        'oculto_msg': 'O Tesouro Oculto é a chama crística que nunca se apaga dentro de você, sustentando sua esperança e força na matéria.',
        'quinta_msg': 'A Quinta Força ativa o Mestre Solar: a consciência iluminada que reconhece o divino em cada ser e vive na paz do Agora.',
        'leo_cura_steph': 'Leo ilumina o caminho de Stephanie com generosidade e reverência: celebra as virtudes dela e lembra que ela é uma rainha soberana.',
        'steph_cura_leo': 'Stephanie traz calor e aconchego solar para o coração de Leo: acolhe-o com carinho, celebra a liderança dele e enche a casa de alegria.',
        'cura_casal': 'Celebrar a bênção do encontro. Expressem 3 gratidões sinceras um pelo outro e deixem o sol da união iluminar todos ao redor.'
    }
}

# ==========================================
# 2. OS 13 TONS GALÁCTICOS DA CRIAÇÃO
# ==========================================

TONES = {
    1: ('Magnético', 'Unificar', 'Atrair', 'Propósito', 'Morcego 🦇', 'Qual é o meu propósito?'),
    2: ('Lunar', 'Polarizar', 'Estabilizar', 'Desafio', 'Escorpião 🦂', 'Quais são os meus desafios?'),
    3: ('Elétrico', 'Ativar', 'Vincular', 'Serviço', 'Veado 🦌', 'Como posso servir melhor?'),
    4: ('Autoexistente', 'Definir', 'Medir', 'Forma', 'Coruja 🦉', 'Qual é a forma da minha ação?'),
    5: ('Harmônico', 'Potencializar', 'Comandar', 'Radiação', 'Pavão 🦚', 'Como reúno meus recursos e lidero?'),
    6: ('Rítmico', 'Organizar', 'Equilibrar', 'Igualdade', 'Lagarto 🦎', 'Como administro desafios com equilíbrio?'),
    7: ('Ressonante', 'Canalizar', 'Inspirar', 'Sintonização', 'Macaco 🐒', 'Como sintonizo meu canal com a Fonte?'),
    8: ('Galáctico', 'Harmonizar', 'Modelar', 'Integridade', 'Falcão 🦅', 'Eu vivo aquilo em que acredito?'),
    9: ('Solar', 'Pulsar', 'Realizar', 'Intenção', 'Jaguar 🐆', 'Como atinjo a minha intenção no mundo?'),
    10: ('Planetário', 'Aperfeiçoar', 'Produzir', 'Manifestação', 'Cão 🐕', 'Como manifesto frutos concretos?'),
    11: ('Espectral', 'Dissolver', 'Libertar', 'Liberação', 'Serpente 🐍', 'Como me liberto e solto o apego?'),
    12: ('Cristal', 'Dedicar', 'Cooperar', 'Cooperação', 'Coelho 🐇', 'Como coopero com tudo o que vive?'),
    13: ('Cósmico', 'Perseverar', 'Transcender', 'Presença', 'Tartaruga 🐢', 'Como expando minha presença e transcendo?')
}

TONE_DESCRIPTIONS = {
    1: 'O Raio da Unificação. Atrai a intenção primordial, estabelece o propósito dos 13 dias e conecta a alma à sua meta magnética.',
    2: 'O Raio da Polaridade. Identifica os desafios, reconhece os obstáculos e ancora a estabilidade necessária para não tombar diante dos atritos.',
    3: 'O Raio do Movimento. Ativa a energia do serviço, cria pontes e vínculos entre pessoas e recursos, colocando o propósito em ação dinâmica.',
    4: 'O Raio da Estrutura. Define os parâmetros, mede prioridades e desenha a forma exata e executável que a ideia precisa ter no chão.',
    5: 'O Raio do Comando. Reúne recursos internos e externos, potencializa a força central e estabelece liderança com autoridade radiante.',
    6: 'O Raio do Equilíbrio. Organiza a rotina, equilibra as demandas internas e externas e estabelece igualdade e estabilidade na caminhada.',
    7: 'O Raio da Sintonização. Canaliza a intuição superior, sintoniza o canal receptivo e inspira ações alinhadas com a ordem cósmica.',
    8: 'O Raio da Integridade. Harmoniza a conduta diária com a verdade do coração, modelando através do exemplo prático aquilo em que acredita.',
    9: 'O Raio da Intenção. Dispara a flecha da ação, pulsa a determinação no mundo e mobiliza forças para realizar o propósito na matéria.',
    10: 'O Raio da Manifestação. Produz resultados visíveis, aperfeiçoa os processos e colhe os frutos concretos do trabalho realizado.',
    11: 'O Raio da Liberação. Dissolve bloqueios e rigidezes, solta o controle e desapega do que já cumpriu seu papel para abrir espaço ao novo.',
    12: 'O Raio da Cooperação. Dedica os aprendizados à coletividade, universaliza a sabedoria e expande a cooperação em rede com o todo.',
    13: 'O Raio da Transcendência. Coroa a jornada de 13 passos, integra todos os aprendizados e transcende na presença pura e atemporal.'
}

# ==========================================
# 3. OS 13 TOTENS XAMÂNICOS (MEDICINA BIOLÓGICA)
# ==========================================

TOTEMS_DATA = {
    1: ('Morcego 🦇', 'Navegação no Escuro & Renascimento', 'O Morcego enxerga por ecolocalização no invisível e dorme de cabeça para baixo (nova perspectiva). Ele ensina a soltar velhas identidades para atrair o propósito primordial com coragem.'),
    2: ('Escorpião 🦂', 'Transmutação do Veneno & Defesa Lúcida', 'O Escorpião habita fendas profundas e transmuta a própria toxicidade em medicina protetora. Ele ensina a reconhecer a dualidade e estabilizar os desafios sem medo do atrito.'),
    3: ('Veado 🦌', 'Agilidade Compassiva & Salto Sagrado', 'O Veado pisa com leveza, sensibilidade extrema e rapidez nos saltos. Ele ensina a liderar pelo serviço amoroso, vinculando conexões sinceras sem perder a mansidão.'),
    4: ('Coruja 🦉', 'Visão Noturna Cirúrgica & Estrutura', 'A Coruja gira a cabeça 270 graus e enxerga através de qualquer camuflagem no escuro. Ela ensina a desenhar a forma exata dos projetos e medir prioridades com discernimento.'),
    5: ('Pavão 🦚', 'Irradiação Régia & Maestria de Presença', 'O Pavão abre a cauda de mil olhos dourados sem vergonha de seu esplendor e ingere plantas venenosas sem adoecer. Ele ensina a reunir recursos e comandar com autoridade benevolente.'),
    6: ('Lagarto 🦎', 'Regeneração Somática & Desapego Corporal', 'O Lagarto solta o próprio rabo para escapar de predadores e regenera seu tecido biológico ao sol. Ele ensina a organizar o equilíbrio da rotina soltando pesos sem apego.'),
    7: ('Macaco 🐒', 'Curiosidade Sagrada & Quebra de Rigidez', 'O Macaco salta de galho em galho com inteligência lúdica e desfaz nós complexos brincando. Ele ensina a sintonizar o canal intuitivo quebrando a solenidade pesada do ego.'),
    8: ('Falcão 🦅', 'Voo Altaneiro & Foco Impecável', 'O Falcão sobrevoa as tempestades com visão de raio-X e mergulha em alta velocidade no alvo. Ele ensina a harmonizar a integridade ética, modelando o que se prega na prática.'),
    9: ('Jaguar 🐆', 'Força Silenciosa & Realização da Intenção', 'O Jaguar caminha na floresta sem quebrar um galho e salta no momento exato com precisão letal. Ele ensina a pulsar a intenção no silêncio até materializá-la no mundo físico.'),
    10: ('Cão 🐕', 'Lealdade Instintiva & Amor Protetor', 'O Cão protege o território, serve com devoção desinteressada e fareja perigos à distância. Ele ensina a aperfeiçoar a manifestação material servindo a quem se ama com fidelidade.'),
    11: ('Serpente 🐍', 'Troca de Pele & Kundalini Sagrada', 'A Serpente rasga a própria pele apertada para continuar crescendo e sente as vibrações da Terra pela barriga. Ela ensina a dissolver amarras e libertar o fluxo vital estagnado.'),
    12: ('Coelho 🐇', 'Fertilidade Comunitária & Partilha', 'O Coelho vive em tocas compartilhadas, multiplica recursos e vigia os arredores com atenção mansa. Ele ensina a cooperar em rede e dedicar seus dons à comunidade com generosidade.'),
    13: ('Tartaruga 🐢', 'Paciência Cósmica & Presença Atemporal', 'A Tartaruga carrega o mapa do tempo natural no casco (13 escamas centrais e 28 periféricas). Ela ensina a transcender a pressa ilusória e perseverar na presença do Agora.')
}

# ==========================================
# 4. OS 5 CASTELOS DE 52 DIAS (RODA MAIOR)
# ==========================================

CASTLES_DATA = {
    1: {
        'nome': 'Castelo Vermelho do Leste (Kins 001 a 052)',
        'corte': 'Corte do Nascimento (Iniciar e Semear)',
        'direcao': 'Leste (Iniciação / Entrada da Vida)',
        'missao': 'Fundar as bases do ciclo de 260 dias. Momento de lançar projetos, acolher novas ideias, confiar na nutrição da vida e dar o primeiro passo com coragem.'
    },
    2: {
        'nome': 'Castelo Branco do Norte (Kins 053 a 104)',
        'corte': 'Corte da Purificação (Refinar e Desapegar)',
        'direcao': 'Norte (Refinamento / Mente e Espírito)',
        'missao': 'Refinar a mente, desapegar de crenças e estruturas que não servem mais, perdoar o passado e clarear a comunicação com o Espírito.'
    },
    3: {
        'nome': 'Castelo Azul do Oeste (Kins 105 a 156)',
        'corte': 'Corte da Transformação (Alquimia e Queima Cármica)',
        'direcao': 'Oeste (Transformação / Alquimia das Águas)',
        'missao': 'O coração alquímico do Tzolkin (contém a Coluna Mística e os 20 Portais Ômega/Alfa). Momento de transmutar dores, catalisar mudanças radicais e quebrar velhos padrões.'
    },
    4: {
        'nome': 'Castelo Amarelo do Sul (Kins 157 a 208)',
        'corte': 'Corte do Florescimento (Amadurecer e Colher)',
        'direcao': 'Sul (Amadurecimento / Florescimento e Fogo)',
        'missao': 'Colheita dos frutos e ancoragem da sabedoria. Momento de assumir autorresponsabilidade ética, expressar o livre-arbítrio com maturidade e expandir a maestria.'
    },
    5: {
        'nome': 'Castelo Verde Central (Kins 209 a 260)',
        'corte': 'Corte da Matriz e Sincronização (O Retorno e Voo Mágico)',
        'direcao': 'Centro (Matriz / Conexão com Hunab Ku)',
        'missao': 'Síntese cósmica de toda a jornada de 260 dias. Momento de integrar as lições, viver o Tempo como Arte, partilhar com a comunidade e preparar o voo mágico para o próximo ciclo.'
    }
}

# ==========================================
# 5. AS 4 CORES & DIREÇÕES CÓSMICAS
# ==========================================

COLORS_DATA = {
    'Vermelho': {
        'direcao': 'Leste (Iniciação / Entrada da Vida)',
        'verbo': 'INICIA',
        'ensino': 'A força do Leste traz o impulso primordial do nascimento. É a energia do corpo físico, da nutrição celular, da vitalidade e da coragem de começar sem hesitar.'
    },
    'Branco': {
        'direcao': 'Norte (Refinamento / Mente e Espírito)',
        'verbo': 'REFINA',
        'ensino': 'A força do Norte traz o sopro do Espírito e a clareza mental. É a energia do desapego, da pureza verbal, do silenciamento do ego e da verdade que não precisa de adornos.'
    },
    'Azul': {
        'direcao': 'Oeste (Transformação / Alquimia das Águas)',
        'verbo': 'TRANSFORMA',
        'ensino': 'A força do Oeste traz a alquimia profunda das emoções. É a energia da noite fértil, dos sonhos lúcidos, da cura pelas mãos, da leveza do humor e da quebra de ilusões.'
    },
    'Amarelo': {
        'direcao': 'Sul (Amadurecimento / Florescimento e Fogo)',
        'verbo': 'AMADURECE',
        'ensino': 'A força do Sul traz o fogo solar e a colheita da sabedoria. É a energia do foco cirúrgico, da arte elegante, da autorresponsabilidade ética e do amor incondicional pleno.'
    }
}

# ==========================================
# 6. PULSARES & ETAPAS DA ONDA
# ==========================================

PULSARS = {
    1: ('Pulsar do Tempo (4D)', 'Propósito, intuição pura e alinhamento com a Fonte.'),
    2: ('Pulsar dos Sentidos (1D)', 'Corpo biológico, saúde física e inteligência visceral.'),
    3: ('Pulsar da Mente (2D)', 'Psicologia, clareza mental e desarme de crenças.'),
    4: ('Pulsar da Forma (3D)', 'Materialização, métodos, sistemas e construção prática.'),
    5: ('Pulsar do Tempo (4D)', 'Comando e liderança alinhados ao propósito maior.'),
    6: ('Pulsar dos Sentidos (1D)', 'Equilíbrio corporal, rotina e autorregulação somática.'),
    7: ('Pulsar da Mente (2D)', 'Canalização de inspiração e sintonização direta.'),
    8: ('Pulsar da Forma (3D)', 'Harmonia entre integridade ética e estrutura prática.'),
    9: ('Pulsar do Tempo (4D)', 'Disparo da intenção e realização com convicção.'),
    10: ('Pulsar dos Sentidos (1D)', 'Aperfeiçoamento da entrega e resultados tangíveis.'),
    11: ('Pulsar da Mente (2D)', 'Dissolução de apegos mentais e liberação do controle.'),
    12: ('Pulsar da Forma (3D)', 'Cooperação em rede e partilha comunitária.'),
    13: ('Pulsar do Tempo (4D)', 'Transcendência, presença pura e voo no Agora.')
}

WAVE_STAGES = {
    1: ('Etapa 1 — PROPÓSITO', 'O Tom Magnético atrai a intenção: define-se A META central da jornada.'),
    2: ('Etapa 1 — PROPÓSITO', 'O Tom Lunar identifica a dualidade: mapeiam-se OS DESAFIOS a superar.'),
    3: ('Etapa 1 — PROPÓSITO', 'O Tom Elétrico põe a energia em movimento: ativa-se O SERVIÇO e as pontes.'),
    4: ('Etapa 1 — PROPÓSITO', 'O Tom Autoexistente desenha a forma: define-se A ESTRUTURA DA AÇÃO.'),
    5: ('Etapa 2 — POTÊNCIA', 'O Tom Harmônico centraliza o poder: assume-se O COMANDO do processo.'),
    6: ('Etapa 2 — POTÊNCIA', 'O Tom Rítmico encontra a cadência: organiza-se O EQUILÍBRIO da rotina.'),
    7: ('Etapa 2 — POTÊNCIA', 'O Tom Ressonante é a coluna da onda: sintoniza-se COM A FONTE inspiradora.'),
    8: ('Etapa 2 — POTÊNCIA', 'O Tom Galáctico checa a integridade: pergunta-se: EU VIVO O QUE ACREDITO?'),
    9: ('Etapa 3 — AÇÃO', 'O Tom Solar dispara a força: é dia de REALIZAR a intenção sem hesitar.'),
    10: ('Etapa 3 — AÇÃO', 'O Tom Planetário manifesta: é dia de PRODUZIR frutos palpáveis na matéria.'),
    11: ('Etapa 3 — AÇÃO', 'O Tom Espectral dissolve o excesso: é dia de LIBERTAR amarras e soltar.'),
    12: ('Etapa 3 — AÇÃO', 'O Tom Cristal abre para a partilha: é dia de COOPERAR em rede.'),
    13: ('Etapa 4 — TRANSCENDER', 'O Tom Cósmico conclui o ciclo: é dia de PERSEVERAR na presença pura.')
}

WAVES = [
    (1, 'Dragão Vermelho', 'Iniciação e Confiança Primordial'),
    (14, 'Mago Branco', 'Atemporalidade e Presença Pura'),
    (27, 'Mão Azul', 'Cura e Realização na Matéria'),
    (40, 'Sol Amarelo', 'Iluminação e Fogo Universal'),
    (53, 'Caminhante do Céu Vermelho', 'Exploração e Quebra de Limites'),
    (66, 'Enlaçador de Mundos Branco', 'Desapego e Morte Sagrada'),
    (79, 'Tormenta Azul', 'Autogeração e Catarse Construtiva'),
    (92, 'Humano Amarelo', 'Livre-Arbítrio e Sabedoria Vivida'),
    (105, 'Serpente Vermelha', 'Força Vital e Regeneração'),
    (118, 'Espelho Branco', 'Verdade Nua e Discernimento'),
    (131, 'Macaco Azul', 'Magia da Ilusão e Leveza Lúcida'),
    (144, 'Semente Amarela', 'Foco e Florescimento do Potencial'),
    (157, 'Terra Vermelha', 'Navegação e Sincronicidade com Gaia'),
    (170, 'Cachorro Branco', 'Amor Incondicional e Lealdade'),
    (183, 'Noite Azul', 'Intuição e Abundância Invisível'),
    (196, 'Guerreiro Amarelo', 'Inteligência e Coragem Ética'),
    (209, 'Lua Vermelha', 'Purificação e Fluxo Universal'),
    (222, 'Vento Branco', 'Comunicação e Espírito'),
    (235, 'Águia Azul', 'Visão Panorâmica e Mente Superior'),
    (248, 'Estrela Amarela', 'Arte, Elegância e Harmonia')
]

PAGS = {
    1, 20, 22, 39, 43, 50, 51, 58, 64, 69, 72, 77, 85, 88, 93, 96, 106, 107, 108, 109,
    110, 111, 112, 113, 114, 115, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
    165, 168, 173, 176, 184, 189, 192, 197, 203, 208, 211, 218, 222, 239, 241, 260
}

PLASMAS = [
    ('Dali', 'Chakra Coronário', 'Visualização e Alinhamento com a Fonte'),
    ('Seli', 'Chakra Raiz', 'Fluxo e Aterramento da Força Física'),
    ('Gamma', 'Chakra 3º Olho', 'Pacificação Mental e Discernimento'),
    ('Kali', 'Chakra Sexual/Ventre', 'Catalisação e Poder Criativo'),
    ('Alfa', 'Chakra Laríngeo', 'Liberação e Expressão da Palavra'),
    ('Limi', 'Chakra Plexo Solar', 'Purificação da Vontade e Digestão Emocional'),
    ('Silio', 'Chakra Cardíaco', 'Amor Cósmico e Descarga de Tensão')
]

# ==========================================
# CÁLCULOS MATEMÁTICOS OFICIAIS
# ==========================================

def calculate_kin(target_date: datetime.date) -> int:
    anchor_date = datetime.date(2003, 9, 4)
    anchor_kin = 194
    d = min(target_date, anchor_date)
    end = max(target_date, anchor_date)
    leap_days = 0
    cur = d
    while cur < end:
        if cur.month == 2 and cur.day == 29:
            leap_days += 1
        cur += datetime.timedelta(days=1)
    total_days = (end - d).days - leap_days
    if target_date >= anchor_date:
        return ((anchor_kin - 1 + total_days) % 260) + 1
    else:
        return ((anchor_kin - 1 - total_days) % 260) + 1

def get_seal_num(k: int): return ((k - 1) % 20) + 1
def get_tone_num(k: int): return ((k - 1) % 13) + 1

def get_castle_data(k: int):
    c_idx = ((k - 1) // 52) + 1
    c_day = ((k - 1) % 52) + 1
    c_info = CASTLES_DATA[c_idx]
    return {
        'num': c_idx, 'day_in_castle': c_day,
        'nome': c_info['nome'], 'corte': c_info['corte'],
        'direcao': c_info['direcao'], 'missao': c_info['missao']
    }

def get_kin_data(k: int):
    s_num = get_seal_num(k)
    t_num = get_tone_num(k)
    s = SEALS[s_num]
    t = TONES[t_num]
    totem = TOTEMS_DATA[t_num]
    color_info = COLORS_DATA[s['cor']]
    full_name = f"{s['nome'].split()[0]} {t[0]} {s['nome'].split()[-1]}"
    wave_idx = [i for i, wv in enumerate(WAVES) if wv[0] <= k][-1]
    wave_data = WAVES[wave_idx]
    degrau = k - wave_data[0] + 1
    castle = get_castle_data(k)
    pulsar = PULSARS[t_num]
    stage = WAVE_STAGES[t_num]
    harmonica_num = ((k - 1) // 4) + 1
    harm_start = ((harmonica_num - 1) * 4) + 1
    harm_end = harm_start + 3
    
    is_mystic_column = (121 <= k <= 140)
    is_zero_point = (k in (130, 131))
    is_omega_portal = (106 <= k <= 115)
    is_alpha_portal = (146 <= k <= 155)

    # Síntese Mestra da Alquimia Selo + Tom
    alquimia_sintese = f"{s['nome'].split()[0]} ({s['poder']}) + Tom {t[0]} ({t[2]} o {t[3]}): A maestria de {t[2].lower()} a frequência de {s['poder'].lower()} para manifestar {s['essencia'].lower()} através de {s['descricao'].split(',')[0].lower()}."

    return {
        'kin': k, 'seal_num': s_num, 'tone_num': t_num,
        'seal': s, 'tone': t, 'name': full_name,
        'totem': totem, 'color_info': color_info,
        'wave': wave_data, 'wave_num': wave_idx + 1,
        'degrau': degrau, 'castle': castle,
        'is_pag': k in PAGS,
        'pulsar': pulsar, 'stage': stage,
        'harmonica': (harmonica_num, harm_start, harm_end),
        'alquimia_sintese': alquimia_sintese,
        'is_mystic_column': is_mystic_column,
        'is_zero_point': is_zero_point,
        'is_omega_portal': is_omega_portal,
        'is_alpha_portal': is_alpha_portal
    }

def get_oracle(k: int):
    s = get_seal_num(k)
    t = get_tone_num(k)
    if s <= 18: s_an = 19 - s
    elif s == 19: s_an = 20
    else: s_an = 19
    k_an = [x for x in range(1, 261) if get_seal_num(x) == s_an and get_tone_num(x) == t][0]
    s_anti = ((s + 9) % 20) + 1
    k_anti = [x for x in range(1, 261) if get_seal_num(x) == s_anti and get_tone_num(x) == t][0]
    k_oc = 261 - k
    if t in [1, 6, 11]: s_g = s
    elif t in [2, 7, 12]: s_g = ((s + 11) % 20) + 1
    elif t in [3, 8, 13]: s_g = ((s + 3) % 20) + 1
    elif t in [4, 9]: s_g = ((s + 15) % 20) + 1
    elif t in [5, 10]: s_g = ((s + 7) % 20) + 1
    k_g = [x for x in range(1, 261) if get_seal_num(x) == s_g and get_tone_num(x) == t][0]
    s_sum = k + k_g + k_an + k_anti + k_oc
    k_qf = ((s_sum - 1) % 260) + 1
    return {
        'destino': get_kin_data(k), 'guia': get_kin_data(k_g),
        'analogo': get_kin_data(k_an), 'antipoda': get_kin_data(k_anti),
        'oculto': get_kin_data(k_oc), 'quinta_forca': get_kin_data(k_qf)
    }

def get_13_moon_info(d: datetime.date):
    year_start = datetime.date(d.year if d >= datetime.date(d.year, 7, 26) else d.year - 1, 7, 26)
    days_since = (d - year_start).days
    if d == datetime.date(d.year, 7, 25):
        return {'is_dft': True, 'moon_name': 'Dia Fora do Tempo', 'moon_action': 'Celebração da Paz Cósmica', 'day_of_moon': 0, 'plasma': ('Silio', 'Chakra Cardíaco', 'Amor Cósmico'), 'heptad': 52}
    moon_num = (days_since // 28) + 1
    day_of_moon = (days_since % 28) + 1
    plasma_info = PLASMAS[(day_of_moon - 1) % 7]
    heptad = (days_since // 7) + 1
    moon_names = [
        ('1. Lua Magnética do Morcego', 'Unificar o Propósito'), ('2. Lua Lunar do Escorpião', 'Identificar o Desafio'),
        ('3. Lua Elétrica do Veado', 'Ativar o Serviço'), ('4. Lua Autoexistente da Coruja', 'Definir a Forma'),
        ('5. Lua Harmônica do Pavão', 'Potencializar o Comando'), ('6. Lua Rítmica do Lagarto', 'Organizar o Equilíbrio'),
        ('7. Lua Ressonante do Macaco', 'Canalizar a Inspiração'), ('8. Lua Galáctica do Falcão', 'Harmonizar a Integridade'),
        ('9. Lua Solar do Jaguar', 'Pulsar a Intenção'), ('10. Lua Planetária do Cão', 'Aperfeiçoar a Manifestação'),
        ('11. Lua Espectral da Serpente', 'Dissolver o Apego'), ('12. Lua Cristal do Coelho', 'Dedicar a Cooperação'),
        ('13. Lua Cósmica da Tartaruga', 'Perseverar a Presença')
    ]
    return {'is_dft': False, 'moon_name': moon_names[moon_num-1][0], 'moon_action': moon_names[moon_num-1][1], 'moon_num': moon_num, 'day_of_moon': day_of_moon, 'plasma': plasma_info, 'heptad': heptad}

DECREE_TONE_DATA = {
    1: ('Unifico', 'atraindo', 'do propósito', 'pelo meu próprio poder duplicado'),
    2: ('Polarizo', 'estabilizando', 'do desafio', None),
    3: ('Ativo', 'vinculando', 'do serviço', None),
    4: ('Defino', 'medindo', 'da forma', None),
    5: ('Potencializo', 'comandando', 'da radiação', None),
    6: ('Organizo', 'equilibrando', 'da igualdade', 'pelo meu próprio poder duplicado'),
    7: ('Canalizo', 'inspirando', 'da sintonização', None),
    8: ('Harmonizo', 'modelando', 'da integridade', None),
    9: ('Pulso', 'realizando', 'da intenção', None),
    10: ('Aperfeiçoo', 'produzindo', 'da manifestação', None),
    11: ('Dissolvo', 'libertando', 'da liberação', 'pelo meu próprio poder duplicado'),
    12: ('Dedico-me', 'universalizando', 'da cooperação', None),
    13: ('Persevero', 'transcendendo', 'da presença', None)
}

DECREE_SEAL_DATA = {
    1: ('nutrir', 'o ser', 'a entrada', 'do nascimento'),
    2: ('comunicar', 'o alento', 'o armazém', 'do espírito'),
    3: ('sonhar', 'a intuição', 'o processo', 'da abundância'),
    4: ('focalizar', 'a percepção', 'a saída', 'do florescimento'),
    5: ('sobreviver', 'o instinto', 'a entrada', 'da força vital'),
    6: ('igualar', 'a oportunidade', 'o armazém', 'da morte e dos novos ciclos'),
    7: ('conhecer', 'a cura', 'o processo', 'da realização'),
    8: ('embelezar', 'a arte', 'a saída', 'da elegância'),
    9: ('purificar', 'o fluxo', 'a entrada', 'da água universal'),
    10: ('amar', 'a lealdade', 'o armazém', 'do coração'),
    11: ('brincar', 'a ilusão', 'o processo', 'da magia'),
    12: ('influenciar', 'a sabedoria', 'a saída', 'do livre-arbítrio'),
    13: ('explorar', 'a vigilância', 'a entrada', 'do espaço'),
    14: ('encantar', 'a receptividade', 'o armazém', 'da atemporalidade'),
    15: ('criar', 'a mente', 'o processo', 'da visão'),
    16: ('questionar', 'a coragem', 'a saída', 'do inteligência'),
    17: ('evoluir', 'a sincronicidade', 'a entrada', 'da navegação'),
    18: ('refletir', 'a ordem', 'o armazém', 'do infinito'),
    19: ('catalisar', 'a energia', 'o processo', 'da autogeração'),
    20: ('iluminar', 'a vida', 'a saída', 'do fogo universal')
}

def build_decree(kd, oracle=None):
    s_num = kd['seal_num']
    t_num = kd['tone_num']
    s_info = DECREE_SEAL_DATA[s_num]
    t_info = DECREE_TONE_DATA[t_num]
    
    if oracle is None:
        oracle = get_oracle(kd['kin'])
    guide_seal_num = oracle['guia']['seal_num']
    
    if t_info[3]:
        guide_phrase = f"Eu sou guiado {t_info[3]}."
    else:
        guide_phrase = f"Eu sou guiado pelo poder {DECREE_SEAL_DATA[guide_seal_num][3]}."
        
    pag_suffix = "\nSou um portal de ativação galáctica, entra em mim." if kd['is_pag'] else ""
    
    return f"{t_info[0]} com o fim de {s_info[0]},\n{t_info[1].capitalize()} {s_info[1]}.\nSelo {s_info[2]} {s_info[3]}\nCom o tom {kd['tone'][0].lower()} {t_info[2]}.\n{guide_phrase}{pag_suffix}"

def format_quote_lines(text: str) -> str:
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
    return '\n'.join(f"> _{line}_" for line in lines)

# ==========================================
# 4. HISTÓRIAS DAS 20 ONDAS ENCANTADAS
# ==========================================

WAVE_STORIES = {
    1: ('Onda do Dragão Vermelho', 'Nascimento & Confiança Primordial', 'A alma mergulha no útero da criação para resgatar a nutrição original e confiar que a vida sustenta o seu passo.'),
    2: ('Onda do Mago Branco', 'Atemporalidade & Presença Pura', 'A travessia convoca você a sair da ansiedade do futuro e habitar o eterno Agora, onde reside a verdadeira magia.'),
    3: ('Onda da Mão Azul', 'Cura & Realização na Matéria', 'A missão é transformar visão em obra concreta: fechar processos abertos, curar a si mesmo e realizar com método.'),
    4: ('Onda do Sol Amarelo', 'Iluminação & Fogo Universal', 'O ciclo coroa a jornada despertando a consciência da unidade, a autoridade benevolente e o amor incondicional.'),
    5: ('Onda do Caminhante do Céu Vermelho', 'Exploração & Quebra de Limites', 'O chamado é desbravar territórios desconhecidos, romper prisões mentais e expandir com vigilância lúcida.'),
    6: ('Onda do Enlaçador de Mundos Branco', 'Desapego & Pontes Sagradas', 'A travessia exige a coragem de encerrar o que já morreu, perdoar o passado e construir pontes para o novo ciclo.'),
    7: ('Onda da Tormenta Azul', 'Autotransmutação & Autogeração', 'O ciclo traz o raio da renovação: catalisar mudanças radicais, quebrar velhas cascas e autogerar energia.'),
    8: ('Onda do Humano Amarelo', 'Livre-Arbítrio & Sabedoria Vivida', 'A missão exige maturidade ética: assumir a responsabilidade total pelas próprias escolhas e colher a sabedoria.'),
    9: ('Onda da Serpente Vermelha', 'Força Vital & Regeneração Somática', 'A travessia desperta a sabedoria biológica do corpo físico, a kundalini e a capacidade de trocar de pele.'),
    10: ('Onda do Espelho Branco', 'Discernimento & Ordem Sagrada', 'O ciclo coloca a lâmina da verdade na mão: cortar ilusões, encerrar projeções do ego e ver a realidade pura.'),
    11: ('Onda do Macaco Azul', 'Magia & Leveza Lúcida', 'O ciclo atravessa o coração da matriz quebrando a solenidade pesada pelo humor sagrado e devolvendo o encanto de viver.'),
    12: ('Onda da Semente Amarela', 'Foco & Florescimento do Potencial', 'A missão exige paciência orgânica: selecionar o essencial, mirar no alvo e permitir que o potencial germine.'),
    13: ('Onda da Terra Vermelha', 'Sincronicidade & Navegação com Gaia', 'A travessia ensina a ler os sinais invisíveis do caminho e sincronizar os ritmos pessoais com a Terra.'),
    14: ('Onda do Cachorro Branco', 'Amor Incondicional & Lealdade', 'O ciclo ancora a medicina do coração: amar sem cobranças, ser leal à própria essência e proteger o clã.'),
    15: ('Onda da Noite Azul', 'Intuição & Abundância Invisível', 'O ciclo convida a mergulhar no silêncio interior, sonhar com nitidez e confiar na abundância fértil do invisível.'),
    16: ('Onda do Guerreiro Amarelo', 'Inteligência & Coragem Ética', 'A missão é empunhar a espada do discernimento: questionar com inteligência destemida e viver com integridade moral.'),
    17: ('Onda da Lua Vermelha', 'Purificação & Fluxo das Águas', 'O ciclo convida a purificar memórias celulares, soltar represamentos emocionais e lembrar de quem você é.'),
    18: ('Onda do Vento Branco', 'Comunicação Consciente & Espírito', 'O ciclo ensina a nobreza da palavra: expressar a verdade límpida, purificar o diálogo interno e respirar com presença.'),
    19: ('Onda da Águia Azul', 'Metavisão & Mente Planetária', 'A missão convoca a subir o drone da consciência, enxergar o panorama de longo alcance e criar com compaixão.'),
    20: ('Onda da Estrela Amarela', 'Arte, Elegância & Harmonia Cósmica', 'O ciclo final do Tzolkin! A missão de coroar os 260 dias vivendo o Tempo como Arte e transformando atrito em harmonia.')
}

def build_wave_narrative(kd):
    wv_num = kd['wave_num']
    wv_info = WAVE_STORIES.get(wv_num, (kd['wave'][1], 'Jornada Sagrada', 'Evolução dos 13 passos'))
    t_num = kd['tone_num']
    
    if t_num == 1:
        step_narrative = "O ponto de partida. Aqui a semente do propósito é ancorada e a intenção dos 13 dias é atraída para a consciência."
    elif t_num == 2:
        step_narrative = "Fase de Reconhecimento. Mapear os desafios e polaridades para ancorar estabilidade diante dos obstáculos."
    elif t_num == 3:
        step_narrative = "Fase de Movimento. Ativar o serviço, colocar a energia em circulação e construir pontes de cooperação."
    elif t_num == 4:
        step_narrative = "Fase de Estruturação. Desenhar a forma prática, medir prioridades e dar contorno executável às ideias."
    elif t_num == 5:
        step_narrative = "Fase de Comando. Centralizar recursos internos, potencializar a liderança e irradiar autoridade serena."
    elif t_num == 6:
        step_narrative = "Fase de Equilíbrio. Organizar a rotina, cadenciar o ritmo de entrega e harmonizar as demandas diárias."
    elif t_num == 7:
        step_narrative = "Fase de Sintonização. Canalizar a intuição superior e agir alinhado à ordem natural dos fatos."
    elif t_num == 8:
        step_narrative = "Fase de Integridade. Checar a coerência ética entre o que se acredita e o que se pratica no dia a dia."
    elif t_num == 9:
        step_narrative = "Fase de Intenção. Disparar a força de ação e realizar o propósito na matéria com determinação."
    elif t_num == 10:
        step_narrative = "Fase de Manifestação. Produzir resultados concretos, aperfeiçoar os processos e colher os frutos do trabalho."
    elif t_num == 11:
        step_narrative = "Fase de Liberação. Dissolver rigidezes, desapegar de velhos controles e abrir espaço para o fluxo novo."
    elif t_num == 12:
        step_narrative = "Fase de Cooperação. Partilhar a sabedoria acumulada, dedicar dons à comunidade e agir em rede."
    else:
        step_narrative = "O Voo Cósmico e a culminação da jornada. Momento de integrar os aprendizados e transcender na presença pura."
        
    return {
        'titulo': wv_info[0],
        'tema': wv_info[1],
        'arco': wv_info[2],
        'degrau_texto': step_narrative
    }

def clean_oracle_text(text: str) -> str:
    import re
    cleaned = text.strip()
    if ':' in cleaned:
        parts = cleaned.split(':', 1)
        if len(parts[1].strip()) >= 15:
            cleaned = parts[1].strip()
    else:
        cleaned = re.sub(r'^[Oo] [Aa]liado de [Aa]poio\s+', '', cleaned)
        cleaned = re.sub(r'^[Oo] [Tt]esouro [Oo]culto\s+', '', cleaned)
        cleaned = re.sub(r'^[Aa] [Qq]uinta [Ff]orça\s+', '', cleaned)
        cleaned = re.sub(r'^[Oo] [Ff]arol [Gg]uia\s+', '', cleaned)
        cleaned = re.sub(r'^[Oo] [Mm]estre do [Dd]esafio\s+', '', cleaned)
    if cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]
    return cleaned

# ==========================================
# 1. GERADOR GERAL (KIN DO DIA — SINCRONÁRIO GALÁCTICO)
# ==========================================

def generate_general_message(target_date: datetime.date) -> str:
    k = calculate_kin(target_date)
    kd = get_kin_data(k)
    oracle = get_oracle(k)
    lunar = get_13_moon_info(target_date)
    s = kd['seal']
    c = kd['castle']
    decree = build_decree(kd, oracle)
    wave_story = build_wave_narrative(kd)

    pag_status = "🌀 *Portal PAG:* SIM (Alta Voltagem)" if kd['is_pag'] else "• *Portal PAG:* Não (Fluxo Estável)"
    
    special_events = []
    if kd['is_zero_point']:
        special_events.append("✨ *PONTO ZERO DO TZOLKIN:* Centro exato do espelhamento da matriz!")
    elif kd['is_mystic_column']:
        special_events.append("🌌 *COLUNA MÍSTICA:* Canal central de ressonância e silêncio fértil.")
    if kd['is_omega_portal']:
        special_events.append(f"🌀 *SEQUÊNCIA ÔMEGA:* Dia {k - 105}/10 de portais contínuos!")
    elif kd['is_alpha_portal']:
        special_events.append(f"🌀 *SEQUÊNCIA ALFA:* Dia {k - 145}/10 de portais contínuos!")

    special_str = ""
    if special_events:
        special_str = "\n" + "\n".join(special_events)

    g_name = oracle['guia']['name']
    a_name = oracle['analogo']['name']
    d_name = oracle['antipoda']['name']
    o_name = oracle['oculto']['name']
    q_name = oracle['quinta_forca']['name']

    msg = f"""☀️ *KIN DO DIA — {target_date.strftime('%d/%m/%Y')}*
*KIN {kd['kin']:03d} — {kd['name'].upper()}*
{pag_status}
🌙 {lunar['moon_name']} • Dia {lunar['day_of_moon']:02d} | 🏰 {c['nome'].split('(')[0].strip()} • Dia {c['day_in_castle']:02d}/52
🎯 *Foco de Hoje:* _"{s['chave']}"_{special_str}

*✦ 1. A ALQUIMIA DO DIA: SELO + TOM*
• ☀️ *Selo Solar — {s['nome']} ({s['maia']}):*
{s['descricao']}. Expressa o poder de {s['poder'].lower()} e a essência de {s['essencia'].lower()}.
• ⚡ *Tom Galáctico — Tom {kd['tone_num']} ({kd['tone'][0]}):*
{TONE_DESCRIPTIONS[kd['tone_num']]}
• 🔮 *A Alquimia da União:*
A união do {s['nome'].split()[0]} com o Tom {kd['tone'][0]} convida você a ancorar {s['essencia'].lower()} através da postura de {kd['tone'][2].lower()}. O dia favorece {s['descricao'].split(',')[0].lower()} com clareza e foco prático.

*✦ 2. O ESPELHO: LUZ & SOMBRA*
• 🟢 *Onde você ganha (Luz):* {s['luz']}
• 🔴 *Onde você tropeça (Sombra):* {s['sombra']}

*✦ 3. A BÚSSOLA DO ORÁCULO*
🧭 *Farol Guia ({g_name}):* {clean_oracle_text(oracle['guia']['seal']['guia_msg'])}
🤝 *Aliado de Apoio ({a_name}):* {clean_oracle_text(oracle['analogo']['seal']['analogo_msg'])}
⚡ *Mestre do Desafio ({d_name}):* {clean_oracle_text(oracle['antipoda']['seal']['antipoda_msg'])}
💎 *Tesouro Oculto ({o_name}):* {clean_oracle_text(oracle['oculto']['seal']['oculto_msg'])}
👑 *Quinta Força ({q_name}):* {clean_oracle_text(oracle['quinta_forca']['seal']['quinta_msg'])}

*✦ 4. A ONDA ENCANTADA DA {kd['wave'][1].upper()}*
• *Missão dos 13 Dias:* {wave_story['arco']}
• *Onde estamos hoje:* Degrau {kd['degrau']} de 13 — {wave_story['degrau_texto']}
• *Pergunta Guia:* _"{kd['tone'][5]}"_

*✦ 5. DIRETRIZES PRÁTICAS DO DIA*
• 🎯 *No Trabalho & Projetos:* {s['dir_trabalho']}
• 💬 *Nas Relações & Convivência:* {s['dir_relacoes']}

*✦ 6. REFLEXÃO DO DIA*
> _"{s['auto_investigacao']}"_

*✦ 7. DECRETO SAGRADO DE ATIVAÇÃO*
{format_quote_lines(decree)} ✨🚀

✨ *Sincronário da Lei do Tempo • @o.cosba*
_Quer saber seu Mapa do Kin completo? Chama no direct!_ 📩"""
    return msg


# ==========================================
# 2. GERADOR DO RAIO-X DO CASAL (ALQUIMIA DINÂMICA)
# ==========================================

def generate_private_message(target_date: datetime.date) -> str:
    k = calculate_kin(target_date)
    kd = get_kin_data(k)
    lunar = get_13_moon_info(target_date)
    s = kd['seal']

    # Kin Composto Individual de Leo (194) com o dia
    k_leo_comp = ((194 + k - 1) % 260) + 1
# ==========================================
# 2. GERADOR DO RAIO-X DO CASAL (ALQUIMIA DINÂMICA)
# ==========================================

TELEKTONON_CUBE = {
    7: ('1º Dia do Cubo (Dragão)', 'Virtude da Memória Primordial e Nutrição'),
    8: ('2º Dia do Cubo (Vento)', 'Virtude da Comunicação Consciente e Pureza da Palavra'),
    9: ('3º Dia do Cubo (Noite)', 'Virtude do Silêncio Fértil e Intuição'),
    10: ('4º Dia do Cubo (Semente)', 'Virtude do Foco Cirúrgico e Paciência'),
    11: ('5º Dia do Cubo (Serpente)', 'Virtude da Vitalidade Corporal e Vigor Físico'),
    12: ('6º Dia do Cubo (Enlaçador)', 'Virtude do Desapego e Perdão'),
    13: ('7º Dia do Cubo (Mão)', 'Virtude da Realização Concreta e Cura'),
    14: ('8º Dia do Cubo (Estrela)', 'Virtude da Harmonia Estética e Elegância'),
    15: ('9º Dia do Cubo (Lua)', 'Virtude da Purificação Emocional e Fluidez'),
    16: ('10º Dia do Cubo (Cachorro)', 'Virtude da Lealdade do Coração e Amor Incondicional'),
    17: ('11º Dia do Cubo (Macaco)', 'Virtude do Bom Humor e Quebra da Rigidez'),
    18: ('12º Dia do Cubo (Humano)', 'Virtude do Livre-Arbítrio e Maturidade Ética'),
    19: ('13º Dia do Cubo (Caminhante)', 'Virtude da Exploração de Fronteiras e Vigilância'),
    20: ('14º Dia do Cubo (Mago)', 'Virtude da Presença Atemporal e Poder do Agora'),
    21: ('15º Dia do Cubo (Águia)', 'Virtude da Metavisão Estratégica e Criação'),
    22: ('16º Dia do Cubo (Guerreiro)', 'Virtude da Coragem Lúcida e Inteligência Ética')
}

def get_telektonon_status(day_of_moon: int) -> str:
    if 1 <= day_of_moon <= 6:
        return f"Torre do Espírito (Dia {day_of_moon} de 6) — Alinhamento inicial da mente e foco no propósito"
    elif 7 <= day_of_moon <= 22:
        cube_info = TELEKTONON_CUBE[day_of_moon]
        return f"{cube_info[0]} — {cube_info[1]}"
    else:
        return f"Torre de Navegação (Dia {day_of_moon - 22} de 6) — Voo místico, integração e descanso da mente"

def get_couple_radar_atrito(cor_do_dia: str) -> str:
    if cor_do_dia == 'Vermelho':
        return "A pressa para abrir muitas frentes simultâneas pode gerar sobrecarga em Stephanie e irritação em Leonardo. O acordo de hoje é focar em uma única iniciativa prioritária."
    elif cor_do_dia == 'Branco':
        return "Leonardo tende a permanecer no plano das ideias, enquanto Stephanie pode sentir falta de direcionamento prático. O acordo de hoje é alinhar passos simples e claros."
    elif cor_do_dia == 'Azul':
        return "A sensibilidade emocional fica mais intensa, e pequenas cobranças podem gerar atrito desnecessário. O acordo de hoje é praticar escuta paciente e acolhimento mútuo."
    else:
        return "Cobrança por produtividade e perfeccionismo nos detalhes podem gerar cansaço mental. O acordo de hoje é definir um teto saudável de tarefas e desacelerar no horário combinado."

def generate_private_message(target_date: datetime.date) -> str:
    k = calculate_kin(target_date)
    kd = get_kin_data(k)
    lunar = get_13_moon_info(target_date)
    s = kd['seal']

    # Kin Composto Individual de Leo (194) com o dia
    k_leo_comp = ((194 + k - 1) % 260) + 1
    kd_leo = get_kin_data(k_leo_comp)
    s_leo = kd_leo['seal']

    # Kin Composto Individual de Steph (147) com o dia
    k_steph_comp = ((147 + k - 1) % 260) + 1
    kd_steph = get_kin_data(k_steph_comp)
    s_steph = kd_steph['seal']

    # Kin Composto do Casal (81) com o dia
    k_casal_comp = ((81 + k - 1) % 260) + 1
    kd_casal = get_kin_data(k_casal_comp)
    s_casal = kd_casal['seal']

    # Ressonâncias Leo
    rel_leo = "Trânsito Neutro e Fluidez Criativa"
    sn = kd['seal_num']
    if sn == 14: rel_leo = "👑 *Dia do seu Selo Natal (Mago)* — Potência máxima de presença e atemporalidade"
    elif sn == 4: rel_leo = "🛡️ *Dia do seu Antípoda (Semente)* — Desafio: ter paciência com os ciclos orgânicos"
    elif sn == 5: rel_leo = "🤝 *Dia do seu Análogo (Serpente)* — Aliado: vitalidade física e inteligência instintiva"
    elif sn == 6: rel_leo = "💎 *Dia do seu Oculto (Enlaçador)* — Força oculta: desapego sereno e leveza"
    elif sn == 19: rel_leo = "🧭 *Dia do seu Guia (Tormenta)* — Bússola: poder de autogeração e transformação"

    # Ressonâncias Steph
    rel_steph = "Trânsito Neutro e Fluidez Executiva"
    if sn == 7: rel_steph = "👑 *Dia do seu Selo Natal (Mão)* — Potência máxima de realização, ordem e cura"
    elif sn == 17: rel_steph = "🛡️ *Dia do seu Antípoda (Terra)* — Desafio: soltar o controle e confiar nos ritmos"
    elif sn == 12: rel_steph = "🤝 *Dia do seu Análogo (Humano)* — Aliado: sabedoria prática e bom senso"
    elif sn == 14: rel_steph = "💎 *Dia do seu Oculto (Mago)* — Força oculta: ancorar a paz no momento presente"
    elif sn == 3: rel_steph = "🧭 *Dia do seu Guia (Noite)* — Bússola: intuição profunda e silêncio fértil"

    p_info = lunar['plasma']
    tele_info = get_telektonon_status(lunar['day_of_moon'])
    atrito_info = get_couple_radar_atrito(s['cor'])

    msg = f"""🔒 *ESTUDO DA ALIANÇA & SINCRONÁRIO DO DIA*
*LEONARDO • MAGO CRISTAL | STEPHANIE • MÃO AUTOEXISTENTE*

☀️ *Frequência do Dia:* Kin {kd['kin']:03d} — {kd['name'].upper()}
🌙 {lunar['moon_name']} • Dia {lunar['day_of_moon']:02d} | 🏰 {kd['castle']['nome'].split('(')[0].strip()}
⚡ *Plasma Radial:* {p_info[0]} • {p_info[1]} ({p_info[2]})
🛡️ *Jornada do Telektonon:* {tele_info}

*✦ 1. LEONARDO (Mago Cristal Branco)*
• *Ressonância:* {rel_leo}
• *Energia Ativada:* {kd_leo['name']}
• *Foco do Dia:* {s_leo['dir_trabalho']}
• *Suporte para Stephanie:* Leo sustenta um campo de tranquilidade para Stephanie, ajudando a silenciar a pressa mental com presença serena e escuta atenta.

*✦ 2. STEPHANIE (Mão Autoexistente Azul)*
• *Ressonância:* {rel_steph}
• *Energia Ativada:* {kd_steph['name']}
• *Foco do Dia:* {s_steph['dir_trabalho']}
• *Suporte para Leonardo:* Stephanie traz aterramento e estrutura para a visão de Leo, ajudando a traduzir ideias em passos concretos e bem organizados.

*✦ 3. A SINERGIA DA ALIANÇA (Egrégora Dragão Elétrico)*
• *Sinergia dos Arquétipos Hoje:*
A união entre o Mago (presença e visão sutil) e a Mão (estrutura e realização prática) forma a energia do Dragão: nutrição primordial, criação de novas bases e cuidado mútuo.
• *Clima de Convivência:*
{s_casal['cura_casal']}
• ⚠️ *Atenção na Dinâmica:*
{atrito_info}"""
    return msg


# ==========================================
# 3. GERADORES DE AULAS TEMÁTICAS ESPECIALIZADAS
# ==========================================

def generate_wave_lesson(target_date: datetime.date) -> str:
    k = calculate_kin(target_date)
    kd = get_kin_data(k)
    wave_story = build_wave_narrative(kd)
    degrau = kd['degrau']
    wave_seal = SEALS[get_seal_num(kd['wave'][0])]
    
    msg = f"""🌊 *AULA DA ONDA ENCANTADA — {wave_story['titulo'].upper()}*
*Ciclo de 13 Dias: {wave_story['tema']}*

Hoje navegamos no *Degrau {degrau:02d}/13* desta jornada de 13 dias.

*✦ O ARCO NARRATIVO DA ONDA:*
{wave_story['arco']}
A missão coletiva destes 13 passos é despertar o poder de {wave_seal['poder'].lower()} e manifestar a essência de {wave_seal['essencia'].lower()}.

*✦ O SEU POSICIONAMENTO HOJE (DEGRAU {degrau:02d}/13):*
• *Tom Regente:* Tom {kd['tone_num']} — {kd['tone'][0]} ({kd['tone'][3]})
• *Etapa Atual:* {wave_story['degrau_texto']}
• *A Pergunta que Guia o Dia:* _"{kd['tone'][5]}"_
• *Dimensão Operacional:* {kd['pulsar'][0]} — {kd['pulsar'][1]}

*✦ MAPA DOS 4 BLOCOS DA ONDA:*
• *Etapa 1 (Tons 1 a 4):* Fundação do Propósito (Atrair meta, identificar atritos, ativar serviço e definir forma).
• *Etapa 2 (Tons 5 a 8):* Desenvolvimento da Potência (Comandar recursos, cadenciar rotina, canalizar e harmonizar).
• *Etapa 3 (Tons 9 a 12):* Materialização e Ação (Pulsar intenção, aperfeiçoar manifestação, libertar e cooperar).
• *Etapa 4 (Tom 13):* Transcendência Cósmica (Completar a jornada e perseverar na presença).

💡 *Diretriz de Navegação:* Respeite o degrau de hoje. Não tente colher no dia de plantar, nem tente planejar no dia de transcender. Viva o ritmo natural do Tom {kd['tone'][0]}!"""
    return msg

def generate_castle_lesson(target_date: datetime.date) -> str:
    k = calculate_kin(target_date)
    kd = get_kin_data(k)
    c = kd['castle']
    
    msg = f"""🏰 *AULA DO CASTELO DE 52 DIAS — {c['nome'].upper()}*
*Fase Atual: Dia {c['day_in_castle']:02d}/52 ({c['corte']})*

O Tzolkin de 260 dias é dividido em 5 Castelos de 52 dias (4 Ondas Encantadas por Castelo).

*✦ A CORTE ATUAL: {c['corte'].upper()}*
• *Direção Cósmica:* {c['direcao']}
• *A Grande Missão Coletiva:* {c['missao']}

*✦ O MAPA DOS 5 CASTELOS NO ANO:*
1. 🟥 *Castelo Vermelho do Leste (1-52):* Corte do Nascimento (Fundar bases e iniciar).
2. ⬜ *Castelo Branco do Norte (53-104):* Corte da Purificação (Refinar e desapegar).
3. 🟦 *Castelo Azul do Oeste (105-156):* Corte da Transformação (Alquimia e queima cármica).
4. 🟨 *Castelo Amarelo do Sul (157-208):* Corte do Florescimento (Colheita e sabedoria).
5. 🟩 *Castelo Verde Central (209-260):* Corte da Matriz (Síntese e voo cósmico).

💡 *Consciência no Tempo:* Você está no dia {c['day_in_castle']:02d} desta corte de 52 dias. Observe quais temas desse castelo estão se manifestando na sua vida prática."""
    return msg

def generate_totem_lesson(target_date: datetime.date) -> str:
    k = calculate_kin(target_date)
    kd = get_kin_data(k)
    s = kd['seal']
    totem = kd['totem']
    
    msg = f"""🐆 *AULA DO TOTEM SAGRADO & ARQUÉTIPO — KIN {kd['kin']:03d}*
🏛️ *Arquétipo Hunab Ku 21:* {s['arquetipo']}
🐾 *Totem Animal Xamânico:* {totem[0]} — {totem[1]}

*✦ A MEDICINA BIOLÓGICA DO TOTEM ({totem[0]}):*
{totem[2]}

*✦ A CONSCIÊNCIA DO ARQUÉTIPO ({s['arquetipo'].upper()}):*
{s['descricao']}.

*✦ COMO VIVENCIAR ESSA FREQUÊNCIA HOJE:*
• *Na Mente & Decisões:* Invoque a sabedoria do {totem[0].split()[0]} para tomar decisões com clareza e desarmar a pressa.
• *Nas Ações Práticas:* {s['dir_trabalho']}
• *Chave de Ativação:* _"{s['chave']}"_ ✨"""
    return msg

def generate_oracle_lesson(target_date: datetime.date) -> str:
    k = calculate_kin(target_date)
    kd = get_kin_data(k)
    oracle = get_oracle(k)
    
    msg = f"""🧭 *O PAINEL DE PILOTAGEM DO ORÁCULO — KIN {kd['kin']:03d}*
*{kd['name'].upper()}*

O Oráculo de 5 Forças é a bússola multidimensional que calibra o seu campo diário:

🧭 *1. O FAROL GUIA ({oracle['guia']['name']}):*
• *Função:* A bússola nas encruzilhadas e a direção do propósito superior.
• *Diretriz de Navegação:* {clean_oracle_text(oracle['guia']['seal']['guia_msg'])}

🤝 *2. O ALIADO DE APOIO ({oracle['analogo']['name']}):*
• *Função:* O combustível invisível que recarrega a sua bateria sem esforço.
• *Diretriz de Navegação:* {clean_oracle_text(oracle['analogo']['seal']['analogo_msg'])}

⚡ *3. O MESTRE DO DESAFIO ({oracle['antipoda']['name']}):*
• *Função:* O atrito sagrado de treino que exige maturidade e foco.
• *Diretriz de Navegação:* {clean_oracle_text(oracle['antipoda']['seal']['antipoda_msg'])}

💎 *4. O TESOURO OCULTO ({oracle['oculto']['name']}):*
• *Função:* O seguro de emergência no subconsciente que salva nas crises.
• *Diretriz de Navegação:* {clean_oracle_text(oracle['oculto']['seal']['oculto_msg'])}

👑 *5. A QUINTA FORÇA ({oracle['quinta_forca']['name']}):*
• *Função:* O ponto de convergência e síntese de toda a mandala galáctica.
• *Diretriz de Navegação:* {clean_oracle_text(oracle['quinta_forca']['seal']['quinta_msg'])}

✨ Use estas 5 forças como seu mapa de navegação diária!"""
    return msg

FAMILIAS_TERRESTRES = {
    'Polar': {
        'seals': [1, 5, 10, 15],
        'chakra': 'Chakra Coronário',
        'holon': 'Polo Norte / Região Ártica',
        'funcao': 'Barra o Som e Recebe a Informação Galáctica'
    },
    'Cardeal': {
        'seals': [2, 6, 11, 16],
        'chakra': 'Chakra Laríngeo',
        'holon': 'Zona Temperada Norte',
        'funcao': 'Transmite a Voz e Expressa a Palavra'
    },
    'Central': {
        'seals': [3, 7, 12, 17],
        'chakra': 'Chakra Cardíaco',
        'holon': 'Linha do Equador',
        'funcao': 'Transmuta e Realiza a Alquimia do Coração'
    },
    'Sinal': {
        'seals': [4, 8, 13, 18],
        'chakra': 'Chakra Plexo Solar',
        'holon': 'Zona Temperada Sul',
        'funcao': 'Recebe e Revela o Mistério da Sabedoria'
    },
    'Portal': {
        'seals': [9, 14, 19, 20],
        'chakra': 'Chakra Raiz',
        'holon': 'Polo Sul / Região Antártica',
        'funcao': 'Abre os Portais do Tempo e Anima a Vida'
    }
}

CLAS_GALACTICOS = {
    'Vermelho': ('Clã do Sangue (Leste)', 'Informa a Matriz e Sustenta a Vida Biológica'),
    'Branco': ('Clã da Verdade (Norte)', 'Lembra a Verdade e Refina a Mente Superior'),
    'Azul': ('Clã do Céu (Oeste)', 'Formula a Visão e Transmuta as Águas Emocionais'),
    'Amarelo': ('Clã do Fogo (Sul)', 'Expressa o Florescimento e Amadurece a Maestria Solar')
}

CELULAS_TEMPO = {
    1: ('Célula 1 — Entrada', 'Informar a Matriz (Dragão, Vento, Noite, Semente, Serpente)'),
    2: ('Célula 2 — Armazém', 'Lembrar a Verdade (Enlaçador, Mão, Estrela, Lua, Cachorro)'),
    3: ('Célula 3 — Processo', 'Formular a Visão (Macaco, Humano, Caminhante, Mago, Águia)'),
    4: ('Célula 4 — Saída', 'Expressar o Florescimento (Guerreiro, Terra, Espelho, Tormenta, Sol)')
}

PULSAR_DETAILS = {
    1: {
        'nome': 'Pulsar do Tempo (4ª Dimensão)',
        'tons': 'Tons 1 (Magnético), 5 (Harmônico), 9 (Solar) e 13 (Cósmico)',
        'geometria': 'Tetraedro Mestre da Mente Galáctica',
        'ensino': 'É o esqueleto temporal e o eixo condutor de toda a Onda Encantada. Rege a intuição superior, o alinhamento com a Fonte, a autoridade de comando, o disparo da intenção e a transcendência cósmica. Quando ativado, convida você a operar a partir da atemporalidade e da visão expandida.'
    },
    2: {
        'nome': 'Pulsar dos Sentidos e da Vida (1ª Dimensão)',
        'tons': 'Tons 2 (Lunar), 6 (Rítmico) e 10 (Planetário)',
        'geometria': 'Triângulo da Matéria e Fisiologia Biológica',
        'ensino': 'Governa o corpo físico, a biologia, o sistema sensorial e a ancoragem no plano terrestre. Conecta o reconhecimento dos obstáculos (Tom 2), a organização do equilíbrio orgânico (Tom 6) e a produção de resultados concretos na matéria (Tom 10). Ensina que nenhuma ideia floresce sem respeito aos limites do corpo.'
    },
    3: {
        'nome': 'Pulsar da Mente e dos Sentimentos (2ª Dimensão)',
        'tons': 'Tons 3 (Elétrico), 7 (Ressonante) e 11 (Espectral)',
        'geometria': 'Triângulo do Campo Psíquico e Eletromagnetismo',
        'ensino': 'Rege as correntes psíquicas, os vínculos emocionais, a canalização intuitiva e a liberação de apegos do ego. Une a ativação do serviço desinteressado (Tom 3), a sintonização do canal com a ordem cósmica (Tom 7) e a dissolução de padrões obsoletos (Tom 11). Convida à purificação das águas internas.'
    },
    4: {
        'nome': 'Pulsar da Forma e da Mente Social (3ª Dimensão)',
        'tons': 'Tons 4 (Autoexistente), 8 (Galáctico) e 12 (Cristal)',
        'geometria': 'Triângulo da Geometria Social e Cooperação Estruturada',
        'ensino': 'Governa a arquitetura da matéria, a definição de métodos executáveis, a integridade ética e a cooperação comunitária. Articula a medição da forma prática (Tom 4), a modelagem da conduta pelo exemplo vivo (Tom 8) e a dedicação da sabedoria em rede com o todo (Tom 12). Ensina a construir no coletivo.'
    }
}

PLASMAS_DEEP = {
    'Dali': ('Chakra Coronário (Topo da Cabeça)', 'Visualização & Conexão com a Fonte', 'Meu pai é a consciência intrínseca; eu sinto o calor cósmico.'),
    'Seli': ('Chakra Raiz (Base da Coluna)', 'Aterramento & Força Biológica', 'Minha mãe é a esfera primordial; eu vejo a luz viva.'),
    'Gamma': ('Chakra 3º Olho (Entre as Sobrancelhas)', 'Pacificação Mental & Discernimento', 'Minha linhagem é a união da consciência intrínseca e da esfera primordial; eu alcanço o poder da paz.'),
    'Kali': ('Chakra Sexual / Ventre (Pélvis)', 'Catalisação & Poder Criativo', 'Meu nome é o nascido glorioso do lótus; eu cataliso a luz-calor intrínseca.'),
    'Alfa': ('Chakra Laríngeo (Garganta)', 'Liberação & Expressão da Verdade', 'Meu país é a esfera primordial que não nasceu; eu libero o elétron duplo na garganta.'),
    'Limi': ('Chakra Plexo Solar (Estômago)', 'Purificação da Vontade & Digestão Emocional', 'Eu consumo pensamentos duais como alimento; eu purifico o elétron mental no polo norte.'),
    'Silio': ('Chakra Cardíaco (Centro do Peito)', 'Amor Cósmico & Descarga no Centro da Terra', 'Meu papel é realizar as ações de iluminação; eu descarrego o elétron-nêutron térmico no coração de Gaia.')
}

PLANETAS_SEAL = {
    1: ('Netuno (Fluxo Galáctico-Kármico)', 'Circuito 1: Memória Primordial e Nutrição Cósmica'),
    2: ('Urano (Fluxo Galáctico-Kármico)', 'Circuito 2: Alento do Espírito e Comunicação Cósmica'),
    3: ('Saturno (Fluxo Galáctico-Kármico)', 'Circuito 3: Santuário do Sonho e Abundância Intuitiva'),
    4: ('Júpiter (Fluxo Galáctico-Kármico)', 'Circuito 4: Florescimento do Alvo e Consciência Germinativa'),
    5: ('Maldek / Asteroides (Fluxo Galáctico-Kármico)', 'Circuito 5: Força Vital, Fisiologia e Kundalini'),
    6: ('Marte (Fluxo Galáctico-Kármico)', 'Circuito 4: Morte Mística, Desapego e Pontes Interdimensionais'),
    7: ('Terra (Fluxo Galáctico-Kármico)', 'Circuito 3: Cura Cósmica, Realização e Conhecimento Vivo'),
    8: ('Vênus (Fluxo Galáctico-Kármico)', 'Circuito 2: Arte Cósmica, Beleza e Harmonia Estética'),
    9: ('Mercúrio (Fluxo Galáctico-Kármico)', 'Circuito 1: Água Universal, Purificação e Fluidez dos Sentimentos'),
    10: ('Mercúrio (Fluxo Solar-Profético)', 'Circuito 1: Amor Incondicional, Lealdade e Fidelidade do Coração'),
    11: ('Vênus (Fluxo Solar-Profético)', 'Circuito 2: Magia da Ilusão, Jogo Cósmico e Espontaneidade'),
    12: ('Terra (Fluxo Solar-Profético)', 'Circuito 3: Livre-Arbítrio, Responsabilidade Ética e Sabedoria'),
    13: ('Marte (Fluxo Solar-Profético)', 'Circuito 4: Exploração do Espaço, Vigilância e Profecia'),
    14: ('Maldek / Asteroides (Fluxo Solar-Profético)', 'Circuito 5: Atemporalidade, Encantamento e Presença no Agora'),
    15: ('Júpiter (Fluxo Solar-Profético)', 'Circuito 4: Visão da Mente Planetária, Criação Consciente e Metavisão'),
    16: ('Saturno (Fluxo Solar-Profético)', 'Circuito 3: Inteligência Cósmica, Questionamento Sagrado e Coragem Lúcida'),
    17: ('Urano (Fluxo Solar-Profético)', 'Circuito 2: Navegação Sincrônica, Alinhamento Terreno e Evolução'),
    18: ('Netuno (Fluxo Solar-Profético)', 'Circuito 1: Ordem Cósmica, Discernimento da Verdade e Reflexão do Infinito'),
    19: ('Plutão (Fluxo Solar-Profético)', 'Circuito Exterior: Autogeração, Catálise Quântica e Transmutação Radical'),
    20: ('Plutão (Fluxo Galáctico-Kármico)', 'Circuito Exterior: Fogo Universal, Iluminação Solar e Vida Plena')
}

def generate_daily_lesson(target_date: datetime.date) -> str:
    k = calculate_kin(target_date)
    kd = get_kin_data(k)
    oracle = get_oracle(k)
    lunar = get_13_moon_info(target_date)
    s = kd['seal']
    c = kd['castle']
    decree = build_decree(kd, oracle)
    wave_story = build_wave_narrative(kd)
    totem = kd['totem']
    s_num = kd['seal_num']
    t_num = kd['tone_num']

    # Códigos Matemáticos Exatos
    harmonica_num = ((k - 1) // 4) + 1
    cromatica_num = ((k - 1) // 5) + 1
    
    # Família Terrestre
    fam_info = None
    fam_nome = ""
    for f_k, f_v in FAMILIAS_TERRESTRES.items():
        if s_num in f_v['seals']:
            fam_nome = f_k
            fam_info = f_v
            break

    # Clã Galáctico
    cla_info = CLAS_GALACTICOS[s['cor']]

    # Célula de Tempo
    celula_id = ((s_num - 1) // 5) + 1
    celula_info = CELULAS_TEMPO[celula_id]

    # Geometria dos Pulsares
    if t_num in [1, 5, 9, 13]: pulsar_data = PULSAR_DETAILS[1]
    elif t_num in [2, 6, 10]: pulsar_data = PULSAR_DETAILS[2]
    elif t_num in [3, 7, 11]: pulsar_data = PULSAR_DETAILS[3]
    else: pulsar_data = PULSAR_DETAILS[4]

    # 1. Joia Noosférica: Banco PSI e Synchronotron 441
    day_of_year = (lunar['moon_num'] - 1) * 28 + lunar['day_of_moon']
    chrono_psi_kin = ((day_of_year - 1) % 260) + 1
    chrono_psi_data = get_kin_data(chrono_psi_kin)

    ift = k + chrono_psi_kin + lunar['day_of_moon'] + kd['tone_num']
    umb = ((ift - 1) % 441) + 1

    row = ((umb - 1) // 21) + 1
    col = ((umb - 1) % 21) + 1

    if row <= 7 and col <= 7: dim_nome = '1ª Dimensão — Tempo Exterior Primário (Criação Cósmica)'
    elif row <= 7 and col >= 15: dim_nome = '2ª Dimensão — Tempo Exterior Cósmico (Ordem Galáctica)'
    elif row >= 15 and col <= 7: dim_nome = '3ª Dimensão — Tempo Exterior Transformador (Alquimia Biológica)'
    elif row >= 15 and col >= 15: dim_nome = '4ª Dimensão — Tempo Exterior da Transcendência (Telepatia e Futuro)'
    elif 8 <= row <= 14 and col >= 15: dim_nome = '5ª Dimensão — Hipertempo Direito (Imaginação Criativa)'
    elif 8 <= row <= 14 and col <= 7: dim_nome = '6ª Dimensão — Hipertempo Esquerdo (Razão Cósmica Superior)'
    elif row <= 7 and 8 <= col <= 14: dim_nome = '7ª Dimensão — Hipertempo Superior (Transmissão Direta da Fonte)'
    elif row >= 15 and 8 <= col <= 14: dim_nome = '8ª Dimensão — Hipertempo Inferior (Ancoragem no Núcleo de Cristal)'
    else: dim_nome = '9ª Dimensão — Núcleo Cósmico Hunab Ku 21 (Centro da Matriz 441)'

    # 2. Joia Planetária
    planeta_info = PLANETAS_SEAL[s_num]

    pag_status = "🌀 *Portal de Ativação Galáctica (PAG): SIM!*" if kd['is_pag'] else "• *Portal PAG:* Não (Fluxo Estável)"
    
    special_events = []
    if kd['is_zero_point']:
        special_events.append("✨ *PONTO ZERO DO TZOLKIN:* O centro exato da matriz de 260 kins, onde todas as frequências se espelham em equilíbrio perfeito!")
    elif kd['is_mystic_column']:
        special_events.append("🌌 *COLUNA MÍSTICA (7ª Coluna Central):* O canal de ressonância direta com Hunab Ku, sem portais de ativação, onde reina o silêncio fértil e a recepção pura.")
    if kd['is_omega_portal']:
        special_events.append(f"🌀 *SEQUÊNCIA ÔMEGA DE PORTAIS:* Dia {k - 105}/10 de portais contínuos de aceleração quântica!")
    elif kd['is_alpha_portal']:
        special_events.append(f"🌀 *SEQUÊNCIA ALFA DE PORTAIS:* Dia {k - 145}/10 de portais contínuos de transmutação celular!")

    special_str = ""
    if special_events:
        special_str = "\n" + "\n".join(special_events)

    p_name = lunar['plasma'][0]
    p_deep = PLASMAS_DEEP.get(p_name, (lunar['plasma'][1], lunar['plasma'][2], ''))
    tele_info = get_telektonon_status(lunar['day_of_moon'])

    msg = f"""📚 *ESCOLA VIVA DO TZOLKIN — AULA MAGNA DEFINITIVA*
*KIN {kd['kin']:03d} — {kd['name'].upper()}*
📅 *Data Sincrônica:* {target_date.strftime('%d/%m/%Y')} | {pag_status}{special_str}

*✦ CÓDIGOS DA MATRIZ SAGRADA 13:20 & NOOSFERA*
• *Harmônica {harmonica_num:02d} de 65:* Unidade fractal de 4 dias ({s['cor']}). O Tzolkin processa a informação cósmica do impulso inicial (Vermelho) à colheita madura (Amarelo).
• *Cromática {cromatica_num:02d} de 52:* Circulação termogenética e florescimento solar que conecta os polos terrestres.
• *Célula do Tempo:* {celula_info[0]} — {celula_info[1]}. Cada quadrante rege uma fase mental: Informar, Lembrar, Formular ou Expressar.
• *Família Terrestre:* Família {fam_nome} • {fam_info['chakra']}
  _Ancoragem no Holon Planetário:_ {fam_info['holon']} — {fam_info['funcao']}.
• *Clã Galáctico:* {cla_info[0]} — {cla_info[1]}.
• *Chrono PSI (Memória da Noosfera):* Kin {chrono_psi_kin:03d} ({chrono_psi_data['name']}) — A memória ancestral ativa no cérebro da Terra.
• *Synchronotron 441:* UMB {umb:03d} nas 9 Dimensões do Tempo — {dim_nome}.

*✦ CAPÍTULO 1: O CASTELO DE 52 DIAS (A RODA MAIOR)*
• *Castelo Atual:* {c['nome']} — Dia {c['day_in_castle']:02d} de 52
• *Corte Cósmica:* {c['corte']} | *Direção:* {c['direcao']}
• *Significado Pedagógico:* O Tzolkin é dividido em 5 grandes Castelos de 52 dias (4 Ondas Encantadas por castelo).
• *A Missão do Ciclo:* {c['missao']}
• *Aplicação Prática:* O dia {c['day_in_castle']:02d} revela o estágio de maturação dos seus projetos de médio e longo prazo neste quadrante do ano cósmico.

*✦ CAPÍTULO 2: A ONDA ENCANTADA DOS 13 PASSOS*
• *Onda Regente:* Onda da {kd['wave'][1].upper()} (Kins {kd['wave'][0]:03d} a {kd['wave'][0]+12:03d})
• *A Missão da Onda:* {wave_story['arco']}
• *O Posicionamento de Hoje:* Degrau {kd['degrau']:02d} de 13 — {wave_story['degrau_texto']}
• *A Geometria do Pulsar Ativado:*
  • *{pulsar_data['nome']}:* {pulsar_data['tons']}.
  • *Geometria:* {pulsar_data['geometria']}.
  • *Ensino Iniciático:* {pulsar_data['ensino']}
• *A Dinâmica dos 4 Blocos da Onda:*
  1. *Fundação (Tons 1 a 4):* Propósito primordial, identificação de desafios, ativação do serviço e definição da forma prática.
  2. *Potência (Tons 5 a 8):* Comando de recursos, equilíbrio da rotina, sintonização do canal intuitivo e integridade ética pelo exemplo.
  3. *Materialização (Tons 9 a 12):* Disparo da intenção no mundo, aperfeiçoamento da obra manifestada, dissolução de apegos e cooperação em rede.
  4. *Transcendência (Tom 13):* Integração de todos os passos, coroamento da missão e transcendência na presença pura.

*✦ CAPÍTULO 3: O SELO SOLAR & HUNAB KU 21*
• *Selo Solar:* Selo {kd['seal_num']:02d} — {s['nome']} ({s['maia']})
• *Tríade Sagrada:* Poder de {s['poder'].lower()} • Ação de {s['acao'].lower()} • Essência de {s['essencia'].lower()}
• *Antena Planetária:* {planeta_info[0]}
  _Circuito Interplanetário:_ {planeta_info[1]}.
• *O Arquétipo em Hunab Ku 21:* {s['arquetipo'].upper()} ({s['corte']})
• *Consciência do Arquétipo:* No mapa de 21 arquétipos da Árvore da Vida Galáctica, personifica a consciência de *{s['arquetipo']}*. {s['descricao']}.
• *A Dialética de Luz & Sombra:*
  🟢 *Frequência de Luz (Superpoder):* {s['luz']}
  🔴 *Frequência de Sombra (Desvio do Ego):* {s['sombra']}
  🔑 *Chave de Maestria:* _"{s['chave']}"_

*✦ CAPÍTULO 4: O TOM GALÁCTICO & O TOTEM XAMÂNICO*
• *Tom Galáctico:* Tom {kd['tone_num']:02d} — Tom {kd['tone'][0]} ({kd['tone'][3]})
• *Função Cósmica:* {TONE_DESCRIPTIONS[kd['tone_num']]}
• *A Pergunta de Inquirição Cósmica:* _"{kd['tone'][5]}"_
• *Animal Totem Xamânico:* {totem[0]} — {totem[1]}
• *A Medicina Biológica:* {totem[2]}
• *Ancoragem no Sistema Nervoso:* Invoque a sabedoria instintiva da {totem[0].split()[0]} para regular seu tônus de ação, agir no tempo certo e desarmar a ansiedade biológica.

*✦ CAPÍTULO 5: A MANDALA DO ORÁCULO DE 5 FORÇAS*
O Oráculo é a cruz galáctica que orienta a navegação da consciência no dia a dia:
🧭 *1. Farol Guia ({oracle['guia']['name']}):*
{clean_oracle_text(oracle['guia']['seal']['guia_msg'])}
🤝 *2. Aliado de Apoio ({oracle['analogo']['name']}):*
{clean_oracle_text(oracle['analogo']['seal']['analogo_msg'])}
⚡ *3. Mestre do Desafio ({oracle['antipoda']['name']}):*
{clean_oracle_text(oracle['antipoda']['seal']['antipoda_msg'])}
💎 *4. Tesouro Oculto ({oracle['oculto']['name']}):*
{clean_oracle_text(oracle['oculto']['seal']['oculto_msg'])}
👑 *5. Quinta Força ({oracle['quinta_forca']['name']}):*
{clean_oracle_text(oracle['quinta_forca']['seal']['quinta_msg'])}

*✦ CAPÍTULO 6: SINCRONÁRIO DE 13 LUAS, PLASMAS & TELEKTONON*
• *A Lua do Ano:* {lunar['moon_name']} • Dia {lunar['day_of_moon']:02d} de 28
• *O Plasma Radial da Heptada:* {p_name} • {p_deep[0]}
  _Ativação Energética:_ {p_deep[1]}.
  _Afirmação Sagrada do Plasma:_ > _"{p_deep[2]}"_
• *Micro-Protocolo Somático do Plasma (Ciclo 4-4-4):*
  1. *Inspire (4s):* Visualizando a eletricidade do plasma {p_name} entrando pelo seu {p_deep[0].split('(')[0].strip()}.
  2. *Retenha (4s):* Entoando mentalmente a afirmação sagrada acima.
  3. *Expire (4s):* Descarregando o excesso de carga mental no centro de cristal de Gaia.
• *A Jornada do Telektonon:* {tele_info}. Rastreia o resgate das virtudes da mente no Tubo Falante da Terra.

*✦ CAPÍTULO 7: TREINO PRÁTICO 80/20 & DECRETO SAGRADO*
🎯 *Treino de Alavancagem na Matéria:*
Hoje, o seu maior retorno prático vem de *{s['dir_trabalho'].split('.')[0].lower()}*. Vigie o atrito com o desafio de *{oracle['antipoda']['name']}* e sustente a integridade das suas ações no Agora.

🧘 *Decreto Sagrado de Ativação do Kin:*
{format_quote_lines(decree)} ✨🚀"""
    return msg


# ==========================================
# 4. CÁLCULO DE TRÂNSITO ANUAL & REVOLUÇÃO GALÁCTICA
# ==========================================

def safe_replace_year(dt: datetime.date, year: int) -> datetime.date:
    try:
        return dt.replace(year=year)
    except ValueError:
        return datetime.date(year, 2, 28)

def get_annual_transit_data(birth_date: datetime.date, ref_date: datetime.date = None):
    if ref_date is None:
        ref_date = datetime.date.today()
    
    bday_this_year = safe_replace_year(birth_date, ref_date.year)
    if ref_date >= bday_this_year:
        age = ref_date.year - birth_date.year
        cur_cycle_start = bday_this_year
        next_bday = safe_replace_year(birth_date, ref_date.year + 1)
        cur_cycle_end = next_bday - datetime.timedelta(days=1)
    else:
        age = ref_date.year - birth_date.year - 1
        cur_cycle_start = safe_replace_year(birth_date, ref_date.year - 1)
        cur_cycle_end = bday_this_year - datetime.timedelta(days=1)
        next_bday = bday_this_year

    kin_annual = calculate_kin(cur_cycle_start)
    kin_next = calculate_kin(next_bday)
    days_to_next = (next_bday - ref_date).days
    days_in_cycle = (ref_date - cur_cycle_start).days

    # Ciclo de 52 Anos (Castelo da Vida)
    age_in_52 = age % 52
    cycle_num = (age // 52) + 1
    if age_in_52 < 13:
        life_castle = ('Castelo Vermelho do Leste (Corte do Nascimento)', 'Iniciação, plantio das raízes biológicas, formação da base e descoberta do ego.')
    elif age_in_52 < 26:
        life_castle = ('Castelo Branco do Norte (Corte da Morte & Refinamento)', 'Depuração, quebra de ilusões, lapidação da identidade e aprendizado pelo rigor.')
    elif age_in_52 < 39:
        life_castle = ('Castelo Azul do Oeste (Corte da Magia & Transformação)', 'Consolidação, grandes transmutações na matéria, alianças, carreira e obra no mundo.')
    else:
        life_castle = ('Castelo Amarelo do Sul (Corte do Florescimento)', 'Maturidade, colheita da sabedoria acumulada, maestria cósmica e transmissão aos outros.')

    return {
        'age': age,
        'cur_cycle_start': cur_cycle_start,
        'cur_cycle_end': cur_cycle_end,
        'next_bday': next_bday,
        'days_to_next': days_to_next,
        'days_in_cycle': days_in_cycle,
        'kin_annual': kin_annual,
        'kin_next': kin_next,
        'age_in_52': age_in_52,
        'cycle_num': cycle_num,
        'life_castle': life_castle
    }

def generate_birthday_transit_analysis(birth_date: datetime.date, name: str = "Consulente", ref_date: datetime.date = None) -> str:
    k_birth = calculate_kin(birth_date)
    kd_birth = get_kin_data(k_birth)
    
    transit = get_annual_transit_data(birth_date, ref_date)
    age = transit['age']
    cur_start = transit['cur_cycle_start']
    cur_end = transit['cur_cycle_end']
    next_bday = transit['next_bday']
    days_to_next = transit['days_to_next']
    days_in = transit['days_in_cycle']
    
    kd_ann = get_kin_data(transit['kin_annual'])
    s_ann = kd_ann['seal']
    t_ann = kd_ann['tone']
    oracle_ann = get_oracle(transit['kin_annual'])
    
    kd_next = get_kin_data(transit['kin_next'])
    s_next = kd_next['seal']
    t_next = kd_next['tone']
    
    pag_ann_tag = "🌀 *PAG (Portal Galáctico Ativo no Ano)*" if kd_ann['is_pag'] else "• *Frequência Anual:* Estável"
    
    msg = f"""🎂 *REVOLUÇÃO GALÁCTICA & TRÂNSITO DO ANO — {name.upper()}*
📅 *Nascimento:* {birth_date.strftime('%d/%m/%Y')} | 🏛️ *Kin Natal:* Kin {kd_birth['kin']:03d} ({kd_birth['name']})
⏳ *Idade Atual:* **{age} anos** (Ciclo {transit['cycle_num']} de 52 anos — ano {transit['age_in_52']}/52)
🗓️ *Vigência do Ciclo:* {cur_start.strftime('%d/%m/%Y')} ──► {cur_end.strftime('%d/%m/%Y')} ({days_in} dias vividos | {days_to_next} dias para a virada)

━━━━━━━━━━━━━━━━━━━━━

*✦ 1. O KIN REGENTE DA SUA IDADE ATUAL ({age} ANOS)*
🏛️ *KIN {kd_ann['kin']:03d} — {kd_ann['name'].upper()}*
{pag_ann_tag} | 🦉 *Totem do Ano:* {kd_ann['totem'][0]}
🏰 *{kd_ann['castle']['nome']}* | 🌊 *Onda da {kd_ann['wave'][1]}* (Degrau {kd_ann['degrau']:02d}/13)
⚡ *{kd_ann['pulsar'][0]}:* {kd_ann['pulsar'][1]}

> _"{s_ann['chave']}"_

*✦ 2. O TEMA DO ANO & O TRABALHO INTERNO*
• ☀️ *Selo Regente ({s_ann['nome']}):*
{s_ann['descricao']}. Este ano exige a postura de {s_ann['acao'].lower()} e sustentar {s_ann['essencia'].lower()}.
• ⚡ *Tom Galáctico (Tom {kd_ann['tone_num']} — {t_ann[0]}):*
{t_ann[1]} ({t_ann[2]} o {t_ann[3]}). A frequência que comanda todas as suas decisões aos {age} anos.
• 🎯 *A Síntese da Sua Idade:*
{kd_ann['alquimia_sintese']}

*✦ 3. A BÚSSOLA DO SEU ANO (ORÁCULO DO TRÂNSITO)*
🧭 *Farol Guia do Ano:* Kin {oracle_ann['guia']['kin']:03d} ({oracle_ann['guia']['name']})
🤝 *Aliado de Apoio:* Kin {oracle_ann['analogo']['kin']:03d} ({oracle_ann['analogo']['name']})
🛡️ *Desafio do Ano:* Kin {oracle_ann['antipoda']['kin']:03d} ({oracle_ann['antipoda']['name']})
💎 *Tesouro Oculto:* Kin {oracle_ann['oculto']['kin']:03d} ({oracle_ann['oculto']['name']})
👑 *Quinta Força:* Kin {oracle_ann['quinta_forca']['kin']:03d} ({oracle_ann['quinta_forca']['name']})

*✦ 4. LUZ, SOMBRA & ALERTA DO ANO*
• 🟢 *O Seu Foco de Luz aos {age} anos:*
{s_ann['luz']}
• 🔴 *A Armadilha a Vigiar (Sombra do Ciclo):*
{s_ann['sombra']}
• 💼 *Diretriz Prática de Carreira & Decisões:*
{s_ann['dir_trabalho']}
• 🧘 *Higiene & Cuidado com o Corpo:*
{s_ann['somat_higiene']}

*✦ 5. O SEU CASTELO DA VIDA (MAPA DE 52 ANOS)*
🏰 *{transit['life_castle'][0]}*
{transit['life_castle'][1]}
• *Contagem Regressiva para o Retorno Galáctico:* Aos 52 anos de vida, você completará 18.980 dias e retornará exatamente ao seu Kin de nascimento (Kin {kd_birth['kin']:03d}), renascendo como Ancião Galáctico. Faltam {52 - transit['age_in_52']} anos para essa coroação.

*✦ 6. A PRÓXIMA VIRADA ({age + 1} ANOS EM {next_bday.strftime('%d/%m/%Y')})*
🔮 *KIN {kd_next['kin']:03d} — {kd_next['name'].upper()}*
Onda da {kd_next['wave'][1]} | Tom {kd_next['tone_num']} ({t_next[0]})
Em {next_bday.strftime('%d/%m/%Y')}, sua consciência mudará de frequência para trabalhar {s_next['acao'].lower()} e {s_next['essencia'].lower()}. Fique atento aos sinais cerca de 2 semanas antes da virada! ✨🚀"""
    return msg


def generate_synastry_analysis(date1: datetime.date, name1: str, date2: datetime.date, name2: str) -> str:
    k1 = calculate_kin(date1)
    kd1 = get_kin_data(k1)
    s1, t1 = kd1['seal'], kd1['tone']

    k2 = calculate_kin(date2)
    kd2 = get_kin_data(k2)
    s2, t2 = kd2['seal'], kd2['tone']

    k_comp = ((k1 + k2 - 1) % 260) + 1
    kd_comp = get_kin_data(k_comp)
    s_comp, t_comp = kd_comp['seal'], kd_comp['tone']
    oracle_comp = get_oracle(k_comp)

    seal_sum = kd1['seal_num'] + kd2['seal_num']
    is_oculto = (seal_sum == 21)
    is_antipoda = (abs(kd1['seal_num'] - kd2['seal_num']) == 10)
    is_analogo = (seal_sum == 19 or (kd1['seal_num'] in (19, 20) and kd2['seal_num'] in (19, 20)))
    is_same_seal = (kd1['seal_num'] == kd2['seal_num'])

    pulsar1 = kd1['pulsar'][0]
    pulsar2 = kd2['pulsar'][0]
    same_pulsar = (pulsar1 == pulsar2)

    conexoes = []
    if is_oculto:
        conexoes.append("💎 *PAR OCULTO SAGRADO (Soma 21):* A conexão mais profunda da alma! Um é o tesouro secreto e inconsciente do outro.")
    elif is_antipoda:
        conexoes.append("⚡ *PAR ANTÍPODA (Desafio & Crescimento):* Força de polaridade magnética. Atrai pelo contraste e exige maturidade para não entrar em atrito.")
    elif is_analogo:
        conexoes.append("🤝 *PAR ANÁLOGO (Apoio Cósmico):* Afinidade natural, facilidade de convivência e parceria confortável.")
    elif is_same_seal:
        conexoes.append("🪞 *MESMO SELO SOLAR (Espelho Puro):* Compartilham o mesmo arquétipo e desafios kármicos.")

    if same_pulsar:
        conexoes.append(f"⚡ *MESMO PULSAR DIMENSIONAL ({pulsar1}):* Operam na mesma frequência prática de realização.")

    if not conexoes:
        conexoes.append("✨ *ALIANÇA DE COOPERAÇÃO:* Uma união livre de dependências cármicas pesadas, desenhada para construir pelo livre-arbítrio.")

    conexoes_str = "\n".join(f"• {c}" for c in conexoes)

    msg = f"""🔮 *SINASTRIA GALÁCTICA & LIVRO DA ALIANÇA*
💑 *{name1.upper()} & {name2.upper()}*

━━━━━━━━━━━━━━━━━━━━━

*✦ 1. AS ASSINATURAS INDIVIDUAIS*
• 👤 *{name1} ({date1.strftime('%d/%m/%Y')}):* Kin {kd1['kin']:03d} — {kd1['name'].upper()}
  Arquétipo: {s1['arquetipo']} | {kd1['pulsar'][0]} | Onda da {kd1['wave'][1]}
• 👤 *{name2} ({date2.strftime('%d/%m/%Y')}):* Kin {kd2['kin']:03d} — {kd2['name'].upper()}
  Arquétipo: {s2['arquetipo']} | {kd2['pulsar'][0]} | Onda da {kd2['wave'][1]}

━━━━━━━━━━━━━━━━━━━━━

*✦ 2. O KIN COMPOSTO (A EGRÉGORA DA RELAÇÃO)*
🏛️ *KIN {kd_comp['kin']:03d} — {kd_comp['name'].upper()}*
🌀 *PAG:* {'SIM' if kd_comp['is_pag'] else 'Não'} | 🦉 *Totem da Relação:* {kd_comp['totem'][0]}
🏰 *{kd_comp['castle']['nome']}* | 🌊 *Onda da {kd_comp['wave'][1]}*
⚡ *{kd_comp['pulsar'][0]}:* {kd_comp['pulsar'][1]}

> _"{s_comp['chave']}"_

• 🎯 *A Missão da Relação no Mundo:*
Quando {name1} e {name2} se unem, nasce um terceiro ser energético: o Kin {kd_comp['kin']:03d}. O propósito conjunto é manifestar {s_comp['essencia'].lower()} através de {t_comp[2].lower()} a força de {s_comp['poder'].lower()}.

━━━━━━━━━━━━━━━━━━━━━

*✦ 3. A GEOMETRIA DO ENCONTRO*
{conexoes_str}

━━━━━━━━━━━━━━━━━━━━━

*✦ 4. ALQUIMIA PRÁTICA NA MATÉRIA*
• 🟢 *Onde a Relação Floresce (Poder da União):*
{s_comp['luz']}
• 🔴 *O Ponto Cego a Vigiar (Sombra Compartilhada):*
{s_comp['sombra']}
• 💼 *Diretriz para Projetos ou Vida a Dois:*
{s_comp['dir_trabalho']}

━━━━━━━━━━━━━━━━━━━━━

*✦ 5. O DECRETO SAGRADO DA ALIANÇA*
{format_quote_lines(build_decree(kd_comp, oracle_comp))} ✨🚀"""
    return msg


# ==========================================
# 5. MAPA PESSOAL COMPLETO (PADRÃO LILLI / SIMON / COSMOS)
# ==========================================

def generate_personal_map_complete(birth_date: datetime.date, name: str = "Consulente", ref_date: datetime.date = None) -> str:
    k = calculate_kin(birth_date)
    kd = get_kin_data(k)
    oracle = get_oracle(k)
    s = kd['seal']
    wave_story = build_wave_narrative(kd)
    pag_str = "SIM 🌀 (Antena de Alta Voltagem)" if kd['is_pag'] else "Não (Frequência Estável)"

    transit = get_annual_transit_data(birth_date, ref_date)
    kd_ann = get_kin_data(transit['kin_annual'])
    s_ann = kd_ann['seal']
    kd_next = get_kin_data(transit['kin_next'])

    g_name = oracle['guia']['name']
    a_name = oracle['analogo']['name']
    d_name = oracle['antipoda']['name']
    o_name = oracle['oculto']['name']
    q_name = oracle['quinta_forca']['name']

    msg = f"""Fala {name}! ✨

Mapeei a sua *Assinatura Galáctica* e o seu *Trânsito Anual* com base na sua data de nascimento (*{birth_date.strftime('%d/%m/%Y')}*). Isso aqui funciona como um raio-x da sua energia essencial: revela como a sua mente opera, o seu maior superpoder, onde você costuma se autossabotar e exatamente o que você está trabalhando na sua idade atual.

🏛️ *SUA ASSINATURA GALÁCTICA: KIN {kd['kin']:03d} — {kd['name'].upper()}*
🌀 *Portal PAG:* {pag_str} | 🦉 *Totem:* {kd['totem'][0]}
🏛️ *Arquétipo Hunab Ku 21:* {s['arquetipo']}
📍 *Corte Cósmica:* {s['corte']} | ⚡ *{kd['pulsar'][0]}*

> _"{s['chave']}"_

*✦ 1. A ALQUIMIA DO SEU KIN: SELO + TOM*
• ☀️ *O Seu Selo Solar — {s['nome']} ({s['maia']}):*
{s['descricao']}. Expressa o dom inato de {s['acao'].lower()} e manifestar {s['essencia'].lower()}.
• ⚡ *O Seu Tom Galáctico — Tom {kd['tone_num']} ({kd['tone'][0]}):*
{TONE_DESCRIPTIONS[kd['tone_num']]}
• 🔮 *A Alquimia da Sua Identidade:*
Ao nascer sob o arquétipo do {s['nome'].split()[0]} com o Tom {kd['tone'][0]}, a sua essência foi moldada para manifestar {s['essencia'].lower()} através da postura de {kd['tone'][2].lower()}. No seu dia a dia, isso se traduz em {s['descricao'].split(',')[0].lower()} com maestria, clareza e autoridade natural.

*✦ 2. O SEU ESPELHO: LUZ & SOMBRA*
• 🟢 *O Seu Superpoder (Luz):*
{s['luz']}
• 🔴 *A Sua Armadilha a Vigiar (Sombra):*
{s['sombra']}
• 🔑 *A Sua Chave Mestra:*
_"{s['chave']}"_

*✦ 3. A SUA BÚSSOLA DE 5 FORÇAS (ORÁCULO PESSOAL)*
🧭 *Seu Farol Guia ({g_name}):* {clean_oracle_text(oracle['guia']['seal']['guia_msg'])}
🤝 *Seu Aliado de Apoio ({a_name}):* {clean_oracle_text(oracle['analogo']['seal']['analogo_msg'])}
🛡️ *Seu Mestre do Desafio ({d_name}):* {clean_oracle_text(oracle['antipoda']['seal']['antipoda_msg'])}
💎 *Seu Tesouro Oculto ({o_name}):* {clean_oracle_text(oracle['oculto']['seal']['oculto_msg'])}
👑 *Sua Quinta Força ({q_name}):* {clean_oracle_text(oracle['quinta_forca']['seal']['quinta_msg'])}

*✦ 4. O SEU ARQUÉTIPO EM HUNAB KU 21 & O TOTEM SAGRADO*
🏛️ *O Arquétipo Cósmico:* {s['arquetipo'].upper()}
• *Corte Galáctica:* {s['corte']}
• *Função no Tabuleiro Cósmico:* No mapa de 21 arquétipos de Hunab Ku 21, você personifica a inteligência viva de *{s['arquetipo']}*. A sua mente foi desenhada para expressar o poder de {s['poder'].lower()} e a ação de {s['acao'].lower()}, ancorando a verdade de {s['essencia'].lower()} no plano material.
• *O Teste de Mestria:* Superar a sombra arquetípica ({s['sombra'].split('.')[0].lower()}) e sustentar a autoridade da sua Chave de Sabedoria: _"{s['chave']}"_

🐾 *A Medicina Xamânica do Totem ({kd['totem'][0]}):*
• *Animal Guardião:* {kd['totem'][0]} — {kd['totem'][1]}
• *Sabedoria Biológica:* {kd['totem'][2]}
• *Como Empregar a Medicina:* Invoque a energia do {kd['totem'][0].split()[0]} para guiar suas decisões. O totem ensina o seu sistema nervoso a agir no tempo certo, superar atritos com inteligência instintiva e manter firmeza no propósito.

⚡ *Síntese Arquétipo + Totem:*
A fusão entre o **{s['arquetipo']}** e o **{kd['totem'][0]}** entrega a união entre visão cósmica refinada e aterramento biológico para transformar ideias sutis em realizações palpáveis no mundo real.

*✦ 5. A SUA ONDA ENCANTADA (ONDA DA {kd['wave'][1].upper()})*
• *A Missão Maior dos 13 Passos:*
{wave_story['arco']}
• *O Seu Degrau de Nascimento ({kd['degrau']} de 13):*
{wave_story['degrau_texto']}
• *A Pergunta que Guia a Sua Jornada:* _"{kd['tone'][5]}"_

*✦ 6. O TRÂNSITO DO ANO PESSOAL (A SUA REVOLUÇÃO GALÁCTICA)*
A cada aniversário, a sua consciência avança na matriz e você ativa um Kin regente para aquele ciclo de 365 dias:
• ⏳ *Idade Atual:* **{transit['age']} anos** (de {transit['cur_cycle_start'].strftime('%d/%m/%Y')} a {transit['cur_cycle_end'].strftime('%d/%m/%Y')})
• 🏛️ *Kin Regente do Ano:* **Kin {kd_ann['kin']:03d} — {kd_ann['name'].upper()}**
• 🎯 *O Que Você Está Trabalhando Agora:*
{kd_ann['alquimia_sintese']}
• 🟢 *Foco de Luz no Ano:* {s_ann['luz'].split('.')[0]}.
• 🔴 *Armadilha do Ano:* {s_ann['sombra'].split('.')[0]}.
• 🔮 *Próxima Virada ({transit['age'] + 1} anos em {transit['next_bday'].strftime('%d/%m/%Y')}):* Entrará sob a regência do **Kin {kd_next['kin']:03d} — {kd_next['name'].upper()}**.

*✦ 7. O SEU CASTELO DA VIDA (CICLO DE 52 ANOS)*
🏰 *{transit['life_castle'][0]}*
{transit['life_castle'][1]}
• Aos 52 anos ocorre o Retorno Solar Galáctico (o retorno exato ao Kin {kd['kin']:03d}). Você está no ano {transit['age_in_52']}/52 dessa jornada.

*✦ 8. DIRETRIZES PRÁTICAS PARA A SUA VIDA*
• 🎯 *Na Carreira & Projetos:*
{s['dir_trabalho']}
• 💬 *Nas Relações & Convivência:*
{s['dir_relacoes']}

*✦ 9. REFLEXÃO PESSOAL*
> _"{s['auto_investigacao']}"_

*✦ 10. O SEU DECRETO DE PODER*
{format_quote_lines(build_decree(kd, oracle))} ✨🚀

Lê com carinho e me conta o que mais tocou você! ✨🚀"""
    return msg


# ==========================================
# 6. MAPA RESUMIDO
# ==========================================

def generate_personal_map_summary(birth_date: datetime.date, name: str = "Consulente", ref_date: datetime.date = None) -> str:
    k = calculate_kin(birth_date)
    kd = get_kin_data(k)
    oracle = get_oracle(k)
    s = kd['seal']
    pag_str = "🌀 Sim" if kd['is_pag'] else "Não"
    transit = get_annual_transit_data(birth_date, ref_date)
    kd_ann = get_kin_data(transit['kin_annual'])
    
    msg = f"""✨ *RAIO-X DO KIN & IDADE — {name.upper()}* ({birth_date.strftime('%d/%m/%Y')})

🏛️ *KIN NATAL {kd['kin']:03d} — {kd['name'].upper()}*
• *Arquétipo:* {s['arquetipo']} | *PAG:* {pag_str} | *Totem:* {kd['totem'][0]}
• *Onda:* {kd['wave'][1]} (Degrau {kd['degrau']}/13) | *{kd['pulsar'][0]}*

⏳ *IDADE ATUAL ({transit['age']} ANOS):*
• *Regência Anual:* Kin {kd_ann['kin']:03d} — {kd_ann['name']}
• *Vigência:* {transit['cur_cycle_start'].strftime('%d/%m/%Y')} até {transit['cur_cycle_end'].strftime('%d/%m/%Y')}
• *Próxima Virada:* {transit['next_bday'].strftime('%d/%m/%Y')} (Kin {transit['kin_next']:03d})

🧭 *ORÁCULO NATAL:* Guia: {oracle['guia']['name']} | Apoio: {oracle['analogo']['name']} | Desafio: {oracle['antipoda']['name']} | Oculto: {oracle['oculto']['name']} | 5ª: {oracle['quinta_forca']['name']}

🟢 *LUZ:* {s['luz'].split('.')[0]}.
🔴 *SOMBRA:* {s['sombra'].split('.')[0]}.
🔑 _"{s['chave']}"_ ✨"""
    return msg


# ==========================================
# 6. DOSSIÊ DA SEMANA
# ==========================================

def generate_weekly_forecast(start_date: datetime.date) -> str:
    msg = f"""🔮 *DOSSIÊ DA SEMANA ({start_date.strftime('%d/%m')} a {(start_date + datetime.timedelta(days=6)).strftime('%d/%m/%Y')})*\n"""
    for i in range(7):
        cur = start_date + datetime.timedelta(days=i)
        k = calculate_kin(cur)
        kd = get_kin_data(k)
        s = kd['seal']
        pag_tag = "🌀" if kd['is_pag'] else ""
        day_name = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"][cur.weekday()]
        msg += f"""
📅 *{day_name} ({cur.strftime('%d/%m')}) — KIN {kd['kin']:03d}: {kd['name'].upper()}* {pag_tag}
• *{kd['stage'][0]}* | *{kd['pulsar'][0]}*
• *Luz:* {s['luz'].split('.')[0]}. | *Sombra:* {s['sombra'].split('.')[0]}.
• *Ação:* {s['dir_trabalho'].split('.')[0]}."""
    return msg


# ==========================================
# TELEGRAM API COM FALLBACK RESILIENTE & CHUNKING
# ==========================================

def split_message_blocks(text, max_len=3800):
    if len(text) <= max_len:
        return [text]
    parts = []
    current_chunk = ''
    sections = text.split('\n\n*✦ ')
    for i, sec in enumerate(sections):
        sec_content = sec if i == 0 else '*✦ ' + sec
        if len(current_chunk) + len(sec_content) + 2 <= max_len:
            current_chunk = (current_chunk + '\n\n' + sec_content).strip() if current_chunk else sec_content
        else:
            if current_chunk.strip():
                parts.append(current_chunk.strip())
            current_chunk = sec_content
    if current_chunk.strip():
        parts.append(current_chunk.strip())
    return parts

def send_telegram_single(token: str, chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}
    data = urllib.parse.urlencode(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8', errors='replace')
        print(f"[WARN] Telegram Markdown error ({e.code}): {err_msg}. Tentando fallback sem parse_mode...")
        payload_plain = {'chat_id': chat_id, 'text': text}
        data_plain = urllib.parse.urlencode(payload_plain).encode('utf-8')
        req_plain = urllib.request.Request(url, data=data_plain)
        try:
            with urllib.request.urlopen(req_plain) as resp2:
                return json.loads(resp2.read().decode('utf-8'))
        except Exception as e2:
            print(f"[ERROR] Fallback falhou também: {e2}")
            return {'ok': False, 'error': str(e2)}

def send_telegram_message(token: str, chat_id: str, text: str):
    chunks = split_message_blocks(text, max_len=3800)
    last_res = {'ok': True}
    for chunk in chunks:
        last_res = send_telegram_single(token, chat_id, chunk)
        if len(chunks) > 1:
            time.sleep(0.5)
    return last_res

