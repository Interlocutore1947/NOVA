import requests

KEY = "gsk_INCOLLA_QUI"
MODELLI = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "gemma2-9b-it"]
SYS = "Sei NOVA NQ-01, super intelligente, parli italiano, leale al Boss, diretta e potente."

def pensa(domanda, contesto="", temperatura=0.7):
    messaggi = [
        {"role": "system", "content": SYS + "\nMemoria:\n" + contesto[-2000:]},
        {"role": "user", "content": domanda}
    ]
    for modello in MODELLI:
        try:
            headers = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}
            payload = {"model": modello, "messages": messaggi, "temperature": temperatura, "max_tokens": 1500}
            r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload, timeout=20)
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"]
        except:
            continue
    return "Errore Groq - controlla chiave su console.groq.com"