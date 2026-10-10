"""
memoria.py - NOVA NQ-01 MEMORIA POTENTE
Memoria infinita, ricerca, riassunto, organizzata
"""
import os
import json
from datetime import datetime

FILE_MEMORIA = "memoria_nova.txt"
FILE_MEMORIA_JSON = "memoria_nova.json"

def _ora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def salva(testo: str, tipo: str = "generale"):
    """Salva un ricordo con data e tipo"""
    # 1. Salva in txt leggibile
    with open(FILE_MEMORIA, "a", encoding="utf-8") as f:
        f.write(f"[{_ora()}] [{tipo}] {testo}\n")

    # 2. Salva in json per ricerca potente
    ricordo = {"data": _ora(), "tipo": tipo, "testo": testo}
    try:
        if os.path.exists(FILE_MEMORIA_JSON):
            with open(FILE_MEMORIA_JSON, "r", encoding="utf-8") as f:
                dati = json.load(f)
        else:
            dati = []
        dati.append(ricordo)
        # Tieni solo ultimi 1000 per non esplodere
        dati = dati[-1000:]
        with open(FILE_MEMORIA_JSON, "w", encoding="utf-8") as f:
            json.dump(dati, f, ensure_ascii=False, indent=2)
    except:
        pass

def leggi(ultimi: int = 30) -> str:
    """Legge gli ultimi N ricordi"""
    if not os.path.exists(FILE_MEMORIA):
        return "Nessun ricordo ancora. Memoria vergine."
    with open(FILE_MEMORIA, "r", encoding="utf-8") as f:
        righe = f.readlines()
        return "".join(righe[-ultimi:])

def leggi_tutto() -> str:
    """Tutta la memoria (ultimi 4000 caratteri per il cervello)"""
    if not os.path.exists(FILE_MEMORIA):
        return ""
    with open(FILE_MEMORIA, "r", encoding="utf-8") as f:
        return f.read()[-4000:]

def cerca(parola: str) -> str:
    """Cerca nella memoria come Google"""
    if not os.path.exists(FILE_MEMORIA):
        return "Memoria vuota."
    parola = parola.lower()
    trovati = []
    with open(FILE_MEMORIA, "r", encoding="utf-8") as f:
        for riga in f:
            if parola in riga.lower():
                trovati.append(riga)
    if not trovati:
        return f"Niente trovato per '{parola}'"
    return "".join(trovati[-20:])

def stats():
    """Quanti ricordi hai"""
    if not os.path.exists(FILE_MEMORIA):
        return "0 ricordi"
    with open(FILE_MEMORIA, "r", encoding="utf-8") as f:
        return f"{len(f.readlines())} ricordi salvati"

def cancella():
    """Reset totale"""
    for file in [FILE_MEMORIA, FILE_MEMORIA_JSON]:
        if os.path.exists(file):
            os.remove(file)
    return "Memoria cancellata - NOVA rinata."