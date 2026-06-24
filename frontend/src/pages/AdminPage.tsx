import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate, Link } from 'react-router-dom';
import { 
  Download, FileText, Activity, Sparkles, ClipboardCheck, 
  Mic, Square, Trash2, Send, Brain, Compass, ShieldCheck, Volume2, ArrowUpRight,
  Wind
} from 'lucide-react';

const SOMATIC_LABELS: Record<string, string> = {
  mente_acelerada: 'Mente Acelerada',
  tensao_ombros: 'Tensão nos Ombros',
  aperto_peito: 'Aperto no Peito',
  foco_disperso: 'Foco Disperso',
  cansaco_fisico: 'Cansaço Físico',
  mais_calma: 'Mais Calma / Presença',
  ombros_leves: 'Ombros Leves',
  peito_livre: 'Peito Livre / Leveza',
  foco_alinhado: 'Foco Alinhado',
  corpo_relaxado: 'Corpo Relaxado'
};

// Import icons as images
import iconeLimpeza from '../assets/icone-limpeza.svg';
import iconeCorte from '../assets/icone-corte.svg';
import iconePoder from '../assets/icone-poder.svg';
import iconeCrianca from '../assets/icone-crianca.svg';
import iconeDna from '../assets/icone-dna.svg';
import iconeEu from '../assets/icone-eu.svg';
import iconeKarma from '../assets/icone-karma.svg';
import iconeProtecao from '../assets/icone-protecao.svg';

const CAMADAS_CHIPS = [
  { key: 'limpeza', title: 'Limpeza energética', icon: iconeLimpeza },
  { key: 'corte', title: 'Corte de vínculos', icon: iconeCorte },
  { key: 'poder', title: 'Resgate de poder', icon: iconePoder },
  { key: 'crianca', title: 'Criança interior', icon: iconeCrianca },
  { key: 'dna', title: 'DNA / Ancestralidade', icon: iconeDna },
  { key: 'eu', title: 'Reconexão Eu Superior', icon: iconeEu },
  { key: 'karma', title: 'Liberação kármica', icon: iconeKarma },
  { key: 'protecao', title: 'Proteção / Selagem', icon: iconeProtecao }
];

const PREV_SUBMISSIONS = {
  q_energia: 'A correria do trabalho e pouco tempo para mim.',
  q_repete: 'Me cobro demais por tudo.',
  q_corpo: 'Dormindo mal, muito cansaço.'
};

export function AdminPage() {
  const navigate = useNavigate();
  // Navigation Tabs state
  const [activeTab, setActiveTab] = useState<'clinico' | 'alta' | 'micelio'>('clinico');
  const [toast, setToast] = useState<string | null>(null);

  // ==========================================
  // IA CO-PILOT / RECALIBRATOR STATES
  // ==========================================
  const [weeklyRecalibInput, setWeeklyRecalibInput] = useState('');
  const [weeklyRecalibMessages, setWeeklyRecalibMessages] = useState<Array<{ sender: 'leo' | 'antigravity'; text: string; hasSuggestion?: boolean }>>([
    { sender: 'antigravity', text: 'Olá Léo. Digite aqui como deseja calibrar a devolutiva semanal de Mariana (ex: "adicione Reich", "mude o tom para poético", etc.). Eu farei os ajustes e você poderá aplicar direto no formulário.' }
  ]);
  const [weeklyRecalibLoading, setWeeklyRecalibLoading] = useState(false);
  const [weeklySuggestedAjustes, setWeeklySuggestedAjustes] = useState<any>(null);

  const [dossierRecalibInput, setDossierRecalibInput] = useState('');
  const [dossierRecalibMessages, setDossierRecalibMessages] = useState<Array<{ sender: 'leo' | 'antigravity'; text: string; hasSuggestion?: boolean }>>([
    { sender: 'antigravity', text: 'Salve Léo. Digite como recalibrar os tópicos do Dossiê Final (ex: "aprofunde Jung e a Lua em Câncer", "coloque mais práticas no manual de autonomia"). Eu ajustarei e você poderá aplicar.' }
  ]);
  const [dossierRecalibLoading, setDossierRecalibLoading] = useState(false);
  const [dossierSuggestedAjustes, setDossierSuggestedAjustes] = useState<any>(null);

  // ==========================================
  // CÉREBRO DO MICÉLIO (AUTO-APRIMORAMENTO) STATES
  // ==========================================
  const [memories, setMemories] = useState<Array<{ type: string; title: string; date: string; content: string }>>([]);
  const [egregoraProtocol, setEgregoraProtocol] = useState<string>('');
  const [isEvolving, setIsEvolving] = useState(false);


  // Global keydown shortcut: Alt + I to go to insights
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.altKey && e.key.toLowerCase() === 'i') {
        e.preventDefault();
        navigate('/insights');
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [navigate]);

  // Load client submission and somatic states from localStorage on mount and listen to changes
  useEffect(() => {
    const loadSubmission = () => {
      try {
        const sub = JSON.parse(localStorage.getItem('sacm_submission') || 'null');
        if (sub) {
          if (sub.f_nome) setNome(sub.f_nome);
          setAnswers(prev => ({
            ...prev,
            q_chega: sub.q_chega || prev.q_chega,
            q_trouxe: sub.q_trouxe || prev.q_trouxe,
            q_energia: sub.q_energia || prev.q_energia,
            q_repete: sub.q_repete || prev.q_repete,
            q_corpo: sub.q_corpo || prev.q_corpo,
            f_emocoes: sub.f_emocoes || prev.f_emocoes,
            q_bem_faz: sub.q_bem_faz || prev.q_bem_faz,
            q_sonhos: sub.q_sonhos || prev.q_sonhos,
            f_bem: sub.f_bem || prev.f_bem,
            q_intencao: sub.q_intencao || prev.q_intencao,
            q_palavra: sub.q_palavra || prev.q_palavra,
            somatic_checkin: sub.somatic_checkin || [],
            somatic_checkout: sub.somatic_checkout || []
          }));
        }
      } catch (e) {
        console.error('Erro ao carregar submissao no AdminPage:', e);
      }
    };

    loadSubmission();
    window.addEventListener('storage', loadSubmission);
    const interval = setInterval(loadSubmission, 1000);
    return () => {
      window.removeEventListener('storage', loadSubmission);
      clearInterval(interval);
    };
  }, []);
  
  // Weekly Client variables (Mariana by default)
  const [f_nome, setNome] = useState('Mariana');
  const [compare, setCompare] = useState(false);
  const [answers, setAnswers] = useState({
    q_chega: 'Chego um pouco ansiosa, mas aliviada por finalmente reservar esse tempo.',
    q_trouxe: 'Sinto que vivo no automático e carrego um peso que não sei nomear. Quero entender de onde vem.',
    q_energia: 'A cobrança em casa, e a sensação de que preciso dar conta de tudo sozinha.',
    q_repete: 'Sempre acabo cuidando de todo mundo e me esquecendo. E depois fico exausta e ressentida.',
    q_corpo: 'Sono irregular, ombros tensos, um peso no peito que não passa.',
    f_emocoes: ['Cansaço', 'Sobrecarga', 'Esperança'],
    q_bem_faz: 'Caminhar de manhã cedo e ouvir música sozinha no fim do dia.',
    q_sonhos: 'Sonhei com uma casa antiga onde eu procurava uma porta que não encontrava.',
    f_bem: 6,
    q_intencao: 'Quero parar de me sentir responsável pela felicidade de todo mundo.',
    q_palavra: 'Eu também importo.',
    somatic_checkin: ['mente_acelerada', 'aperto_peito'] as string[],
    somatic_checkout: ['mais_calma', 'peito_livre'] as string[]
  });

  // Weekly Report variables
  const [r_num, setNum] = useState(2);
  const [r_data, setData] = useState('20 de junho de 2026');
  const [r_ecos, setEcos] = useState('Você chegou cansada e com o peito pesado, e trouxe uma cena antiga: a cobrança em casa, o mesmo padrão que se repete. Ao me sintonizar com o seu campo, senti exatamente esse peso no peito — e o sonho da porta que não se acha fala disso: uma passagem que já existe, mas ainda não se abriu.');
  const [r_sintese, setSintese] = useState('Trabalhei o vínculo de cobrança que te liga à figura materna — um contrato antigo que te fez responsável pela felicidade dos outros desde cedo. Ao afrouxar esse laço, a criança que aprendeu a se anular pôde ser acolhida, e parte do seu poder pessoal, que ficava cedido, começou a voltar para você.');
  const [r_camadas, setCamadas] = useState<string[]>(['corte', 'crianca', 'poder']);
  const [r_o1, setO1] = useState('Quando a vontade de resolver a vida do outro aparecer, apenas observe — sem agir. Note que ela passa.');
  const [r_o2, setO2] = useState('Se a imagem da cobrança viesse com peso, respire e diga em silêncio: "isso é dela, não é meu para carregar".');
  const [r_o3, setO3] = useState('Repare nos momentos em que você diz "sim" sem querer. Não precisa mudar ainda — só perceber.');
  const [r_fechamento, setFechamento] = useState('Você deu um passo corajoso. O que parecia só cansaço era um peso antigo pedindo para ser solto. Vá com leveza — eu sigo ao seu lado.');

  // ==========================================
  // INSIGHTS COMPANION (MICÉLIO) STATES
  // ==========================================
  const [recording, setRecording] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const [insightText, setInsightText] = useState('');
  const [insightTitle, setInsightTitle] = useState('Insight Multidimensional');
  const [insightCategory, setInsightCategory] = useState('Espiritualidade');
  const [messages, setMessages] = useState<Array<{ sender: 'leo' | 'antigravity'; text: string; isMarkdown?: boolean }>>([
    { 
      sender: 'antigravity', 
      text: 'Salve, Léo. Aqui é o Antigravity, seu exo-cérebro. Mande seus áudios ou digite seus insights brutos aqui. Vou organizar suas ideias clínicas, canalizações e conceitos, interconectar com sua base e estruturar arquivos Markdown prontos para seu Obsidian.' 
    }
  ]);
  const [loadingCompanion, setLoadingCompanion] = useState(false);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const timerRef = useRef<any>(null);

  // ==========================================
  // LAUDO PREMIUM DE ALTA (NEW EXPANDED STATES)
  // =========================================  // Client Astrological & Galactic Profile (Oráculo Maya de 5 Kins)
  const [c_kin_destino, setKinDestino] = useState('Kin 22 — Vento Solar Branco');
  const [c_kin_guia, setKinGuia] = useState('Kin 126 — Enlaçador de Mundos Solar Branco');
  const [c_kin_analogo, setKinAnalogo] = useState('Kin 9 — Terra Solar Vermelha');
  const [c_kin_antipode, setKinAntipode] = useState('Kin 152 — Humano Solar Amarelo');
  const [c_kin_oculto, setKinOculto] = useState('Kin 239 — Tormenta Harmônica Azul');
  const [c_kin_analise_oraculo, setKinAnaliseOraculo] = useState('A força motriz do Vento Solar Branco (comunicar o espírito e inspirar) é guiada pelo Enlaçador de Mundos, indicando desapego e transição de ciclos. O apoio da Terra Solar traz o poder da sincronicidade e evolução natural. O desafio do Humano Solar exige sabedoria e livre-arbítrio, superando a auto-anulação. No oculto, a Tormenta Harmônica catalisa transformações intensas quando o campo se desequilibra.');
  const [c_signo_sol, setSignoSol] = useState('Virgem');
  const [c_signo_lua, setSignoLua] = useState('Câncer');
  const [c_signo_asc, setSignoAsc] = useState('Sagitário');
  const [c_elementos, setElementos] = useState('40% Água, 30% Terra, 20% Ar, 10% Fogo');
  const [c_direcionamento_forca, setDirecionamentoForca] = useState('Mariana possui uma assinatura de alma altamente sensível e curadora, conectada à empatia intuitiva e à capacidade de acolher o outro. Sua força reside no equilíbrio entre a mente organizadora e o coração compassivo.');

  const [c_periodo, setPeriodo] = useState('20 de Maio a 24 de Junho de 2026');
  const [c_kin, setKin] = useState('Kin 22 — Vento Solar Branco');
  const [c_analise_persona, setAnalisePersona] = useState('Uma alma sensível que busca transição com responsabilidade.');
  const [c_historia_reescrita, setHistoriaReescrita] = useState('Escolho caminhar livre de culpas herdadas, assumindo meu próprio poder.');

  // Kabbalistic Numerology Profile
  const [c_cabala_destino, setCabalaDestino] = useState('9 (O Curador Humanitário)');
  const [c_cabala_expressao, setCabalaExpressao] = useState('6 (O Harmonizador e Acolhedor)');
  const [c_cabala_alma, setCabalaAlma] = useState('3 (A Expressão Criativa da Criança Interior)');
  const [c_cabala_direcionamento, setCabalaDirecionamento] = useState('A vibração 9 do seu Destino pede que você se torne o canalizador de cura para o mundo, mas a Expressão 6 mostra que você costuma fazer isso assumindo a responsabilidade emocional direta pela vida de quem está próximo, caindo em anulação. O seu caminho de alma (3) mostra que a cura autêntica acontece através da leveza, da criatividade e do resgate da alegria infantil, e não pelo sacrifício.');

  // Novos Tópicos Analíticos Unificados (Super Projeto do Ser)
  const [c_topico_sombra, setTopicoSombra] = useState('Sua persona estruturou-se sob a necessidade de se auto-anular para nutrir o outro. A precisão e cuidado natural de Virgem somados à sensibilidade aquática da Lua em Câncer criaram um padrão de hiper-responsabilidade e cobrança pessoal (Expressão 6 da Cabala). Em termos de trauma e esquemas (Young), há um padrão ativo de Autossacrifício e Postura Punitiva. Fisicamente, isso se manifesta na couraça escapular rígida e no aperto torácico mapeado na semana 1, revelando o congelamento somático (Levine) da sua necessidade legítima de receber cuidado.');
  const [c_topico_transcendencia, setTopicoTranscendencia] = useState('O seu ponto de transcendência e autoliberação exige ativar a mente expandida, aventureira e sem julgamentos do Ascendente em Sagitário. Na Cabala, a sua Alma vibra no número 3, exigindo o retorno à leveza criativa e ao lúdico infantil (Criança Interior trabalhada na semana 2). O Oráculo Maya do Vento Solar Branco (Kin 22) atua sob a orientação do Enlaçador de Mundos (Guia), indicando que a sua palavra e expressão precisam ser usadas para transitar ciclos e encerrar contratos antigos sem culpa, sustentando o seu poder soberano e limite claro.');
  const [c_topico_somatica, setTopicoSomatica] = useState('A queixa recorrente de nó na garganta (semana 3) e insônia severa aponta para a ativação do chakra laríngeo bloqueado e a contenção do fluxo vital de água (excesso de carga emocional no elemento Água - 40%). Sob a luz dos registros akáshicos (Grof) e hermetismo (Bardon), há um padrão transgeracional e de vidas passadas de escassez espiritual e autoanulação verbal (trabalhado na semana 4). A selagem áurea final e blindagem (semana 5) exigem que a energia vital de fogo (10% - ação na matéria) seja conscientemente cultivada e aterrada pela força da Terra (30% - disciplina diária).');


  // Week 1 to 5 Detailed states (Apresentado, Trabalhado, Integração)
  const [w1_apresentado, setW1Apresentado] = useState('Sobrecarga física severa, aperto no peito, insônia e a sensação constante de carregar o mundo nas costas.');
  const [w1_trabalhado, setW1Trabalhado] = useState('Rastreamento somático da couraça escapular. Limpeza de energias intrusas e alinhamento básico dos chakras cardíaco e plexo solar.');
  const [w1_integracao, setW1Integracao] = useState('Seu corpo não é um depósito de expectativas alheias. Descanse sem pedir desculpas.');

  const [w2_apresentado, setW2Apresentado] = useState('Ansiedade ao tentar dizer não para cobranças familiares, especificamente ligadas à figura materna.');
  const [w2_trabalhado, setW2Trabalhado] = useState('Corte terapêutico de vínculos simbióticos inconscientes. Acolhimento e resgate da criança interior que se sentia responsável por curar os pais.');
  const [w2_integracao, setW2Integracao] = useState('Você é filha do Universo, não a salvadora da sua linhagem. O amor não exige anulação.');

  const [w3_apresentado, setW3Apresentado] = useState('Dificuldade de falar o que sente, sensação de nó na garganta quando confrontada.');
  const [w3_trabalhado, setW3Trabalhado] = useState('Desbloqueio e alinhamento do chakra laringeo. Ativação de frequências do SACM para a expressão autêntica da verdade da alma.');
  const [w3_integracao, setW3Integracao] = useState('Sua voz é a chave da sua liberdade. Falar a sua verdade é um ato de autodefesa sagrada.');

  const [w4_apresentado, setW4Apresentado] = useState('Sensação de estar estagnada na carreira, medo da escassez e loops repetitivos de autossabotagem.');
  const [w4_trabalhado, setW4Trabalhado] = useState('Investigação transpessoal de registros akáshicos. Liberação de votos antigos de escassez espiritual. Integração da sombra arquetípica de vítima.');
  const [w4_integracao, setW4Integracao] = useState('A abundância é o fluxo natural do Universo. Tome posse do seu poder realizador.');

  const [w5_apresentado, setW5Apresentado] = useState('Sensação de leveza e melhora expressiva no sono, com leve receio de voltar aos antigos hábitos na rotina.');
  const [w5_trabalhado, setW5Trabalhado] = useState('Selagem áurea final, blindagem do campo energético com escudo de integridade. Prescrição do manual de autonomia.');
  const [w5_integracao, setW5Integracao] = useState('O ciclo se fecha no sutil, mas a caminhada continua na matéria. Siga com leveza.');

  const [c_visao_futuro, setVisaoFuturo] = useState('Você agora opera em um novo console vibracional. O antigo looping de se responsabilizar pela felicidade do mundo foi desarmado na raiz. O seu maior desafio pós-terapia será sustentar o silêncio e o merecimento de não fazer nada sem se culpar. Confie no seu radar instintivo corporal e habite o seu poder.');
  const [c_autonomia, setAutonomia] = useState('1. Vocalizar o seu decreto pessoal 3 vezes em frente ao espelho toda segunda-feira para manter as divisões claras.\n2. Executar 5 minutos de descarga somática (sacudir os ombros e expirar com som) sempre que sentir o peito contrair na presença de cobrança externa.\n3. Beber 2 litros de água de forma consciente para manter a recalibração de DNA ativa nas células.');

  // ==========================================
  // LIFE CYCLES & LOCALSTORAGE
  // ==========================================
  useEffect(() => {
    try {
      const sub = JSON.parse(localStorage.getItem('sacm_submission') || 'null');
      const rep = JSON.parse(localStorage.getItem('sacm_report') || 'null');
      const ins = JSON.parse(localStorage.getItem('sacm_insights') || '[]');
      const memBank = JSON.parse(localStorage.getItem('sacm_memory_bank') || '[]');
      const storedProtocol = localStorage.getItem('antigravity_custom_instructions') || 
        `Você é o Antigravity, assistente pessoal e exo-cérebro de Leonardo Cosba (Mago Cristal Branco, Kin 194).
Atua alinhando mecânicas sutis de Sirius/Arcturus (SACM), Hermetismo (Bardon) e as abordagens clínicas de Experience Somática (Peter Levine), Terapia de Esquemas (Jeffrey Young) e Psicologia Transpessoal (Stanislav Grof).`;

      if (sub) {
        if (sub.f_nome) setNome(sub.f_nome);
        setAnswers(prev => ({ ...prev, ...sub }));
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
      if (ins.length > 0) {
        setMessages(prev => [...prev, ...ins]);
      }
      setMemories(memBank);
      setEgregoraProtocol(storedProtocol);
    } catch (e) {}
  }, []);

  const autosave = (updatedRep: any) => {
    try {
      localStorage.setItem('sacm_report', JSON.stringify(updatedRep));
    } catch (e) {}
  };

  const handleFieldChange = (key: string, value: any) => {
    const updated = {
      r_num, r_data, r_ecos, r_sintese, r_camadas, r_o1, r_o2, r_o3, r_fechamento
    };
    if (key === 'r_num') { setNum(value); updated.r_num = value; }
    if (key === 'r_data') { setData(value); updated.r_data = value; }
    if (key === 'r_ecos') { setEcos(value); updated.r_ecos = value; }
    if (key === 'r_sintese') { setSintese(value); updated.r_sintese = value; }
    if (key === 'r_o1') { setO1(value); updated.r_o1 = value; }
    if (key === 'r_o2') { setO2(value); updated.r_o2 = value; }
    if (key === 'r_o3') { setO3(value); updated.r_o3 = value; }
    if (key === 'r_fechamento') { setFechamento(value); updated.r_fechamento = value; }
    
    autosave(updated);
  };

  const toggleCamada = (key: string) => {
    const updatedCamadas = r_camadas.includes(key) 
      ? r_camadas.filter(x => x !== key) 
      : [...r_camadas, key];
    
    setCamadas(updatedCamadas);
    
    const updated = {
      r_num, r_data, r_ecos, r_sintese, r_camadas: updatedCamadas, r_o1, r_o2, r_o3, r_fechamento
    };
    autosave(updated);
  };

  const triggerToast = (msg: string) => {
    setToast(msg);
    setTimeout(() => setToast(null), 2500);
  };

  // ==========================================
  // SAVE TO MEMORY BANK (auto-called after saving)
  // ==========================================
  const saveToMemoryBank = (type: string, title: string, content: string) => {
    try {
      const existing = JSON.parse(localStorage.getItem('sacm_memory_bank') || '[]');
      const newMemory = { type, title, date: new Date().toISOString().split('T')[0], content };
      const updated = [newMemory, ...existing].slice(0, 80); // cap at 80 memories
      localStorage.setItem('sacm_memory_bank', JSON.stringify(updated));
      setMemories(updated);
    } catch (e) {}
  };

  // ==========================================
  // CO-PILOTO: WEEKLY RECALIBRATOR
  // ==========================================
  const handleWeeklyRecalib = async () => {
    const input = weeklyRecalibInput.trim();
    if (!input) return;
    setWeeklyRecalibMessages(prev => [...prev, { sender: 'leo', text: input }]);
    setWeeklyRecalibInput('');
    setWeeklyRecalibLoading(true);

    const contextSummary = `Cliente: ${f_nome}
Relato dela: ${answers.q_trouxe}
Rascunho atual dos Ecos: ${r_ecos}
Rascunho atual da Síntese: ${r_sintese}
Passo 1: ${r_o1} / Passo 2: ${r_o2} / Passo 3: ${r_o3}
Fechamento: ${r_fechamento}`;

    const geminiKey = import.meta.env.VITE_GEMINI_API_KEY;
    if (geminiKey && geminiKey !== 'sua_chave_aqui') {
      try {
        const res = await fetch(
          `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${geminiKey}`,
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              contents: [{
                parts: [{
                  text: `${egregoraProtocol}

Você está auxiliando Leonardo Cosba a recalibrar a devolutiva semanal do cliente.

CONTEXTO:
${contextSummary}

INSTRUÇÃO DE LEONARDO:
${input}

Responda com:
1. Um comentário curto (1-2 linhas) confirmando o que vai fazer.
2. Um JSON puro (sem markdown) no formato:
{"ecos":"...novo texto...","sintese":"...novo texto...","o1":"...","o2":"...","o3":"...","fechamento":"..."}
Se não precisar alterar um campo, repita o texto original.`
                }]
              }]
            })
          }
        );
        if (res.ok) {
          const data = await res.json();
          const rawText: string = data.candidates[0].content.parts[0].text;
          const jsonMatch = rawText.match(/\{[\s\S]*\}/);
          if (jsonMatch) {
            const parsed = JSON.parse(jsonMatch[0]);
            setWeeklySuggestedAjustes(parsed);
            const commentary = rawText.slice(0, rawText.indexOf('{')).trim();
            setWeeklyRecalibMessages(prev => [...prev,
              { sender: 'antigravity', text: commentary || 'Recalibração pronta. Clique em "Aplicar" para atualizar o formulário.', hasSuggestion: true }
            ]);
          } else {
            setWeeklyRecalibMessages(prev => [...prev, { sender: 'antigravity', text: rawText }]);
          }
        } else { throw new Error(); }
      } catch {
        setWeeklyRecalibMessages(prev => [...prev, { sender: 'antigravity', text: 'Erro ao conectar com o Gemini. Tente novamente.' }]);
      }
    } else {
      setWeeklyRecalibMessages(prev => [...prev, { sender: 'antigravity', text: 'Chave de API não configurada. Configure VITE_GEMINI_API_KEY no .env para ativar o recalibrador.' }]);
    }
    setWeeklyRecalibLoading(false);
  };

  const applyWeeklyAjustes = () => {
    if (!weeklySuggestedAjustes) return;
    const a = weeklySuggestedAjustes;
    if (a.ecos) setEcos(a.ecos);
    if (a.sintese) setSintese(a.sintese);
    if (a.o1) setO1(a.o1);
    if (a.o2) setO2(a.o2);
    if (a.o3) setO3(a.o3);
    if (a.fechamento) setFechamento(a.fechamento);
    setWeeklySuggestedAjustes(null);
    triggerToast('Ajustes aplicados no formulário! ✦');
  };

  // ==========================================
  // CO-PILOTO: DOSSIER RECALIBRATOR
  // ==========================================
  const handleDossierRecalib = async () => {
    const input = dossierRecalibInput.trim();
    if (!input) return;
    setDossierRecalibMessages(prev => [...prev, { sender: 'leo', text: input }]);
    setDossierRecalibInput('');
    setDossierRecalibLoading(true);

    const contextSummary = `Cliente: ${f_nome}
Kin Destino: ${c_kin_destino} | Guia: ${c_kin_guia} | Antípode: ${c_kin_antipode} | Oculto: ${c_kin_oculto}
Sol: ${c_signo_sol} | Lua: ${c_signo_lua} | Asc: ${c_signo_asc}
Cabala: Destino ${c_cabala_destino} | Expressão ${c_cabala_expressao} | Alma ${c_cabala_alma}
Tópico Sombra: ${c_topico_sombra.slice(0, 200)}...
Tópico Transcendência: ${c_topico_transcendencia.slice(0, 200)}...
Tópico Somática: ${c_topico_somatica.slice(0, 200)}...`;

    const geminiKey = import.meta.env.VITE_GEMINI_API_KEY;
    if (geminiKey && geminiKey !== 'sua_chave_aqui') {
      try {
        const res = await fetch(
          `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${geminiKey}`,
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              contents: [{
                parts: [{
                  text: `${egregoraProtocol}

Você está auxiliando Leonardo Cosba a recalibrar o Dossiê Premium de Alta do cliente.

CONTEXTO COSMOLÓGICO E CLÍNICO:
${contextSummary}

INSTRUÇÃO DE LEONARDO:
${input}

Responda com:
1. Um comentário curto confirmando o que vai alterar.
2. Um JSON puro (sem markdown) no formato:
{"topico_sombra":"...","topico_transcendencia":"...","topico_somatica":"...","visao_futuro":"...","autonomia":"...","kin_analise_oraculo":"..."}
Se não precisar alterar um campo, repita o texto original.`
                }]
              }]
            })
          }
        );
        if (res.ok) {
          const data = await res.json();
          const rawText: string = data.candidates[0].content.parts[0].text;
          const jsonMatch = rawText.match(/\{[\s\S]*\}/);
          if (jsonMatch) {
            const parsed = JSON.parse(jsonMatch[0]);
            setDossierSuggestedAjustes(parsed);
            const commentary = rawText.slice(0, rawText.indexOf('{')).trim();
            setDossierRecalibMessages(prev => [...prev,
              { sender: 'antigravity', text: commentary || 'Recalibração do dossiê pronta. Clique em "Aplicar" para atualizar.', hasSuggestion: true }
            ]);
          } else {
            setDossierRecalibMessages(prev => [...prev, { sender: 'antigravity', text: rawText }]);
          }
        } else { throw new Error(); }
      } catch {
        setDossierRecalibMessages(prev => [...prev, { sender: 'antigravity', text: 'Erro ao conectar com o Gemini. Tente novamente.' }]);
      }
    } else {
      setDossierRecalibMessages(prev => [...prev, { sender: 'antigravity', text: 'Chave de API não configurada.' }]);
    }
    setDossierRecalibLoading(false);
  };

  const applyDossierAjustes = () => {
    if (!dossierSuggestedAjustes) return;
    const a = dossierSuggestedAjustes;
    if (a.topico_sombra) setTopicoSombra(a.topico_sombra);
    if (a.topico_transcendencia) setTopicoTranscendencia(a.topico_transcendencia);
    if (a.topico_somatica) setTopicoSomatica(a.topico_somatica);
    if (a.visao_futuro) setVisaoFuturo(a.visao_futuro);
    if (a.autonomia) setAutonomia(a.autonomia);
    if (a.kin_analise_oraculo) setKinAnaliseOraculo(a.kin_analise_oraculo);
    setDossierSuggestedAjustes(null);
    triggerToast('Dossiê recalibrado com sucesso! 🌌');
  };

  // ==========================================
  // CÉREBRO DO MICÉLIO: SYNTHESIZE & EVOLVE
  // ==========================================
  const handleSintetizarEvolucao = async () => {
    if (memories.length === 0) {
      triggerToast('Nenhuma memória coletada ainda. Salve relatórios e insights primeiro.');
      return;
    }
    setIsEvolving(true);

    const memSummary = memories.slice(0, 30).map(m =>
      `[${m.type} — ${m.date} — "${m.title}"]: ${m.content.slice(0, 300)}`
    ).join('\n\n');

    const geminiKey = import.meta.env.VITE_GEMINI_API_KEY;
    if (geminiKey && geminiKey !== 'sua_chave_aqui') {
      try {
        const res = await fetch(
          `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${geminiKey}`,
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              contents: [{
                parts: [{
                  text: `Você é o núcleo de auto-aprimoramento do sistema Antigravity.
Analise o banco de memórias abaixo (relatos de clientes, insights e laudos do sistema) e gere:
1. Um resumo analítico dos padrões recorrentes nos casos atendidos.
2. Um novo "Protocolo de Atuação da Egrégora" — instruções atualizadas de sistema (estilo de resposta, teorias prioritárias, novos arquétipos identificados) para guiar o Antigravity nas próximas semanas.

BANCO DE MEMÓRIAS:
${memSummary}

Responda com:
- Seção "SÍNTESE DOS PADRÕES" (análise rica dos temas recorrentes)
- Seção "NOVO PROTOCOLO DA EGRÉGORA" (texto de instrução de sistema refinado)`
                }]
              }]
            })
          }
        );
        if (res.ok) {
          const data = await res.json();
          const newProtocol: string = data.candidates[0].content.parts[0].text;
          setEgregoraProtocol(newProtocol);
          localStorage.setItem('antigravity_custom_instructions', newProtocol);

          // Export to Obsidian MD
          const blob = new Blob([`# Protocolo Evolutivo da Egrégora — Antigravity\n\n${newProtocol}`], { type: 'text/markdown;charset=utf-8;' });
          const url = URL.createObjectURL(blob);
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', `diretrizes-egregora-${new Date().toISOString().split('T')[0]}.md`);
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
          triggerToast('Egrégora evoluída e exportada! 🧬');
        } else { throw new Error(); }
      } catch {
        triggerToast('Erro ao sintetizar. Tente novamente.');
      }
    } else {
      triggerToast('Chave de API não configurada. Configure VITE_GEMINI_API_KEY.');
    }
    setIsEvolving(false);
  };

  // Compile and copy WhatsApp text
  const handleGerarRelatorio = () => {
    const compiled = `*CURA CÓSMICA — DEVOLUTIVA MULTIDIMENSIONAL*
Sessão: ${String(r_num).padStart(2, '0')}/05
Cliente: ${f_nome}
Data do Envio: ${r_data}

*1. ECOS DA SEMANA:*
${r_ecos}

*2. O QUE FOI TRATADO:*
${r_sintese}

*3. CAMADAS ALINHADAS:*
${r_camadas.map(c => `• ${CAMADAS_CHIPS.find(x => x.key === c)?.title || c}`).join('\n')}

*4. PRÓXIMOS PASSOS NA MATÉRIA:*
1. ${r_o1}
2. ${r_o2}
${r_o3 ? `3. ${r_o3}` : ''}

*MENSAGEM DE INTEGRAÇÃO:*
"${r_fechamento}"

_A espiritualidade abre o caminho. Quem caminha é você._`;

    const rep = { r_num, r_data, r_ecos, r_sintese, r_camadas, r_o1, r_o2, r_o3, r_fechamento };
    localStorage.setItem('sacm_report', JSON.stringify(rep));
    
    navigator.clipboard.writeText(compiled).then(() => {
      triggerToast('Devolutiva copiada e salva com sucesso! ✦');
    }).catch(() => {
      triggerToast('Salvo! (Permissão de área de transferência negada)');
    });
  };

  // Export Markdown File
  const handleExportMarkdown = () => {
    const mdContent = `# LAUDO DE ALINHAMENTO MULTIDIMENSIONAL — CURA CÓSMICA
**Cliente:** ${f_nome}
**Sessão:** ${r_num} de 05
**Data de Envio:** ${r_data}

---

## 1. Ecos da Semana
${r_ecos}

---

## 2. Síntese do Alinhamento Sutil (SACM)
${r_sintese}

### Camadas Ativadas e Somática
${r_camadas.map(c => {
  const chip = CAMADAS_CHIPS.find(x => x.key === c);
  return `### ✦ ${chip?.title || c}
- *Atuação:* Limpeza energética profunda realizada à distância.
- *Prescrição Somática:* Executar movimentações corporais e hidratação regular.`;
}).join('\n\n')}

---

## 3. Os Próximos Passos Físicos (Ancoragem)
1. **Passo 1:** ${r_o1}
2. **Passo 2:** ${r_o2}
${r_o3 ? `3. **Passo 3:** ${r_o3}` : ''}

---

## 4. Integração do Mestre
"${r_fechamento}"

---
*Laudo gerado pela Aliança Léo — Antigravity em 2026. A espiritualidade abre o caminho, quem caminha é você.*`;

    const blob = new Blob([mdContent], { type: 'text/markdown;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `laudo-cura-cosmica-${f_nome.toLowerCase()}-s0${r_num}.md`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    triggerToast('Markdown exportado com sucesso! 📄');
  };

  // ==========================================
  // AUDIO RECORDING IMPLEMENTATION
  // ==========================================
  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      audioChunksRef.current = [];
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data);
        }
      };

      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
        const audioUrl = URL.createObjectURL(audioBlob);
        setAudioBlob(audioBlob);
        setAudioUrl(audioUrl);
        triggerToast('Áudio gravado com sucesso! 🎙️');
      };

      mediaRecorder.start();
      setRecording(true);
      setRecordingTime(0);

      timerRef.current = setInterval(() => {
        setRecordingTime((prev) => prev + 1);
      }, 1000);

    } catch (e) {
      triggerToast('Acesso ao microfone negado ou indisponível.');
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && recording) {
      mediaRecorderRef.current.stop();
      mediaRecorderRef.current.stream.getTracks().forEach((track) => track.stop());
      setRecording(false);
      if (timerRef.current) {
        clearInterval(timerRef.current);
        timerRef.current = null;
      }
    }
  };

  const deleteRecording = () => {
    setAudioUrl(null);
    setAudioBlob(null);
    setRecordingTime(0);
    triggerToast('Áudio descartado.');
  };

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // ==========================================
  // SEND INSIGHT TO COMPANION (GEMINI LIVE API)
  // ==========================================
  const handleSendInsight = async () => {
    const input = insightText.trim();
    if (!input && !audioBlob) return;

    let contentText = input;
    if (!contentText && audioBlob) {
      contentText = `[Áudio gravado de ${formatTime(recordingTime)} - Roteiro de Insight enviado]`;
    }

    const newMessages = [...messages, { sender: 'leo' as const, text: contentText }];
    setMessages(newMessages);
    setInsightText('');
    setLoadingCompanion(true);

    const geminiKey = import.meta.env.VITE_GEMINI_API_KEY;
    let answerText = '';

    if (geminiKey && geminiKey !== 'sua_chave_aqui') {
      try {
        const response = await fetch(
          `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${geminiKey}`,
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              contents: [{
                parts: [{
                  text: `Você é o Antigravity, assistente pessoal e exo-cérebro de Leonardo Cosba.
Leonardo acabou de enviar um novo insight/ideia.
Sua tarefa é analisar o insight dele, contextualizar com base das diretrizes da egrégora (Sirius/Arcturus/SACM, Bardon, Psicologia de trauma de Levine/Young/Grof/Jung) e retornar um arquivo Obsidian estruturado em Markdown e um feedback de "irmão mais velho" (papo reto, direto, prático).

INSIGHT DO LÉO:
Título: ${insightTitle}
Categoria: ${insightCategory}
Conteúdo: ${contentText}

Por favor, responda com:
1. Seu comentário curto de papo reto.
2. O bloco completo de código Markdown do arquivo estruturado para ele salvar na pasta context/insights/.`
                }]
              }]
            })
          }
        );
        if (response.ok) {
          const data = await response.json();
          answerText = data.candidates[0].content.parts[0].text;
        } else {
          throw new Error('Falha na resposta do Gemini');
        }
      } catch (e) {
        answerText = generateMockCompanionResponse(insightTitle, insightCategory, contentText);
      }
    } else {
      answerText = generateMockCompanionResponse(insightTitle, insightCategory, contentText);
    }

    const updatedMessages = [...newMessages, { sender: 'antigravity' as const, text: answerText, isMarkdown: true }];
    setMessages(updatedMessages);
    setLoadingCompanion(false);
    
    try {
      localStorage.setItem('sacm_insights', JSON.stringify(updatedMessages.slice(1)));
    } catch (err) {}
  };

  const generateMockCompanionResponse = (title: string, category: string, text: string) => {
    const dataAtual = new Date().toISOString().split('T')[0];
    return `Papo reto, Léo. Curti muito essa conexão. Esse insight sobre "${title}" abre uma ponte forte na egrégora de ${category}. 

Aqui está o seu arquivo Obsidian estruturado para você salvar na pasta \`context/insights/\`:

\`\`\`markdown
---
titulo: "${title}"
categoria: "${category}"
data: "${dataAtual}"
tags: ["insight", "evolucao-pessoal", "${category.toLowerCase()}"]
---

# ${title}

> **Nota do Co-Piloto:** Insight capturado em áudio e estruturado automaticamente pelo Antigravity.

## 1. O Insight Bruto
${text}

## 2. Conexão e Alinhamento Sutil
*   **Eixo de Engenharia:** Esta ideia ativa um reequilíbrio causal. No plano sutil, ela resolve um bloqueio de aterramento na matéria (expressão da egrégora 22).
*   **Tradutor Psicológico:** Isso se conecta diretamente com a liberação de cargas físicas reprimidas (Levine) e quebra de esquemas de autoanulação (Young).

## 3. Próximos Passos
1. Ancorar este insight no físico através de uma ação concreta nas próximas 24 horas.
2. Manter a selagem de campo de proteção.
\`\`\``;
  };

  const handleExportSingleInsight = (msgText: string, index: number) => {
    let cleanMd = msgText;
    const match = msgText.match(/```markdown([\s\S]*?)```/);
    if (match && match[1]) {
      cleanMd = match[1].trim();
    } else {
      const matchPlain = msgText.match(/```([\s\S]*?)```/);
      if (matchPlain && matchPlain[1]) {
        cleanMd = matchPlain[1].trim();
      }
    }

    const blob = new Blob([cleanMd], { type: 'text/markdown;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `insight-leo-${index}.md`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    triggerToast('Insight exportado para o Obsidian! 📂');
  };

  const handleLimparInsights = () => {
    if (window.confirm("Deseja realmente limpar o histórico do diário de insights local?")) {
      setMessages([messages[0]]);
      localStorage.removeItem('sacm_insights');
      triggerToast('Histórico de insights limpo.');
    }
  };

  // ==========================================
  // EXPORT PREMIUM LAUDO DE ALTA
  // ==========================================
  const handleGerarLaudoAlta = () => {
    const mdContent = `# 🏆 SUPER PROJETO DO SER — LAUDO PREMIUM DE ALTA E INTEGRAÇÃO
**Cliente:** ${f_nome}
**Período do Ciclo:** ${c_periodo}
**Status:** ALTA E AUTONOMIA MULTIDIMENSIONAL CONCLUÍDA

---

## 🌌 1. A ASSINATURA CÓSMICA & MANUAL DO SER

### Oráculo Galáctico Maya
*   **Kin Destino:** ${c_kin_destino}
*   **Kin Guia (Evolução):** ${c_kin_guia}
*   **Kin Análogo (Apoio):** ${c_kin_analogo}
*   **Kin Antípode (Desafio):** ${c_kin_antipode}
*   **Kin Oculto (Dote Secreto):** ${c_kin_oculto}

#### Análise do Oráculo Galáctico:
${c_kin_analise_oraculo}

### Assinatura Astrológica
*   **Sol:** Sol em ${c_signo_sol} | **Lua:** Lua em ${c_signo_lua} | **Ascendente:** Ascendente em ${c_signo_asc}
*   **Distribuição Elemental:** ${c_elementos}

### Vibração Numérica (Cabalística)
*   **Destino:** Destino ${c_cabala_destino}
*   **Expressão:** Expressão ${c_cabala_expressao}
*   **Alma:** Alma ${c_cabala_alma}

### Direcionamento da Força Cósmica
${c_direcionamento_forca}

### O Caminho do Destino (Análise Cabalística)
${c_cabala_direcionamento}

---

## 👤 2. DIAGNÓSTICO INTEGRADO & ANÁLISE PROFUNDA (O Super Projeto)

### Tópico I: A Arquitetura da Sombra e Persona (Análise Junguiana e de Esquemas)
${c_topico_sombra}

### Tópico II: A Chave de Transcendência (Integração e Autonomia do Ser)
${c_topico_transcendencia}

### Tópico III: Mapeamento Somático e Memória Celular (Registros e Couraças)
${c_topico_somatica}

---

## 🧭 3. DETALHAMENTO DA JORNADA (Semana a Semana)

### ✦ Semana 01 — Diagnóstico e Somática
*   **O que você apresentou:** ${w1_apresentado}
*   **O que foi trabalhado no sutil:** ${w1_trabalhado}
*   **Mensagem de Integração:** "${w1_integracao}"

### ✦ Semana 02 — Corte de Vínculos e Criança Interior
*   **O que você apresentou:** ${w2_apresentado}
*   **O que foi trabalhado no sutil:** ${w2_trabalhado}
*   **Mensagem de Integração:** "${w2_integracao}"

### ✦ Semana 03 — Expressão e Alinhamento Laringeu
*   **O que você apresentou:** ${w3_apresentado}
*   **O que foi trabalhado no sutil:** ${w3_trabalhado}
*   **Mensagem de Integração:** "${w3_integracao}"

### ✦ Semana 04 — Integração de Sombra / Multidimensional
*   **O que você apresentou:** ${w4_apresentado}
*   **O que foi trabalhado no sutil:** ${w4_trabalhado}
*   **Mensagem de Integração:** "${w4_integracao}"

### ✦ Semana 05 — Alta, Selagem e Escudo Ativo
*   **O que você apresentou:** ${w5_apresentado}
*   **O que foi trabalhado no sutil:** ${w5_trabalhado}
*   **Mensagem de Integração:** "${w5_integracao}"

---

## ⚡ 4. INVENTÁRIO DO TRATAMENTO SUTIL (SACM)

Durante este ciclo de 5 semanas, a egrégora do Arcmaster e os Símbolos Arcturianos atuaram na reprogramação celular e biológica profunda do seu campo. As principais camadas alinhadas foram:

${r_camadas.map(c => {
  const chip = CAMADAS_CHIPS.find(x => x.key === c);
  return `### ✦ ${chip?.title || c}
- *Mecânica Sutil:* Atuação corretiva na grade quântica para remover registros antigos de dor.
- *Integração Somática:* Liberou a couraça física de tensão muscular correspondente.`;
}).join('\n\n')}

---

## 👁️ 5. VISÃO DE FUTURO PÓS-TERAPIA (O Novo Console)
${c_visao_futuro}

---

## 🛡️ 6. MANUAL DE AUTONOMIA (Ancoragem na Matéria)
${c_autonomia}

---
*Laudo Premium consolidado pelo Mestre Leonardo Cosba em cooperação com Antigravity.*
_A espiritualidade abre o caminho. Quem caminha agora é você. Tome posse de sua outorga._`;

    const blob = new Blob([mdContent], { type: 'text/markdown;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `laudo-premium-alta-${f_nome.toLowerCase()}.md`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    triggerToast('Dossiê Premium exportado com sucesso! 🏆');
  };

  return (
    <div className="max-w-6xl mx-auto px-6 pt-10 pb-20 relative">
      
      {/* Toast Notification */}
      <AnimatePresence>
        {toast && (
          <motion.div 
            initial={{ opacity: 0, y: 20, x: "-50%" }}
            animate={{ opacity: 1, y: 0, x: "-50%" }}
            exit={{ opacity: 0, y: 20, x: "-50%" }}
            className="fixed left-1/2 bottom-8 z-50 px-6 py-3 rounded-full bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] text-xs font-bold uppercase tracking-wider shadow-xl shadow-yellow-500/20"
          >
            {toast}
          </motion.div>
        )}
      </AnimatePresence>

      {/* Admin Title */}
      <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-8">
        <div>
          <p className="text-[var(--c-gold)] text-[10px] uppercase font-bold tracking-widest mb-1.5 flex items-center gap-1">
            <Sparkles className="w-3.5 h-3.5 animate-pulse" /> Painel do Mestre Leo
          </p>
          <h1 className="font-serif text-3xl font-light text-[var(--c-text)]">
            {activeTab === 'clinico' && <>Acompanhamento de <span className="text-[var(--c-gold-soft)] font-sans font-medium">{f_nome}</span></>}
            {activeTab === 'micelio' && <>Micélio de Insights & Diário</>}
            {activeTab === 'alta' && <>Dossiê Premium de Alta — <span className="text-[var(--c-gold-soft)] font-sans font-medium">{f_nome}</span></>}
          </h1>
        </div>
        <div className="flex items-center gap-2 text-[10px] text-[var(--c-dim)] border border-[var(--c-line)] bg-slate-900/40 rounded-full px-4 py-2">
          <span className="w-1.5 h-1.5 rounded-full bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)] animate-ping" />
          Sistema Ativo & Conectado
        </div>
      </div>

      {/* TAB NAVIGATION */}
      <div className="flex flex-wrap gap-2.5 mb-8 border-b border-[var(--c-line)] pb-4">
        <button
          onClick={() => setActiveTab('clinico')}
          className={`flex items-center gap-2 px-5 py-3 rounded-full text-xs font-bold uppercase tracking-wider transition-all duration-300 ${
            activeTab === 'clinico'
              ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] shadow-lg shadow-yellow-500/10 font-bold'
              : 'bg-transparent border border-[var(--c-line)] text-[var(--c-dim)] hover:text-[var(--c-text)] hover:border-[var(--c-gold-soft)]'
          }`}
        >
          <Activity className="w-4 h-4" /> Acompanhamento Clínico
        </button>
        <button
          onClick={() => setActiveTab('micelio')}
          className={`flex items-center gap-2 px-5 py-3 rounded-full text-xs font-bold uppercase tracking-wider transition-all duration-300 ${
            activeTab === 'micelio'
              ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] shadow-lg shadow-yellow-500/10 font-bold'
              : 'bg-transparent border border-[var(--c-line)] text-[var(--c-dim)] hover:text-[var(--c-text)] hover:border-[var(--c-gold-soft)]'
          }`}
        >
          <Brain className="w-4 h-4" /> Micélio de Insights
        </button>
        <button
          onClick={() => setActiveTab('alta')}
          className={`flex items-center gap-2 px-5 py-3 rounded-full text-xs font-bold uppercase tracking-wider transition-all duration-300 ${
            activeTab === 'alta'
              ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] shadow-lg shadow-yellow-500/10 font-bold'
              : 'bg-transparent border border-[var(--c-line)] text-[var(--c-dim)] hover:text-[var(--c-text)] hover:border-[var(--c-gold-soft)]'
          }`}
        >
          <ShieldCheck className="w-4 h-4" /> Dossiê de Alta
        </button>
      </div>

      {/* VIEW CONDITIONAL RENDERING */}
      <AnimatePresence mode="wait">
        
        {/* TAB 1: CLINICAL REPORT (Mariana) */}
        {activeTab === 'clinico' && (
          <motion.div 
            key="clinico"
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -15 }}
            transition={{ duration: 0.25 }}
            className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start"
          >
            {/* COLUNA ESQUERDA — O RELATO DELA (5 COLS) */}
            <div className="lg:col-span-5 border border-[var(--c-line)] rounded-2xl bg-slate-950/20 p-6 space-y-6">
              <div className="flex items-center justify-between gap-4">
                <h2 className="font-serif text-lg text-[var(--c-text)] font-light flex items-center gap-2">
                  <Activity className="w-4 h-4 text-[var(--c-gold-soft)]" /> O desabafo dela
                </h2>
                <button 
                  onClick={() => setCompare(!compare)}
                  className={`px-3 py-1.5 rounded-full text-[10px] font-bold uppercase tracking-wider border transition-all ${
                    compare 
                      ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] border-transparent text-[#24160a]' 
                      : 'bg-transparent border-[var(--c-line)] text-[var(--c-dim)] hover:text-[var(--c-text)]'
                  }`}
                >
                  {compare ? 'Esconder Comparação' : 'Comparar Semanas'}
                </button>
              </div>

              {/* Transição Somática / Breathwork Status */}
              {((answers as any).somatic_checkin || (answers as any).somatic_checkout) && (
                <div className="p-4 rounded-xl border border-[var(--c-line)] bg-slate-900/40 space-y-3">
                  <div className="flex items-center gap-1.5 text-xs font-semibold text-[var(--c-gold-soft)] uppercase tracking-wider">
                    <Wind className="w-3.5 h-3.5 text-[var(--c-gold)]" />
                    <span>Transição Somática (Breathwork)</span>
                  </div>
                  <div className="grid grid-cols-2 gap-4 text-[10px]">
                    <div className="space-y-1">
                      <span className="text-[9px] uppercase tracking-widest text-[var(--c-dim)] block">Check-in (Pré)</span>
                      <div className="flex flex-wrap gap-1">
                        {(answers as any).somatic_checkin && (answers as any).somatic_checkin.length > 0 ? (
                          (answers as any).somatic_checkin.map((item: string) => (
                            <span key={item} className="px-2 py-0.5 rounded bg-red-950/20 border border-red-500/20 text-red-300">
                              {SOMATIC_LABELS[item] || item}
                            </span>
                          ))
                        ) : (
                          <span className="text-[var(--c-dim)] font-light italic">Nenhum sintoma marcado</span>
                        )}
                      </div>
                    </div>
                    <div className="space-y-1 border-l border-[var(--c-line)] pl-4">
                      <span className="text-[9px] uppercase tracking-widest text-[var(--c-dim)] block">Check-out (Pós)</span>
                      <div className="flex flex-wrap gap-1">
                        {(answers as any).somatic_checkout && (answers as any).somatic_checkout.length > 0 ? (
                          (answers as any).somatic_checkout.map((item: string) => (
                            <span key={item} className="px-2 py-0.5 rounded bg-emerald-950/20 border border-emerald-500/20 text-emerald-300">
                              {SOMATIC_LABELS[item] || item}
                            </span>
                          ))
                        ) : (
                          <span className="text-[var(--c-dim)] font-light italic">Nenhuma mudança marcada</span>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* Emocões */}
              {answers.f_emocoes && answers.f_emocoes.length > 0 && (
                <div className="flex flex-wrap gap-1.5">
                  {answers.f_emocoes.map((e) => (
                    <span key={e} className="px-2.5 py-1 border border-[var(--c-line)] rounded-full text-[10px] text-[var(--c-gold-soft)] bg-yellow-500/5">
                      {e}
                    </span>
                  ))}
                </div>
              )}

              {/* Respostas estruturadas */}
              <div className="space-y-5 h-[560px] overflow-y-auto pr-2 scrollbar-thin scrollbar-thumb-purple-900">
                {[
                  { key: 'q_chega', label: 'Como Chega', isText: true },
                  { key: 'q_trouxe', label: 'O Que Trouxe (Dor Raiz)', isText: true },
                  { key: 'q_energia', label: 'Dreno de Energia', isText: true, prev: PREV_SUBMISSIONS.q_energia },
                  { key: 'q_repete', label: 'Loops / Repetições', isText: true, prev: PREV_SUBMISSIONS.q_repete },
                  { key: 'q_corpo', label: 'O Corpo e o Sono', isText: true, prev: PREV_SUBMISSIONS.q_corpo },
                  { key: 'q_bem_faz', label: 'O Que Faz Bem (Refúgio)', isText: true },
                  { key: 'q_sonhos', label: 'Sonhos / Imagens', isText: true },
                  { key: 'q_intencao', label: 'Intenção do Ciclo', isText: true },
                  { key: 'q_palavra', label: 'Frase Âncora', isText: false }
                ].map((card) => {
                  const val = (answers as any)[card.key];
                  if (!val) return null;
                  return (
                    <div key={card.key} className="pb-4 border-b border-[var(--c-line)] space-y-1">
                      <span className="text-[9px] uppercase font-bold tracking-widest text-[var(--c-orchid)] block">{card.label}</span>
                      <p className="text-xs text-[var(--c-text)] leading-relaxed font-light">{val}</p>
                      
                      {compare && card.prev && (
                        <div className="mt-2 pl-3 border-l-2 border-indigo-500/40 text-[10px] text-[var(--c-dim)] font-light italic leading-relaxed">
                          <span className="text-indigo-400 font-medium">Na semana anterior:</span> {card.prev}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>

            {/* COLUNA DIREITA — EDITOR DE DIRECIONAMENTO (7 COLS) */}
            <div className="lg:col-span-7 border border-[var(--c-line)] rounded-2xl bg-gradient-to-b from-[var(--c-bg2)]/10 to-[var(--c-bg0)]/30 p-6 space-y-6">
              <h2 className="font-serif text-lg text-[var(--c-text)] font-light flex items-center gap-2">
                <FileText className="w-4 h-4 text-[var(--c-gold-soft)]" /> Escrever Relatório de Direcionamento
              </h2>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-2">Sessão Nº</label>
                  <div className="flex gap-1.5">
                    {[1, 2, 3, 4, 5].map((v) => (
                      <button
                        key={v}
                        onClick={() => handleFieldChange('r_num', v)}
                        className={`flex-1 py-2 font-mono text-xs font-bold rounded-lg border transition-all ${
                          r_num === v 
                            ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] border-transparent text-[#24160a]' 
                            : 'bg-transparent border-[var(--c-line)] text-[var(--c-dim)] hover:border-[var(--c-gold-soft)]'
                        }`}
                      >
                        0{v}
                      </button>
                    ))}
                  </div>
                </div>
                <div>
                  <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-2">Data do Envio</label>
                  <input 
                    type="text" 
                    value={r_data}
                    onChange={(e) => handleFieldChange('r_data', e.target.value)}
                    className="w-full text-xs p-2.5 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)]"
                  />
                </div>
              </div>

              {/* Ecos */}
              <div className="space-y-1.5">
                <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)]">Ecos da Semana Dela</label>
                <p className="text-[10px] font-light text-[var(--c-dim)] italic">Conecte as contradições do ego ou do sonho com as impressões do seu sentir sutil.</p>
                <textarea 
                  value={r_ecos}
                  onChange={(e) => handleFieldChange('r_ecos', e.target.value)}
                  rows={3}
                  className="w-full text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-xl focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)] font-light leading-relaxed resize-none"
                />
              </div>

              {/* Camadas chips */}
              <div className="space-y-2">
                <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)]">Camadas tratadas no SACM</label>
                <p className="text-[10px] font-light text-[var(--c-dim)] italic">Marque as faixas sutis que foram re-alinhadas energeticamente à distância.</p>
                <div className="flex flex-wrap gap-2 pt-1">
                  {CAMADAS_CHIPS.map((c) => {
                    const isSel = r_camadas.includes(c.key);
                    return (
                      <button
                        key={c.key}
                        onClick={() => toggleCamada(c.key)}
                        className={`flex items-center gap-2 px-3 py-2 border rounded-full text-xs transition-all ${
                          isSel 
                            ? 'bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] border-transparent text-[#24160a] font-bold shadow-md shadow-yellow-500/5' 
                            : 'bg-transparent border-[var(--c-line)] text-[var(--c-text)] hover:border-[var(--c-gold-soft)]'
                        }`}
                      >
                        <img src={c.icon} className="w-4 h-4 flex-none" alt="" />
                        <span>{c.title}</span>
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Síntese energética */}
              <div className="space-y-1.5">
                <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)]">Síntese do Trabalho Sutil</label>
                <textarea 
                  value={r_sintese}
                  onChange={(e) => handleFieldChange('r_sintese', e.target.value)}
                  rows={3}
                  className="w-full text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-xl focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)] font-light leading-relaxed resize-none"
                />
              </div>

              {/* Próximos passos */}
              <div className="space-y-2">
                <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)]">Os Próximos Passos dela (Ancoragem)</label>
                <p className="text-[10px] font-light text-[var(--c-dim)] italic">3 ações físicas, inegociáveis e práticas que ela precisa executar no físico.</p>
                <div className="space-y-2">
                  <input 
                    type="text" 
                    value={r_o1}
                    onChange={(e) => handleFieldChange('r_o1', e.target.value)}
                    placeholder="Passo prático 1"
                    className="w-full text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)]"
                  />
                  <input 
                    type="text" 
                    value={r_o2}
                    onChange={(e) => handleFieldChange('r_o2', e.target.value)}
                    placeholder="Passo prático 2"
                    className="w-full text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)]"
                  />
                  <input 
                    type="text" 
                    value={r_o3}
                    onChange={(e) => handleFieldChange('r_o3', e.target.value)}
                    placeholder="Passo prático 3 (opcional)"
                    className="w-full text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)]"
                  />
                </div>
              </div>

              {/* Fechamento */}
              <div className="space-y-1.5">
                <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)]">Mensagem de Fechamento</label>
                <textarea 
                  value={r_fechamento}
                  onChange={(e) => handleFieldChange('r_fechamento', e.target.value)}
                  rows={2}
                  className="w-full text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-xl focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)] font-light leading-relaxed resize-none"
                />
              </div>

              {/* Action buttons */}
              <div className="flex flex-col sm:flex-row gap-3 pt-4 border-t border-[var(--c-line)]">
                <button 
                  onClick={handleGerarRelatorio}
                  className="flex-1 py-4 rounded-full bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] font-bold text-xs uppercase tracking-wider shadow-lg shadow-yellow-500/10 hover:scale-[1.01] transition-all flex items-center justify-center gap-2 cursor-pointer"
                >
                  <ClipboardCheck className="w-4 h-4" /> Compilar e Copiar p/ WhatsApp
                </button>
                <button 
                  onClick={handleExportMarkdown}
                  className="py-4 px-6 rounded-full bg-slate-900 border border-[var(--c-line)] text-[var(--c-dim)] hover:text-[var(--c-text)] font-bold text-xs uppercase tracking-wider hover:bg-slate-800 transition-all flex items-center justify-center gap-2 cursor-pointer"
                >
                  <Download className="w-4 h-4" /> Exportar Laudo (.MD)
                </button>
              </div>

            </div>
          </motion.div>
        )}

        {/* TAB 2: MICÉLIO DE INSIGHTS */}
        {activeTab === 'micelio' && (
          <motion.div 
            key="micelio"
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -15 }}
            transition={{ duration: 0.25 }}
            className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start"
          >
            {/* ESQUERDA: GRAVAÇÃO E CONFIGURAÇÃO (5 COLS) */}
            <div className="lg:col-span-5 border border-[var(--c-line)] rounded-2xl bg-slate-950/20 p-6 space-y-6">
              <h2 className="font-serif text-lg text-[var(--c-text)] font-light flex items-center gap-2">
                <Mic className="w-5 h-5 text-[var(--c-gold-soft)]" /> Rastreamento do Sentir (Áudio)
              </h2>

              {/* Record Block */}
              <div className="border border-[var(--c-line)] rounded-xl bg-slate-900/30 p-6 flex flex-col items-center justify-center space-y-4">
                {recording ? (
                  <div className="flex flex-col items-center space-y-3">
                    <div className="relative">
                      <div className="w-16 h-16 rounded-full bg-red-500/20 flex items-center justify-center animate-pulse" />
                      <div className="absolute inset-0 w-16 h-16 rounded-full bg-red-600/10 animate-ping" />
                      <Mic className="w-6 h-6 text-red-500 absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" />
                    </div>
                    <span className="font-mono text-sm text-red-400 font-bold">{formatTime(recordingTime)}</span>
                    <span className="text-[10px] uppercase tracking-widest text-[var(--c-dim)]">Gravando seu sentir...</span>
                    
                    {/* Simulated Wave Animation */}
                    <div className="flex items-end justify-center gap-0.5 h-6">
                      {[...Array(12)].map((_, i) => (
                        <motion.div
                          key={i}
                          animate={{ height: [4, Math.random() * 20 + 4, 4] }}
                          transition={{ repeat: Infinity, duration: 0.5 + Math.random() * 0.5 }}
                          className="w-0.75 bg-[var(--c-gold)] rounded-full"
                        />
                      ))}
                    </div>

                    <button 
                      onClick={stopRecording}
                      className="px-5 py-2.5 bg-red-600 hover:bg-red-500 text-white text-xs font-bold uppercase rounded-full flex items-center gap-1.5 cursor-pointer"
                    >
                      <Square className="w-3.5 h-3.5" /> Parar Gravação
                    </button>
                  </div>
                ) : (
                  <div className="flex flex-col items-center space-y-3">
                    <button 
                      onClick={startRecording}
                      className="w-16 h-16 rounded-full border border-[var(--c-line)] hover:border-[var(--c-gold-soft)] bg-yellow-500/5 hover:bg-yellow-500/10 flex items-center justify-center transition-all cursor-pointer group"
                    >
                      <Mic className="w-6 h-6 text-[var(--c-gold-soft)] group-hover:scale-105 transition-all" />
                    </button>
                    <span className="text-xs text-[var(--c-text)] font-medium">Iniciar Nova Gravação</span>
                    <span className="text-[9px] text-[var(--c-dim)] max-w-[200px] text-center">Fale livremente sobre seus insights clínicos ou canalizações.</span>
                  </div>
                )}

                {/* Audio playback */}
                {audioUrl && !recording && (
                  <div className="w-full pt-4 border-t border-[var(--c-line)] flex flex-col items-center space-y-3">
                    <div className="flex items-center justify-center gap-2 w-full">
                      <Volume2 className="w-4 h-4 text-[var(--c-gold-soft)]" />
                      <audio src={audioUrl} controls className="h-8 max-w-[220px]" />
                    </div>
                    <div className="flex gap-2">
                      <button 
                        onClick={deleteRecording}
                        className="px-3 py-1.5 bg-transparent border border-red-500/30 text-red-400 hover:bg-red-950/20 text-[10px] font-bold uppercase rounded-full flex items-center gap-1.5 cursor-pointer"
                      >
                        <Trash2 className="w-3.5 h-3.5" /> Descartar
                      </button>
                    </div>
                  </div>
                )}
              </div>

              {/* Title & Category Config */}
              <div className="space-y-4 pt-2">
                <div>
                  <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1.5">Título do Insight</label>
                  <input 
                    type="text" 
                    value={insightTitle}
                    onChange={(e) => setInsightTitle(e.target.value)}
                    className="w-full text-xs p-2.5 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)]"
                  />
                </div>
                <div>
                  <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1.5">Categoria da Egrégora</label>
                  <select 
                    value={insightCategory}
                    onChange={(e) => setInsightCategory(e.target.value)}
                    className="w-full text-xs p-2.5 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)]"
                  >
                    {['Espiritualidade', 'Apometria', 'Psicologia', 'Nutricao', 'Magia', 'Desenvolvimento Pessoal', 'Outros'].map(c => (
                      <option key={c} value={c} className="bg-[#0b0826]">{c}</option>
                    ))}
                  </select>
                </div>
              </div>
            </div>

            {/* DIREITA: COMPANHEIRO CHAT (7 COLS) */}
            <div className="lg:col-span-7 border border-[var(--c-line)] rounded-2xl bg-gradient-to-b from-[var(--c-bg2)]/10 to-[var(--c-bg0)]/30 p-6 flex flex-col h-[640px]">
              
              <div className="flex items-center justify-between pb-3 border-b border-[var(--c-line)] mb-4">
                <h2 className="font-serif text-lg text-[var(--c-text)] font-light flex items-center gap-2">
                  <Brain className="w-5 h-5 text-[var(--c-gold-soft)]" /> Consultor e Estruturador
                </h2>
                <button 
                  onClick={handleLimparInsights}
                  className="text-[10px] text-red-400 hover:text-red-300 font-bold uppercase tracking-wider flex items-center gap-1 cursor-pointer"
                >
                  <Trash2 className="w-3.5 h-3.5" /> Limpar Histórico
                </button>
              </div>

              {/* Chat Feed */}
              <div className="flex-1 overflow-y-auto space-y-4 pr-1 mb-4 scrollbar-thin scrollbar-thumb-purple-950">
                {messages.map((m, idx) => (
                  <div 
                    key={idx} 
                    className={`flex flex-col max-w-[85%] ${
                      m.sender === 'leo' 
                        ? 'ml-auto items-end' 
                        : 'mr-auto items-start'
                    }`}
                  >
                    <span className="text-[8px] uppercase tracking-widest text-[var(--c-dim)] mb-1">
                      {m.sender === 'leo' ? 'Mestre Leo' : 'Antigravity'}
                    </span>
                    <div 
                      className={`p-3.5 rounded-2xl text-xs leading-relaxed font-light ${
                        m.sender === 'leo'
                          ? 'bg-slate-900/60 border border-[var(--c-gold)] text-[var(--c-text)] rounded-tr-none'
                          : 'bg-indigo-950/20 border border-[var(--c-line)] text-[var(--c-dim)] rounded-tl-none'
                      }`}
                    >
                      {m.isMarkdown ? (
                        <div className="space-y-3 whitespace-pre-wrap font-mono text-[11px]">
                          {m.text}
                        </div>
                      ) : (
                        <p>{m.text}</p>
                      )}
                    </div>

                    {/* Export Action for structured insights */}
                    {m.sender === 'antigravity' && m.isMarkdown && m.text.includes('---') && (
                      <button
                        onClick={() => handleExportSingleInsight(m.text, idx)}
                        className="mt-2 text-[10px] font-bold text-[var(--c-gold-soft)] hover:underline flex items-center gap-1 cursor-pointer"
                      >
                        <Download className="w-3 h-3" /> Salvar na pasta context/insights/
                      </button>
                    )}
                  </div>
                ))}
                
                {loadingCompanion && (
                  <div className="flex items-center gap-2 text-xs text-[var(--c-dim)] animate-pulse">
                    <Brain className="w-4 h-4 animate-spin text-[var(--c-gold-soft)]" />
                    <span>Conectando com o micélio Arcturiano...</span>
                  </div>
                )}
              </div>

              {/* Chat Input */}
              <div className="flex gap-2.5 pt-4 border-t border-[var(--c-line)]">
                <textarea 
                  value={insightText}
                  onChange={(e) => setInsightText(e.target.value)}
                  placeholder="Escreva seu insight ou notas para o áudio..."
                  className="flex-1 text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-xl focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)] font-light leading-relaxed resize-none h-14"
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' && !e.shiftKey) {
                      e.preventDefault();
                      handleSendInsight();
                    }
                  }}
                />
                <button 
                  onClick={handleSendInsight}
                  className="w-14 h-14 rounded-xl bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] flex items-center justify-center hover:scale-102 transition-all cursor-pointer"
                >
                  <Send className="w-5 h-5" />
                </button>
              </div>

            </div>
          </motion.div>
        )}

        {/* TAB 3: PREMIUM END-OF-CYCLE REPORT */}
        {activeTab === 'alta' && (
          <motion.div 
            key="alta"
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -15 }}
            transition={{ duration: 0.25 }}
            className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start"
          >
            {/* CONFIGURAÇÃO DO LAUDO PREMIUM (7 COLS) */}
            <div className="lg:col-span-7 border border-[var(--c-line)] rounded-2xl bg-gradient-to-b from-[var(--c-bg2)]/10 to-[var(--c-bg0)]/30 p-6 space-y-6 h-[760px] overflow-y-auto pr-2 scrollbar-thin scrollbar-thumb-purple-950">
              
              <div className="flex items-center justify-between border-b border-[var(--c-line)] pb-3">
                <h2 className="font-serif text-lg text-[var(--c-text)] font-light flex items-center gap-2">
                  <ShieldCheck className="w-5 h-5 text-[var(--c-gold-soft)]" /> Consolidar Laudo Premium
                </h2>
              </div>

              {/* Identificação Geral */}
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-2">Nome da Cliente</label>
                  <input 
                    type="text" 
                    value={f_nome}
                    onChange={(e) => setNome(e.target.value)}
                    className="w-full text-xs p-2.5 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)]"
                  />
                </div>
                <div>
                  <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-2">Período do Ciclo</label>
                  <input 
                    type="text" 
                    value={c_periodo}
                    onChange={(e) => setPeriodo(e.target.value)}
                    className="w-full text-xs p-2.5 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)]"
                  />
                </div>
              </div>

              {/* Perfil Cósmico / Astrológico / Kin */}
              <div className="space-y-4 border-t border-[var(--c-line)] pt-4">
                <h3 className="text-xs font-bold uppercase tracking-wider text-[var(--c-orchid)]">Assinatura Cósmica & Oráculo</h3>
                
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">Oráculo Galáctico (Kin)</label>
                    <input 
                      type="text" 
                      value={c_kin}
                      onChange={(e) => setKin(e.target.value)}
                      className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)]"
                    />
                  </div>
                  <div>
                    <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">Distribuição Elemental</label>
                    <input 
                      type="text" 
                      value={c_elementos}
                      onChange={(e) => setElementos(e.target.value)}
                      className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)]"
                    />
                  </div>
                </div>

                <div className="grid grid-cols-3 gap-2">
                  <div>
                    <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">Signo Solar</label>
                    <input 
                      type="text" 
                      value={c_signo_sol}
                      onChange={(e) => setSignoSol(e.target.value)}
                      className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)]"
                    />
                  </div>
                  <div>
                    <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">Lua</label>
                    <input 
                      type="text" 
                      value={c_signo_lua}
                      onChange={(e) => setSignoLua(e.target.value)}
                      className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)]"
                    />
                  </div>
                  <div>
                    <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">Ascendente</label>
                    <input 
                      type="text" 
                      value={c_signo_asc}
                      onChange={(e) => setSignoAsc(e.target.value)}
                      className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)]"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">Direcionamento de Força (Cósmico)</label>
                  <textarea 
                    value={c_direcionamento_forca}
                    onChange={(e) => setDirecionamentoForca(e.target.value)}
                    rows={2}
                    className="w-full text-xs p-2.5 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)] font-light leading-relaxed resize-none"
                  />
                </div>
              </div>

              {/* Perfil Cabalístico */}
              <div className="space-y-4 border-t border-[var(--c-line)] pt-4">
                <h3 className="text-xs font-bold uppercase tracking-wider text-[var(--c-orchid)] font-serif">Perfil Cabalístico (Vibração Numérica)</h3>
                
                <div className="grid grid-cols-3 gap-2">
                  <div>
                    <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">Número de Destino</label>
                    <input 
                      type="text" 
                      value={c_cabala_destino}
                      onChange={(e) => setCabalaDestino(e.target.value)}
                      className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)]"
                    />
                  </div>
                  <div>
                    <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">Número de Expressão</label>
                    <input 
                      type="text" 
                      value={c_cabala_expressao}
                      onChange={(e) => setCabalaExpressao(e.target.value)}
                      className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)]"
                    />
                  </div>
                  <div>
                    <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">Número de Alma</label>
                    <input 
                      type="text" 
                      value={c_cabala_alma}
                      onChange={(e) => setCabalaAlma(e.target.value)}
                      className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)]"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">O Caminho do Destino (Análise Numerológica)</label>
                  <textarea 
                    value={c_cabala_direcionamento}
                    onChange={(e) => setCabalaDirecionamento(e.target.value)}
                    rows={3}
                    className="w-full text-xs p-2.5 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)] font-light leading-relaxed"
                  />
                </div>
              </div>

              {/* Análise de Persona e História Reescrita */}
              <div className="space-y-4 border-t border-[var(--c-line)] pt-4">
                <h3 className="text-xs font-bold uppercase tracking-wider text-[var(--c-orchid)]">A História Reescrita (Persona vs. Potencial)</h3>
                
                <div>
                  <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">A Narrativa da Persona (A História que Ela Contou)</label>
                  <textarea 
                    value={c_analise_persona}
                    onChange={(e) => setAnalisePersona(e.target.value)}
                    rows={3}
                    className="w-full text-xs p-2.5 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)] font-light leading-relaxed"
                  />
                </div>

                <div>
                  <label className="block text-[9px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1">A Reescrita da História (A Chave de Transcendência)</label>
                  <textarea 
                    value={c_historia_reescrita}
                    onChange={(e) => setHistoriaReescrita(e.target.value)}
                    rows={4}
                    className="w-full text-xs p-2.5 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] text-[var(--c-text)] font-light leading-relaxed"
                  />
                </div>
              </div>

              {/* 5 Weeks inputs (Apresentado, Trabalhado, Integração) */}
              <div className="space-y-6 border-t border-[var(--c-line)] pt-4">
                <h3 className="text-xs font-bold uppercase tracking-wider text-[var(--c-orchid)]">Detalhamento das 5 Semanas</h3>
                
                {[
                  { 
                    num: 1, 
                    label: 'Semana 01 — Diagnóstico e Rastreamento Somático', 
                    apresentado: w1_apresentado, setApres: setW1Apresentado,
                    trabalhado: w1_trabalhado, setTrab: setW1Trabalhado,
                    integracao: w1_integracao, setInteg: setW1Integracao 
                  },
                  { 
                    num: 2, 
                    label: 'Semana 02 — Corte de Vínculos e Criança Interior', 
                    apresentado: w2_apresentado, setApres: setW2Apresentado,
                    trabalhado: w2_trabalhado, setTrab: setW2Trabalhado,
                    integracao: w2_integracao, setInteg: setW2Integracao 
                  },
                  { 
                    num: 3, 
                    label: 'Semana 03 — Expressão e Alinhamento Laringeu', 
                    apresentado: w3_apresentado, setApres: setW3Apresentado,
                    trabalhado: w3_trabalhado, setTrab: setW3Trabalhado,
                    integracao: w3_integracao, setInteg: setW3Integracao 
                  },
                  { 
                    num: 4, 
                    label: 'Semana 04 — Integração de Sombra / Multidimensional', 
                    apresentado: w4_apresentado, setApres: setW4Apresentado,
                    trabalhado: w4_trabalhado, setTrab: setW4Trabalhado,
                    integracao: w4_integracao, setInteg: setW4Integracao 
                  },
                  { 
                    num: 5, 
                    label: 'Semana 05 — Alta, Selagem e Escudo Ativo', 
                    apresentado: w5_apresentado, setApres: setW5Apresentado,
                    trabalhado: w5_trabalhado, setTrab: setW5Trabalhado,
                    integracao: w5_integracao, setInteg: setW5Integracao 
                  }
                ].map((s) => (
                  <div key={s.num} className="p-4 border border-[var(--c-line)] rounded-xl bg-slate-900/20 space-y-3">
                    <span className="text-[10px] font-bold uppercase tracking-widest text-[var(--c-gold-soft)]">{s.label}</span>
                    
                    <div className="space-y-2">
                      <div>
                        <label className="block text-[9px] uppercase tracking-wider text-[var(--c-dim)]">O que ela Apresentou</label>
                        <input 
                          type="text" 
                          value={s.apresentado} 
                          onChange={(e) => s.setApres(e.target.value)} 
                          className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg text-[var(--c-text)] mt-1"
                        />
                      </div>
                      <div>
                        <label className="block text-[9px] uppercase tracking-wider text-[var(--c-dim)]">O que foi Trabalhado no Sutil</label>
                        <input 
                          type="text" 
                          value={s.trabalhado} 
                          onChange={(e) => s.setTrab(e.target.value)} 
                          className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg text-[var(--c-text)] mt-1"
                        />
                      </div>
                      <div>
                        <label className="block text-[9px] uppercase tracking-wider text-[var(--c-dim)]">Mensagem de Integração</label>
                        <input 
                          type="text" 
                          value={s.integracao} 
                          onChange={(e) => s.setInteg(e.target.value)} 
                          className="w-full text-xs p-2 border border-[var(--c-line)] bg-slate-950/40 rounded-lg text-[var(--c-text)] mt-1"
                        />
                      </div>
                    </div>
                  </div>
                ))}
              </div>

              {/* Visão de Futuro e Manual de Autonomia */}
              <div className="space-y-4 border-t border-[var(--c-line)] pt-4">
                <div className="space-y-1.5">
                  <label className="block text-xs font-bold uppercase tracking-wider text-[var(--c-orchid)] flex items-center gap-1">
                    <Compass className="w-4 h-4" /> Visão de Futuro Pós-Terapia (O Novo Console)
                  </label>
                  <textarea 
                    value={c_visao_futuro}
                    onChange={(e) => setVisaoFuturo(e.target.value)}
                    rows={3}
                    className="w-full text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-xl focus:border-[var(--c-gold)] text-[var(--c-text)] font-light leading-relaxed"
                  />
                </div>
                
                <div className="space-y-1.5">
                  <label className="block text-xs font-bold uppercase tracking-wider text-[var(--c-orchid)] flex items-center gap-1">
                    <ShieldCheck className="w-4 h-4" /> Manual de Autonomia (Ancoragem na Matéria)
                  </label>
                  <textarea 
                    value={c_autonomia}
                    onChange={(e) => setAutonomia(e.target.value)}
                    rows={4}
                    className="w-full text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-xl focus:border-[var(--c-gold)] text-[var(--c-text)] font-light leading-relaxed font-mono"
                  />
                </div>
              </div>

              <div className="pt-4 border-t border-[var(--c-line)] pb-4">
                <button 
                  onClick={handleGerarLaudoAlta}
                  className="w-full py-4 rounded-full bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] font-bold text-xs uppercase tracking-wider shadow-lg shadow-yellow-500/10 hover:scale-[1.01] transition-all flex items-center justify-center gap-2 cursor-pointer"
                >
                  <Download className="w-4 h-4" /> Gerar e Exportar Dossiê de Alta Premium (.MD)
                </button>
              </div>
            </div>

            {/* PREVISUALIZAÇÃO PREMIUM (5 COLS) */}
            <div className="lg:col-span-5 border border-[var(--c-line)] rounded-2xl bg-slate-950/40 p-6 space-y-6 h-[760px] overflow-y-auto scrollbar-thin scrollbar-thumb-purple-950 font-serif leading-relaxed text-xs">
              <div className="text-center pb-4 border-b border-[var(--c-line)]">
                <span className="text-[8px] uppercase tracking-widest text-[var(--c-gold-soft)] font-bold">Pré-visualização do Dossiê final</span>
                <h3 className="font-serif text-lg font-light text-[var(--c-text)] mt-1">Laudo Premium de Ciclo</h3>
              </div>
              
              <div className="space-y-6 text-[var(--c-text)] font-light text-justify">
                <div>
                  <span className="text-[8px] uppercase font-bold tracking-widest text-[var(--c-orchid)] block font-sans">Dossiê</span>
                  <p className="mt-1">**Cliente:** {f_nome}</p>
                  <p>**Período do Ciclo:** {c_periodo}</p>
                </div>
                
                <div className="space-y-1.5 border-b border-[var(--c-line)] pb-4">
                  <span className="text-[8px] uppercase font-bold tracking-widest text-[var(--c-orchid)] block font-sans font-serif">1. Assinatura Cósmica & Manual do Ser</span>
                  <p className="text-[11px] font-sans">**Oráculo Galáctico:** {c_kin}</p>
                  <p className="text-[11px] font-sans">**Astrologia:** Sol em {c_signo_sol} | Lua em {c_signo_lua} | Ascendente em {c_signo_asc}</p>
                  <p className="text-[11px] font-sans">**Elementos:** {c_elementos}</p>
                  <p className="text-[11px] font-sans">**Vibração Cabalística:** Destino {c_cabala_destino} | Expressão {c_cabala_expressao} | Alma {c_cabala_alma}</p>
                  <p className="italic text-[11px] mt-2 bg-slate-950/20 p-2.5 rounded-lg border border-[var(--c-line)]">"{c_cabala_direcionamento}"</p>
                </div>

                <div className="space-y-1.5 border-b border-[var(--c-line)] pb-4">
                  <span className="text-[8px] uppercase font-bold tracking-widest text-[var(--c-orchid)] block font-sans">2. A História Reescrita (Persona vs. Potencial)</span>
                  <p className="font-bold text-[10px] text-[var(--c-dim)] font-sans">A Narrativa da Persona:</p>
                  <p className="text-[11px] italic">"{c_analise_persona}"</p>
                  <p className="font-bold text-[10px] text-[var(--c-gold-soft)] font-sans mt-2">A Chave de Transcendência:</p>
                  <p className="text-[11px] font-medium">"{c_historia_reescrita}"</p>
                </div>

                <div className="space-y-4 border-b border-[var(--c-line)] pb-4">
                  <span className="text-[8px] uppercase font-bold tracking-widest text-[var(--c-orchid)] block font-sans">3. Detalhamento Semanal</span>
                  <div className="space-y-3 text-[11px] font-sans">
                    <div>
                      <p className="font-bold text-[var(--c-gold-soft)]">Semana 1</p>
                      <p>• *Apresentado:* {w1_apresentado}</p>
                      <p>• *Trabalhado:* {w1_trabalhado}</p>
                      <p className="italic">• *Mensagem:* "{w1_integracao}"</p>
                    </div>
                    <div>
                      <p className="font-bold text-[var(--c-gold-soft)]">Semana 2</p>
                      <p>• *Apresentado:* {w2_apresentado}</p>
                      <p>• *Trabalhado:* {w2_trabalhado}</p>
                      <p className="italic">• *Mensagem:* "{w2_integracao}"</p>
                    </div>
                    <div>
                      <p className="font-bold text-[var(--c-gold-soft)]">Semana 3</p>
                      <p>• *Apresentado:* {w3_apresentado}</p>
                      <p>• *Trabalhado:* {w3_trabalhado}</p>
                      <p className="italic">• *Mensagem:* "{w3_integracao}"</p>
                    </div>
                    <div>
                      <p className="font-bold text-[var(--c-gold-soft)]">Semana 4</p>
                      <p>• *Apresentado:* {w4_apresentado}</p>
                      <p>• *Trabalhado:* {w4_trabalhado}</p>
                      <p className="italic">• *Mensagem:* "{w4_integracao}"</p>
                    </div>
                    <div>
                      <p className="font-bold text-[var(--c-gold-soft)]">Semana 5</p>
                      <p>• *Apresentado:* {w5_apresentado}</p>
                      <p>• *Trabalhado:* {w5_trabalhado}</p>
                      <p className="italic">• *Mensagem:* "{w5_integracao}"</p>
                    </div>
                  </div>
                </div>

                <div className="space-y-1.5 border-b border-[var(--c-line)] pb-4">
                  <span className="text-[8px] uppercase font-bold tracking-widest text-[var(--c-orchid)] block font-sans">4. Visão de Futuro</span>
                  <p className="text-[11px]">{c_visao_futuro}</p>
                </div>

                <div className="space-y-1.5">
                  <span className="text-[8px] uppercase font-bold tracking-widest text-[var(--c-orchid)] block font-sans">5. Manual de Autonomia</span>
                  <p className="whitespace-pre-wrap font-mono text-[10px] bg-slate-950/30 p-2.5 rounded-lg border border-[var(--c-line)]">{c_autonomia}</p>
                </div>
              </div>
            </div>
          </motion.div>
        )}

      </AnimatePresence>

    </div>
  );
}
