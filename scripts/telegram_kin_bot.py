# -*- coding: utf-8 -*-
"""COMPATIBILIDADE — a fonte única virou `scripts/bot.py` em 03/09/2026.

Mesmo motivo do `bot_server.py`: se o Start Command gravado no painel da nuvem
ainda apontar para este caminho, o deploy quebrava no boot e o serviço ficava
preso no commit velho. Com esta ponte, qualquer um dos caminhos antigos sobe o
bot novo.

Pode apagar quando o Start Command do painel apontar para `scripts/bot.py`.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bot  # noqa: E402

if __name__ == '__main__':
    print('[compat] scripts/telegram_kin_bot.py → scripts/bot.py', flush=True)
    bot.main()
