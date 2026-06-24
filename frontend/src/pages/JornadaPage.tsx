import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Wind, ArrowLeft, ArrowRight, Sparkles, 
  ChevronDown, ChevronUp, AlertCircle
} from 'lucide-react';
import { MarkSmall, MarkGlow } from '../components/SacredGeometry';

// Import icons as images
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

const EMO = ['Ansiedade','Tristeza','Cansaço','Irritação','Medo','Confusão','Solidão','Sobrecarga','Esperança','Alegria','Gratidão','Paz'];

const SOMATIC_CHECKIN_OPTIONS = [
  { key: 'mente_acelerada', label: 'Mente Acelerada' },
  { key: 'tensao_ombros', label: 'Tensão nos Ombros' },
  { key: 'aperto_peito', label: 'Aperto no Peito' },
  { key: 'foco_disperso', label: 'Foco Disperso' },
  { key: 'cansaco_fisico', label: 'Cansaço Físico' }
];

const SOMATIC_CHECKOUT_OPTIONS = [
  { key: 'mais_calma', label: 'Mais Calma / Presença' },
  { key: 'ombros_leves', label: 'Ombros Leves' },
  { key: 'peito_livre', label: 'Peito Livre / Leveza' },
  { key: 'foco_alinhado', label: 'Foco Alinhado' },
  { key: 'corpo_relaxado', label: 'Corpo Relaxado' }
];

const QUESTIONS = [
  { type: 'text', key: 'q_chega', label: 'Como você chega para começar este processo?', guide: 'Não pense muito. Repare como estão o seu corpo e o seu ânimo neste exato momento, e descreva em poucas palavras.', placeholder: 'Eu chego...', minLength: 30 },
  { type: 'text', key: 'q_trouxe', label: 'O que te trouxe até aqui, neste momento da sua vida?', guide: 'Fale com as suas palavras, como se contasse para alguém de confiança. Não precisa organizar — só ser verdadeira.', placeholder: 'O que me trouxe...', minLength: 45 },
  { type: 'text', key: 'q_energia', label: 'O que tem pedido mais da sua energia ultimamente?', guide: 'Pessoas, situações, pensamentos. Onde você sente que se esvai sem perceber.', placeholder: 'Tem pedido de mim...', minLength: 30 },
  { type: 'text', key: 'q_repete', label: 'Existe algo que se repete e que você gostaria de entender?', guide: 'Um padrão, uma cena que volta, uma sensação familiar. Se não souber nomear, descreva a sensação.', placeholder: 'O que se repete...', minLength: 40 },
  { type: 'text', key: 'q_corpo', label: 'Como tem sido a sua relação com o corpo, o sono e o descanso?', guide: 'O corpo guarda o que a mente esquece. Repare sem julgar.', placeholder: 'Meu corpo tem...', minLength: 30 },
  { type: 'emo', key: 'f_emocoes', label: 'Quais emoções têm predominado?', guide: 'Respire e sinta antes de escolher. Pode marcar quantas forem verdadeiras para você.' },
  { type: 'text', key: 'q_bem_faz', label: 'O que te faz bem hoje? Onde você sente um pouco de leveza?', guide: 'Tão importante quanto a dor. Procure um lugar de descanso dentro de você.', placeholder: 'Me faz bem...', minLength: 20 },
  { type: 'text', key: 'q_sonhos', label: 'Há sonhos ou imagens que têm voltado?', guide: 'Mesmo fragmentos. O que aparece quando você fecha os olhos antes de dormir.', placeholder: 'Tenho sonhado...', minLength: 20 },
  { type: 'scale', key: 'f_bem', label: 'Como está o seu bem-estar geral agora?', guide: 'De 1 (muito difícil) a 10 (muito leve). Sinta o número, não o calcule.' },
  { type: 'text', key: 'q_intencao', label: 'Se algo pudesse se mover dentro de você neste ciclo, o que seria?', guide: 'Esta é a sua intenção. Escreva como um pedido sincero a si mesma.', placeholder: 'Eu gostaria de...', minLength: 30 },
  { type: 'text', key: 'q_palavra', label: 'Uma palavra, frase ou imagem para carregar com você esta semana.', guide: 'Algo curto que você possa lembrar nos momentos difíceis. Será o seu fio condutor.', placeholder: 'Vou carregar...', minLength: 5 }
];

const CAMADAS_INFO = {
  limpeza: {
    title: 'Limpeza e equilíbrio energético',
    icon: iconeLimpeza,
    somaticTip: 'Beba 2 litros de água por dia. A água mineral ajuda na desintegração linfática das memórias energéticas liberadas.',
    desc: 'Dissolve o acúmulo de frequências de ansiedade, estresse e pensamentos alheios que pairam sobre o seu campo sutil, restaurando a livre circulação de vitalidade nos seus meridianos.',
    reflection: 'Você se abriu de forma honesta no relato. Esta limpeza só consegue se manter estável se você sustentar a auto-observação diária do seu nível de saturação emocional.'
  },
  corte: {
    title: 'Corte de contratos e vínculos',
    icon: iconeCorte,
    somaticTip: 'Alongue o peito e faça expirações sonoras (soltando o ar com som de "Ah") para relaxar o plexo solar.',
    desc: 'Encerra cordões energéticos obsoletos e conexões de co-dependência que sugavam seu vigor pessoal, libertando-a de laços com figuras do passado.',
    reflection: 'O corte foi profundo porque você expôs a verdade da sua dor no relato. Agora, a matéria exige que você diga não no físico quando a antiga dinâmica bater à sua porta.'
  },
  poder: {
    title: 'Resgate do poder pessoal',
    icon: iconePoder,
    somaticTip: 'Pratique exercícios de força física ou calistenia curta ao acordar para ativar seu plexo solar.',
    desc: 'Recolhe fragmentos da sua presença que foram cedidos a outras pessoas ou situações por carência, devolvendo a soberania de decidir por si mesma.',
    reflection: 'Você relatou como vinha se anulando, e o campo agiu para recuperar sua presença. O poder sutil só permanece se você ocupar seu espaço na rotina com ação firme.'
  },
  crianca: {
    title: 'Cura da criança interior',
    icon: iconeCrianca,
    somaticTip: 'Reserve 10 minutos de silêncio absoluto no fim do dia sem telas, respirando suavemente no abdômen.',
    desc: 'Acolhe e re-programa feridas formadas na primeira infância (abandono, rejeição ou cobrança severa) que ativavam reações reativas inconscientes no presente.',
    reflection: 'A sua vulnerabilidade ao descrever sua infância no portal abriu a comporta para que esta camada fosse limpa. Acolha suas falhas com amor esta semana.'
  },
  dna: {
    title: 'Purificação do DNA e ancestralidade',
    icon: iconeDna,
    somaticTip: 'Caminhe descalça na terra ou grama por 10 minutos para descarregar a eletricidade do corpo.',
    desc: 'Desativa padrões de sofrimento repetitivos herdados transgeracionalmente das linhagens materna ou paterna, que rodavam como softwares de autolimitação.',
    reflection: 'Ao reconhecer no relato que carrega cargas idênticas às de seus pais, o sistema liberou o contrato ancestral. O ciclo termina em você.'
  },
  eu: {
    title: 'Reconexão com o Eu Superior',
    icon: iconeEu,
    somaticTip: 'Passe 5 minutos no sol pela manhã e imagine uma luz dourada descendo pelo topo da cabeça.',
    desc: 'Fortalece o canal de recepção intuitiva, sintonizando as suas escolhas diárias ao seu blueprint original (o plano sagrado da sua alma).',
    reflection: 'Sua intenção clara abriu o canal. A voz do Eu Superior fala por meio da sua primeira intuição sem lógica. Não duvide dela.'
  },
  karma: {
    title: 'Cura e liberação kármica',
    icon: iconeKarma,
    somaticTip: 'Escreva um diário curto à noite anotando as situações onde você quase reagiu no piloto automático.',
    desc: 'Desativa gatilhos de reações kármicas repetitivas estruturadas em vidas passadas, cortando loops de destino infelizes.',
    reflection: 'O desabafo profundo que você fez no relato sobre o que sempre se repete na sua vida deu à egrégora a chave exata para quebrar o ciclo kármico.'
  },
  protecao: {
    title: 'Proteção e selagem do campo',
    icon: iconeProtecao,
    somaticTip: 'Ao acordar, sintonize no seu coração e imagine uma barreira de luz dourada se expandindo a 1 metro do corpo.',
    desc: 'Sela as aberturas do seu campo áurico após a cirurgia sutil, impedindo que influências pesadas do ambiente externo voltem a desgastar a sua energia.',
    reflection: 'Sua presença se fortaleceu esta semana. Carregue sua palavra-âncora com convicção e proteja o seu templo.'
  }
};

export function JornadaPage() {
  const [view, setView] = useState('form'); // form | relatorio | fechamento
  const [phase, setPhase] = useState('intro'); // intro | breathwork | q | done
  const [step, setStep] = useState(0);
  const [breathCycle, setBreathCycle] = useState(0);
  const [breathText, setBreathText] = useState('Respire e sintonize');
  const [breathPhase, setBreathPhase] = useState('idle'); // idle | inhale | hold | exhale
  const [validationError, setValidationError] = useState('');
  
  const [somaticCheckin, setSomaticCheckin] = useState<string[]>([]);
  const [somaticCheckout, setSomaticCheckout] = useState<string[]>([]);

  const handleSomaticCheckinToggle = (key: string) => {
    setSomaticCheckin(prev => prev.includes(key) ? prev.filter(x => x !== key) : [...prev, key]);
  };

  const handleSomaticCheckoutToggle = (key: string) => {
    setSomaticCheckout(prev => prev.includes(key) ? prev.filter(x => x !== key) : [...prev, key]);
  };
  
  // Client state
  const [f_nome, setNome] = useState('Mariana');
  const [answers, setAnswers] = useState<Record<string, any>>({
    q_chega: '',
    q_trouxe: '',
    q_energia: '',
    q_repete: '',
    q_corpo: '',
    f_emocoes: [],
    q_bem_faz: '',
    q_sonhos: '',
    f_bem: 5,
    q_intencao: '',
    q_palavra: ''
  });

  // Report state from therapist (persisted mock or localStorage)
  const [r_num, setNum] = useState(2);
  const [r_data, setData] = useState('20 de junho de 2026');
  const [r_ecos, setEcos] = useState('Você chegou cansada e com o peito pesado, e trouxe uma cena antiga: a cobrança em casa, o mesmo padrão que se repete. Ao me sintonizar com o seu campo, senti exatamente esse peso no peito — e o sonho da porta que não se acha fala disso: uma passagem que já existe, mas ainda não se abriu.');
  const [r_sintese, setSintese] = useState('Trabalhei o vínculo de cobrança que te liga à figura materna — um contrato antigo que te fez responsável pela felicidade dos outros desde cedo. Ao afrouxar esse laço, a criança que aprendeu a se anular pôde ser acolhida, e parte do seu poder pessoal, que ficava cedido, começou a voltar para você.');
  const [r_camadas, setCamadas] = useState(['corte', 'crianca', 'poder']);
  const [r_o1, setO1] = useState('Quando a vontade de resolver a vida do outro aparecer, apenas observe — sem agir. Note que ela passa.');
  const [r_o2, setO2] = useState('Se a imagem da cobrança vier com peso, respire e diga em silêncio: "isso é dela, não é meu para carregar".');
  const [r_o3, setO3] = useState('Repare nos momentos em que você diz "sim" sem querer. Não precisa mudar ainda — só perceber.');
  const [r_fechamento, setFechamento] = useState('Você deu um passo corajoso. O que parecia só cansaço era um peso antigo pedindo para ser solto. Vá com leveza — eu sigo ao seu lado.');

  // Active expanded layer info
  const [expandedLayer, setExpandedLayer] = useState<string | null>(null);

  // Load from localStorage on mount
  useEffect(() => {
    try {
      const sub = JSON.parse(localStorage.getItem('sacm_submission') || 'null');
      const rep = JSON.parse(localStorage.getItem('sacm_report') || 'null');
      const viewSaved = localStorage.getItem('sacm_view');
      
      if (sub) {
        if (sub.f_nome) setNome(sub.f_nome);
        setAnswers(prev => ({ ...prev, ...sub }));
        if (sub.somatic_checkin) setSomaticCheckin(sub.somatic_checkin);
        if (sub.somatic_checkout) setSomaticCheckout(sub.somatic_checkout);
      }
      if (rep) {
        if (rep.r_num) setNum(rep.r_num);
        if (rep.r_data) setData(rep.r_data);
        if (rep.r_ecos) setEcos(rep.r_ecos);
        if (rep.r_sintese) setSintese(rep.r_sintese);
        if (rep.r_camadas) setCamadas(rep.r_camadas);
        if (rep.r_o1) setO1(rep.r_o1);
        if (rep.r_o2) setO2(rep.r_o2);
        if (rep.r_o3) setO3(rep.r_o3);
        if (rep.r_fechamento) setFechamento(rep.r_fechamento);
      }
      if (viewSaved && ['form', 'relatorio', 'fechamento'].includes(viewSaved)) {
        setView(viewSaved);
      }
    } catch (e) {
      console.error(e);
    }
  }, []);

  // Listen to changes in localStorage
  useEffect(() => {
    const handleStorageChange = () => {
      try {
        const sub = JSON.parse(localStorage.getItem('sacm_submission') || 'null');
        const rep = JSON.parse(localStorage.getItem('sacm_report') || 'null');
        const viewSaved = localStorage.getItem('sacm_view');
        
        if (sub) {
          if (sub.f_nome) setNome(sub.f_nome);
          setAnswers(prev => ({ ...prev, ...sub }));
          if (sub.somatic_checkin) setSomaticCheckin(sub.somatic_checkin);
          if (sub.somatic_checkout) setSomaticCheckout(sub.somatic_checkout);
        }
        if (rep) {
          if (rep.r_num) setNum(rep.r_num);
          if (rep.r_data) setData(rep.r_data);
          if (rep.r_ecos) setEcos(rep.r_ecos);
          if (rep.r_sintese) setSintese(rep.r_sintese);
          if (rep.r_camadas) setCamadas(rep.r_camadas);
          if (rep.r_o1) setO1(rep.r_o1);
          if (rep.r_o2) setO2(rep.r_o2);
          if (rep.r_o3) setO3(rep.r_o3);
          if (rep.r_fechamento) setFechamento(rep.r_fechamento);
        }
        if (viewSaved && ['form', 'relatorio', 'fechamento'].includes(viewSaved)) {
          setView(viewSaved);
        }
      } catch (e) {}
    };

    window.addEventListener('storage', handleStorageChange);
    // Polling as fallback for single-page changes in the same tab
    const interval = setInterval(handleStorageChange, 1000);

    return () => {
      window.removeEventListener('storage', handleStorageChange);
      clearInterval(interval);
    };
  }, []);

  const changeView = (v: string) => {
    setView(v);
    localStorage.setItem('sacm_view', v);
  };

  const saveSubmission = (newAnswers: typeof answers) => {
    try {
      localStorage.setItem('sacm_submission', JSON.stringify({ 
        f_nome, 
        somatic_checkin: somaticCheckin,
        somatic_checkout: somaticCheckout,
        ...newAnswers 
      }));
    } catch (e) {}
  };

  // Breathwork loop
  useEffect(() => {
    if (phase !== 'breathwork') return;

    let timer: any;
    const runCycle = (cycle: number) => {
      if (cycle >= 3) {
        setPhase('somatic_checkout');
        return;
      }

      setBreathCycle(cycle + 1);
      
      // Inhale
      setBreathPhase('inhale');
      setBreathText('Inale o ar... sinta o sopro do Vento Branco');
      timer = setTimeout(() => {
        // Hold
        setBreathPhase('hold');
        setBreathText('Retenha e sinta a presença no coração');
        timer = setTimeout(() => {
          // Exhale
          setBreathPhase('exhale');
          setBreathText('Expire todo o peso e solte as amarras');
          timer = setTimeout(() => {
            runCycle(cycle + 1);
          }, 4000);
        }, 4000);
      }, 4000);
    };

    runCycle(0);

    return () => clearTimeout(timer);
  }, [phase]);

  const handleNext = () => {
    const q = QUESTIONS[step];
    const value = answers[q.key];

    // Clear error
    setValidationError('');

    // Strict Validation for "Desabafo Real"
    if (q.type === 'text') {
      const minLen = q.minLength || 10;
      if (!value || value.trim().length < minLen) {
        setValidationError(
          `O pacto exige a sua verdade. Este campo pede uma resposta mais profunda (mínimo de ${minLen} caracteres) para co-criarmos a mudança. Por favor, reveja e se aprofunde.`
        );
        return;
      }
    }

    if (step < QUESTIONS.length - 1) {
      setStep(step + 1);
    } else {
      // Done! Save and submit
      saveSubmission(answers);
      setPhase('done');
    }
  };

  const handleBack = () => {
    setValidationError('');
    if (step > 0) {
      setStep(step - 1);
    } else {
      setPhase('intro');
    }
  };

  const handleEmoToggle = (emo: string) => {
    const prev = answers.f_emocoes || [];
    const has = prev.includes(emo);
    const updated = has ? prev.filter((x: string) => x !== emo) : [...prev, emo];
    const newAnswers = { ...answers, f_emocoes: updated };
    setAnswers(newAnswers);
    saveSubmission(newAnswers);
  };

  const handleScaleSelect = (val: number) => {
    const newAnswers = { ...answers, f_bem: val };
    setAnswers(newAnswers);
    saveSubmission(newAnswers);
  };

  const handleTextChange = (key: string, val: string) => {
    const newAnswers = { ...answers, [key]: val };
    setAnswers(newAnswers);
    saveSubmission(newAnswers);
  };

  const curQ = QUESTIONS[step];

  return (
    <div className="min-h-screen text-[var(--c-text)] pb-24">
      {/* HEADER NAV */}
      <header className="sticky top-0 z-50 bg-[var(--c-bg0)]/80 backdrop-blur-md border-b border-[var(--c-line)] py-3 px-4 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <MarkSmall />
          <span className="font-mono text-xs uppercase tracking-widest text-[var(--c-gold-soft)]">Cura Cósmica</span>
        </div>
        <div className="flex bg-slate-950/60 p-1 rounded-full border border-[var(--c-line)] gap-1">
          <button 
            onClick={() => changeView('form')}
            className={`px-3 py-1.5 rounded-full text-xs font-semibold tracking-wide transition-all ${
              view === 'form' ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a]' : 'text-[var(--c-dim)] hover:text-[var(--c-text)]'
            }`}
          >
            1. Relato
          </button>
          <button 
            onClick={() => changeView('relatorio')}
            className={`px-3 py-1.5 rounded-full text-xs font-semibold tracking-wide transition-all ${
              view === 'relatorio' ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a]' : 'text-[var(--c-dim)] hover:text-[var(--c-text)]'
            }`}
          >
            2. Devolutiva
          </button>
          <button 
            onClick={() => changeView('fechamento')}
            className={`px-3 py-1.5 rounded-full text-xs font-semibold tracking-wide transition-all ${
              view === 'fechamento' ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a]' : 'text-[var(--c-dim)] hover:text-[var(--c-text)]'
            }`}
          >
            3. Fechamento
          </button>
        </div>
      </header>

      {/* TELA 1 — FORMULÁRIO MEDITATIVO */}
      {view === 'form' && (
        <div className="max-w-xl mx-auto px-6 pt-12 flex flex-col justify-center min-h-[calc(100vh-140px)]">
          <AnimatePresence mode="wait">
            {phase === 'intro' && (
              <motion.div 
                key="intro"
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -15 }}
                className="text-center"
              >
                <div className="flex justify-center mb-6 animate-pulse">
                  <MarkGlow />
                </div>
                <p className="text-[var(--c-gold)] text-xs uppercase tracking-widest font-semibold mb-2">Início da sua jornada</p>
                <h1 className="font-serif text-3xl sm:text-4xl font-normal leading-tight mb-4">
                  O desabafo cura. <br /><span className="text-[var(--c-gold-soft)] font-sans font-medium">Mas antes, respire.</span>
                </h1>
                <p className="text-[var(--c-dim)] text-sm leading-relaxed mb-6 font-light max-w-md mx-auto">
                  Este é o seu portal de acompanhamento semanal. O quanto você se abre e conta o que quer tratar dita a profundidade do envio energético.
                </p>
                
                <div className="max-w-xs mx-auto mb-8">
                  <label className="block text-xs font-semibold text-[var(--c-gold-soft)] mb-2 uppercase tracking-wide">Como prefere ser chamado?</label>
                  <input 
                    type="text" 
                    value={f_nome}
                    onChange={(e) => setNome(e.target.value)}
                    className="w-full text-center py-3 px-4 rounded-xl border border-[var(--c-line)] bg-slate-950/40 focus:border-[var(--c-gold)] focus:outline-none transition-all text-sm font-semibold tracking-wide"
                    placeholder="Seu nome"
                  />
                </div>

                <button 
                  onClick={() => setPhase('somatic_checkin')}
                  className="w-full max-w-xs py-4 rounded-full bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] font-bold text-sm uppercase tracking-wider shadow-lg shadow-yellow-500/20 hover:scale-[1.02] transition-all"
                >
                  Entrar em sintonia
                </button>
              </motion.div>
            )}

            {phase === 'somatic_checkin' && (
              <motion.div 
                key="somatic_checkin"
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -15 }}
                className="text-center w-full"
              >
                <div className="flex justify-center mb-6">
                  <Wind className="w-12 h-12 text-[var(--c-gold)] animate-pulse" />
                </div>
                <p className="text-[var(--c-gold)] text-xs uppercase tracking-widest font-semibold mb-2">Check-in Somático</p>
                <h2 className="font-serif text-2xl font-light leading-snug mb-4 text-[var(--c-text)]">
                  Como está o seu corpo antes de respirar?
                </h2>
                <p className="text-[var(--c-dim)] text-xs leading-relaxed mb-6 font-light max-w-sm mx-auto">
                  Selecione os marcadores físicos e de energia que você sente presentes neste momento. Isso guiará o direcionamento do tratamento.
                </p>

                <div className="flex flex-wrap gap-2.5 justify-center mb-8 max-w-md mx-auto">
                  {SOMATIC_CHECKIN_OPTIONS.map((opt) => {
                    const isSel = somaticCheckin.includes(opt.key);
                    return (
                      <button
                        key={opt.key}
                        onClick={() => handleSomaticCheckinToggle(opt.key)}
                        className={`px-4 py-2.5 rounded-xl text-xs font-medium border transition-all ${
                          isSel 
                            ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] border-transparent text-[#24160a] font-bold shadow-md shadow-yellow-500/10' 
                            : 'bg-slate-950/30 border-[var(--c-line)] text-[var(--c-text)] hover:border-[var(--c-gold-soft)]'
                        }`}
                      >
                        {opt.label}
                      </button>
                    );
                  })}
                </div>

                <div className="flex gap-4 max-w-xs mx-auto">
                  <button 
                    onClick={() => setPhase('intro')}
                    className="flex-1 py-3.5 rounded-full border border-[var(--c-line)] text-[var(--c-dim)] font-semibold text-xs uppercase tracking-wider hover:text-[var(--c-text)] transition-all"
                  >
                    Voltar
                  </button>
                  <button 
                    onClick={() => setPhase('breathwork')}
                    className="flex-1 py-3.5 rounded-full bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] font-bold text-xs uppercase tracking-wider hover:scale-[1.02] transition-all"
                  >
                    Respirar
                  </button>
                </div>
              </motion.div>
            )}

            {phase === 'somatic_checkout' && (
              <motion.div 
                key="somatic_checkout"
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -15 }}
                className="text-center w-full"
              >
                <div className="flex justify-center mb-6">
                  <Sparkles className="w-12 h-12 text-[var(--c-gold)]" />
                </div>
                <p className="text-[var(--c-gold)] text-xs uppercase tracking-widest font-semibold mb-2">Check-out Somático</p>
                <h2 className="font-serif text-2xl font-light leading-snug mb-4 text-[var(--c-text)]">
                  Como você se sente após o Breathwork?
                </h2>
                <p className="text-[var(--c-dim)] text-xs leading-relaxed mb-6 font-light max-w-sm mx-auto">
                  Sinta os efeitos da respiração e marque quais melhorias ou estados de presença se instalaram no seu corpo físico.
                </p>

                <div className="flex flex-wrap gap-2.5 justify-center mb-8 max-w-md mx-auto">
                  {SOMATIC_CHECKOUT_OPTIONS.map((opt) => {
                    const isSel = somaticCheckout.includes(opt.key);
                    return (
                      <button
                        key={opt.key}
                        onClick={() => handleSomaticCheckoutToggle(opt.key)}
                        className={`px-4 py-2.5 rounded-xl text-xs font-medium border transition-all ${
                          isSel 
                            ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] border-transparent text-[#24160a] font-bold shadow-md shadow-yellow-500/10' 
                            : 'bg-slate-950/30 border-[var(--c-line)] text-[var(--c-text)] hover:border-[var(--c-gold-soft)]'
                        }`}
                      >
                        {opt.label}
                      </button>
                    );
                  })}
                </div>

                <div className="flex gap-4 max-w-xs mx-auto">
                  <button 
                    onClick={() => setPhase('breathwork')}
                    className="flex-1 py-3.5 rounded-full border border-[var(--c-line)] text-[var(--c-dim)] font-semibold text-xs uppercase tracking-wider hover:text-[var(--c-text)] transition-all"
                  >
                    Repetir
                  </button>
                  <button 
                    onClick={() => {
                      setPhase('q');
                      setStep(0);
                    }}
                    className="flex-1 py-3.5 rounded-full bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] font-bold text-xs uppercase tracking-wider hover:scale-[1.02] transition-all"
                  >
                    Iniciar Relato
                  </button>
                </div>
              </motion.div>
            )}

            {phase === 'breathwork' && (
              <motion.div 
                key="breath"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="text-center flex flex-col items-center justify-center py-12"
              >
                <div className="mb-8">
                  <p className="text-[var(--c-gold)] text-xs uppercase tracking-widest font-semibold mb-1">Guia Vento Branco</p>
                  <h3 className="text-xl font-medium tracking-wide text-[var(--c-text)]">Sintonização {breathCycle}/3</h3>
                </div>

                {/* Animated breathing circle */}
                <div className="relative w-56 h-56 flex items-center justify-center mb-8">
                  <motion.div 
                    animate={{
                      scale: breathPhase === 'inhale' ? 1.6 : breathPhase === 'hold' ? 1.6 : 1.0,
                      opacity: breathPhase === 'inhale' ? 0.75 : breathPhase === 'hold' ? 1.0 : 0.25,
                    }}
                    transition={{ duration: 4.0, ease: "easeInOut" }}
                    className="absolute inset-0 rounded-full bg-indigo-500/10 border-2 border-[var(--c-violet)] shadow-[0_0_40px_rgba(99,102,241,0.2)]"
                  />
                  <motion.div 
                    animate={{
                      scale: breathPhase === 'inhale' ? 1.3 : breathPhase === 'hold' ? 1.3 : 1.0,
                    }}
                    transition={{ duration: 4.0, ease: "easeInOut" }}
                    className="absolute w-36 h-36 rounded-full bg-purple-900/30 border border-[var(--c-orchid)] flex items-center justify-center"
                  >
                    <Wind className="w-8 h-8 text-[var(--c-gold)] animate-pulse" />
                  </motion.div>
                </div>

                <p className="text-lg font-light text-[var(--c-gold-soft)] max-w-sm h-12 leading-relaxed transition-all">
                  {breathText}
                </p>
              </motion.div>
            )}

            {phase === 'q' && curQ && (
              <motion.div 
                key={step}
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -20 }}
                transition={{ duration: 0.3 }}
                className="w-full"
              >
                {/* Progress bar */}
                <div className="flex gap-1.5 mb-8 justify-center items-center">
                  {QUESTIONS.map((_, i) => (
                    <span 
                      key={i} 
                      className={`h-1.5 rounded-full transition-all duration-300 ${
                        i === step 
                          ? 'w-6 bg-[var(--c-gold-soft)]' 
                          : i < step 
                          ? 'w-2 bg-[var(--c-gold)]' 
                          : 'w-2 bg-[var(--c-line)]'
                      }`}
                    />
                  ))}
                </div>

                <div className="text-center mb-8">
                  <p className="text-[var(--c-orchid)] text-[10px] uppercase font-bold tracking-widest mb-1">
                    Pergunta {step + 1} de {QUESTIONS.length}
                  </p>
                  <h2 className="text-2xl font-serif font-light leading-snug mb-3 text-[var(--c-text)]">
                    {curQ.label}
                  </h2>
                  <p className="text-[var(--c-dim)] text-xs font-light italic max-w-md mx-auto leading-relaxed">
                    {curQ.guide}
                  </p>
                </div>

                {/* Question Inputs */}
                <div className="mb-8">
                  {curQ.type === 'text' && (
                    <textarea 
                      value={answers[curQ.key] || ''}
                      onChange={(e) => handleTextChange(curQ.key, e.target.value)}
                      placeholder={curQ.placeholder}
                      rows={5}
                      className="w-full p-4 rounded-2xl border border-[var(--c-line)] bg-slate-950/40 text-sm leading-relaxed text-[var(--c-text)] focus:border-[var(--c-gold)] focus:outline-none focus:ring-1 focus:ring-[var(--c-gold)] transition-all resize-none font-light"
                    />
                  )}

                  {curQ.type === 'emo' && (
                    <div className="flex flex-wrap gap-2.5 justify-center">
                      {EMO.map((emo) => {
                        const isSel = (answers.f_emocoes || []).includes(emo);
                        return (
                          <button
                            key={emo}
                            onClick={() => handleEmoToggle(emo)}
                            className={`px-4 py-2 rounded-full text-xs font-medium border transition-all ${
                              isSel 
                                ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] border-transparent text-[#24160a] font-bold shadow-md shadow-yellow-500/10' 
                                : 'bg-slate-950/30 border-[var(--c-line)] text-[var(--c-text)] hover:border-[var(--c-gold-soft)]'
                            }`}
                          >
                            {emo}
                          </button>
                        );
                      })}
                    </div>
                  )}

                  {curQ.type === 'scale' && (
                    <div className="flex flex-wrap gap-2 justify-center max-w-md mx-auto">
                      {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((num) => {
                        const isSel = answers.f_bem === num;
                        return (
                          <button
                            key={num}
                            onClick={() => handleScaleSelect(num)}
                            className={`w-10 h-10 rounded-xl font-mono text-sm font-bold border transition-all ${
                              isSel 
                                ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] border-transparent text-[#24160a]' 
                                : 'bg-slate-950/30 border-[var(--c-line)] text-[var(--c-dim)] hover:border-[var(--c-gold-soft)]'
                            }`}
                          >
                            {num}
                          </button>
                        );
                      })}
                    </div>
                  )}
                </div>

                {/* Validation Error Alert */}
                {validationError && (
                  <motion.div 
                    initial={{ opacity: 0, y: 5 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="mb-6 p-4 rounded-xl border border-red-500/20 bg-red-950/20 text-red-400 text-xs flex gap-3 items-start leading-relaxed text-left"
                  >
                    <AlertCircle className="w-4 h-4 mt-0.5 flex-none" />
                    <div>{validationError}</div>
                  </motion.div>
                )}

                {/* Nav buttons */}
                <div className="flex items-center justify-between gap-6 pt-4 border-t border-[var(--c-line)]">
                  <button 
                    onClick={handleBack}
                    className="flex items-center gap-2 text-xs font-semibold text-[var(--c-dim)] hover:text-[var(--c-text)] transition-colors"
                  >
                    <ArrowLeft className="w-3.5 h-3.5" /> Voltar
                  </button>
                  <button 
                    onClick={handleNext}
                    className="py-3 px-8 rounded-full bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] font-bold text-xs uppercase tracking-wider hover:scale-[1.01] transition-all flex items-center gap-1.5 shadow-md shadow-yellow-500/10"
                  >
                    {step === QUESTIONS.length - 1 ? 'Concluir' : 'Continuar'} <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </motion.div>
            )}

            {phase === 'done' && (
              <motion.div 
                key="done"
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-center"
              >
                <div className="flex justify-center mb-6 animate-pulse">
                  <MarkGlow />
                </div>
                <p className="text-[var(--c-gold)] text-xs uppercase tracking-widest font-semibold mb-2">Relato Concluído ✦</p>
                <h1 className="font-serif text-3xl font-normal leading-tight mb-4">
                  Obrigado por se abrir
                </h1>
                <p className="text-[var(--c-dim)] text-sm leading-relaxed mb-6 font-light max-w-md mx-auto">
                  Suas palavras já chegaram ao Leo. Ele se sintonizará com você na quarta-feira e enviará a devolutiva com o laudo de alinhamento na quinta. Até lá, guarde a sua frase-âncora:
                </p>
                
                {answers.q_palavra && (
                  <div className="inline-block px-8 py-5 border border-[var(--c-line)] bg-yellow-500/5 rounded-2xl mb-8">
                    <p className="font-serif italic text-lg text-[var(--c-gold-soft)] font-light">
                      "{answers.q_palavra}"
                    </p>
                  </div>
                )}

                <div className="flex flex-col gap-3 max-w-xs mx-auto">
                  <button 
                    onClick={() => changeView('relatorio')}
                    className="py-4 rounded-full bg-slate-900 border border-[var(--c-line)] text-[var(--c-gold-soft)] font-bold text-xs uppercase tracking-wider hover:bg-slate-800 transition-all"
                  >
                    Ir para Devolutiva (Dia Seguinte)
                  </button>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      )}

      {/* TELA 2 — DEVOLUTIVA COM CLIPE EXPANSÍVEL */}
      {view === 'relatorio' && (
        <div className="max-w-md mx-auto px-4 pt-10">
          <div className="border border-[var(--c-line)] rounded-3xl overflow-hidden bg-gradient-to-b from-[var(--c-bg2)]/30 to-[var(--c-bg0)]/60 shadow-2xl relative">
            <div className="absolute inset-x-0 top-0 h-40 bg-gradient-to-b from-indigo-500/10 to-transparent pointer-events-none" />
            
            {/* Header Devolutiva */}
            <div className="relative text-center pt-10 pb-6 px-6 border-b border-[var(--c-line)]">
              <div className="flex justify-center mb-4">
                <MarkSmall />
              </div>
              <p className="text-[var(--c-gold)] text-[10px] uppercase font-bold tracking-widest mb-1">Sua sessão esta semana</p>
              <h2 className="font-serif text-2xl text-[var(--c-text)] font-light mb-4">{f_nome}</h2>
              
              <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border border-[var(--c-line)] bg-slate-950/40 text-xs">
                <span className="text-[var(--c-dim)] uppercase tracking-wider font-semibold text-[9px]">Sessão {r_num} de 5</span>
                <span className="w-1.5 h-1.5 rounded-full bg-green-500" />
                <span className="text-[var(--c-dim)]">{r_data}</span>
              </div>
            </div>

            <div className="p-6 sm:p-8 space-y-8">
              {/* Ecos */}
              <div>
                <p className="text-[var(--c-gold)] text-[10px] uppercase font-bold tracking-widest mb-3">Ecos da sua semana</p>
                <p className="text-[var(--c-text)] text-sm font-light leading-relaxed">{r_ecos}</p>
              </div>

              {/* Síntese */}
              <div>
                <p className="text-[var(--c-gold)] text-[10px] uppercase font-bold tracking-widest mb-3">O que foi tratado</p>
                <p className="text-[var(--c-dim)] text-xs font-light leading-relaxed mb-4">{r_sintese}</p>
                
                {/* Camadas chips clicáveis */}
                <div className="flex flex-col gap-2 mt-4">
                  {r_camadas.map((key) => {
                    const info = CAMADAS_INFO[key as keyof typeof CAMADAS_INFO];
                    if (!info) return null;
                    const isExpanded = expandedLayer === key;
                    
                    return (
                      <div key={key} className="border border-[var(--c-line)] rounded-xl overflow-hidden bg-slate-900/40 transition-all">
                        <button 
                          onClick={() => setExpandedLayer(isExpanded ? null : key)}
                          className="w-full flex items-center justify-between p-3.5 text-left hover:bg-slate-800/40 transition-colors"
                        >
                          <div className="flex items-center gap-3">
                            <img src={info.icon} className="w-6 h-6 flex-none" alt="" />
                            <span className="text-xs font-semibold text-[var(--c-gold-soft)]">{info.title}</span>
                          </div>
                          {isExpanded ? <ChevronUp className="w-4 h-4 text-[var(--c-dim)]" /> : <ChevronDown className="w-4 h-4 text-[var(--c-dim)]" />}
                        </button>

                        <AnimatePresence>
                          {isExpanded && (
                            <motion.div 
                              initial={{ height: 0, opacity: 0 }}
                              animate={{ height: "auto", opacity: 1 }}
                              exit={{ height: 0, opacity: 0 }}
                              className="overflow-hidden"
                            >
                              <div className="p-4 bg-slate-950/30 border-t border-[var(--c-line)] space-y-3.5">
                                <p className="text-xs text-[var(--c-text)] font-light leading-relaxed">
                                  {info.desc}
                                </p>
                                <div className="p-3 rounded-lg bg-yellow-500/5 border border-yellow-500/10 text-xs space-y-1">
                                  <span className="text-[var(--c-gold)] font-bold text-[9px] uppercase tracking-wider block">Ancoragem Somática:</span>
                                  <p className="text-[var(--c-gold-soft)] font-light leading-relaxed">{info.somaticTip}</p>
                                </div>
                                <div className="p-3 rounded-lg bg-indigo-950/20 border border-indigo-500/10 text-xs">
                                  <span className="text-[var(--c-orchid)] font-bold text-[9px] uppercase tracking-wider block mb-1">O Pacto da Presença:</span>
                                  <p className="text-[var(--c-dim)] italic font-light leading-relaxed">
                                    "{info.reflection}"
                                  </p>
                                </div>
                              </div>
                            </motion.div>
                          )}
                        </AnimatePresence>
                      </div>
                    );
                  })}
                </div>
              </div>

              {/* Próximos passos */}
              <div className="border-t border-[var(--c-line)] pt-6">
                <p className="text-[var(--c-gold)] text-[10px] uppercase font-bold tracking-widest mb-4">Seus Próximos Passos</p>
                <div className="space-y-4">
                  {[r_o1, r_o2, r_o3].filter(x => x && x.trim()).map((text, i) => (
                    <div key={i} className="flex gap-3 items-start">
                      <span className="w-5 h-5 mt-0.5 rounded-full flex items-center justify-center border border-[var(--c-line)] bg-slate-950/40 text-[10px] font-mono font-bold text-[var(--c-gold)]">
                        {i + 1}
                      </span>
                      <p className="text-xs text-[var(--c-text)] leading-relaxed font-light">{text}</p>
                    </div>
                  ))}
                </div>
              </div>

              {/* Mensagem de encerramento */}
              <div className="text-center pt-6 border-t border-[var(--c-line)] space-y-3">
                <p className="text-xs font-light italic leading-relaxed text-[var(--c-dim)]">
                  "{r_fechamento}"
                </p>
                <p className="text-[10px] tracking-widest uppercase font-semibold text-[var(--c-gold)]">Leo Cosba</p>
              </div>

            </div>
          </div>
        </div>
      )}

      {/* TELA 3 — CHECKPOINT DE FECHAMENTO */}
      {view === 'fechamento' && (
        <div className="max-w-2xl mx-auto px-4 pt-10">
          <div className="border border-[var(--c-line)] rounded-3xl overflow-hidden bg-gradient-to-b from-[var(--c-bg2)]/30 to-[var(--c-bg0)]/60 shadow-2xl relative p-6 sm:p-10">
            <div className="absolute inset-x-0 top-0 h-56 bg-gradient-to-b from-purple-500/10 to-transparent pointer-events-none" />

            <div className="text-center pb-8 border-b border-[var(--c-line)] relative">
              <div className="flex justify-center mb-6">
                <MarkGlow />
              </div>
              <p className="text-[var(--c-gold)] text-[10px] uppercase font-bold tracking-widest mb-1">Checkpoint de Vida</p>
              <h1 className="font-serif text-3xl font-light text-[var(--c-text)] mb-3">A jornada de {f_nome}</h1>
              <p className="text-xs text-[var(--c-dim)] font-light">Ciclo Completo de 5 semanas · Análise & Reprogramação</p>
            </div>

            <div className="py-8 space-y-10">
              {/* De/Para */}
              <div className="space-y-4">
                <p className="text-[var(--c-gold)] text-[10px] uppercase font-bold tracking-widest">De onde você partiu para onde chegou</p>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-5 rounded-2xl border border-[var(--c-line)] bg-slate-950/20">
                    <span className="text-[9px] uppercase tracking-wider font-bold text-[var(--c-violet)] block mb-1">Sua Intenção</span>
                    <p className="text-sm font-serif italic font-light text-[var(--c-gold-soft)]">
                      "{answers.q_intencao || 'Quero parar de me sentir responsável pela felicidade de todo mundo.'}"
                    </p>
                  </div>
                  <div className="p-5 rounded-2xl border border-[var(--c-line)] bg-indigo-950/20">
                    <span className="text-[9px] uppercase tracking-wider font-bold text-[var(--c-orchid)] block mb-1">Onde Você Chegou</span>
                    <p className="text-xs font-light text-[var(--c-text)] leading-relaxed">
                      Você aprendeu a dar a pausa entre a reação automática e a escolha consciente. O peso no peito deu lugar a uma respiração mais larga, firmando seu próprio espaço e presença na sua vida.
                    </p>
                  </div>
                </div>
              </div>

              {/* As 3 áreas da vida */}
              <div className="space-y-4">
                <p className="text-[var(--c-gold)] text-[10px] uppercase font-bold tracking-widest">Evolução por área de vida</p>
                <div className="space-y-3">
                  {[
                    { title: 'Relações', icon: iconeRelacoes, before: 'Dificuldade de impor limites; sensação de se anular.', after: 'Se posiciona sem culpa. Vínculos que drenavam perderam força.', beforeVal: 3, afterVal: 8 },
                    { title: 'Saúde e Vitalidade', icon: iconeSaude, before: 'Cansaço constante e ansiedade de fundo.', after: 'Mais disposição, sono reparador. Energia circulando de novo.', beforeVal: 4, afterVal: 9 },
                    { title: 'Prosperidade', icon: iconeProsperidade, before: 'Trava de merecimento herdada de ancestrais.', after: 'Abertura para o fluxo, agarrando oportunidades físicas.', beforeVal: 2, afterVal: 7 }
                  ].map((area, i) => (
                    <div key={i} className="p-4 rounded-xl border border-[var(--c-line)] bg-slate-900/30 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                      <div className="flex items-center gap-3">
                        <img src={area.icon} className="w-8 h-8 flex-none" alt="" />
                        <div>
                          <h4 className="text-xs font-semibold text-[var(--c-text)]">{area.title}</h4>
                          <div className="flex items-center gap-2 mt-0.5 text-[10px] font-light">
                            <span className="text-red-400">Antes: {area.beforeVal}</span>
                            <span className="text-[var(--c-dim)]">→</span>
                            <span className="text-green-400 font-bold">Agora: {area.afterVal}</span>
                          </div>
                        </div>
                      </div>
                      <div className="space-y-1 max-w-md">
                        <p className="text-[10px] text-[var(--c-dim)] font-light leading-relaxed"><span className="text-[9px] font-bold text-[var(--c-violet)] uppercase">Antes:</span> {area.before}</p>
                        <p className="text-[10px] text-[var(--c-text)] font-light leading-relaxed"><span className="text-[9px] font-bold text-[var(--c-gold)] uppercase">Agora:</span> {area.after}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Práticas de sustentação */}
              <div className="p-6 rounded-2xl border border-yellow-500/20 bg-yellow-500/5 space-y-4">
                <p className="text-[var(--c-gold)] text-[10px] uppercase font-bold tracking-widest flex items-center gap-1.5">
                  <Sparkles className="w-3.5 h-3.5" /> Práticas para sustentar a realidade co-criada
                </p>
                <div className="flex flex-wrap gap-2">
                  {[
                    'Breathwork consciente ao acordar',
                    'Dizer Não sem se justificar',
                    'Registrar 1 sincronicidade por dia',
                    'Meditação curta antes de dormir'
                  ].map((pratica, i) => (
                    <span key={i} className="px-3.5 py-2 border border-[var(--c-line)] rounded-full text-xs font-light text-[var(--c-gold-soft)] bg-slate-950/40">
                      {pratica}
                    </span>
                  ))}
                </div>
              </div>

              {/* Mensagem integradora */}
              <div className="text-center pt-8 border-t border-[var(--c-line)] space-y-3 max-w-md mx-auto">
                <p className="text-sm font-light text-[var(--c-text)] leading-relaxed">
                  "Cuidar dos outros nunca foi o problema — esquecer de si era. Você não precisa escolher entre amar e se preservar. Que você leve daqui a certeza de que também merece o cuidado que oferece."
                </p>
                <p className="text-[10px] tracking-widest uppercase font-semibold text-[var(--c-gold-soft)] pt-2">Leo Cosba · Terapeuta Multidimensional</p>
              </div>

            </div>
          </div>
        </div>
      )}
    </div>
  );
}
