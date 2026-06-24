# Design system — tokens, tipografia, animações, componentes

> Referência técnica autocontida. Valores exatos do projeto.

## Tokens CSS
```css
:root {
  --c-bg0: #0b0826;   /* fundo profundo */
  --c-bg1: #15104a;   /* fundo secundário */
  --c-bg2: #241a6e;   /* cards / elevados */
  --c-gold: #E3BE45;  /* acento principal */
  --c-gold-soft: #f2dd93;
  --c-violet: #C3B8EC;
  --c-violet-deep: #4a2f7e;
  --c-orchid: #B06CB0;
  --c-glow: #cfc6f3;
  --c-text: #ECE9FA;  /* texto primário */
  --c-dim: #ABA1CE;   /* texto secundário */
  --c-line: rgba(227,190,69,.20); /* bordas */
}
```

## Fundo multi-camada
```css
background:
  radial-gradient(ellipse 85% 50% at 50% -6%, var(--c-bg2), transparent 56%),
  radial-gradient(ellipse 60% 42% at 86% 100%, color-mix(in oklab,var(--c-orchid) 30%,transparent), transparent 56%),
  radial-gradient(ellipse 55% 42% at 8% 58%, color-mix(in oklab,var(--c-violet-deep) 42%,transparent), transparent 55%),
  var(--c-bg0);
```

## Fontes (Google Fonts)
```css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&family=Spectral:ital,wght@0,300;0,400;0,500;1,400&family=Chakra+Petch:wght@400;600;700&display=swap');
```
| Papel | Fonte | Spec |
|---|---|---|
| H1 hero | Poppins 600 | `clamp(36px,6vw,68px)` · lh 1.06 · ls −.01em |
| H2 seção | Poppins 600 | `clamp(28px,4.4vw,48px)` · lh 1.12 |
| H3 | Poppins 600 | `clamp(18px,2.4vw,24px)` |
| Corpo | Poppins 300 | `clamp(16px,1.6vw,19px)` · lh 1.82 · `--c-dim` |
| Eyebrow | Chakra Petch 600 | 12.5px · ls .28em · UPPERCASE · `--c-gold` |
| Rótulo/número | Chakra Petch 400–700 | 12–15px |
| Contemplativo/citação | Spectral 300 / italic | 15–18px · lh 1.8 |

## Animações
```css
@keyframes arcPulse  { 0%,100%{transform:scale(1);opacity:.45} 50%{transform:scale(1.12);opacity:.8} }
@keyframes arcFloat  { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-14px)} }
@keyframes arcSpin   { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }
@keyframes arcSpinR  { from{transform:rotate(0deg)} to{transform:rotate(-360deg)} }
@keyframes arcShimmer{ 0%{background-position:0% 50%} 100%{background-position:200% 50%} }
```
Texto gradiente do hero:
```css
background: linear-gradient(110deg, #E3BE45, #f2dd93, #B06CB0, #E3BE45);
background-size: 220% auto;
-webkit-background-clip: text; background-clip: text; color: transparent;
animation: arcShimmer 9s linear infinite;
```

## Padrões de componente
**Card**
```css
border-radius: 18px;
border: 1px solid var(--c-line);
background: linear-gradient(160deg,
  color-mix(in oklab, var(--c-bg2) 44%, transparent),
  color-mix(in oklab, var(--c-bg1) 38%, transparent));
backdrop-filter: blur(8px);
padding: 26px 22px;
```
**CTA primário**
```css
background: linear-gradient(135deg, var(--c-gold), var(--c-gold-soft));
color: #0b0826; border-radius: 999px; font-weight: 600; padding: 18px 34px; border: none;
box-shadow: 0 0 46px color-mix(in oklab, var(--c-gold) 42%, transparent);
transition: transform .3s, box-shadow .3s;
/* hover: translateY(-3px); shadow 64px @58% */
```
**CTA ghost**
```css
background: none; border: 1px solid rgba(227,190,69,.30); border-radius: 999px;
color: var(--c-text); padding: 17px 26px; /* hover: border-color var(--c-gold) */
```
**NAV glass**
```css
position: sticky; top: 0; z-index: 20; backdrop-filter: blur(14px);
background: linear-gradient(to bottom,
  color-mix(in oklab,#0b0826 92%,transparent),
  color-mix(in oklab,#0b0826 60%,transparent));
border-bottom: 1px solid rgba(227,190,69,.08);
```
**Eyebrow** (rótulo de seção)
```css
display:inline-flex; align-items:center; gap:12px;
font-family:'Chakra Petch'; font-size:12.5px; letter-spacing:.28em;
text-transform:uppercase; color:var(--c-gold); font-weight:600;
/* ::before e ::after: width:26px; height:1px; background:var(--c-gold); opacity:.6 */
```

## Seção padrão
```css
section { position:relative; z-index:1; padding: clamp(60px,8vw,100px) clamp(20px,5vw,56px); }
```

## Ordem das seções
NAV · HERO · Sobre · O que é · 4 Pilares · Carrossel (3) · Camadas (8) · Quiz-filtro (4) · Como funciona (3 tempos + 5 passos) · Terapeuta · Depoimentos (2) · FAQ (9) · CTA final · Footer.
