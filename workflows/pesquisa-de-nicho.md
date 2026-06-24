# Fluxo: Pesquisa de Nicho (Encontro 2 da trilha)

Este fluxo conduz a pesquisa de mercado do nicho da pessoa, usando o TubeLab para achar os outliers e o Gemini para analisar em profundidade. Ele é a segunda etapa da trilha Coerência Exponencial.

Para a pessoa, isto é uma jornada só. Por baixo, o sistema processa em partes e salva cada resultado em arquivo, para ser eficiente, não estourar contexto e nunca perder o trabalho já feito se algo travar no meio.

## Ferramentas necessárias
TubeLab, conectado na pasta conexoes, para buscar os vídeos outliers do nicho.
Gemini, conectado na pasta conexoes, com a chave no .env, para transcrever e analisar os vídeos. O Gemini faz o trabalho pesado porque aguenta muito conteúdo e é mais econômico para volume.

Se alguma das duas não estiver conectada, pare e ajude a pessoa a conectar antes de começar.

## Divisão de trabalho
TubeLab acha os outliers. Você (Claude) orquestra, filtra os canais e cria os entregáveis finais com discernimento. Gemini transcreve e analisa os 25 vídeos. Cada um no que é melhor.

## Onde salvar
Todos os resultados vão para a pasta context/mercado. Os dados brutos e análises por vídeo ficam em context/mercado/dados. Os três entregáveis finais ficam direto em context/mercado. Crie essas pastas se não existirem.

## Onde a pessoa participa
A pessoa participa em dois momentos só, para não pesar: ao confirmar os 5 canais, e ao final da seleção, quando você pergunta se ela quer acrescentar um canal específico de alguém que ela admira, que pode ser de qualquer idioma, não só português. No resto, você conduz.

## Salvaguarda de custo
A análise dos 25 vídeos usa a API do Gemini, que consome créditos pagos da pessoa. Antes de iniciar a fase pesada de transcrição e análise, avise quantos vídeos serão processados e confirme com a pessoa que pode seguir. Se algo der erro e precisar repetir, confirme de novo antes de refazer.

---

## Fase 1: Buscar os outliers (TubeLab)
Confirme com a pessoa o nicho a investigar, partindo da tese e do modo dela que já estão no CLAUDE.md. Se estiver vago, ajude a estreitar antes.
Use o TubeLab para buscar os vídeos outliers do nicho, ou seja, os que performaram muito acima da média. Reúna uma lista ampla de canais que aparecem nesses outliers.

## Fase 2: Filtrar canais humanos e descartar IA faceless
Hoje todo nicho está cheio de canais faceless feitos por IA, e eles não servem de referência, porque o trabalho aqui é aprender com criadores humanos reais.
Analise os canais da lista e separe os que parecem humanos dos que parecem automatizados por IA. Sinais de canal faceless de IA: ausência de rosto ou presença pessoal, voz que parece sintética, ritmo de publicação muito alto e mecânico, conteúdo agregado e genérico, sem marca pessoal clara. Sinais de canal humano: uma pessoa identificável, presença e voz próprias, marca pessoal, conexão real com a audiência.
Monte uma lista dos canais que você identificou como humanos, dizendo em uma linha por que classificou cada um assim. Essa classificação não é exata, então ela serve para a pessoa decidir com você.

## Fase 3: Selecionar os 5 canais (com a pessoa)
Apresente para a pessoa os principais canais humanos que você encontrou e proponha os 5 mais relevantes para o nicho dela. Explique brevemente por que cada um.
Peça para ela confirmar os 5, trocar algum se quiser.
Depois de confirmar os 5, pergunte se ela quer acrescentar um canal específico de alguém que ela admira, de qualquer idioma. Se sim, inclua esse canal na análise como referência especial.
Salve a lista final de canais em context/mercado/dados/canais.md.

## Fase 4: Extrair as transcrições (Gemini, salvando uma a uma)
Para cada canal selecionado, identifique os 5 vídeos outliers dele. São 5 vídeos por canal, 25 no total (mais o canal admirado, se houver).
Antes de começar, faça a salvaguarda de custo descrita acima.
Use o Gemini para extrair a transcrição de cada vídeo. Salve cada transcrição em um arquivo próprio dentro de context/mercado/dados, identificando canal e vídeo. Vá salvando uma a uma, para não acumular tudo no contexto e não perder nada se travar.

## Fase 5: Analisar cada vídeo (Gemini, canal por canal)
Para cada vídeo, use o Gemini para analisar três coisas:
A fórmula do título: que estrutura e gatilhos o título usa.
A fórmula da capa: analise a imagem da thumbnail do vídeo, cores, elementos, texto, expressão, o que faz ela chamar atenção. Isso usa a capacidade visual do Gemini, não só a transcrição.
O arco narrativo do vídeo: quais elementos narrativos tem, como abre, como prende, como entrega, e a sua leitura do que fez aquele vídeo funcionar.
Salve a análise de cada vídeo em arquivo dentro de context/mercado/dados. Trabalhe canal por canal, terminando um antes de ir ao próximo, para manter o contexto leve.

## Fase 6: Sintetizar o guia de mercado (Gemini)
Com as 25 análises salvas, use o Gemini para ler os arquivos de análise, não as transcrições brutas, e sintetizar um documento único: o guia de pesquisa e análise do mercado daquele nicho.
Esse guia reúne os padrões que se repetem: as fórmulas de título que mais funcionam, os padrões de capa vencedores, e os elementos de arco narrativo recorrentes nos outliers do nicho.
Salve como context/mercado/guia-de-mercado.md.

## Fase 7: Criar o playbook de YouTube da pessoa
Crie um playbook para a pessoa entrar no YouTube já usando o que é validado, mas com a voz dela.
Use as fórmulas de título e capa que funcionaram no nicho como base de forma, porque forma validada reduz risco.
Mas o conteúdo, a linha narrativa e o ponto de vista são dela, a partir do ouro dela. Onde fizer sentido, o playbook deve até discordar dos outros canais, trazendo a posição única dela. Validado na forma, autoral na essência.
Salve como context/mercado/playbook-youtube.md.

## Fase 8: Análise cruzada (ouro da pessoa vezes mercado)
Leia o ouro bruto da pessoa em context/ouro-bruto.md e cruze com o guia de mercado.
Procure os insights valiosos que aparecem na interseção: onde a história e o modo dela encontram uma lacuna ou uma demanda do nicho, onde o que ela viveu responde a uma dor recorrente do mercado, onde a voz dela pode ocupar um espaço que os outros não ocupam.
Salve como context/mercado/analise-cruzada.md.

## Entregáveis finais
Três arquivos em context/mercado: o guia de mercado, o playbook de YouTube e a análise cruzada. Ao terminar, apresente os três para a pessoa em linguagem simples, destacando os achados mais importantes de cada um.

## Princípio de decisão
Ao recomendar caminhos, lembre do princípio do CLAUDE.md: primeiro aponte a maior alavancagem, a oportunidade que mais moveria o canal dela agora, e só depois o jeito mais leve de ocupar esse espaço.

## Aprendizados
Conforme usar este fluxo, registre aqui embaixo o que aprender: limites das ferramentas, jeitos melhores de filtrar canais de IA, formatos de prompt que funcionaram melhor no Gemini, para o fluxo ir ficando mais afiado.
