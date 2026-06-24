# Dados concretos — contato, SEO & metadados

> Valores reais para não inventar placeholders.

---

## Contato
- **WhatsApp:** (11) 93391-5702 → link: `https://wa.me/5511933915702`
- **Mensagem pré-preenchida do WhatsApp:**
  `Olá Leo! Vi seu trabalho e quero saber se é o meu momento de dar esse passo.`
  (URL-encoded: `https://wa.me/5511933915702?text=Ol%C3%A1%20Leo!%20Vi%20seu%20trabalho%20e%20quero%20saber%20se%20%C3%A9%20o%20meu%20momento%20de%20dar%20esse%20passo.`)
- **Instagram:** @o.cosba
- **Profissional:** Leo Cosba — Terapeuta Multidimensional
- **Área atendida:** Brasil (atendimento 100% à distância)

---

## SEO — meta tags
```html
<title>Cura Arcturiana — SACM | Terapia Espiritual Ativa · Leo Cosba</title>
<meta name="description" content="Terapia espiritual ativa (SACM): desbloqueia e impulsiona os seus próprios movimentos. Trabalhamos as suas travas na raiz e devolvemos clareza e direção para você agir. Primeira conversa gratuita com Leo Cosba.">
<meta name="keywords" content="cura arcturiana, SACM, terapia espiritual ativa, auto-responsabilidade, espiritualidade ativa, desbloqueio para a ação, geometria sagrada, símbolos arcturianos, Leo Cosba, terapia complementar, direcionamento">

<!-- Open Graph -->
<meta property="og:title" content="Cura Arcturiana — SACM | Terapia Espiritual Ativa">
<meta property="og:description" content="Uma terapia espiritual ativa que destrava e impulsiona os seus próprios movimentos. Clareza e direção para agir. Dê o seu próximo passo pelo WhatsApp.">
<meta property="og:image" content="assets/leo-portrait.png">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Cura Arcturiana — SACM | Terapia Espiritual Ativa">
<meta name="twitter:description" content="A espiritualidade trabalha através de você, não por você. Desbloqueio e direção para você agir. Dê o seu próximo passo.">
<meta name="twitter:image" content="assets/leo-portrait.png">
```

---

## JSON-LD (Schema.org)
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "name": "SACM — Sistema Arcturiano de Cura Multidimensional",
      "serviceType": "Terapia espiritual complementar a distância",
      "description": "Terapia espiritual ativa de 5 sessões semanais à distância que desbloqueia e impulsiona os movimentos próprios da pessoa, atuando na raiz energética das suas travas e entregando direcionamento prático para a ação.",
      "provider": { "@type": "Person", "name": "Leo Cosba", "jobTitle": "Terapeuta Multidimensional" },
      "areaServed": "BR",
      "availableChannel": { "@type": "ServiceChannel", "serviceUrl": "https://wa.me/5511933915702" }
    },
    {
      "@type": "FAQPage",
      "mainEntity": "(ver as 9 perguntas em 01-copy-verbatim.md, seção FAQ)"
    }
  ]
}
```

---

## Disclaimer legal (rodapé — manter literal)
Terapia complementar de bem-estar e desenvolvimento espiritual. Não substitui acompanhamento médico, psicológico ou psiquiátrico, nem o uso de medicamentos prescritos.

---

## Assets de imagem (na pasta `assets/`)
| Arquivo | Uso |
|---|---|
| `leo-portrait.png` | Foto do terapeuta (seção Terapeuta + og:image). Circular, borda dourada. |
| `favicon.svg` | Ícone da aba/site. |
| `carol.jpg` | Foto depoimento — Carol. |
| `saeid.jpg` | Foto depoimento — Saeid. |
