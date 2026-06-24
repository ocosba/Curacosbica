# Spec de interações & comportamento — Cura Arcturiana

> Tudo que vive no JS e descrição/screenshot não transmite. Valores exatos do código-fonte.
> **Nota:** o sistema de constelações foi deixado de fora propositalmente — não replicar.

---

## 1. Canvas de partículas (starfield de fundo)

`<canvas>` fixo, `position:fixed; inset:0; z-index:0; pointer-events:none` (atrás de todo o conteúdo, que fica em `z-index:1`).

### Setup
- `dpr = min(devicePixelRatio, 2)`; canvas redimensionado para `innerWidth/Height × dpr`; `ctx.setTransform(dpr,0,0,dpr,0,0)`.
- Recalcula no `resize`.

### Estrelas
- **Quantidade:** `210`; em telas `< 700px` → `× 0.6` (≈126).
- Cada estrela:
  - `nx, ny`: posição normalizada (0–1) × W/H
  - `r`: raio `random()*1.5 + 0.4` (0.4–1.9px)
  - `depth`: `random()*0.06 + 0.01` (parallax com scroll)
  - `col`: cor sorteada da paleta (abaixo)
  - `baseA`: alpha base `random()*0.5 + 0.4`
  - `tw`: velocidade de cintilação `random()*1.6 + 0.4`
  - `ph`: fase inicial `random()*2π`
  - `big`: `random() < 0.12` → ganha glow (shadowBlur 8)

### Paleta de cores das estrelas (peso = probabilidade)
| Cor | RGB | Peso |
|---|---|---|
| Branco | 255,255,255 | 0.60 |
| Dourado `#E3BE45` | 227,190,69 | 0.18 |
| Brilho `#cfc6f3` | 207,198,243 | 0.12 |
| Orquídea `#B06CB0` | 176,108,176 | 0.10 |

### Animação por frame
- `clearRect` a cada frame; `dt` limitado a `0.05`.
- **Parallax:** `y = (ny*H − scrollY*depth) % (H+40)` (estrelas sobem devagar ao rolar).
- **Cintilação:** `alpha = baseA * (0.55 + 0.45*sin(t*tw + ph))`.
- Estrelas `big` recebem `shadowBlur=8` com `shadowColor` da própria cor a 0.9.

### Estrela cadente (shooting star)
- Timer inicial: `3 + random()*5` s. Após disparar, próximo: `6 + random()*8` s.
- Surge em `x: random()*W*0.7`, `y: random()*H*0.4`.
- `len: 140 + random()*120`; `vx: 320 + random()*180`; `vy: 120 + random()*90` (px/s).
- Rastro: `linearGradient` de `rgba(255,255,255, 0.85*fade)` → transparente; `lineWidth 1.6`.
- `fade = max(0, 1 − life/1.1)`; some quando sai da tela ou `fade<=0`.

### Loop
- `requestAnimationFrame`; para no `componentWillUnmount` (`_mounted=false`).

---

## 2. Carrossel de transformações (arrastável)

- 3 slides; track com `transform: translateX(-card*100%)`.
- **Drag por ponteiro** (`onPointerDown/Move/Up/Leave/Cancel`) — funciona com toque E mouse.
- Durante o arraste: `transform: translateX(calc(-card*100% + dx px)); transition:none` (segue o dedo).
- Ao soltar: snap. **Threshold** = `min(largura*0.2, 80px)`. Passou → vai pro próximo/anterior; senão volta.
- Transição de snap: `transform .6s cubic-bezier(.22,.61,.36,1)`.
- `touch-action:pan-y` (permite scroll vertical), `cursor:grab`, `user-select:none`.
- Dots clicáveis: ativo vira pílula `width:30px` (vs `9px`), `transition: width .4s, background .4s`.
- Setas prev/next escondidas no mobile; aparece dica “← arraste para deslizar →”.

---

## 3. Reveal on scroll

- Alvos: `[data-reveal]` com estado inicial `opacity:0; transform:translateY(28px)`.
- Transição: `opacity 1s ease, transform 1s ease`.
- `IntersectionObserver`, `threshold: 0.1`, `rootMargin: '0px 0px -6% 0px'`. Ao entrar → `opacity:1; transform:none`, depois `unobserve`.
- `data-reveal-delay` (ms) opcional via `setTimeout` para escalonar.
- **Fallbacks:** sem IntersectionObserver → revela tudo; e um `setTimeout(4000ms)` força revelar qualquer elemento ainda em `opacity:0` (à prova de falha).

---

## 4. Hover states

- Links de nav: `color var(--c-dim)` → `var(--c-gold-soft)`, `transition: color .3s`.
- CTA primário: `translateY(-3px)` + box-shadow glow mais forte (`58%` vs `42%`), `transition: transform .3s, box-shadow .3s`.
- CTA secundário/ghost: `border-color` → `var(--c-gold)`.
- Cards de pilar/camada: leve `translateY` + borda mais brilhante.

---

## 5. Responsividade

- Breakpoint único: **`max-width: 760px`**.
- No mobile: links de nav escondidos (`[data-navlinks]`), CTA da nav compacto, hero com padding vertical reduzido, ambient gradient simplificado, partículas reduzidas (≈126).
- Tamanhos fluidos com `clamp()` em toda parte (ex.: H1 `clamp(36px,6vw,68px)`).

---

## 6. Easing & durações de referência

| Uso | Valor |
|---|---|
| Snap do carrossel | `.6s cubic-bezier(.22,.61,.36,1)` |
| Reveal on scroll | `1s ease` |
| Hover de cor | `.3s` |
| Hover de botão (lift) | `.3s` |
| Dots do carrossel | `.4s ease` |
| Shimmer do texto hero | `9s linear infinite` |
| Mandala — rotações | 60s–160s `linear infinite` (ver símbolos) |
| Mandala — pulso de anel | 3.5s–5s `ease-in-out infinite` |
| Mandala — flutuação | `arcFloat 6s ease-in-out infinite` |
