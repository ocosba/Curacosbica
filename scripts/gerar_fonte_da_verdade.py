# -*- coding: utf-8 -*-
"""
Gera context/metodo/tzolkin-fonte-da-verdade.md a partir do core.

Rode isto sempre que mudar uma tabela no core.py. O documento passa a ser
consequência do código, não uma cópia paralela que diverge com o tempo —
que é exatamente o que aconteceu com as três tabelas de Família Terrestre.

    python scripts/gerar_fonte_da_verdade.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tzolkin import core, textos as T  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, 'context', 'metodo', 'tzolkin-fonte-da-verdade.md')

L = []
w = L.append

w('---')
w('tipo: referencia-tecnica')
w('gerado-por: scripts/gerar_fonte_da_verdade.py')
w('aviso: NAO EDITE A MAO. Mude scripts/tzolkin/core.py e rode o gerador.')
w('---')
w('')
w('# Tzolkin — Fonte da Verdade')
w('')
w('Este arquivo e gerado pelo codigo. Se um outro documento do vault discordar')
w('daqui, o outro documento esta errado.')
w('')
w('Convencao de Familias Terrestres: **canone Arguelles** (agrupamento de 5 em 5).')
w('Decidido em 03/09/2026.')
w('')
w('## Calculo do Kin')
w('')
w(f'- Ancora: {core.ANCHOR_DATE:%d/%m/%Y} = Kin {core.ANCHOR_KIN}')
w('- 29 de fevereiro nao e contado: carrega o Kin do dia 28.')
w('- Formula: `((ANCHOR_KIN - 1 + dias - bissextos) % 260) + 1`')
w('')
w('## Os 20 Selos Solares')
w('')
w('| # | Selo | Maia | Cla | Acao | Poder | Familia | Chakra | Arquetipo (Hunab Ku 21) |')
w('|---|---|---|---|---|---|---|---|---|')
for n in range(1, 21):
    s = core.SELOS[n]
    f = core.familia_de(n)
    a = core.arquetipo_de(n)
    w(f"| {n} | {core.SELO_NOME_COMPLETO[n]} | {s['maia']} | {s['cla']} | {s['acao']} | "
      f"{s['poder']} | {f['nome']} | {f['chakra']} | {a['nome']} |")
w('')
w('## Os 13 Tons Galacticos')
w('')
w('| # | Tom | Poder | Essencia | Totem | Faz | Pergunta |')
w('|---|---|---|---|---|---|---|')
for n in range(1, 14):
    t = core.TONS[n]
    w(f"| {n} | {t[0]} | {t[1]} | {t[3]} | {t[4]} | {T.TOM_FRASE[n]} | {t[5]} |")
w('')
w('## Familias Terrestres e a ponte com o corpo')
w('')
w('| Familia | Selos | Chakra | Corpo | Holon | Quando desalinha |')
w('|---|---|---|---|---|---|')
for nome in core._FAMILIA_ORDEM:
    dados = core.FAMILIAS[nome]
    selos = [n for n in range(1, 21) if core.familia_de(n)['nome'] == nome]
    corpo, sintoma = T.CHAKRA_CORPO[dados['chakra']]
    w(f"| {nome} | {', '.join(str(x) for x in selos)} | {dados['chakra']} | {corpo} | "
      f"{dados['holon']} | {sintoma.split('— quando desalinha, ')[-1]} |")
w('')
w('## As 20 Ondas Encantadas')
w('')
w('| Kin inicial | Onda | Tema |')
w('|---|---|---|')
for inicio, nome, tema in core.ONDAS:
    art = core.artigo_do_selo(core.seal_of(inicio))
    w(f"| {inicio} | Onda {art} {nome} | {tema} |")
w('')
w('## Os 13 degraus de qualquer Onda')
w('')
w('| Degrau | Etapa | O que acontece |')
w('|---|---|---|')
for n in range(1, 14):
    nome, texto = T.DEGRAUS[n]
    w(f'| {n} | {nome} | {texto} |')
w('')
w('## Os 5 Castelos')
w('')
w('| # | Castelo | Corte | Kins | Missao |')
w('|---|---|---|---|---|')
for n, (nome, corte, missao) in core.CASTELOS.items():
    w(f'| {n} | {nome} | Corte {corte} | {(n-1)*52+1}–{n*52} | {missao} |')
w('')
w('## Oraculo — as formulas')
w('')
w('| Posicao | Formula |')
w('|---|---|')
w('| Analogo | selo = 19 - selo (19 e 20 trocam entre si), mesmo tom |')
w('| Antipoda | selo = ((selo + 9) % 20) + 1, mesmo tom |')
w('| Oculto | kin = 261 - kin |')
w('| Guia | selo deslocado pelo tom: 1/6/11 = +0, 2/7/12 = +12, 3/8/13 = +4, 4/9 = +16, 5/10 = +8 |')
w('| Quinta Forca | soma dos cinco kins, modulo 260 |')
w('')
w(f'## Portais de Ativacao Galactica ({len(core.PAGS)})')
w('')
w(', '.join(str(k) for k in sorted(core.PAGS)))
w('')
w('## Marcos do tabuleiro')
w('')
w('- Coluna Mistica: kins 121 a 140 (coluna central)')
w('- Ponto Zero: kins 130 e 131')
w('- Ciclo de 52 anos: 18.980 dias = 73 voltas do Tzolkin. O Kin natal retorna aos 52 anos.')
w('')

os.makedirs(os.path.dirname(DESTINO), exist_ok=True)
with open(DESTINO, 'w', encoding='utf-8') as f:
    f.write('\n'.join(L))

print(f'Gerado: {DESTINO}')
print(f'{len(L)} linhas')
