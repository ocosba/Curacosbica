import { useState, useRef } from 'react';
import { BreathingStars } from '../components/BreathingStars';
import { MandalaHero, MarkSmall, MarkGlow } from '../components/SacredGeometry';
import { Reveal } from '../components/Reveal';

// Pilares
import pilarGeometria from '../assets/pilar-geometria.svg';
import pilarHierarquia from '../assets/pilar-hierarquia.svg';
import pilarAmor from '../assets/pilar-amor.svg';
import pilarResponsabilidade from '../assets/pilar-responsabilidade.svg';

// Icones
import iconeRelacoes from '../assets/icone-relacoes.svg';
import iconeSaude from '../assets/icone-saude.svg';
import iconeProsperidade from '../assets/icone-prosperidade.svg';

import iconeLimpeza from '../assets/icone-limpeza.svg';
import iconeCorte from '../assets/icone-corte.svg';
import iconePoder from '../assets/icone-poder.svg';
import iconeCrianca from '../assets/icone-crianca.svg';
import iconeDna from '../assets/icone-dna.svg';
import iconeEu from '../assets/icone-eu.svg';
import iconeKarma from '../assets/icone-karma.svg';
import iconeProtecao from '../assets/icone-protecao.svg';

// Brand and portraits
import marcaCosbaRaios from '../assets/marca-cosba-raios.svg';
import leoPortrait from '../assets/leo-portrait.png';
import carolJpg from '../assets/carol.jpg';
import saeidJpg from '../assets/saeid.jpg';

const WA_LINK = 'https://wa.me/5511933915702?text=Olá%20Leo!%20Vi%20seu%20trabalho%20e%20quero%20saber%20se%20é%20o%20meu%20momento%20de%20dar%20esse%20passo.';

const pilares = [
  {
    icon: pilarGeometria,
    title: 'Geometria Sagrada',
    body: 'Os símbolos arcturianos são códigos de frequência. Cada um age sobre um padrão específico — como uma chave desenhada para uma fechadura exata.'
  },
  {
    icon: pilarHierarquia,
    title: 'Hierarquia de Luz',
    body: 'O trabalho é conduzido em conexão com os Arcturianos e os Mestres de Luz. Você não está só: há uma inteligência maior sustentando cada passo que você dá.'
  },
  {
    icon: pilarAmor,
    title: 'Amor Incondicional',
    body: 'Nada é forçado. A cura abre o caminho no ritmo que é seguro para você, sempre respeitando o seu livre-arbítrio e o seu tempo.'
  },
  {
    icon: pilarResponsabilidade,
    title: 'Auto-responsabilidade',
    body: 'Nada é feito no seu lugar. Caminhar é a sua parte — e é ela que torna a mudança real e duradoura.'
  }
];

const cards = [
  {
    num: '01',
    icon: iconeRelacoes,
    title: 'Nas suas relações',
    body: 'Os padrões que se repetem têm raiz energética: o mesmo vínculo, a mesma dor, a mesma dificuldade de impor limites. O trabalho libera os laços vencidos e te devolve algo que ninguém faz por você: a capacidade de se posicionar e escolher de novo.'
  },
  {
    num: '02',
    icon: iconeSaude,
    title: 'Na sua saúde e vitalidade',
    body: 'Cansaço que não passa, ansiedade sem motivo claro, peso que vem de longe. Quando a energia volta a circular, o corpo respira — e você reencontra a disposição para fazer o que vinha adiando.'
  },
  {
    num: '03',
    icon: iconeProsperidade,
    title: 'Na sua prosperidade',
    body: 'Bloqueios de merecimento e medos herdados travam, em silêncio, o que você se permite buscar. Dissolvida a trava, abre-se espaço — mas a oportunidade você ainda precisa agarrar.'
  }
];

const layers = [
  { title: 'Limpeza e equilíbrio energético', body: 'dissolve o peso acumulado no campo, de onde nascem o cansaço sem causa e a sobrecarga que paralisa.', icon: iconeLimpeza },
  { title: 'Corte de contratos e vínculos', body: 'encerra ligações que drenam a sua energia e te prendem a quem já deveria ter ficado para trás.', icon: iconeCorte },
  { title: 'Resgate do poder pessoal', body: 'recolhe a presença que você cedeu ou adormeceu — e devolve a você o comando das próprias escolhas.', icon: iconePoder },
  { title: 'Cura da criança interior', body: 'alcança feridas antigas que ainda comandam reações de hoje, sem que você precise reviver a dor para se libertar.', icon: iconeCrianca },
  { title: 'Purificação do DNA e ancestralidade', body: 'limpa heranças de linhagem que você carrega sem ter escolhido — padrões que não precisam continuar em você.', icon: iconeDna },
  { title: 'Reconexão com o Eu Superior', body: 'fortalece a conexão com a sua essência, e as escolhas ficam mais claras de dentro para fora.', icon: iconeEu },
  { title: 'Cura e liberação kármica', body: 'desativa repetições que resistem a tudo, registros que atravessam mais de uma experiência de alma.', icon: iconeKarma },
  { title: 'Proteção e selagem do campo', body: 'sela o que foi trabalhado para que a leveza conquistada se sustente no dia a dia.', icon: iconeProtecao }
];

const jornada = [
  { n: '1', tag: 'Antes de começar', title: 'Dar o primeiro passo', body: 'Uma conversa de alinhamento para entender o seu momento e ver, juntos, se você está pronto para fazer a sua parte.' },
  { n: '2', tag: 'Toda semana · começo', title: 'O seu relato', body: 'Antes de cada sessão você conta como foi a semana: o que travou, o que se moveu, onde precisa de direção. A sessão é desenhada a partir daí.' },
  { n: '3', tag: 'A sessão', title: 'Trabalho energético + seu direcionamento', body: 'Eu conduzo a sessão à distância e, em seguida, te devolvo o feedback prático: o que foi trabalhado e qual o seu próximo movimento.' },
  { n: '4', tag: 'Durante a semana · meio', title: 'Você coloca em prática', body: 'Aqui o trabalho vira ação no plano físico. Eu fico ao seu lado para você atravessar esse movimento com apoio — mas o passo é seu.' },
  { n: '5', tag: 'Fim do ciclo de um mês', title: 'Relatório de caminhada', body: 'O panorama do que foi destravado e do quanto você avançou — com a direção para seguir caminhando por conta própria.' },
];

const faqs = [
  { q: 'Esse trabalho é para qualquer pessoa?', a: 'Não. É para quem está disposto a agir por conta própria. Se você espera que a espiritualidade resolva tudo sem nenhum movimento seu, este não é o lugar — e tudo bem ser honesto sobre isso desde já.' },
  { q: 'Preciso acreditar para funcionar?', a: 'Não precisa de fé, mas precisa de disposição. A frequência dos símbolos age independentemente da sua crença; o que faz a diferença é você dar os passos que o trabalho destrava.' },
  { q: 'Como funciona uma terapia à distância?', a: 'A energia não depende de proximidade física. No horário combinado, eu conduzo a sessão sintonizado na sua frequência. A sua participação é antes, no relato, e depois, colocando o direcionamento em prática.' },
  { q: 'O que eu preciso fazer?', a: 'Duas coisas: antes de cada sessão, relatar com sinceridade a sua semana e as suas travas; e, depois, agir sobre o direcionamento que você recebe. É esse movimento que torna a cura real.' },
  { q: 'Por que cinco sessões, uma por semana?', a: 'Cada sessão movimenta muito o interno, e a semana é o tempo de você integrar agindo. As cinco formam um ciclo de um mês, cada uma construída a partir do seu retorno da anterior.' },
  { q: 'Como recebo o direcionamento?', a: 'A cada sessão você recebe um feedback prático do que foi trabalhado e do próximo passo a dar; ao final do ciclo, um relatório de caminhada com o panorama completo.' },
  { q: 'Quando começo a sentir os efeitos?', a: 'Varia — e depende também do quanto você se move. Há quem perceba mudanças nos primeiros dias; em outros casos o movimento aparece ao longo das semanas, conforme você coloca em prática.' },
  { q: 'Isso substitui terapia ou tratamento médico?', a: 'Não. É uma terapia complementar de bem-estar e desenvolvimento espiritual. Não substitui acompanhamento médico, psicológico ou psiquiátrico, nem o uso de medicamentos prescritos. Caminha lado a lado com eles.' },
  { q: 'É seguro? E se mexer demais comigo?', a: 'O trabalho respeita sempre o seu livre-arbítrio e o seu tempo — nada é forçado. E você não fica sozinho: eu acompanho a sua semana de perto para te amparar enquanto você dá os seus passos.' }
];

const quizOptions = [
  {
    label: 'Quero mudar, mas espero que aconteça sozinho',
    title: 'Talvez ainda não seja a sua hora',
    body: 'Com sinceridade: a espiritualidade não faz no seu lugar. Quando bater a disposição de dar o primeiro passo — mesmo pequeno — eu estou aqui para te impulsionar.'
  },
  {
    label: 'Estou cansado de tentar e travar no mesmo ponto',
    title: 'É exatamente aqui que eu entro',
    body: 'Tentar e travar é sinal de que a raiz não foi tocada. A gente desbloqueia a origem e você recebe direção para o próximo movimento.'
  },
  {
    label: 'Sei o que preciso fazer, mas algo me paralisa',
    title: 'Esse "algo" tem endereço energético',
    body: 'O trabalho dissolve a trava e te devolve o impulso para agir — com clareza de por onde começar.'
  },
  {
    label: 'Estou pronto para agir, só preciso de direção',
    title: 'Você é exatamente quem este trabalho impulsiona',
    body: 'Vamos transformar a sua disposição em movimento direcionado, passo a passo.'
  }
];

const depoimentos = [
  {
    text: 'Cheguei no limite: ansiedade, cansaço constante e irritação — e tudo isso respingava no meu relacionamento e no trabalho que eu mal havia começado. Nos primeiros dias senti altos e baixos, mas também os primeiros momentos de paz. A leitura que o Léo indicou para a noite trouxe calma ao coração e à mente. Semana após semana, os sentimentos foram assentando e as ideias se organizando — em casa, no trabalho e comigo mesma. Reaprendi a respirar e a confiar, porque entendi que nunca estou sozinha. Léo, seu trabalho é profundo e sério. Gratidão imensa.',
    name: 'Carol',
    role: 'Acompanhamento SACM',
    img: carolJpg
  },
  {
    text: 'No começo de 2026, eu vivia uma espiral de dúvidas, insegurança e ansiedade, em meio a um quadro de depressão. Desde que me fardei no Santo Daime, em 2023, muitos processos se abriram, e a confusão mental me travava até nas tarefas mais simples do dia. Foi quando conheci o Leonardo e o SACM — confesso que comecei cético. Aos poucos, a mente foi clareando e firmando, e voltou a me concentrar para estudar, trabalhar e viver. Hoje tenho muito mais clareza sobre quem sou e sobre o caminho que sigo, e decido com a serenidade que a ansiedade não me deixava ter. Sigo em tratamento, e tenho certeza de que o SACM me ajudou demais. Recomendo a todos.',
    name: 'Saeid',
    role: 'Acompanhamento SACM',
    img: saeidJpg
  }
];

export function LandingPage() {
  const [activeTab, setActiveTab] = useState(0);
  const [quiz, setQuiz] = useState<number | null>(null);
  const [openFaq, setOpenFaq] = useState<number | null>(null);

  // Drag Carousel State & Handlers
  const [dragStart, setDragStart] = useState<number | null>(null);
  const [dragOffset, setDragOffset] = useState(0);
  const [isDragging, setIsDragging] = useState(false);
  const carouselRef = useRef<HTMLDivElement>(null);

  const handlePointerDown = (e: React.PointerEvent) => {
    if (e.button !== 0 && e.pointerType === 'mouse') return;
    setDragStart(e.clientX);
    setIsDragging(true);
    if (carouselRef.current) {
      carouselRef.current.setPointerCapture(e.pointerId);
    }
  };

  const handlePointerMove = (e: React.PointerEvent) => {
    if (!isDragging || dragStart === null) return;
    const currentX = e.clientX;
    const diff = currentX - dragStart;
    setDragOffset(diff);
  };

  const handlePointerUp = (e: React.PointerEvent) => {
    if (!isDragging) return;
    setIsDragging(false);
    if (carouselRef.current) {
      carouselRef.current.releasePointerCapture(e.pointerId);
    }

    const W = carouselRef.current?.getBoundingClientRect().width || 300;
    const threshold = Math.min(W * 0.2, 80);

    if (dragOffset < -threshold) {
      if (activeTab < cards.length - 1) {
        setActiveTab(activeTab + 1);
      }
    } else if (dragOffset > threshold) {
      if (activeTab > 0) {
        setActiveTab(activeTab - 1);
      }
    }

    setDragStart(null);
    setDragOffset(0);
  };

  const handlePointerCancel = () => {
    setIsDragging(false);
    setDragStart(null);
    setDragOffset(0);
  };

  return (
    <div style={{
      position: 'relative',
      minHeight: '100vh',
      background: 'transparent',
      color: 'var(--c-text)',
      fontFamily: "'Poppins', sans-serif",
      overflowX: 'clip',
    }}>
      <BreathingStars />

      {/* ---- NAV ---- */}
      <nav style={{
        position: 'sticky', top: 0, zIndex: 20,
        display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 24,
        padding: 'clamp(14px,2vw,18px) clamp(20px,5vw,56px)',
        backdropFilter: 'blur(14px)',
        background: 'linear-gradient(180deg, rgba(11,8,38,.82) 0%, rgba(11,8,38,.34) 100%)',
        borderBottom: '1px solid var(--c-line)',
      }}>
        <a href="#topo" style={{ display: 'flex', alignItems: 'center', gap: 13, textDecoration: 'none', color: 'var(--c-text)' }}>
          <span style={{ display: 'flex', width: 42 }}><MarkSmall /></span>
          <span style={{ display: 'flex', flexDirection: 'column', lineHeight: 1 }}>
            <span style={{ fontFamily: "'Chakra Petch', sans-serif", fontSize: 23, fontWeight: 700, letterSpacing: '.14em', color: 'var(--c-violet)' }}>COSBA</span>
            <span style={{ fontSize: '8.5px', fontWeight: 600, letterSpacing: '.34em', color: 'var(--c-orchid)', marginTop: 3 }}>CURA MULTIDIMENSIONAL</span>
          </span>
        </a>
        <div style={{ display: 'flex', alignItems: 'center', gap: 30 }}>
          <div className="nav-links" style={{ display: 'flex', gap: 26, alignItems: 'center' }}>
            {[['#trabalho','O trabalho'],['#transformacoes','Transformações'],['#jornada','Acompanhamento'],['#perguntas','Perguntas']].map(([href, label]) => (
              <a key={href} href={href} style={{ textDecoration: 'none', color: 'var(--c-dim)', fontSize: 14, fontWeight: 400, letterSpacing: '.02em', transition: 'color .3s' }}
                onMouseEnter={e => (e.target as HTMLElement).style.color = 'var(--c-gold-soft)'}
                onMouseLeave={e => (e.target as HTMLElement).style.color = 'var(--c-dim)'}
              >{label}</a>
            ))}
          </div>
          <a href={WA_LINK} target="_blank" rel="noopener" className="nav-cta" style={{
            padding: '11px 22px', borderRadius: 999, border: '1px solid var(--c-line)',
            color: 'var(--c-gold-soft)', textDecoration: 'none', fontSize: 14, fontWeight: 500,
            letterSpacing: '.02em', transition: 'background .3s, border-color .3s', whiteSpace: 'nowrap',
          }}
            onMouseEnter={e => { const el = e.target as HTMLElement; el.style.background = 'color-mix(in oklab,#E3BE45 14%,transparent)'; el.style.borderColor = 'var(--c-gold)'; }}
            onMouseLeave={e => { const el = e.target as HTMLElement; el.style.background = 'transparent'; el.style.borderColor = 'var(--c-line)'; }}
          >Dar o meu próximo passo</a>
        </div>
      </nav>

      {/* ---- HERO ---- */}
      <header id="topo" className="hero-header" style={{ position: 'relative', zIndex: 1, padding: 'clamp(60px,8vw,110px) clamp(20px,5vw,56px) clamp(70px,9vw,120px)', textAlign: 'center' }}>
        <div style={{ position: 'relative', maxWidth: 900, margin: '0 auto', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <div style={{ position: 'relative', marginBottom: 'clamp(34px,5vw,52px)', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
            <div style={{ position: 'absolute', width: 'min(80vw,420px)', aspectRatio: '1', borderRadius: '50%', background: 'radial-gradient(circle, color-mix(in oklab,#B06CB0 30%,transparent), transparent 62%)', filter: 'blur(34px)', animation: 'arcPulse 8s ease-in-out infinite' }} />
            <div style={{ position: 'relative' }}>
              <MandalaHero />
            </div>
          </div>

          <p className="section-label"><span />{' '}Terapia Espiritual Ativa · SACM{' '}<span /></p>

          <h1 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(36px,6vw,68px)', lineHeight: 1.06, margin: '0 0 26px', letterSpacing: '-.01em' }}>
            A espiritualidade trabalha{' '}
            <span className="shimmer-text">através de você</span>.
            {' '}Não por você.
          </h1>

          <p style={{ fontWeight: 300, fontSize: 'clamp(16px,1.9vw,20px)', lineHeight: 1.75, color: 'var(--c-dim)', maxWidth: '60ch', margin: '0 0 40px' }}>
            O SACM é uma terapia que{' '}
            <span style={{ color: 'var(--c-gold-soft)' }}>desbloqueia e impulsiona os seus próprios movimentos</span>.
            {' '}Trabalhamos espiritualmente as suas travas na raiz e devolvemos clareza e direção — porque os passos, no plano físico, são seus para dar.
          </p>

          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 16, alignItems: 'center', justifyContent: 'center' }}>
            <a href={WA_LINK} target="_blank" rel="noopener" className="btn-gold" style={{ padding: '17px 38px', fontSize: 16 }}>
              Quero dar o meu próximo passo
            </a>
            <a href="#trabalho" style={{
              display: 'inline-flex',
              alignItems: 'center',
              background: 'none',
              border: '1px solid rgba(227, 190, 69, 0.30)',
              borderRadius: 999,
              color: 'var(--c-text)',
              padding: '17px 26px',
              textDecoration: 'none',
              fontSize: 16,
              fontWeight: 400,
              transition: 'border-color .3s'
            }}
              onMouseEnter={e => (e.currentTarget as HTMLElement).style.borderColor = 'var(--c-gold)'}
              onMouseLeave={e => (e.currentTarget as HTMLElement).style.borderColor = 'rgba(227, 190, 69, 0.30)'}
            >Entender como funciona</a>
          </div>

          <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: '14px 30px', marginTop: 42 }}>
            {['Atendimento 100% à distância', '5 sessões · 1 por semana', 'Direcionamento prático a cada sessão'].map(t => (
              <span key={t} style={{ display: 'inline-flex', alignItems: 'center', gap: 9, fontSize: 14, fontWeight: 300, color: 'var(--c-dim)' }}>
                <span style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--c-gold)', boxShadow: '0 0 8px var(--c-gold)', flex: 'none' }} />
                {t}
              </span>
            ))}
          </div>
        </div>
      </header>

      {/* ---- SOBRE O TRABALHO ---- */}
      <section id="trabalho" style={{ position: 'relative', zIndex: 1, padding: 'clamp(60px,8vw,100px) clamp(20px,5vw,56px)' }}>
        <Reveal>
          <div style={{ maxWidth: 780, margin: '0 auto', textAlign: 'center' }}>
            <p className="section-label"><span />Sobre o trabalho<span /></p>
            <h2 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(28px,4.4vw,48px)', lineHeight: 1.12, margin: '0 0 26px' }}>
              A espiritualidade abre o caminho. Quem caminha é você.
            </h2>
            <p style={{ fontWeight: 300, fontSize: 'clamp(16px,1.6vw,19px)', lineHeight: 1.82, color: 'var(--c-dim)', margin: '0 auto 18px', maxWidth: '62ch' }}>
              Talvez você já tenha pedido sinais, esperado o momento certo, tentado "elevar a vibração" — e mesmo assim sentido que a vida não destrava. Não destrava porque transformação não acontece{' '}
              <span style={{ color: 'var(--c-gold-soft)' }}>sobre</span> você enquanto você espera: ela acontece{' '}
              <span style={{ color: 'var(--c-gold-soft)' }}>através</span> de você, quando você se move.
            </p>
            <p style={{ fontWeight: 300, fontSize: 'clamp(16px,1.6vw,19px)', lineHeight: 1.82, color: 'var(--c-dim)', margin: '0 auto 18px', maxWidth: '62ch' }}>
              O que trava esse movimento quase nunca está só na mente. Está mais fundo, no seu{' '}
              <span style={{ color: 'var(--c-gold-soft)' }}>campo energético</span> — onde memórias, vínculos e heranças seguram você num mesmo lugar, em silêncio. Enquanto essa raiz não é tocada, agir custa, e o mesmo padrão volta com outra roupa.
            </p>
            <p style={{ fontWeight: 300, fontSize: 'clamp(16px,1.6vw,19px)', lineHeight: 1.82, color: 'var(--c-dim)', margin: '0 auto 24px', maxWidth: '62ch' }}>
              O SACM atua nessa raiz para te desbloquear — e devolve a você a direção do próximo passo.
            </p>
            <p style={{ fontWeight: 500, fontSize: 'clamp(18px,2vw,24px)', lineHeight: 1.5, color: 'var(--c-gold-soft)', margin: '0 auto', maxWidth: '62ch' }}>
              A espiritualidade trabalha através de você. A sua parte é se mover.
            </p>
          </div>
        </Reveal>
      </section>

      {/* ---- O QUE É O SACM ---- */}
      <section id="cura" style={{ position: 'relative', zIndex: 1, padding: 'clamp(50px,6vw,80px) clamp(20px,5vw,56px)' }}>
        <div style={{ maxWidth: 1000, margin: '0 auto' }}>
          <Reveal>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(320px,1fr))', gap: '40px', alignItems: 'center' }}>
              <div style={{ textAlign: 'left' }}>
                <p className="section-label" style={{ margin: '0 0 16px' }}><span />O que é o SACM</p>
                <h2 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(28px,4vw,44px)', lineHeight: 1.14, margin: '0 0 24px' }}>
                  Desbloqueio para a ação — não um milagre para esperar
                </h2>
                <p style={{ fontWeight: 300, fontSize: 'clamp(15px,1.6vw,17.5px)', lineHeight: 1.8, color: 'var(--c-dim)', margin: '0 0 18px' }}>
                  Um sistema de cura energética que atua nos seus{' '}
                  <span style={{ color: 'var(--c-gold-soft)' }}>corpos sutis</span> — as camadas de energia, emoção e memória que organizam, de dentro para fora, o que se manifesta na sua vida. É ali que mora a trava; é ali que o trabalho age.
                </p>
                <p style={{ fontWeight: 300, fontSize: 'clamp(15px,1.6vw,17.5px)', lineHeight: 1.8, color: 'var(--c-dim)', margin: 0 }}>
                  A linguagem dessa cura são as{' '}
                  <span style={{ color: 'var(--c-gold-soft)' }}>geometrias sagradas — os símbolos arcturianos</span>: cada um é um código de frequência que atua sobre um padrão específico. A frequência faz a parte dela — abre, dissolve, destrava.{' '}
                  <span style={{ color: 'var(--c-gold-soft)' }}>A outra parte é sua: dar o passo que antes parecia impossível.</span>
                </p>
              </div>
              <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
                <div style={{ position: 'absolute', width: '280px', height: '280px', borderRadius: '50%', background: 'radial-gradient(circle, color-mix(in oklab,var(--c-violet-deep) 34%,transparent), transparent 70%)', filter: 'blur(20px)', zIndex: -1 }} />
                <img src={marcaCosbaRaios} alt="Símbolo COSBA" style={{ width: '220px', height: 'auto', display: 'block', animation: 'arcFloat 8s ease-in-out infinite' }} />
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ---- OS QUATRO PILARES ---- */}
      <section id="pilares" style={{ position: 'relative', zIndex: 1, padding: 'clamp(50px,6vw,80px) clamp(20px,5vw,56px)' }}>
        <div style={{ maxWidth: 1080, margin: '0 auto' }}>
          <Reveal>
            <div style={{ textAlign: 'center', marginBottom: 54 }}>
              <p style={{ margin: '0 0 16px', fontSize: 12.5, letterSpacing: '.28em', textTransform: 'uppercase', color: 'var(--c-gold)', fontWeight: 600 }}>A base do sistema</p>
              <h2 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(28px,4.4vw,50px)', lineHeight: 1.08, margin: 0 }}>Os quatro pilares</h2>
            </div>
          </Reveal>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(min(100%,420px),1fr))', gap: 20 }}>
            {pilares.map((p, i) => (
              <Reveal key={i} delay={i * 80}>
                <div className="card-glass" style={{ padding: '40px 30px', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                  <div style={{ marginBottom: 22 }}>
                    <img src={p.icon} alt={p.title} style={{ width: '88px', height: '88px', objectFit: 'contain' }} />
                  </div>
                  <h3 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 13, letterSpacing: '.16em', textTransform: 'uppercase', color: 'var(--c-gold-soft)', margin: '0 0 16px' }}>{p.title}</h3>
                  <p style={{ fontWeight: 300, fontSize: 15, lineHeight: 1.7, color: 'var(--c-dim)', margin: 0 }}>{p.body}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ---- TRANSFORMAÇÕES ---- */}
      <section id="transformacoes" style={{ position: 'relative', zIndex: 1, padding: 'clamp(60px,7vw,90px) clamp(20px,5vw,56px)' }}>
        <div style={{ maxWidth: 1080, margin: '0 auto', textAlign: 'center' }}>
          <Reveal>
            <p style={{ margin: '0 0 16px', fontSize: 12.5, letterSpacing: '.28em', textTransform: 'uppercase', color: 'var(--c-gold)', fontWeight: 600 }}>O que se destrava quando você age</p>
            <h2 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(28px,4.4vw,50px)', lineHeight: 1.08, margin: '0 0 14px' }}>A mudança aparece onde você decide se mover</h2>
            <p style={{ fontWeight: 300, fontSize: 17, color: 'var(--c-dim)', maxWidth: '56ch', margin: '0 auto 48px' }}>Quando o campo é desbloqueado, a ação que estava travada volta a ser possível — nas três áreas que mais pesam.</p>
          </Reveal>

          {/* CARROSSEL ARRASTÁVEL */}
          <Reveal>
            <div style={{ maxWidth: 880, margin: '0 auto', position: 'relative' }}>
              
              {/* Abas Superiores (Sincronizadas) */}
              <div style={{ display: 'flex', gap: 12, justifyContent: 'center', marginBottom: 34, flexWrap: 'wrap' }}>
                {cards.map((c, i) => {
                  const on = activeTab === i;
                  return (
                    <button
                      key={i}
                      onClick={() => setActiveTab(i)}
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: 9,
                        padding: '13px 22px',
                        borderRadius: 999,
                        cursor: 'pointer',
                        transition: 'all .3s',
                        border: `1px solid ${on ? 'color-mix(in oklab,var(--c-gold) 55%,transparent)' : 'var(--c-line)'}`,
                        background: on ? 'linear-gradient(160deg, color-mix(in oklab,var(--c-gold) 18%,transparent), transparent)' : 'transparent',
                        color: on ? 'var(--c-gold-soft)' : 'var(--c-dim)',
                        fontFamily: "'Poppins', sans-serif",
                        fontSize: '14.5px',
                        fontWeight: 500
                      }}
                    >
                      <span style={{ fontFamily: "'Chakra Petch',sans-serif", fontSize: 12, fontWeight: 700, opacity: 0.7 }}>{c.num}</span>
                      <span>{i === 0 ? 'Relações' : i === 1 ? 'Saúde' : 'Prosperidade'}</span>
                    </button>
                  );
                })}
              </div>

              {/* Slider Wrapper (com setas laterais em telas maiores) */}
              <div style={{ display: 'flex', alignItems: 'center', gap: 20, position: 'relative' }}>
                
                {/* Seta Anterior */}
                <button
                  onClick={() => activeTab > 0 && setActiveTab(activeTab - 1)}
                  disabled={activeTab === 0}
                  className="carousel-arrow"
                  style={{ flexShrink: 0 }}
                  aria-label="Slide anterior"
                >
                  ←
                </button>

                {/* Janela de Recorte (Viewport) */}
                <div 
                  ref={carouselRef}
                  onPointerDown={handlePointerDown}
                  onPointerMove={handlePointerMove}
                  onPointerUp={handlePointerUp}
                  onPointerCancel={handlePointerCancel}
                  onPointerLeave={handlePointerUp}
                  style={{
                    flexGrow: 1,
                    overflow: 'hidden',
                    borderRadius: 24,
                    touchAction: 'pan-y',
                    userSelect: 'none',
                  }}
                >
                  {/* Trilho (Track) */}
                  <div
                    style={{
                      display: 'flex',
                      width: '100%',
                      transform: `translateX(calc(-${activeTab * 100}% + ${dragOffset}px))`,
                      transition: isDragging ? 'none' : 'transform .6s cubic-bezier(.22,.61,.36,1)',
                      cursor: isDragging ? 'grabbing' : 'grab',
                    }}
                  >
                    {cards.map((c, i) => {
                      return (
                        <div
                          key={i}
                          style={{
                            flex: '0 0 100%',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            padding: 'clamp(34px,5vw,56px) clamp(26px,5vw,60px)',
                            borderRadius: 24,
                            border: '1px solid var(--c-line)',
                            background: 'radial-gradient(ellipse 90% 70% at 50% 0%, color-mix(in oklab,var(--c-orchid) 16%,transparent), transparent 66%), linear-gradient(160deg, color-mix(in oklab,var(--c-bg2) 64%,transparent), color-mix(in oklab,var(--c-bg1) 52%,transparent))',
                            backdropFilter: 'blur(8px)',
                            overflow: 'hidden',
                            position: 'relative',
                          }}
                        >
                          {/* Marca d'água de número */}
                          <span
                            style={{
                              position: 'absolute',
                              top: 'clamp(-30px,-3vw,-10px)',
                              right: 'clamp(-10px,1vw,24px)',
                              fontFamily: "'Chakra Petch',sans-serif",
                              fontWeight: 700,
                              fontSize: 'clamp(150px,22vw,240px)',
                              lineHeight: 1,
                              color: 'color-mix(in oklab,var(--c-gold) 8%,transparent)',
                              pointerEvents: 'none',
                              userSelect: 'none',
                              zIndex: 0,
                              animation: 'arcFloat 7s ease-in-out infinite'
                            }}
                          >
                            {c.num}
                          </span>

                          <div className="trans-inner" style={{ position: 'relative', zIndex: 1, width: '100%', display: 'flex', gap: 'clamp(22px,4vw,46px)', alignItems: 'center', justifyContent: 'center' }}>
                            <div style={{ flex: 'none' }}>
                              <img src={c.icon} alt={c.title} style={{ width: '116px', height: '116px', objectFit: 'contain' }} />
                            </div>
                            <div className="trans-divider" style={{ width: 1, alignSelf: 'stretch', background: 'linear-gradient(to bottom, transparent, color-mix(in oklab,var(--c-gold) 50%,transparent), transparent)' }}></div>
                            <div style={{ textAlign: 'left', maxWidth: '42ch' }}>
                              <h3 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(24px,3vw,34px)', lineHeight: 1.12, margin: '0 0 16px' }}>{c.title}</h3>
                              <p style={{ fontWeight: 300, fontSize: 'clamp(15px,1.6vw,17px)', lineHeight: 1.78, color: 'var(--c-dim)', margin: 0 }}>{c.body}</p>
                            </div>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>

                {/* Seta Próxima */}
                <button
                  onClick={() => activeTab < cards.length - 1 && setActiveTab(activeTab + 1)}
                  disabled={activeTab === cards.length - 1}
                  className="carousel-arrow"
                  style={{ flexShrink: 0 }}
                  aria-label="Próximo slide"
                >
                  →
                </button>
              </div>

              {/* Dots e Dica de Arraste Mobile */}
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: 24 }}>
                <div style={{ display: 'flex', gap: 8, justifyContent: 'center' }}>
                  {cards.map((_, idx) => {
                    const active = activeTab === idx;
                    return (
                      <button
                        key={idx}
                        onClick={() => setActiveTab(idx)}
                        style={{
                          height: 9,
                          width: active ? 30 : 9,
                          borderRadius: 99,
                          border: 'none',
                          padding: 0,
                          background: active ? 'var(--c-gold)' : 'color-mix(in oklab, var(--c-gold) 30%, transparent)',
                          transition: 'width .4s, background .4s',
                          cursor: 'pointer',
                        }}
                        aria-label={`Ir para slide ${idx + 1}`}
                      />
                    );
                  })}
                </div>
                
                <p className="carousel-mobile-tip" style={{ fontSize: 13, color: 'var(--c-dim)', marginTop: 14, textAlign: 'center' }}>
                  ← arraste para deslizar →
                </p>
              </div>

            </div>
          </Reveal>

          {/* CAMADAS */}
          <Reveal>
            <div style={{ marginTop: 84 }}>
              <h3 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(22px,3vw,34px)', lineHeight: 1.12, margin: '0 0 12px' }}>As camadas que destravamos para você agir</h3>
              <p style={{ fontWeight: 300, fontSize: 16, color: 'var(--c-dim)', maxWidth: '56ch', margin: '0 auto 40px' }}>Por trás de cada movimento que volta a ser possível, o processo atua em camadas profundas. Estas são as principais.</p>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(240px,1fr))', gap: 16, textAlign: 'left' }}>
                {layers.map((l, i) => (
                  <div key={i} style={{ padding: '26px 24px', borderRadius: 18, border: '1px solid var(--c-line)', background: 'linear-gradient(160deg, color-mix(in oklab,#241a6e 50%,transparent), color-mix(in oklab,#15104a 44%,transparent))' }}>
                    <div style={{ marginBottom: 14 }}>
                      <img src={l.icon} alt={l.title} style={{ width: '76px', height: '76px', objectFit: 'contain' }} />
                    </div>
                    <h4 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 17, lineHeight: 1.2, margin: '0 0 8px', color: 'var(--c-text)' }}>{l.title}</h4>
                    <p style={{ fontWeight: 300, fontSize: 14.5, lineHeight: 1.6, color: 'var(--c-dim)', margin: 0 }}>{l.body}</p>
                  </div>
                ))}
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ---- QUIZ ---- */}
      <section style={{ position: 'relative', zIndex: 1, padding: 'clamp(50px,6vw,80px) clamp(20px,5vw,56px)' }}>
        <div style={{ maxWidth: 860, margin: '0 auto' }}>
          <Reveal>
            <div style={{ textAlign: 'center', padding: 'clamp(36px,5vw,58px) clamp(24px,5vw,54px)', borderRadius: 28, border: '1px solid var(--c-line)', background: 'radial-gradient(ellipse 90% 80% at 50% 0%, color-mix(in oklab,#B06CB0 24%,transparent), transparent 70%), linear-gradient(160deg, color-mix(in oklab,#241a6e 60%,transparent), color-mix(in oklab,#15104a 50%,transparent))', backdropFilter: 'blur(8px)' }}>
              <p style={{ margin: '0 0 16px', fontSize: 12.5, letterSpacing: '.28em', textTransform: 'uppercase', color: 'var(--c-gold)', fontWeight: 600 }}>Antes de tudo, uma pergunta honesta</p>
              <h2 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(25px,3.6vw,40px)', lineHeight: 1.1, margin: '0 0 14px' }}>Você está disposto a fazer a sua parte?</h2>
              <p style={{ fontWeight: 300, fontSize: 16, lineHeight: 1.6, color: 'var(--c-dim)', maxWidth: '46ch', margin: '0 auto 30px' }}>Este trabalho impulsiona quem se move. Onde você está hoje?</p>
              <div style={{ display: 'grid', gap: 12, maxWidth: 580, margin: '0 auto' }}>
                {quizOptions.map((q, i) => (
                  <button key={i} onClick={() => setQuiz(i)} style={{
                    padding: '16px 24px',
                    borderRadius: 14,
                    border: quiz === i ? '1px solid transparent' : '1px solid var(--c-line)',
                    background: quiz === i ? 'linear-gradient(120deg, var(--c-gold), var(--c-gold-soft))' : 'color-mix(in oklab,#15104a 38%,transparent)',
                    color: quiz === i ? '#24160a' : 'var(--c-text)',
                    fontFamily: "'Poppins',sans-serif",
                    fontSize: 15,
                    fontWeight: quiz === i ? 600 : 400,
                    cursor: 'pointer',
                    textAlign: 'left',
                    transition: 'all .3s',
                    lineHeight: 1.5
                  }}>
                    {q.label}
                  </button>
                ))}
              </div>
              {quiz !== null && (
                <div style={{ marginTop: 34, paddingTop: 32, borderTop: '1px solid var(--c-line)' }}>
                  <p style={{ fontSize: 12, letterSpacing: '.26em', textTransform: 'uppercase', color: 'var(--c-dim)', margin: '0 0 12px' }}>O que isso diz sobre o seu momento</p>
                  <h3 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(22px,3vw,30px)', color: 'var(--c-gold-soft)', margin: '0 0 16px' }}>{quizOptions[quiz].title}</h3>
                  <p style={{ fontWeight: 300, fontSize: 17, lineHeight: 1.7, color: 'var(--c-dim)', maxWidth: '52ch', margin: '0 auto 28px' }}>{quizOptions[quiz].body}</p>
                  <a href={WA_LINK} target="_blank" rel="noopener" style={{ display: 'inline-flex', alignItems: 'center', gap: 10, padding: '14px 32px', borderRadius: 999, background: 'linear-gradient(120deg,#E3BE45,#f2dd93)', color: '#24160a', fontWeight: 600, fontSize: 15, textDecoration: 'none', boxShadow: '0 0 36px color-mix(in oklab,#E3BE45 40%,transparent)' }}>
                    Conversar sobre isso
                  </a>
                </div>
              )}
            </div>
          </Reveal>
        </div>
      </section>

      {/* ---- COMO FUNCIONA ---- */}
      <section id="jornada" style={{ position: 'relative', zIndex: 1, padding: 'clamp(60px,7vw,100px) clamp(20px,5vw,56px)' }}>
        <div style={{ maxWidth: 760, margin: '0 auto' }}>
          <Reveal>
            <div style={{ textAlign: 'center', marginBottom: 50 }}>
              <p style={{ margin: '0 0 18px', fontSize: 12.5, letterSpacing: '.28em', textTransform: 'uppercase', color: 'var(--c-gold)', fontWeight: 600 }}>O acompanhamento</p>
              <h2 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(28px,4.4vw,48px)', lineHeight: 1.08, margin: '0 0 16px' }}>Como funciona</h2>
              <p style={{ fontWeight: 300, fontSize: 'clamp(16px,1.6vw,18px)', lineHeight: 1.75, color: 'var(--c-dim)', maxWidth: '56ch', margin: '0 auto' }}>Um acompanhamento à distância de cinco sessões semanais — um ciclo de um mês, com começo, meio e fim. E, no centro de cada semana, a mesma dinâmica ativa.</p>
            </div>
          </Reveal>

          <Reveal delay={100}>
            <h3 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(18px,2.4vw,23px)', textAlign: 'center', margin: '0 0 26px', color: 'var(--c-gold-soft)' }}>A dinâmica de cada sessão</h3>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(190px,1fr))', gap: 14 }}>
              {[
                { n: '01', title: 'Você relata', body: 'Você traz a sua vida real e as suas travas, sem rodeios. É o seu movimento que abre o trabalho.' },
                { n: '02', title: 'Trabalhamos na raiz', body: 'Eu atuo espiritualmente sobre essas questões, na origem energética do que te prende.' },
                { n: '03', title: 'Você recebe direção', body: 'Um feedback prático e direcionado: clareza sobre os próximos passos que você precisa dar.', gold: true },
              ].map((s, i) => (
                <div key={i} style={{ padding: '26px 22px', borderRadius: 18, border: `1px solid ${s.gold ? 'color-mix(in oklab,#E3BE45 40%,transparent)' : 'var(--c-line)'}`, background: s.gold ? 'linear-gradient(160deg, color-mix(in oklab,#E3BE45 14%,transparent), color-mix(in oklab,#15104a 46%,transparent))' : 'linear-gradient(160deg, color-mix(in oklab,#241a6e 54%,transparent), color-mix(in oklab,#15104a 46%,transparent))' }}>
                  <div style={{ fontFamily: "'Chakra Petch',sans-serif", fontSize: 13, letterSpacing: '.3em', color: 'var(--c-gold)', marginBottom: 12 }}>{s.n}</div>
                  <h4 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 17, lineHeight: 1.2, margin: '0 0 8px' }}>{s.title}</h4>
                  <p style={{ fontWeight: 300, fontSize: 14.5, lineHeight: 1.62, color: 'var(--c-dim)', margin: 0 }}>{s.body}</p>
                </div>
              ))}
            </div>
          </Reveal>

          <div style={{ marginTop: 48 }}>
            <h3 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(18px,2.4vw,23px)', textAlign: 'center', margin: '0 0 30px', color: 'var(--c-gold-soft)' }}>O ciclo de um mês</h3>
            <div style={{ display: 'grid', gap: 6 }}>
              {jornada.map((j, i) => (
                <Reveal key={i} delay={i * 80}>
                  <div style={{ display: 'grid', gridTemplateColumns: 'auto 1fr', gap: 22, alignItems: 'start', padding: '18px 0' }}>
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 8 }}>
                      <span style={{ width: 50, height: 50, borderRadius: '50%', border: '1px solid var(--c-line)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: "'Chakra Petch',sans-serif", fontSize: 20, fontWeight: 700, color: 'var(--c-gold)', background: 'color-mix(in oklab,#15104a 60%,transparent)', flex: 'none' }}>{j.n}</span>
                      {i < jornada.length - 1 && <span style={{ width: 1, flex: 1, minHeight: 22, background: 'linear-gradient(var(--c-line), transparent)' }} />}
                    </div>
                    <div style={{ paddingTop: 6 }}>
                      <p style={{ fontSize: 11, letterSpacing: '.24em', textTransform: 'uppercase', color: 'var(--c-gold)', margin: '0 0 7px' }}>{j.tag}</p>
                      <h3 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(19px,2.4vw,24px)', margin: '0 0 8px' }}>{j.title}</h3>
                      <p style={{ fontWeight: 300, fontSize: 15.5, lineHeight: 1.65, color: 'var(--c-dim)', margin: 0 }}>{j.body}</p>
                    </div>
                  </div>
                </Reveal>
              ))}
            </div>
          </div>

          <Reveal>
            <div style={{ marginTop: 40, textAlign: 'center' }}>
              <a href={WA_LINK} target="_blank" rel="noopener" className="btn-gold" style={{ padding: '16px 36px', fontSize: 16 }}>Quero começar</a>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ---- TERAPEUTA ---- */}
      <section id="terapeuta" style={{ position: 'relative', zIndex: 1, padding: 'clamp(60px,7vw,90px) clamp(20px,5vw,56px)' }}>
        <div style={{ maxWidth: 1000, margin: '0 auto', display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(260px,1fr))', gap: 'clamp(40px,5vw,60px)', alignItems: 'center' }}>
          <Reveal>
            <div style={{ display: 'flex', justifyContent: 'center' }}>
              <div style={{ position: 'relative', width: 'min(74vw,300px)', aspectRatio: '1' }}>
                <div style={{ position: 'absolute', inset: -16, borderRadius: '50%', background: 'radial-gradient(circle, color-mix(in oklab,#B06CB0 34%,transparent), transparent 66%)', filter: 'blur(24px)', animation: 'arcPulse 8s ease-in-out infinite' }} />
                <div style={{ position: 'absolute', inset: -9, borderRadius: '50%', border: '1px solid color-mix(in oklab,#E3BE45 30%,transparent)' }} />
                <div style={{ position: 'relative', width: '100%', height: '100%', borderRadius: '50%', border: '1px solid color-mix(in oklab,#E3BE45 55%,transparent)', overflow: 'hidden', boxShadow: '0 18px 54px rgba(0,0,0,.5)', background: 'linear-gradient(135deg, #241a6e, #0b0826)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  <img src={leoPortrait} alt="Leo Cosba" style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                </div>
              </div>
            </div>
          </Reveal>
          <Reveal delay={120}>
            <p style={{ margin: '0 0 16px', fontSize: 12.5, letterSpacing: '.28em', textTransform: 'uppercase', color: 'var(--c-gold)', fontWeight: 600 }}>Quem conduz</p>
            <h2 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(28px,4vw,44px)', lineHeight: 1.08, margin: '0 0 16px' }}>Leo Cosba</h2>
            <p style={{ fontFamily: "'Poppins',sans-serif", fontStyle: 'italic', fontWeight: 300, fontSize: 'clamp(17px,2vw,21px)', color: 'var(--c-gold-soft)', margin: '0 0 20px', lineHeight: 1.55 }}>
              "Eu não caminho por você. Eu te dou luz, clareza e direção — para que você caminhe."
            </p>
            <p style={{ fontWeight: 300, fontSize: 'clamp(15px,1.6vw,17px)', lineHeight: 1.78, color: 'var(--c-dim)', margin: '0 0 18px', maxWidth: '56ch' }}>
              Sempre busquei ajudar a todos. Com meu despertar bem cedo no Santo Daime, desenvolvi minha consciência espiritual e me conectei, através de muitas sincronicidades, aos Arcturianos — que me trouxeram a ferramenta para tratar a causa mais comum: a desconexão da Fonte, e a paralisia diante da própria vida. Estou aqui para te impulsionar, não para fazer no seu lugar.
            </p>
            <p style={{ fontSize: 13, letterSpacing: '.16em', textTransform: 'uppercase', color: 'var(--c-orchid)', fontWeight: 600, margin: 0 }}>Terapeuta Multidimensional</p>
          </Reveal>
        </div>
      </section>

      {/* ---- DEPOIMENTOS ---- */}
      <section id="depoimentos" style={{ position: 'relative', zIndex: 1, padding: 'clamp(60px,7vw,90px) clamp(20px,5vw,56px)' }}>
        <div style={{ maxWidth: 1000, margin: '0 auto', textAlign: 'center' }}>
          <Reveal>
            <p className="section-label"><span />Depoimentos<span /></p>
            <h2 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(28px,4.4vw,50px)', lineHeight: 1.08, margin: '0 0 14px' }}>Quem decidiu se mover</h2>
            <p style={{ fontWeight: 300, fontSize: 17, color: 'var(--c-dim)', maxWidth: '56ch', margin: '0 auto 48px' }}>Relatos de pessoas que escolheram dar os seus próprios passos sob a luz do acompanhamento.</p>
          </Reveal>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(320px,1fr))', gap: 24, textAlign: 'left' }}>
            {depoimentos.map((d, i) => (
              <Reveal key={i} delay={i * 120}>
                <div className="card-glass" style={{ padding: '34px 30px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', height: '100%' }}>
                  <p style={{ fontWeight: 300, fontSize: '15px', lineHeight: '1.75', color: 'var(--c-dim)', fontStyle: 'italic', margin: '0 0 24px' }}>
                    “{d.text}”
                  </p>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                    <img src={d.img} alt={d.name} style={{ width: '48px', height: '48px', borderRadius: '50%', objectFit: 'cover', border: '1.5px solid var(--c-gold)', boxShadow: '0 4px 14px rgba(0,0,0,.3)' }} />
                    <div style={{ display: 'flex', flexDirection: 'column', lineHeight: 1.1 }}>
                      <span style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: '15px', color: 'var(--c-text)' }}>{d.name}</span>
                      <span style={{ fontSize: '10.5px', letterSpacing: '.14em', textTransform: 'uppercase', color: 'var(--c-gold)', fontWeight: 600, marginTop: '4px' }}>{d.role}</span>
                    </div>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ---- FAQ ---- */}
      <section id="perguntas" style={{ position: 'relative', zIndex: 1, padding: 'clamp(60px,7vw,90px) clamp(20px,5vw,56px)' }}>
        <div style={{ maxWidth: 780, margin: '0 auto' }}>
          <Reveal>
            <div style={{ textAlign: 'center', marginBottom: 44 }}>
              <p style={{ margin: '0 0 16px', fontSize: 12.5, letterSpacing: '.28em', textTransform: 'uppercase', color: 'var(--c-gold)', fontWeight: 600 }}>Perguntas frequentes</p>
              <h2 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(27px,4vw,46px)', lineHeight: 1.08, margin: 0 }}>Antes de começar</h2>
            </div>
          </Reveal>
          <div style={{ display: 'grid', gap: 12 }}>
            {faqs.map((f, i) => (
              <Reveal key={i} delay={i * 40}>
                <div style={{ border: '1px solid var(--c-line)', borderRadius: 16, overflow: 'hidden', background: 'color-mix(in oklab,#15104a 42%,transparent)' }}>
                  <button onClick={() => setOpenFaq(openFaq === i ? null : i)} style={{ width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 18, padding: '21px 26px', background: 'none', border: 'none', cursor: 'pointer', textAlign: 'left', color: 'var(--c-text)', fontFamily: "'Poppins',sans-serif", fontSize: 'clamp(15px,1.6vw,17px)', fontWeight: 500 }}>
                    <span>{f.q}</span>
                    <span style={{ color: 'var(--c-gold)', fontSize: 24, fontWeight: 300, transform: openFaq === i ? 'rotate(45deg)' : 'none', transition: 'transform .3s', flexShrink: 0 }}>+</span>
                  </button>
                  {openFaq === i && (
                    <div style={{ padding: '0 26px 24px' }}>
                      <p style={{ fontWeight: 300, fontSize: 15.5, lineHeight: 1.75, color: 'var(--c-dim)', margin: 0, maxWidth: '60ch' }}>{f.a}</p>
                    </div>
                  )}
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ---- CTA FINAL ---- */}
      <section id="contato" style={{ position: 'relative', zIndex: 1, padding: 'clamp(70px,8vw,110px) clamp(20px,5vw,56px) clamp(50px,6vw,80px)' }}>
        <div style={{ maxWidth: 820, margin: '0 auto', textAlign: 'center' }}>
          <Reveal>
            <div style={{ display: 'flex', justifyContent: 'center', marginBottom: 34 }}><MarkGlow /></div>
            <h2 style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 600, fontSize: 'clamp(30px,5vw,56px)', lineHeight: 1.08, margin: '0 0 22px' }}>
              A sua transformação começa<br />com um <span style={{ color: 'var(--c-gold-soft)' }}>movimento seu</span>
            </h2>
            <p style={{ fontWeight: 300, fontSize: 'clamp(16px,1.7vw,19px)', lineHeight: 1.7, color: 'var(--c-dim)', maxWidth: '52ch', margin: '0 auto 36px' }}>
              Uma conversa de alinhamento — gratuita e sem compromisso. Você traz o que está vivendo, e vemos juntos se você está pronto para fazer a sua parte. Você sai com clareza — o que faz com ela já é o seu primeiro passo.
            </p>
            <a href={WA_LINK} target="_blank" rel="noopener" className="btn-gold" style={{ padding: '19px 46px', fontSize: 17 }}>
              Quero dar o meu primeiro passo
            </a>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '14px 32px', justifyContent: 'center', marginTop: 36, color: 'var(--c-dim)', fontSize: 15 }}>
              <span style={{ display: 'inline-flex', alignItems: 'center', gap: 8 }}><span style={{ color: 'var(--c-gold)' }}>·</span> WhatsApp (11) 93391-5702</span>
              <span style={{ display: 'inline-flex', alignItems: 'center', gap: 8 }}><span style={{ color: 'var(--c-gold)' }}>·</span> @o.cosba</span>
            </div>
            <p style={{ fontFamily: "'Poppins',sans-serif", fontWeight: 300, fontStyle: 'italic', fontSize: 'clamp(15px,1.7vw,18px)', letterSpacing: '.04em', color: 'var(--c-gold-soft)', margin: '44px 0 0' }}>
              Que a luz dos Arcturianos ilumine os seus próprios passos.
            </p>
          </Reveal>
        </div>
      </section>

      {/* ---- FOOTER ---- */}
      <footer style={{ position: 'relative', zIndex: 1, padding: '40px 24px 56px', borderTop: '1px solid var(--c-line)', textAlign: 'center' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 12, marginBottom: 16 }}>
          <span style={{ display: 'flex', width: 36 }}><MarkSmall /></span>
          <span style={{ display: 'flex', flexDirection: 'column', lineHeight: 1, textAlign: 'left' }}>
            <span style={{ fontFamily: "'Chakra Petch', sans-serif", fontSize: 19, fontWeight: 700, letterSpacing: '.14em', color: 'var(--c-violet)' }}>COSBA</span>
            <span style={{ fontSize: '7.5px', fontWeight: 600, letterSpacing: '.32em', color: 'var(--c-orchid)', marginTop: 3 }}>CURA MULTIDIMENSIONAL</span>
          </span>
        </div>
        <p style={{ fontWeight: 300, fontSize: 13, lineHeight: 1.7, color: 'var(--c-dim)', maxWidth: '62ch', margin: '0 auto 14px' }}>
          Terapia complementar de bem-estar e desenvolvimento espiritual. Não substitui acompanhamento médico, psicológico ou psiquiátrico, nem o uso de medicamentos prescritos.
        </p>
        <p style={{ fontSize: 12, color: 'var(--c-dim)', opacity: .7, margin: 0 }}>© Sistema Arcturiano de Cura Multidimensional · Leo Cosba</p>
      </footer>
    </div>
  );
}
