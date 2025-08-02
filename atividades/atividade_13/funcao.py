import os
import classe as cl

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def deposito(d):
    return cl.saldo + d
