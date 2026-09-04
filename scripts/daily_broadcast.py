# -*- coding: utf-8 -*-
"""COMPATIBILIDADE — o disparo diário mora em `scripts/bot.py` desde 03/09/2026.

Diferente das outras duas pontes, esta NÃO sobe o bot: ela dispara o Kin do dia
uma vez e sai. É o comportamento que um cron job espera de um script de
broadcast — se algum agendador na nuvem ainda chamar este caminho, ele passa a
mandar o texto NOVO em vez do antigo.

O bot em pé já tem agendador próprio (`bot.agendador`), então rodar isto junto
com o serviço manda o diário duas vezes. Use um ou outro.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bot  # noqa: E402

if __name__ == '__main__':
    bot.carrega_env()
    token = bot.carrega_token()
    inscritos = bot.carrega_inscritos()
    hoje = bot.agora_brt().date()
    print(f'[compat] disparo único do Kin do dia para {len(inscritos)} inscritos', flush=True)
    bot.dispara_diario(token, inscritos, hoje)
