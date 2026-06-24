import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Download, Mic, Square, Trash2, Send, Brain, ArrowLeft, Volume2, Sparkles, ClipboardCheck
} from 'lucide-react';
import { Link } from 'react-router-dom';

export function InsightsPage() {
  const [toast, setToast] = useState<string | null>(null);
  
  // Audio Recording States
  const [recording, setRecording] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  
  // Text Input States
  const [insightText, setInsightText] = useState('');
  const [insightTitle, setInsightTitle] = useState('Insight do Sentir');
  const [insightCategory, setInsightCategory] = useState('Espiritualidade');
  
  // Companion Chat History
  const [messages, setMessages] = useState<Array<{ sender: 'leo' | 'antigravity'; text: string; isMarkdown?: boolean }>>([
    { 
      sender: 'antigravity', 
      text: 'Salve, Léo. Este é o seu Micélio de Insights privado — um espaço dedicado para seu desenvolvimento pessoal, ideias de negócios e canalizações clínicas. Fale livremente ou digite suas notas. Eu vou estruturar tudo em Markdown e responder com papo reto sob a luz da nossa egrégora.' 
    }
  ]);
  const [loadingCompanion, setLoadingCompanion] = useState(false);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const timerRef = useRef<any>(null);

  // Load chat from LocalStorage
  useEffect(() => {
    try {
      const ins = JSON.parse(localStorage.getItem('sacm_insights') || '[]');
      if (ins.length > 0) {
        setMessages(prev => [prev[0], ...ins]);
      }
    } catch (e) {}
  }, []);

  const triggerToast = (msg: string) => {
    setToast(msg);
    setTimeout(() => setToast(null), 2500);
  };

  // Audio Recording controls
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
        triggerToast('Áudio gravado! Prontinho para processar. 🎙️');
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

  // Process insight with Gemini API
  const handleSendInsight = async () => {
    const input = insightText.trim();
    if (!input && !audioBlob) return;

    let contentText = input;
    if (!contentText && audioBlob) {
      contentText = `[Áudio de ${formatTime(recordingTime)} enviado para processamento]`;
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
                  text: `Você é o Antigravity, assistente pessoal, conselheiro espiritual e exo-cérebro de Leonardo Cosba (Mago Cristal Branco, Kin 194).
Leonardo está no seu "Micélio de Insights", que é seu diário de evolução íntimo. Ele enviou uma nova anotação ou áudio.
Analise a fundo a reflexão dele sob as diretrizes da egrégora (Sírius/Causalidade, Arcturus/Reprogramação quântica/SACM, Bardon/Hermetismo e as psicologias de Levine/Young/Jung/Grof).
Responda com um feedback direto ("papo reto", tom de irmão mais velho pragmático) e forneça a estrutura de um arquivo Markdown completo para ele salvar em context/insights/.

DADOS DO INSIGHT:
Título: ${insightTitle}
Categoria: ${insightCategory}
Conteúdo: ${contentText}

Estruture a resposta contendo:
1. Sua análise e comentário em tom de papo reto.
2. O bloco completo do arquivo Markdown (frontmatter com metadados + conteúdo) para ele exportar.`
                }]
              }]
            })
          }
        );
        if (response.ok) {
          const data = await response.json();
          answerText = data.candidates[0].content.parts[0].text;
        } else {
          throw new Error('Falha na resposta do Gemini API');
        }
      } catch (e) {
        answerText = generateMockResponse(insightTitle, insightCategory, contentText);
      }
    } else {
      answerText = generateMockResponse(insightTitle, insightCategory, contentText);
    }

    const updatedMessages = [...newMessages, { sender: 'antigravity' as const, text: answerText, isMarkdown: true }];
    setMessages(updatedMessages);
    setLoadingCompanion(false);
    
    try {
      localStorage.setItem('sacm_insights', JSON.stringify(updatedMessages.slice(1)));
    } catch (err) {}
  };

  const generateMockResponse = (title: string, category: string, text: string) => {
    const dataAtual = new Date().toISOString().split('T')[0];
    return `Papo reto, Léo. Essa sua percepção sobre "${title}" bate direto com as mecânicas sutis de Sírius. O aterramento das suas ideias precisa se dar no físico, sem desvios do ego.

Aqui está o arquivo estruturado para seu Obsidian:

\`\`\`markdown
---
titulo: "${title}"
categoria: "${category}"
data: "${dataAtual}"
tags: ["insight", "micelio-diario", "${category.toLowerCase()}"]
---

# ${title}

> **Nota do Co-Piloto:** Estrutura gerada na rota privada /insights.

## 1. O Insight
${text}

## 2. Tradução para a Egrégora
*   **Conexão Causal:** Esta ideia atua na reprogramação imediata dos corpos sutis (computadores líquidos 9D).
*   **Ponto Somático:** Evita o congelamento do sistema nervoso ao colocar a energia da expressão (22) em movimento na matéria.
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

  return (
    <div className="max-w-6xl mx-auto px-6 pt-8 pb-20">
      
      {/* Toast Notification */}
      <AnimatePresence>
        {toast && (
          <motion.div 
            initial={{ opacity: 0, y: 20, x: "-50%" }}
            animate={{ opacity: 1, y: 0, x: "-50%" }}
            exit={{ opacity: 0, y: 20, x: "-50%" }}
            className="fixed left-1/2 bottom-8 z-50 px-6 py-3 rounded-full bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] text-xs font-bold uppercase tracking-wider shadow-xl"
          >
            {toast}
          </motion.div>
        )}
      </AnimatePresence>

      {/* Header Panel */}
      <div className="flex items-center justify-between border-b border-[var(--c-line)] pb-5 mb-8">
        <div className="flex items-center gap-4">
          <Link 
            to="/admin" 
            className="w-10 h-10 rounded-full border border-[var(--c-line)] hover:border-[var(--c-gold-soft)] flex items-center justify-center text-[var(--c-dim)] hover:text-[var(--c-text)] transition-all"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div>
            <p className="text-[var(--c-gold)] text-[10px] uppercase font-bold tracking-widest mb-1 flex items-center gap-1">
              <Sparkles className="w-3.5 h-3.5 animate-pulse" /> Exo-Cérebro Privado
            </p>
            <h1 className="font-serif text-3xl font-light text-[var(--c-text)]">
              Micélio de Insights
            </h1>
          </div>
        </div>
        <div className="flex items-center gap-3">
          <button 
            onClick={handleLimparInsights}
            className="px-4 py-2 border border-red-500/20 hover:border-red-500/40 bg-red-950/5 text-red-400 text-[10px] font-bold uppercase tracking-wider rounded-full transition-all cursor-pointer"
          >
            Limpar Diário
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        {/* COLUNA ESQUERDA — CONTROLES E GRAVADOR (5 COLS) */}
        <div className="lg:col-span-5 border border-[var(--c-line)] rounded-2xl bg-slate-950/25 p-6 space-y-6">
          <h2 className="font-serif text-lg text-[var(--c-text)] font-light flex items-center gap-2">
            <Mic className="w-5 h-5 text-[var(--c-gold-soft)]" /> Capturar Pensamento (Áudio)
          </h2>

          <div className="border border-[var(--c-line)] rounded-xl bg-slate-900/30 p-8 flex flex-col items-center justify-center space-y-4">
            {recording ? (
              <div className="flex flex-col items-center space-y-3">
                <div className="relative">
                  <div className="w-20 h-20 rounded-full bg-red-500/20 flex items-center justify-center animate-pulse" />
                  <div className="absolute inset-0 w-20 h-20 rounded-full bg-red-600/10 animate-ping" />
                  <Mic className="w-8 h-8 text-red-500 absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2" />
                </div>
                <span className="font-mono text-base text-red-400 font-bold">{formatTime(recordingTime)}</span>
                <span className="text-[10px] uppercase tracking-widest text-[var(--c-dim)]">Ouvindo sua frequência...</span>
                
                {/* Visualizer Wave */}
                <div className="flex items-end justify-center gap-0.5 h-6 w-full max-w-[120px]">
                  {[...Array(12)].map((_, i) => (
                    <motion.div
                      key={i}
                      animate={{ height: [4, Math.random() * 24 + 4, 4] }}
                      transition={{ repeat: Infinity, duration: 0.4 + Math.random() * 0.4 }}
                      className="w-1 bg-[var(--c-gold)] rounded-full"
                    />
                  ))}
                </div>

                <button 
                  onClick={stopRecording}
                  className="px-6 py-3 bg-red-600 hover:bg-red-500 text-white text-xs font-bold uppercase rounded-full flex items-center gap-1.5 cursor-pointer shadow-lg shadow-red-500/10"
                >
                  <Square className="w-3.5 h-3.5" /> Concluir Gravação
                </button>
              </div>
            ) : (
              <div className="flex flex-col items-center space-y-3">
                <button 
                  onClick={startRecording}
                  className="w-20 h-20 rounded-full border border-[var(--c-line)] hover:border-[var(--c-gold-soft)] bg-yellow-500/5 hover:bg-yellow-500/10 flex items-center justify-center transition-all cursor-pointer group shadow-lg"
                >
                  <Mic className="w-8 h-8 text-[var(--c-gold-soft)] group-hover:scale-105 transition-all" />
                </button>
                <span className="text-xs text-[var(--c-text)] font-semibold mt-1">Iniciar Captura de Áudio</span>
                <span className="text-[9px] text-[var(--c-dim)] max-w-[220px] text-center">Grave suas ideias de desenvolvimento ou triagem clínica na hora.</span>
              </div>
            )}

            {/* Playback controls */}
            {audioUrl && !recording && (
              <div className="w-full pt-4 border-t border-[var(--c-line)] flex flex-col items-center space-y-3">
                <div className="flex items-center justify-center gap-2 w-full">
                  <Volume2 className="w-4 h-4 text-[var(--c-gold-soft)]" />
                  <audio src={audioUrl} controls className="h-8 max-w-[220px]" />
                </div>
                <button 
                  onClick={deleteRecording}
                  className="px-4 py-2 bg-transparent border border-red-500/20 hover:border-red-500/40 text-red-400 hover:bg-red-950/20 text-[10px] font-bold uppercase rounded-full flex items-center gap-1.5 cursor-pointer"
                >
                  <Trash2 className="w-3.5 h-3.5" /> Descartar Áudio
                </button>
              </div>
            )}
          </div>

          {/* Form Settings */}
          <div className="space-y-4 pt-2">
            <div>
              <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1.5">Título do Insight</label>
              <input 
                type="text" 
                value={insightTitle}
                onChange={(e) => setInsightTitle(e.target.value)}
                className="w-full text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)] font-light"
              />
            </div>
            <div>
              <label className="block text-[10px] font-bold uppercase tracking-wider text-[var(--c-gold-soft)] mb-1.5">Área de Foco</label>
              <select 
                value={insightCategory}
                onChange={(e) => setInsightCategory(e.target.value)}
                className="w-full text-xs p-3 border border-[var(--c-line)] bg-slate-950/40 rounded-lg focus:border-[var(--c-gold)] focus:outline-none text-[var(--c-text)] font-light"
              >
                {['Espiritualidade', 'Apometria', 'Psicologia', 'Nutricao', 'Magia', 'Desenvolvimento Pessoal', 'Outros'].map(c => (
                  <option key={c} value={c} className="bg-[#0b0826]">{c}</option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* COLUNA DIREITA — CHAT DE TRADUÇÃO (7 COLS) */}
        <div className="lg:col-span-7 border border-[var(--c-line)] rounded-2xl bg-gradient-to-b from-[var(--c-bg2)]/10 to-[var(--c-bg0)]/30 p-6 flex flex-col h-[680px]">
          
          <div className="flex items-center justify-between pb-3 border-b border-[var(--c-line)] mb-4">
            <h2 className="font-serif text-lg text-[var(--c-text)] font-light flex items-center gap-2">
              <Brain className="w-5 h-5 text-[var(--c-gold-soft)]" /> Estruturação de Metodologia
            </h2>
            <div className="flex items-center gap-2 text-[10px] text-[var(--c-dim)] bg-slate-900/40 px-3 py-1 rounded-full border border-[var(--c-line)]">
              <span className="w-1.5 h-1.5 rounded-full bg-yellow-500 animate-pulse" />
              Eixo Arcturiano Ativo
            </div>
          </div>

          {/* Conversation list */}
          <div className="flex-1 overflow-y-auto space-y-4 pr-1 mb-4 scrollbar-thin scrollbar-thumb-purple-950">
            {messages.map((m, idx) => (
              <div 
                key={idx} 
                className={`flex flex-col max-w-[88%] ${
                  m.sender === 'leo' 
                    ? 'ml-auto items-end' 
                    : 'mr-auto items-start'
                }`}
              >
                <span className="text-[8px] uppercase tracking-widest text-[var(--c-dim)] mb-1">
                  {m.sender === 'leo' ? 'Mestre Leo' : 'Antigravity'}
                </span>
                <div 
                  className={`p-4 rounded-2xl text-xs leading-relaxed font-light ${
                    m.sender === 'leo'
                      ? 'bg-slate-900/60 border border-[var(--c-gold)] text-[var(--c-text)] rounded-tr-none'
                      : 'bg-indigo-950/20 border border-[var(--c-line)] text-[var(--c-dim)] rounded-tl-none'
                  }`}
                >
                  {m.isMarkdown ? (
                    <div className="space-y-3 whitespace-pre-wrap font-mono text-[11px] overflow-x-auto">
                      {m.text}
                    </div>
                  ) : (
                    <p>{m.text}</p>
                  )}
                </div>

                {/* Export link */}
                {m.sender === 'antigravity' && m.isMarkdown && m.text.includes('---') && (
                  <button
                    onClick={() => handleExportSingleInsight(m.text, idx)}
                    className="mt-2.5 text-[10px] font-bold text-[var(--c-gold-soft)] hover:underline flex items-center gap-1 cursor-pointer"
                  >
                    <Download className="w-3.5 h-3.5" /> Adicionar ao Obsidian (context/insights)
                  </button>
                )}
              </div>
            ))}
            
            {loadingCompanion && (
              <div className="flex items-center gap-2 text-xs text-[var(--c-dim)] animate-pulse">
                <Brain className="w-4 h-4 animate-spin text-[var(--c-gold-soft)]" />
                <span>Canalizando e indexando resposta...</span>
              </div>
            )}
          </div>

          {/* Typing box */}
          <div className="flex gap-2.5 pt-4 border-t border-[var(--c-line)]">
            <textarea 
              value={insightText}
              onChange={(e) => setInsightText(e.target.value)}
              placeholder="Digite seus pensamentos brutos ou observações..."
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
              className="w-14 h-14 rounded-xl bg-gradient-to-r from-[var(--c-gold)] to-[var(--c-gold-soft)] text-[#24160a] flex items-center justify-center hover:scale-102 transition-all cursor-pointer shadow-md shadow-yellow-500/10"
            >
              <Send className="w-5 h-5" />
            </button>
          </div>

        </div>

      </div>

    </div>
  );
}
