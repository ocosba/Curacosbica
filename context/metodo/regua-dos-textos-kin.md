---
tipo: padrao-editorial
tema: textos do Sincronário
decidido-em: 2026-09-03
decidido-por: Leonardo Cosba, após roast do conselho
implementado-em: scripts/tzolkin/
---

# A Régua dos Textos do Kin

Padrão editorial das leituras do Sincronário. Definido depois de rodar um conselho
adversário (especialista em Kin, iniciante, curioso em terapia multidimensional)
sobre os sete textos de referência escritos entre 2026.

O diagnóstico que originou esta régua: existiam **dois autores** no mesmo sistema.
Os textos escritos à mão (Lilli, Simon, Stephanie) tinham alma, frase-manifesto,
sombra com nome próprio e fechamento que abre conversa. Os textos gerados por
template (Kin do dia, Fabio) tinham concordância quebrada, frases costuradas
visíveis e fechamento que vende produto. A régua existe para que só reste um autor.

---

## Regra zero: se o título já explica, não explique de novo

Adicionada em 03/09/2026, na segunda rodada de revisão. A primeira versão da
régua produziu um texto que virou **aula sobre o sistema** em vez de leitura
sobre a pessoa. Foram cortados dali:

- "a atualização de 2010 do sistema, em que cada Selo encarna uma figura..."
- "O Tom é o ritmo. São 13, e o seu diz como você opera."
- "Os 20 Selos se agrupam de 5 em 5 nas Famílias Terrestres..."
- a lista dos 13 degraus com nome e Kin, longa e sem conteúdo

O termo entra como **aposto curto dentro da própria frase**, e a pessoa entende
pelo contexto. Quem quiser a teoria vai atrás por conta — não é função da
leitura ensinar o sistema.

**Corolário:** moldura curta, conteúdo longo. Se a explicação da seção é maior
que o que ela diz sobre a pessoa, está invertido.

**Tamanho alvo:** Kin do dia até 2.800 caracteres; mapa pessoal até 7.500.
Formatação enxuta para WhatsApp: poucas divisórias, sem saltos duplos de linha.

---

## A gramática de dois níveis (versão 1.0, 03/09/2026)

A decisão que fecha a régua. Todo termo do sistema aparece em **duas linhas**:

```
🛡️ *O Mestre de Atrito* — Semente Cristal Amarela
_A Semente é o potencial puro, a promessa do que ainda pode florescer._   ← o arquétipo, igual para todos
Gente que atropela processo vai te tirar do eixo. O treino é sustentar     ← você
o seu tempo sem se justificar.
```

**Itálico = o arquétipo. Texto normal = a pessoa.** Sempre nessa ordem.

Resolve três coisas de uma vez: a leitura para de soar como palpite sobre a
vida de um desconhecido; quem acompanha aprende o alfabeto dos 20 selos lendo
o próprio mapa; e o especialista reconhece o cânone na primeira linha.

Vale no selo, no tom, nas 5 forças e na onda. As 20 frases de arquétipo moram
em `ONDA_NARRATIVA` (`textos_oraculo.py`) e são as mesmas em toda leitura —
repetição aqui é vocabulário, não preguiça.

**Um selo só é apresentado uma vez por bússola.** Se a Quinta Força repete um
selo que já apareceu, entra direto na leitura.

---

## O que voltou do texto de 2025

O texto de referência gerado pela IA anterior errava o português em série
("Semente Galáctico Amarela", "Modelar o Integridade", "o dom inato de refina"),
mas acertava quatro coisas que a reformulação tinha perdido:

1. **A alquimia Selo + Tom.** Descrever os dois e nunca dizer o que a
   *combinação* produz deixa a leitura pela metade. Agora fecha com
   "é esse cruzamento que faz o seu Kin ser o 194 e não outro".
2. **O PAG marcado mesmo quando é não.** Ausência também é informação, e é
   boa notícia: *frequência estável*.
3. **O contador do castelo:** "você está no ano 22 de 52 dessa volta".
4. **A virada do ano galáctico** — acrescentada agora, não estava lá: nos 30
   dias antes do aniversário a leitura avisa que o ciclo está fechando. É a
   informação mais acionável do texto inteiro, e ninguém sabe dela.

**Fora, e por quê:** pulsar, célula do tempo e harmônica (não viram leitura
sobre a pessoa) e o decreto mecânico, que a frase-manifesto em 1ª pessoa
substitui com folga.

---

## Formatação: o destino é o WhatsApp, não o Telegram

O bot manda **texto cru, sem `parse_mode`**. Se o Telegram renderizar o
Markdown, o texto copiado chega no WhatsApp sem asterisco nenhum e sem
negrito. Mandando cru, o que se vê no Telegram é exatamente o que o WhatsApp
vai renderizar.

Só continua formatado o que se lê dentro do próprio Telegram: `/ajuda`, avisos
do bot e a aula do `/estudo`.

**O mapa sai em duas peças**, e a quebra é editorial, não de tamanho:
peça 1 = *quem você é*, peça 2 = *a sua rota*. O limite de 4.096 caracteres do
Telegram pode dividir a peça 2 em duas mensagens — no WhatsApp não existe esse
limite, então as partes podem ser coladas juntas.

---

## As 6 regras inegociáveis

1. **Nenhum termo aparece sozinho.**
   Formato fixo: `TERMO (o que é, em ≤10 palavras) → o que significa pra você`.
   O objetivo não é remover o jargão — é ensinar o jargão. Iniciante entende,
   especialista respeita.

2. **Todo termo tem que virar leitura sobre a pessoa.**
   Se não vira, corta. Foi assim que Pulsar, Célula do Tempo, Harmônica e Castelo
   saíram do texto público e foram para a aula.

3. **A armadilha sempre ganha nome próprio.**
   "O Complexo de Salvador", "O Apego ao que Já Acabou", "A Guerra Mental".
   O conselho foi unânime: é o nome que faz a pessoa se reconhecer, não o Kin.

4. **A frase-manifesto em 1ª pessoa substitui o decreto mecânico** no texto público.
   O decreto tradicional ("Selo a saída do inteligência") fica na aula do Leo.

5. **O corpo é sempre órgão e sintoma nomeado.**
   "Pigarro constante e nó na garganta" funciona. "Desequilíbrio energético" não.
   É o gancho de conversão mais forte que existe no texto.

6. **Fecha abrindo conversa, nunca vendendo.**
   `me conta o que mais ressoou` supera `chama no direct` com folga.
   E toda leitura pessoal termina na fronteira honesta: o mapa é a superfície,
   a leitura de verdade vem da conversa.

---

## Convenções fixadas

- **Famílias Terrestres: cânone Argüelles** (agrupamento de 5 em 5).
  Decisão de 03/09/2026, caminho A. Ver `tzolkin-fonte-da-verdade.md`.
  Consequência aceita: os textos entregues antes dessa data (Lilli, Stephanie,
  Simon) usam a convenção anterior e apontam outro centro do corpo.
- **Concordância conferida por código.** O nome do Kin flexiona o tom conforme o
  gênero do selo (Estrela Galáctica, não Galáctico) e a onda leva artigo correto
  (Onda da Semente, não do Semente). Testado nos 260 kins.
- **Formatação WhatsApp-safe:** `*negrito*` e `_itálico_` simples, que funcionam
  igual no Telegram e no WhatsApp. Sem link markdown, sem tabela.

---

## ESTRUTURA A — Kin do dia (peça de grupo)

```
Cabeçalho: data, Kin, nome do Kin
A frase do dia (uma linha, linguagem de gente)
Marcos, se houver: PAG, Coluna Mística, Ponto Zero

1. A energia de hoje ......... Selo + Tom + Arquétipo, cada um traduzido
2. Luz e sombra .............. a armadilha com nome próprio
3. A bússola do dia .......... 4 forças + a síntese, com nomes memoráveis
4. Onde estamos na onda ...... degrau nomeado + a fase do ciclo
5. O corpo hoje .............. família → centro → 3 sintomas + higiene
6. A ação de hoje ............ UMA coisa
7. A pergunta ................ uma linha

Assinatura + convite de conversa
```
**Fora:** castelo, decreto mecânico, pulsar, célula, harmônica.
**Tamanho alvo:** até 3.800 caracteres (um bloco de Telegram).

---

## ESTRUTURA B — Mapa pessoal (peça de captação)

Baseada no texto da Lilli, o melhor da série.

```
Abertura: "Fala [Nome]!" + a promessa em uma frase
Cartão de identidade: Kin, Clã, Totem, Arquétipo Hunab Ku, marcos
A FRASE-MANIFESTO em 1ª pessoa            ← o momento de arrepio

1. O seu arquétipo cósmico ... + "o que isso significa na prática"
2. O seu DNA de ação ......... superpoder → armadilha (com nome) → chave de ouro
3. O seu ritmo ............... tom + a pergunta que guia + totem
4. A sua bússola de 5 forças . nomes memoráveis + PAGs contados no oráculo
5. O enredo da sua vida ...... a onda como NARRATIVA (o que representa + a
                               tensão dela) + "o seu papel nessa história".
                               Nunca listar os 13 degraus: fica longo e vazio.
6. O seu momento atual ....... ⬅ ESTRUTURA C inteira
7. O corpo e o ponto de alerta  órgão + 3 sintomas + higiene
8. Três diretrizes ........... carreira · relações · autocuidado
9. A pergunta que você carrega + o dia de hoje para ela

A fronteira honesta
Fechamento que abre conversa
```

---

## ESTRUTURA C — O ciclo anual

O item 1 não existia em nenhum texto de referência e é o mais forte de todos.

```
1. A RELAÇÃO COM O KIN NATAL
   "Ano de Desafio", "Ano do seu próprio Arquétipo", "Ano de Apoio"...
   → a frase mais útil que existe sobre um ano de vida

2. O ANO CORRENTE — idade, Kin, datas exatas de vigência
   o que trabalha · a luz · a armadilha nomeada · a diretriz

3. O QUE VEM DEPOIS — os 2 anos seguintes, com data
   + por que emenda: o tom avança exatamente 1 por ano

4. A REGRA QUE EXPLICA TUDO
   tom +1 e selo +5 por ano → o selo volta a cada 4 anos,
   e em 52 anos os dois fecham juntos no Kin de nascimento

5. O CASTELO DE VIDA — o quadrante de 13 anos

6. O RETORNO GALÁCTICO — data exata, como clímax
```

**A leitura da relação, por posição:** Desafio é a mais valiosa (ano de treino
com o próprio ponto cego); Guia é o melhor ano para decidir; Análogo é ano de
menos atrito; Mesmo Selo é degrau de amadurecimento do mesmo tema; Destino é o
Retorno Galáctico.

---

## Onde cada coisa mora no código

| Camada | Arquivo |
|---|---|
| Matemática e tabelas | `scripts/tzolkin/core.py` |
| Manifesto, superpoder, armadilha, chave, corpo, diretrizes | `scripts/tzolkin/textos_mapa.py` |
| As 4 forças com peso e a narrativa das ondas | `scripts/tzolkin/textos_oraculo.py` |
| Frase do dia, glossário, degraus, tons | `scripts/tzolkin/textos.py` |
| A alquimia Selo + Tom (`TOM_MODO`) | `scripts/tzolkin/textos_mapa.py` |
| Material profundo (só a aula) | `scripts/tzolkin/textos_profundos.py` |
| O ciclo anual | `scripts/tzolkin/ano.py` |
| Montagem das 3 leituras | `scripts/tzolkin/mensagens.py` |

Para ajustar **texto**, abra `textos_mapa.py` ou `textos.py`.
Para ajustar **estrutura**, abra `mensagens.py`.
Nunca reescreva tabela do `core.py` em outro lugar.
