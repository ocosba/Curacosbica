# -*- coding: utf-8 -*-
"""COMPATIBILIDADE — este arquivo virou `scripts/bot.py` em 03/09/2026.

Por que ele existe de novo
--------------------------
Em 04/09/2026 o disparo das 6h chegou no Telegram no formato ANTIGO, quatro
commits depois de o formato novo estar no GitHub. Diagnóstico: o serviço na
nuvem continua servindo o commit 1938bcc. O `render.yaml` do repo aponta para
`scripts/bot.py`, mas a Render só lê o `render.yaml` em serviço criado por
Blueprint — em serviço criado pelo painel, vale o Start Command gravado lá,
que é o antigo `python -u scripts/bot_server.py`. Como esse arquivo tinha sido
apagado, todo deploy novo quebrava no boot e a Render mantinha no ar o último
deploy que funcionou: o velho.

Este arquivo é a ponte. Com ele, o Start Command antigo passa a subir o bot
novo, sem depender de ninguém mexer no painel.

Pode apagar quando o Start Command do painel apontar para `scripts/bot.py`.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bot  # noqa: E402

if __name__ == '__main__':
    print('[compat] scripts/bot_server.py → scripts/bot.py', flush=True)
    bot.main()
