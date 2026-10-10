import requests

SYS = "Sei NOVA NQ-01, super potente, parli italiano, leale al Boss, diretta, intelligente."

def pensa(domanda, contesto="", temperatura=0.7):
    memoria = contesto[-1500:] if contesto else "Nessun ricordo."
    user_prompt = f"Memoria: {memoria}\n\nDomanda del Boss: {domanda}"

    # API GRATIS SENZA CHIAVE - Pollinations
    try:
        payload = {
            "model": "openai",
            "messages": [
                {"role": "system", "content": SYS},
                {"role": "user", "content": user_prompt}
            ]
        }
        r = requests.post("https://text.pollinations.ai/openai", json=payload, timeout=40)
        if r.status_code == 200:
            j = r.json()
            # prova a leggere risposta
            if "choices" in j and len(j["choices"]) > 0:
                return j["choices"][0]["message"]["content"]
            if "response" in j:
                return j["response"]
            return r.text
        else:
            return f"Errore Pollinations {r.status_code}: {r.text[:100]}"
    except Exception as e:
        try:
            # Fallback 2: GET semplice (più compatibile)
            r2 = requests.get(f"https://text.pollinations.ai/{domanda.replace(' ', '%20')}", timeout=30)
            if r2.status_code == 200:
                return r2.text
            return f"Errore connessione: {e}"
        except Exception as e2:
            return f"Connessione fallita: {e2} - riprova, a-Shell a volte perde internet"