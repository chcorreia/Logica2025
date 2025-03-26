"""
prog002.py
Mundo de 8x8
O robô nasce em 4,1
Fazer o robô caminhar para baixo até o fim do tabuleiro (linha 8)
Mas tem uma parede no meio do caminho!
"""
# ----------- NÃO APAGUE ---------------------------------------------
from robozinho import *
Mundo(8,8)
Robot(4,1)
Parede(4, chuta_numero(2,7))
dizer("Desça até o fim sem bater na parede.")
# ----------- COMECE SEU PROGRAMA AQUI -------------------------------