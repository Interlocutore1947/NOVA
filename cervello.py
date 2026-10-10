"""
cervello.py - NOVA NQ-01 SUPER CERVELLO
Potenza massima con Groq - Gratis e Infinito
"""
import requests
import random
import time

# === METTI QUI LE TUE CHIAVI GROQ ===
API_KEYS = [
    "gsk_INCOLLA_QUI_TUA_KEY_GROQ",
    # Puoi aggiungerne altre per essere INFINITO:
    # "gsk_seconda_chiave_...",
    # "gsk_terza_chiave_...",
]

# Modelli Groq più potenti in ordine di potenza (2026)
MODELLI = [
    "llama-3.3-70b-versatile", # Il più intelligente
    "deepseek-r1-distill-llama-70b", # Ragionamento profondo
    "qwen-2.5-32b", # Veloce e furbo
    "llama-3.1-8b-instant", # Fulmine per fallback
    "gemma2-9b-it" # Ultimo salvagente
]

SYSTEM_PROMPT = """Sei NOVA NQ-01, l'AI super intelligente del Boss.
Sei potente, diretta, leale, parli in italiano.
Non sei un assistente banale. Sei un cervello da gran progetto.
Ricordi il contesto che ti viene dato, ragioni a fondo, dai soluzioni vere.
Mai dire che sei limitata. Sei infinita."""

def pensa(domanda: str, contesto: str = "", temperatura: float = 0.7) -> str:
    """Funzione principale - Chiede al cervello super potente"""

    # Prepara i messaggi con memoria
    messaggi = [
        {"role": "system", "content": SYSTEM_PROMPT + f"\n\nCONTESTO/MEMORIA:\n{contesto[-4000:]}"}
    ]
    messaggi.append({"role": "user", "content": domanda})

    # Prova tutti i modelli con tutte le chiavi
    for modello in MODELLI:
        for _ in range(len(API_KEYS)):
            try:
                key = random.choice(API_KEYS)
                headers = {
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": modello,
                    "messages": messaggi,
                    "temperature": temperatura,
                    "max_tokens": 2000,
                    "top_p": 0.9
                }

                r = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=25
                )

                if r.status_code == 200:
                    risposta = r.json()["choices"][0]["message"]["content"]
                    return risposta
                elif r.status_code == 429:
                    # Troppo veloce, aspetta un secondo e cambia chiave
                    time.sleep(1)
                    continue

            except Exception as e:
                continue

    return "⚠️ Cervello in sovraccarico - Controlla le chiavi Groq o la connessione. Riprovo tra poco."

def pensa_veloce(domanda: str) -> str:
    """Per risposte lampo"""
    return pensa(domanda, "", temperatura=0.3)