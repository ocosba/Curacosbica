"""
Disparo Diário Automático — Sincronário Galáctico Cósbico
Projetado para rodar via GitHub Actions, Cron ou linha de comando.
Envia a Leitura Pública + Aula Magna do Kin do Dia para todos os assinantes cadastrados.
"""

import datetime
import json
import os
import sys
import time

# Adiciona diretório atual ao path se necessário
sys.path.insert(0, os.path.dirname(__file__))

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from telegram_kin_bot import (
    calculate_kin,
    generate_general_message,
    generate_daily_lesson,
    send_telegram_message
)

CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'telegram_config.json')
DEFAULT_TOKEN = '8343193098:AAGeIRsG2OgRAIKP-h-t_ASIPuj7jo6JjtQ'

def get_brt_today():
    brt_tz = datetime.timezone(datetime.timedelta(hours=-3))
    return datetime.datetime.now(brt_tz).date()

def load_credentials():
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
            print(f"[WARN] Erro ao ler telegram_config.json: {e}", flush=True)

    if not token:
        token = DEFAULT_TOKEN

    return token, subscribers

def run_broadcast():
    token, subscribers = load_credentials()
    today = get_brt_today()
    kin_num = calculate_kin(today)
    
    print(f"=== DISPARO DIÁRIO AUTOMÁTICO ===", flush=True)
    print(f"Data: {today.strftime('%d/%m/%Y')} | Kin do Dia: {kin_num:03d}", flush=True)
    print(f"Total de assinantes: {len(subscribers)}", flush=True)
    
    if not subscribers:
        print("[ERRO] Nenhum assinante configurado.", flush=True)
        return False
    
    print("Gerando mensagens do dia...", flush=True)
    msg_geral = generate_general_message(today)
    msg_aula = generate_daily_lesson(today)
    
    sucessos = 0
    erros = 0
    
    for chat_id in subscribers:
        print(f"-> Enviando para chat_id: {chat_id}...", flush=True)
        try:
            res1 = send_telegram_message(token, chat_id, msg_geral)
            time.sleep(1)
            res2 = send_telegram_message(token, chat_id, msg_aula)
            time.sleep(1)
            
            if res1.get('ok') is not False and res2.get('ok') is not False:
                sucessos += 1
                print(f"   [OK] Enviado com sucesso para {chat_id}", flush=True)
            else:
                erros += 1
                print(f"   [FALHA] Retorno API para {chat_id}: {res1}, {res2}", flush=True)
        except Exception as e:
            erros += 1
            print(f"   [ERRO] Exceção ao enviar para {chat_id}: {e}", flush=True)

    print(f"=== FIM DO DISPARO: {sucessos} sucessos, {erros} falhas ===", flush=True)
    return erros == 0

if __name__ == '__main__':
    ok = run_broadcast()
    sys.exit(0 if ok else 1)
