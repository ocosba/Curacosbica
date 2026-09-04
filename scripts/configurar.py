# -*- coding: utf-8 -*-
"""
Configuração do bot — roda uma vez, depois de revogar o token.

    python scripts/configurar.py

O que ele faz:
  1. Confere se TELEGRAM_BOT_TOKEN está no .env e se o token é válido.
  2. Espera você mandar qualquer mensagem para o bot no Telegram.
  3. Captura o seu chat id e grava ADMIN_CHAT_ID no .env sozinho.
  4. Confirma mandando uma mensagem de volta.

Nunca imprime o token na tela.
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = os.path.join(RAIZ, '.env')

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def le_env() -> dict:
    valores = {}
    if not os.path.exists(ENV):
        return valores
    with open(ENV, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if linha and not linha.startswith('#') and '=' in linha:
                c, v = linha.split('=', 1)
                valores[c.strip()] = v.strip().strip('"').strip("'")
    return valores


def grava_env(chave: str, valor: str):
    """Atualiza uma chave no .env preservando todo o resto do arquivo."""
    linhas = []
    achou = False
    if os.path.exists(ENV):
        with open(ENV, 'r', encoding='utf-8') as f:
            linhas = f.read().splitlines()
    for i, linha in enumerate(linhas):
        if re.match(rf'^\s*{re.escape(chave)}\s*=', linha):
            linhas[i] = f'{chave}={valor}'
            achou = True
            break
    if not achou:
        linhas.append(f'{chave}={valor}')
    with open(ENV, 'w', encoding='utf-8') as f:
        f.write('\n'.join(linhas) + '\n')


def api(token: str, metodo: str, params: dict = None):
    url = f'https://api.telegram.org/bot{token}/{metodo}'
    if params:
        url += '?' + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=35) as r:
            return json.loads(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        try:
            return json.loads(e.read().decode('utf-8'))
        except Exception:
            return {'ok': False, 'error_code': e.code, 'description': str(e)}
    except Exception as e:
        return {'ok': False, 'description': str(e)}


def main():
    print()
    print('=' * 58)
    print('  CONFIGURAÇÃO DO BOT DO SINCRONÁRIO')
    print('=' * 58)
    print()

    env = le_env()
    token = env.get('TELEGRAM_BOT_TOKEN', '').strip()

    # ---- Passo 1: o token ----
    if not token:
        print('❌ TELEGRAM_BOT_TOKEN está vazio no .env')
        print()
        print('   Faça assim, no Telegram:')
        print('   1. Fale com @BotFather')
        print('   2. Envie  /revoke')
        print('   3. Escolha o seu bot na lista')
        print('   4. Ele devolve um token NOVO (o antigo morre na hora)')
        print('   5. Copie e cole no .env, na linha TELEGRAM_BOT_TOKEN=')
        print()
        print(f'   O arquivo fica em: {ENV}')
        print()
        print('   Depois rode este script de novo.')
        return 1

    print('🔑 Testando o token...')
    r = api(token, 'getMe')
    if not r.get('ok'):
        print(f'❌ Token inválido. O Telegram respondeu: {r.get("description", "erro")}')
        print()
        print('   Se você acabou de revogar, confira se colou o token NOVO,')
        print('   inteiro e sem espaços em volta.')
        return 1

    bot = r['result']
    print(f'   ✅ Conectado ao bot: @{bot.get("username")} ({bot.get("first_name")})')
    print()

    # ---- Passo 2: o chat id ----
    ja_tem = env.get('ADMIN_CHAT_ID', '').strip()
    if ja_tem:
        print(f'ℹ️  Já existe um ADMIN_CHAT_ID configurado: {ja_tem}')
        resp = input('   Quer trocar? (s/N): ').strip().lower()
        if resp != 's':
            print('\n✅ Nada alterado. Tudo pronto para rodar o bot.')
            return 0
        print()

    print('👤 Agora preciso descobrir o seu chat id.')
    print()
    print(f'   Abra o Telegram, procure por @{bot.get("username")}')
    print('   e mande QUALQUER mensagem para ele. Pode ser "oi".')
    print()
    print('   Estou esperando... (2 minutos, Ctrl+C para cancelar)')
    print()

    # Limpa updates velhos para não pegar mensagem antiga de outra pessoa
    antigos = api(token, 'getUpdates', {'timeout': 0})
    offset = None
    if antigos.get('ok') and antigos.get('result'):
        offset = antigos['result'][-1]['update_id'] + 1

    limite = time.time() + 120
    chat_id = None
    nome = ''
    while time.time() < limite:
        params = {'timeout': 20}
        if offset:
            params['offset'] = offset
        upd = api(token, 'getUpdates', params)

        if not upd.get('ok'):
            desc = upd.get('description', '')
            if upd.get('error_code') == 409 or 'conflict' in desc.lower():
                print('❌ O bot já está rodando em outro lugar (provavelmente o Render).')
                print('   Pause o serviço lá, rode este script, e ligue de novo depois.')
                return 1
            print(f'   ...aguardando ({desc})')
            time.sleep(2)
            continue

        for u in upd.get('result', []):
            offset = u['update_id'] + 1
            msg = u.get('message') or u.get('edited_message') or {}
            chat = msg.get('chat', {})
            if chat.get('id') and chat.get('type') == 'private':
                chat_id = str(chat['id'])
                nome = chat.get('first_name', '')
                break
        if chat_id:
            break
        time.sleep(1)

    if not chat_id:
        print()
        print('⏱️  Não chegou mensagem nenhuma em 2 minutos.')
        print('   Rode de novo e mande um "oi" para o bot enquanto ele espera.')
        return 1

    print(f'   ✅ Recebi de: {nome} — chat id {chat_id}')
    print()

    grava_env('ADMIN_CHAT_ID', chat_id)
    print(f'💾 ADMIN_CHAT_ID gravado no .env')
    print()

    # ---- Passo 3: confirmação ----
    texto = (f'✅ *Configuração concluída, {nome}!*\n\n'
             f'Você agora é o administrador deste bot.\n'
             f'Só o seu chat pode usar */estudo* e */disparo*.\n\n'
             f'Rode o bot com `python scripts/bot.py` e mande */hoje*.')
    api(token, 'sendMessage', {'chat_id': chat_id, 'text': texto, 'parse_mode': 'Markdown'})
    print('📨 Mandei uma confirmação no seu Telegram. Confere lá.')
    print()
    print('=' * 58)
    print('  TUDO PRONTO')
    print('=' * 58)
    print()
    print('  Rodar o bot:      python scripts/bot.py')
    print('                    (ou clique em iniciar_bot.bat)')
    print()
    print('  Na nuvem (Render), defina estas duas variáveis no painel:')
    print('    TELEGRAM_BOT_TOKEN  = o token novo')
    print(f'    ADMIN_CHAT_ID       = {chat_id}')
    print()
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print('\n\nCancelado.')
        sys.exit(1)
