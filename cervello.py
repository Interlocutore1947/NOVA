import requests

SYS = "Sei NOVA NQ-01, super intelligente, parli italiano, sei leale al tuo Boss, diretta, potente, con memoria."

def pensa(domanda, contesto="", temperatura=0.7):
    # Costruisce il prompt con memoria
    prompt = f"{SYS}\n\nMEMORIA RECENTE:\n{contesto[-2000:]}\n\nBoss dice: {domanda}\nNOVA rispondi:"

    # 3 tentativi con API gratis senza chiave
    urls = [
        f"https://text.pollinations.ai/{requests.utils.quote(prompt)}",
        "https://api.duckduckgo.com",
    ]

    try:
        # Metodo 1: Pollinations (gratis, no chiave, super veloce)
        r = requests.get(f"https://text.pollinations.ai/{requests.utils.quote(prompt)}", timeout=30)
        if r.status_code == 200 and len(r.text) > 5:
            return r.text.strip()
    except:
        pass

    try:
        # Metodo 2: Pollinations POST (più stabile)
        r = requests.post(
            "https://text.pollinations.ai/openai",
            json={
                "model": "openai",
                "messages": [
                    {"role": "system", "content": SYS},
                    {"role": "user", "content": f"Memoria: {contesto[-1500:]}\n\n{domanda}"}
                ],
                "seed": 42
            },
            timeout=30
        )
        if r.status_code == 200:
            data = r.json()
            if "choices" in data:
                return data["choices"][0]["message"]["content"]
            return data.get("response", r.text)
    except Exception as e:
        return f"Errore connessione: {e} - riprova"

    return "NOVA è in attesa di connessione... riprova tra 2 sec"
    