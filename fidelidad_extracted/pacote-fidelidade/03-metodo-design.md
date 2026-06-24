# Método de design — como replicar o padrão em qualquer projeto

> Este documento ensina o **jeito de construir**, não só este projeto. Use como regras gerais ao recriar designs deste autor no Antigravity.

---

## Princípio nº 1 — Comprometa-se com uma direção estética forte
Nada de "design seguro". Cada projeto tem **um clima** (aqui: místico-cósmico, escuro, dourado sobre índigo). Escolha o clima primeiro e leve até o fim — fundo, tipografia, cor, movimento e copy reforçam o MESMO sentimento.

## Princípio nº 2 — Tokens primeiro, sempre
Defina um conjunto pequeno de CSS custom properties (`--c-*`) e use SÓ eles. Nunca cores soltas no meio do código. Para tons intermediários, use `color-mix(in oklab, var(--c-x) N%, transparent)` em vez de inventar hex novos.

## Princípio nº 3 — Três famílias tipográficas, papéis fixos
- **Display/UI** (aqui Poppins) — títulos e botões.
- **Corpo contemplativo** (aqui Spectral, serifada) — textos longos e citações.
- **Técnica/mono** (aqui Chakra Petch) — eyebrows, números, rótulos.
Cada papel sempre na mesma família. Pesos: títulos 600, corpo 300, eyebrows 600.

## Princípio nº 4 — Escala fluida com `clamp()`
Todo tamanho relevante usa `clamp(min, vw, max)`. Nada de breakpoints múltiplos para tipografia — um único `@media (max-width:760px)` para ajustes estruturais (esconder nav, reduzir densidade).

## Princípio nº 5 — Profundidade por camadas, não por sombra pesada
- Fundo = múltiplos `radial-gradient` empilhados + cor base.
- Canvas de partículas atrás de tudo (`z-index:0`), conteúdo em `z-index:1`.
- Vidro fosco (`backdrop-filter: blur`) na nav e em cards.
- Glow via `box-shadow` colorido de baixa opacidade, não sombra preta.

## Princípio nº 6 — Movimento com propósito, sutil
- `@keyframes` lentos (shimmer 9s, rotações 60–160s). Nada de animação rápida ou chamativa.
- Reveal on scroll com `IntersectionObserver` (opacity + translateY), sempre com fallback que garante o conteúdo visível.
- Interações por toque pensadas para mobile (drag real, não só botões).

## Princípio nº 7 — Símbolos próprios, desenhados em código
Ícones e ornamentos são **SVG geométrico desenhado programaticamente** (círculos, polígonos, paths), não biblioteca de ícones genérica nem emoji. Isso dá identidade. Reaproveite a paleta de stroke nos ícones.

## Princípio nº 8 — Densidade baixa, hierarquia clara
Muito respiro. `padding` de seção generoso: `clamp(60px,8vw,100px)`. Eyebrow → Título → Corpo → CTA, nessa ordem, repetidos como ritmo. Largura de leitura limitada (`max-width: ~60ch`).

## Princípio nº 9 — Eyebrow como assinatura de seção
Rótulo em maiúsculas, `letter-spacing` largo (`.28em`), na cor de acento, com **linhas curtas dos dois lados** (`::before`/`::after`, 26px×1px). É o elemento que costura todas as seções.

## Princípio nº 10 — Copy é parte do design
O texto carrega a tese. Aqui: auto-responsabilidade ativa, mentor firme. Verbos de ação, frases que filtram o público. Nunca placeholder/lorem — se faltar conteúdo, é problema de design, não de preencher espaço.

---

## Checklist de fidelidade (rode ao recriar)
- [ ] Tokens `--c-*` definidos e usados em tudo
- [ ] 3 famílias de fonte nos papéis certos (Google Fonts)
- [ ] Fundo multi-camada + canvas de partículas
- [ ] Eyebrow com linhas laterais em cada seção
- [ ] Tamanhos em `clamp()`; único breakpoint 760px
- [ ] Cards com vidro fosco + borda dourada sutil
- [ ] CTA primário gradiente ouro + glow; ghost com border
- [ ] Ícones SVG geométricos (usar os 21 SVGs entregues)
- [ ] Reveal on scroll com fallback
- [ ] Carrossel arrastável (drag por ponteiro)
- [ ] Copy verbatim do arquivo `01-copy-verbatim.md` (não parafrasear)
- [ ] Sem emojis, sem gradientes berrantes, sem cantos arredondados com borda-accent à esquerda
