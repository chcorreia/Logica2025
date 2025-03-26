"""
prog004.py
Mundo de 8x8
O robô nasce em 1,1
Existe uma barreira no meio do caminho, com um buraco
A barreira pode aparecer em qualquer linha entre a 2 e a 7
O robô precisa passar pelo buraco e chegar em qualquer lugar da linha 8
"""
# ----------- NÃO APAGUE ---------------------------------------------
from robozinho import *
Mundo(8,8)
Robot(1,1)
buraco = chuta_numero(1,8)
linha = chuta_numero(2,7)
for i in range(1,9):
    if i != buraco: Parede(i,linha)
dizer("Passe pelo buraco no muro e desça até o fim.")
# ----------- COMECE SEU PROGRAMA AQUI -------------------------------


