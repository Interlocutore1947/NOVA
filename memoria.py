"""
memoria.py - NOVA NQ-01
Tutta la memoria separata dal cervello
"""
import os
from datetime import datetime

FILE_MEMORIA = "memoria_nova.txt"

def salva(ricordo: str):
    with open(FILE_MEMORIA, "a", encoding="utf-8") as f:
        ora = datetime.now().strftime("%d/%m %H:%M")
        f.write(f"[{ora}] {ricordo}\n")

def leggi():
    if not os.path.exists(FILE_MEMORIA):
        return "Nessun ricordo ancora."
    with open(FILE_MEMORIA, "r", encoding="utf-8") as f:
        return f.read()[-3000:]  # ultimi 3000 caratteri per non pesare

def cancella():
    if os.path.exists(FILE_MEMORIA):
        os.remove(FILE_MEMORIA)
        return "Memoria cancellata"
    return "Già vuota"