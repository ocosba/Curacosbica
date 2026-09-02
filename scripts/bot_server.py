"""
Servidor Interativo & Disparador Diário do Telegram — Sincronário Galáctico Cósbico
Edição Oráculo Vivo (24/7 Cloud Ready com Agendador Interno e Health Check)

Funcionalidades:
- Bot Interativo 24/7 (Long Polling)
- Agendador de Disparo Matinal Automático (ex: 06:00 BRT)
- Servidor HTTP leve integrado para Health Check em nuvem (Render, Railway, Koyeb)
- Suporte a Variáveis de Ambiente e arquivo local telegram_config.json
"""

import datetime
import http.server
import json
import os
import re
import socketserver
import sys
import threading
import time
import urllib.request
import urllib.parse

# Garante path para import do telegram_kin_bot
sys.path.insert(0, os.path.dirname(__file__))

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from telegram_kin_bot import (
    calculate_kin,
    get_kin_data,
    get_oracle,
    build_decree,
    generate_general_message,
    generate_private_message,
    generate_personal_map_complete,
    generate_personal_map_summary,
    generate_birthday_transit_analysis,
    get_annual_transit_data,
    generate_synastry_analysis,
    generate_weekly_forecast,
    generate_wave_lesson,
    generate_castle_lesson,
    generate_totem_lesson,
    generate_oracle_lesson,
    generate_daily_lesson,
    send_telegram_message
)

CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'telegram_config.json')
DEFAULT_TOKEN = '8343193098:AAGeIRsG2OgRAIKP-h-t_ASIPuj7jo6JjtQ'
BRT_TZ = datetime.timezone(datetime.timedelta(hours=-3))
DISPATCH_HOUR = int(os.environ.get('DISPATCH_HOUR', '6'))     # 06:00 BRT
DISPATCH_MINUTE = int(os.environ.get('DISPATCH_MINUTE', '0')) # :00

def get_brt_now():
    return datetime.datetime.now(BRT_TZ)

def load_config():
    token = os.environ.get('TELEGRAM_BOT_TOKEN', '').strip()
    subscribers = []
    
    env_subs = os.environ.get('TELEGRAM_SUBSCRIBERS', '').strip()
    if env_subs:
        subscribers = [s.strip() for s in env_subs.split(',') if s.strip()]

    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                cfg = json.load(f)
                if not token:
                    token = cfg.get('token', '')
                for sub in cfg.get('subscribers', []):
                    s_str = str(sub).strip()
                    if s_str and s_str not in subscribers:
                        subscribers.append(s_str)
        except Exception as e:
            print(f"[WARN] Erro ao ler {CONFIG_FILE}: {e}", flush=True)

    if not token:
        token = DEFAULT_TOKEN

    return {'token': token, 'subscribers': subscribers}

def save_config(cfg):
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[WARN] Não foi possível salvar em {CONFIG_FILE}: {e}", flush=True)

def get_updates(token, offset=None):
    url = f"https://api.telegram.org/bot{token}/getUpdates?timeout=20"
    if offset:
        url += f"&offset={offset}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=25) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"[WARN] Erro ao buscar updates: {e}", flush=True)
        return {'ok': False, 'result': []}

def parse_date_and_name(args_text):
    pattern = r'(\d{1,2})[/\-\.](\d{1,2})[/\-\.](\d{4})'
    match = re.search(pattern, args_text)
    if match:
        day, month, year = int(match.group(1)), int(match.group(2)), int(match.group(3))
        name_part = args_text[:match.start()] + args_text[match.end():]
        name = name_part.strip() or "Consulente"
        try:
            target_date = datetime.date(year, month, day)
            return target_date, name
        except ValueError:
            return None, None
    return None, None

def parse_two_dates_and_names(text):
    pattern = r'(\d{1,2})[/\-\.](\d{1,2})[/\-\.](\d{4})'
    matches = list(re.finditer(pattern, text))
    if len(matches) >= 2:
        m1, m2 = matches[0], matches[1]
        try:
            dt1 = datetime.date(int(m1.group(3)), int(m1.group(2)), int(m1.group(1)))
            dt2 = datetime.date(int(m2.group(3)), int(m2.group(2)), int(m2.group(1)))
        except ValueError:
            return None, None, None, None

        middle = text[m1.end():m2.start()].strip(' e&/-,')
        after = text[m2.end():].strip(' e&/-,')
        before = text[:m1.start()].strip(' e&/-,')

        if middle and after:
            name1, name2 = middle, after
        elif after:
            names = re.split(r'\s+(?:e|&|\+)\s+|\s*,\s*', after)
            if len(names) >= 2:
                name1, name2 = names[0].strip(), names[1].strip()
            else:
                parts = after.split()
                if len(parts) >= 2:
                    name1, name2 = parts[0], parts[1]
                else:
                    name1, name2 = after, 'Parceiro(a)'
        elif before and middle:
            name1, name2 = before, middle
        else:
            name1, name2 = 'Pessoa 1', 'Pessoa 2'

        return dt1, name1, dt2, name2
    return None, None, None, None

def broadcast_daily_kin(token, subscribers, force_date=None):
    today = force_date or get_brt_now().date()
    kin_num = calculate_kin(today)
    print(f"\n📢 [AUTO-DISPATCH] Iniciando transmissão do Kin {kin_num:03d} ({today.strftime('%d/%m/%Y')}) para {len(subscribers)} inscritos...", flush=True)
    
    msg_geral = generate_general_message(today)
    msg_aula = generate_daily_lesson(today)
    
    count = 0
    for chat_id in subscribers:
        try:
            send_telegram_message(token, chat_id, msg_geral)
            time.sleep(1)
            send_telegram_message(token, chat_id, msg_aula)
            time.sleep(1)
            count += 1
            print(f"   ✓ Enviado para {chat_id}", flush=True)
        except Exception as e:
            print(f"   ✗ Falha ao enviar para {chat_id}: {e}", flush=True)
    
    print(f"📢 [AUTO-DISPATCH] Concluído: {count}/{len(subscribers)} entregues com sucesso.\n", flush=True)

def process_message(token, chat_id, text, user_name=""):
    today = get_brt_now().date()
    clean_text = text.strip()
    parts = clean_text.split()
    cmd = parts[0].lower().split('@')[0] if parts else ""
    args_str = " ".join(parts[1:]) if len(parts) > 1 else ""
    
    cfg = load_config()
    chat_id_str = str(chat_id).strip()
    
    # Auto-inscrever novos usuários
    if chat_id_str not in cfg.get('subscribers', []):
        if 'subscribers' not in cfg:
            cfg['subscribers'] = []
        cfg['subscribers'].append(chat_id_str)
        save_config(cfg)
        print(f"Novo assinante registrado: {chat_id_str} ({user_name})", flush=True)

    if cmd in ['/start', '/inicio', '/comecar']:
        welcome = f"""✨ *Bem-vindo ao Sincronário Galáctico da Lei do Tempo!* ✨
Olá, *{user_name}*! O seu portal do tempo natural (13:20) está ativo.

🔔 *Você foi inscrito para receber o briefing diário todas as manhãs às 06:00!*

Comandos rápidos:
• `/hoje` ──► ☀️ *Briefing Matinal Completo* (Resumo WhatsApp + Aula Magna)
• `/aula` ──► 📚 *Aula Magna do Tzolkin do Dia* (Estudo Aprofundado)
• `/geral` ──► 📲 Mensagem formatada para WhatsApp & Grupos
• `/casal` ──► 🔒 Estudo da Aliança de Leo & Steph (Kin 81)
• `/onda` ──► 🌊 A Onda Encantada de 13 dias
• `/oraculo` ──► 🧭 O Oráculo das 5 Forças do dia
• `/totem` ──► 🐆 O Totem e Arquétipo do dia
• `/castelo` ──► 🏰 O Castelo de 52 dias
• `/semana` ──► 📅 Dossiê dos próximos 7 dias
• `/decreto` ──► 🧘 Decreto sagrado de ativação
• `/calcular DD/MM/AAAA [Nome]` ──► 🏛️ Mapa Galáctico completo + Trânsito
• `/aniversario DD/MM/AAAA [Nome]` ──► 🎂 Trânsito do Ano & Revolução Galáctica
• `/sinastria DD/MM/AAAA [N1] DD/MM/AAAA [N2]` ──► 🔮 Sinastria & Kin Composto
• `/kin [Número 1-260]` ──► 📜 Ficha do Kin
• `/desinscrever` ──► Cancelar recebimento automático matinal

Enviando agora o briefing de hoje... 👇"""
        send_telegram_message(token, chat_id, welcome)
        time.sleep(1)
        send_telegram_message(token, chat_id, generate_general_message(today))
        time.sleep(1)
        send_telegram_message(token, chat_id, generate_daily_lesson(today))

    elif cmd in ['/inscrever', '/assinar']:
        if chat_id_str not in cfg['subscribers']:
            cfg['subscribers'].append(chat_id_str)
            save_config(cfg)
        send_telegram_message(token, chat_id, "✅ *Inscrição confirmada!* Você receberá o Kin do dia todas as manhãs às 06:00.")

    elif cmd in ['/desinscrever', '/cancelar']:
        if chat_id_str in cfg['subscribers']:
            cfg['subscribers'].remove(chat_id_str)
            save_config(cfg)
        send_telegram_message(token, chat_id, "🔕 *Assinatura cancelada.* Você não receberá mais os disparos automáticos diários (mas pode continuar consultando os comandos quando quiser).")

    elif cmd in ['/disparo', '/broadcast']:
        send_telegram_message(token, chat_id, "⏳ *Disparando briefing diário para todos os assinantes...*")
        broadcast_daily_kin(token, cfg['subscribers'], today)
        send_telegram_message(token, chat_id, "✅ *Disparo concluído com sucesso!*")

    elif cmd in ['/hoje', 'hoje']:
        send_telegram_message(token, chat_id, generate_general_message(today))
        time.sleep(1)
        send_telegram_message(token, chat_id, generate_daily_lesson(today))

    elif cmd in ['/aula', 'aula', '/estudo', 'estudo']:
        target_date = today
        if args_str:
            dt_match = re.search(r'(\d{1,2})[/\-\.](\d{1,2})[/\-\.](\d{4})', args_str)
            if dt_match:
                try:
                    target_date = datetime.date(int(dt_match.group(3)), int(dt_match.group(2)), int(dt_match.group(1)))
                except ValueError:
                    target_date = today
            else:
                num_match = re.search(r'^\s*(\d{1,3})\s*$', args_str)
                if num_match:
                    k_num = int(num_match.group(1))
                    if 1 <= k_num <= 260:
                        cur_k = calculate_kin(today)
                        diff = (k_num - cur_k) % 260
                        target_date = today + datetime.timedelta(days=diff)
        send_telegram_message(token, chat_id, f"📚 *Carregando a Aula Magna do Tzolkin ({target_date.strftime('%d/%m/%Y')} | Kin {calculate_kin(target_date):03d})...*")
        time.sleep(1)
        send_telegram_message(token, chat_id, generate_daily_lesson(target_date))

    elif cmd in ['/amanha', 'amanha', 'amanhã']:
        tomorrow = today + datetime.timedelta(days=1)
        send_telegram_message(token, chat_id, f"🔮 *ANTECIPAÇÃO PARA AMANHÃ ({tomorrow.strftime('%d/%m/%Y')}):*")
        time.sleep(1)
        send_telegram_message(token, chat_id, generate_general_message(tomorrow))
        time.sleep(1)
        send_telegram_message(token, chat_id, generate_private_message(tomorrow))

    elif cmd in ['/ontem', 'ontem']:
        yesterday = today - datetime.timedelta(days=1)
        send_telegram_message(token, chat_id, f"🕰️ *REVISÃO DE ONTEM ({yesterday.strftime('%d/%m/%Y')}):*")
        time.sleep(1)
        send_telegram_message(token, chat_id, generate_general_message(yesterday))

    elif cmd in ['/geral', 'geral', '/publico', 'publico']:
        send_telegram_message(token, chat_id, generate_general_message(today))

    elif cmd in ['/casal', 'casal', '/privado', 'privado', '/leo', '/steph']:
        send_telegram_message(token, chat_id, generate_private_message(today))

    elif cmd in ['/onda', 'onda']:
        send_telegram_message(token, chat_id, generate_wave_lesson(today))

    elif cmd in ['/castelo', 'castelo']:
        send_telegram_message(token, chat_id, generate_castle_lesson(today))

    elif cmd in ['/totem', 'totem']:
        send_telegram_message(token, chat_id, generate_totem_lesson(today))

    elif cmd in ['/oraculo', 'oraculo']:
        send_telegram_message(token, chat_id, generate_oracle_lesson(today))

    elif cmd in ['/semana', 'semana', '/7dias']:
        send_telegram_message(token, chat_id, generate_weekly_forecast(today))

    elif cmd in ['/decreto', 'decreto']:
        k = calculate_kin(today)
        kd = get_kin_data(k)
        oracle = get_oracle(k)
        dec = build_decree(kd, oracle)
        msg_dec = f"""🧘 *DECRETO SAGRADO DE ATIVAÇÃO — KIN {kd['kin']:03d}*
*{kd['name'].upper()}*

> {dec} ✨🚀"""
        send_telegram_message(token, chat_id, msg_dec)

    elif cmd in ['/calcular', '/mapa']:
        dt, name = parse_date_and_name(args_str)
        if dt:
            send_telegram_message(token, chat_id, f"⏳ *Calculando Mapa Completo de {name} ({dt.strftime('%d/%m/%Y')})...*")
            time.sleep(1)
            send_telegram_message(token, chat_id, generate_personal_map_complete(dt, name))
        else:
            send_telegram_message(token, chat_id, "⚠️ *Formato incorreto!*\nUse: `/calcular DD/MM/AAAA [Nome]`\nExemplo: `/calcular 04/02/2004 Simon`")

    elif cmd in ['/kin']:
        num_match = re.search(r'^\s*(\d{1,3})\s*$', args_str)
        if num_match:
            k_num = int(num_match.group(1))
            if 1 <= k_num <= 260:
                kd = get_kin_data(k_num)
                oracle = get_oracle(k_num)
                s = kd['seal']
                c = kd['castle']
                dec = build_decree(kd, oracle)
                pag_tag = "🌀 *PAG (Portal Galáctico): SIM!*" if kd['is_pag'] else "• *PAG:* Não"
                msg_k = f"""🏛️ *FICHA DO KIN {kd['kin']:03d} — {kd['name'].upper()}*
{pag_tag} | 🦉 *Totem:* {kd['totem'][0]}
⚡ *{kd['pulsar'][0]}:* {kd['pulsar'][1]}
🏰 *{c['nome']}* | *Onda:* {kd['wave'][1]} (Degrau {kd['degrau']:02d}/13)
📍 *Hunab Ku 21:* {s['corte']} — *{s['arquetipo']}*

━━━━━━━━━━━━━━━━━━━━━

✦ A ALQUIMIA DO KIN:
• *Selo:* {s['nome']} ({s['maia']}) — {s['acao']} {s['poder']}. {s['descricao']}.
• *Tom:* Tom {kd['tone_num']} ({kd['tone'][0]}) — {kd['tone'][1]} ({kd['tone'][2]} o {kd['tone'][3]}).

━━━━━━━━━━━━━━━━━━━━━

✦ O ORÁCULO DE 5 FORÇAS:
🧭 *Guia:* Kin {oracle['guia']['kin']:03d} ({oracle['guia']['name']})
🤝 *Apoio:* Kin {oracle['analogo']['kin']:03d} ({oracle['analogo']['name']})
⚡ *Desafio:* Kin {oracle['antipoda']['kin']:03d} ({oracle['antipoda']['name']})
💎 *Oculto:* Kin {oracle['oculto']['kin']:03d} ({oracle['oculto']['name']})
👑 *5ª Força:* Kin {oracle['quinta_forca']['kin']:03d} ({oracle['quinta_forca']['name']})

━━━━━━━━━━━━━━━━━━━━━

✦ O ARQUÉTIPO & TOTEM:
• 🏛️ *Arquétipo ({s['arquetipo']}):* {s['descricao']}.
• 🐆 *Totem ({kd['totem'][0]}):* {kd['totem'][2]}

━━━━━━━━━━━━━━━━━━━━━

✦ LUZ & SOMBRA:
• 🟢 *LUZ:* {s['luz']}
• 🔴 *SOMBRA:* {s['sombra']}
• 🔑 *Chave:* "{s['chave']}"

━━━━━━━━━━━━━━━━━━━━━

🧘 *DECRETO:*
> {dec}"""
                send_telegram_message(token, chat_id, msg_k)
            else:
                send_telegram_message(token, chat_id, "⚠️ O número do Kin deve estar entre 1 e 260.")
        else:
            dt, name = parse_date_and_name(args_str)
            if dt:
                send_telegram_message(token, chat_id, generate_personal_map_complete(dt, name))
            else:
                send_telegram_message(token, chat_id, "⚠️ *Formato:* `/kin [1-260]` ou `/kin DD/MM/AAAA [Nome]`\nExemplo: `/kin 194` ou `/kin 04/02/2004 Simon`")

    elif cmd in ['/resumo', '/rapido']:
        dt, name = parse_date_and_name(args_str)
        if dt:
            send_telegram_message(token, chat_id, generate_personal_map_summary(dt, name))
        else:
            send_telegram_message(token, chat_id, "⚠️ *Formato incorreto!*\nUse: `/resumo DD/MM/AAAA [Nome]`\nExemplo: `/resumo 04/02/2004 Simon`")

    elif cmd in ['/aniversario', 'aniversario', '/transito', 'transito', '/ano', 'ano', '/revolucao']:
        dt, name = parse_date_and_name(args_str)
        if dt:
            send_telegram_message(token, chat_id, f"🎂 *Calculando Trânsito do Ano & Revolução Galáctica para {name} ({dt.strftime('%d/%m/%Y')})...*")
            time.sleep(1)
            send_telegram_message(token, chat_id, generate_birthday_transit_analysis(dt, name))
        else:
            send_telegram_message(token, chat_id, "⚠️ *Formato incorreto!*\nUse: `/aniversario DD/MM/AAAA [Nome]`\nExemplo: `/aniversario 04/02/2004 Simon`")

    elif cmd in ['/sinastria', 'sinastria', '/alianca', 'alianca', '/compatibilidade']:
        dt1, name1, dt2, name2 = parse_two_dates_and_names(args_str)
        if dt1 and dt2:
            send_telegram_message(token, chat_id, f"🔮 *Calculando Sinastria Galáctica entre {name1} e {name2}...*")
            time.sleep(1)
            send_telegram_message(token, chat_id, generate_synastry_analysis(dt1, name1, dt2, name2))
        else:
            send_telegram_message(token, chat_id, "⚠️ *Formato:* `/sinastria DD/MM/AAAA [Nome1] DD/MM/AAAA [Nome2]`\nExemplo: `/sinastria 04/09/2003 Leo 27/09/1985 Steph`")

    elif cmd in ['/ajuda', '/help', 'ajuda']:
        help_msg = """📖 *SINCRONÁRIO GALÁCTICO DA LEI DO TEMPO:*

🌟 *SINCRONIZAÇÃO DIÁRIA:*
• `/hoje` — Leitura completa de hoje (Geral + Aula)
• `/geral` — Leitura pública do Kin do Dia
• `/aula` — Aula Magna do Tzolkin aprofundada
• `/casal` — Raio-X exclusivo da Aliança Leo & Steph (Kin 81)
• `/amanha` — Antecipação do Kin de amanhã
• `/ontem` — Revisão do Kin de ontem

🎓 *LEITURAS ESPECIALIZADAS:*
• `/onda` — A jornada dos 13 dias e seu degrau atual
• `/oraculo` — A bússola das 5 Forças do dia
• `/totem` — A medicina animal e o arquétipo do dia
• `/castelo` — O Castelo de 52 dias em que estamos
• `/semana` — Dossiê completo dos próximos 7 dias
• `/decreto` — Poema sagrado de ativação do Kin

👤 *MAPAS PESSOAIS, ANIVERSÁRIO & SINASTRIA:*
• `/aniversario DD/MM/AAAA [Nome]` — 🎂 Trânsito do Ano, Idade & Revolução Galáctica
• `/calcular DD/MM/AAAA [Nome]` — 🏛️ Mapa Galáctico Completo + Trânsito
• `/sinastria DD/MM/AAAA [N1] DD/MM/AAAA [N2]` — 🔮 Sinastria & Kin Composto da Aliança
• `/resumo DD/MM/AAAA [Nome]` — ⚡ Raio-X Rápido
• `/kin [1-260]` — 📜 Ficha completa de qualquer Kin

⚙️ *PREFERÊNCIAS:*
• `/inscrever` — Ativar disparo diário às 06:00 BRT
• `/desinscrever` — Cancelar disparo diário automático"""
        send_telegram_message(token, chat_id, help_msg)

    else:
        send_telegram_message(token, chat_id, "✨ Comando não reconhecido. Digite `/ajuda` para ver o menu completo ou `/hoje` para a leitura do dia!")

# ==========================================
# THREAD 1: AGENDADOR DE DISPARO MATINAL
# ==========================================
def daily_scheduler_thread():
    last_dispatched_date = None
    print(f"⏰ [SCHEDULER] Agendador matinal ativo (Horário alvo: {DISPATCH_HOUR:02d}:{DISPATCH_MINUTE:02d} BRT)...", flush=True)
    
    while True:
        try:
            now_brt = get_brt_now()
            today = now_brt.date()
            
            if (now_brt.hour == DISPATCH_HOUR and 
                now_brt.minute >= DISPATCH_MINUTE and 
                last_dispatched_date != today):
                
                cfg = load_config()
                subs = cfg.get('subscribers', [])
                if subs:
                    broadcast_daily_kin(cfg['token'], subs, today)
                last_dispatched_date = today
                
            time.sleep(30)
        except Exception as e:
            print(f"[WARN] Erro no scheduler: {e}", flush=True)
            time.sleep(60)

# ==========================================
# THREAD 2: SERVIDOR HTTP PARA HEALTH CHECK (NUVEM)
# ==========================================
class HealthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        today = get_brt_now().date()
        kin = calculate_kin(today)
        data = {
            "status": "online",
            "service": "Sincronario Cosbico Telegram Bot",
            "tz": "America/Sao_Paulo (UTC-3)",
            "today": today.strftime('%d/%m/%Y'),
            "kin_hoje": kin,
            "dispatch_schedule": f"{DISPATCH_HOUR:02d}:{DISPATCH_MINUTE:02d} BRT"
        }
        resp_bytes = json.dumps(data, indent=2, ensure_ascii=False).encode('utf-8')
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(resp_bytes)))
        self.end_headers()
        self.wfile.write(resp_bytes)

    def log_message(self, format, *args):
        pass # Silencia logs de health check para não poluir terminal

def start_health_server(port=8080):
    try:
        class ReuseServer(socketserver.TCPServer):
            allow_reuse_address = True
        httpd = ReuseServer(("", port), HealthHandler)
        print(f"🌐 [HTTP] Health Check Server escutando na porta {port}...", flush=True)
        httpd.serve_forever()
    except Exception as e:
        print(f"[WARN] Servidor HTTP não pôde ser iniciado na porta {port}: {e}", flush=True)

# ==========================================
# MAIN LOOP: TELEGRAM POLLING
# ==========================================
if __name__ == '__main__':
    cfg = load_config()
    print("=" * 60, flush=True)
    print("🚀 SINCRONÁRIO COSBICO — TELEGRAM BOT 24/7", flush=True)
    print(f"• Token: {cfg['token'][:15]}...", flush=True)
    print(f"• Assinantes carregados: {len(cfg.get('subscribers', []))}", flush=True)
    print("=" * 60, flush=True)

    # Inicia agendador diário em background
    scheduler_t = threading.Thread(target=daily_scheduler_thread, daemon=True)
    scheduler_t.start()

    # Inicia servidor HTTP para Render/Railway em background se PORT existir
    port_env = os.environ.get('PORT')
    if port_env:
        try:
            http_port = int(port_env)
            http_t = threading.Thread(target=start_health_server, args=(http_port,), daemon=True)
            http_t.start()
        except ValueError:
            pass

    offset = None
    print("🤖 Bot ouvindo mensagens...", flush=True)
    while True:
        try:
            updates = get_updates(cfg['token'], offset)
            if updates.get('ok') and updates.get('result'):
                for u in updates['result']:
                    offset = u['update_id'] + 1
                    msg = u.get('message', {})
                    chat = msg.get('chat', {})
                    chat_id = chat.get('id')
                    text = msg.get('text', '')
                    user_name = chat.get('first_name', '')
                    if chat_id and text:
                        print(f"📩 Mensagem de {user_name} ({chat_id}): {text}", flush=True)
                        process_message(cfg['token'], str(chat_id), text, user_name)
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nEncerrando bot.", flush=True)
            break
        except Exception as e:
            print(f"[WARN] Erro no polling: {e}", flush=True)
            time.sleep(3)
