import json
import os

pessoa = {}

try:
     with open(f"dado.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    
except Exception as e:
    print(f"Não foi possível inserir pessoa. {e}.")
