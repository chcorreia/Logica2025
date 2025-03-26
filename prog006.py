"""
prog006.py
Mundo de 8x8
Cada vez que encontrar uma pilha de moedas, dizer o valor dela
No final dizer qual a soma de todas as moedas
"""
# ----------- NÃO APAGUE ---------------------------------------------
from robozinho import *
Mundo(8,8)

for j in range(1,8):
    if chuta_numero(1,2) == 1:
        Moedas(2,j)

Robot(1,1)
dizer("Diga quanto valem as moedas.")
# ----------- COMECE SEU PROGRAMA AQUI -------------------------------