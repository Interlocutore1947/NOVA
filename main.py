"""
main.py - NOVA NQ-01 - Corpo principale
Collega cervello super potente + memoria potente
"""
from cervello import pensa
from memoria import salva, leggi, cerca, stats, leggi_tutto

print("===================================")
print("   NOVA NQ-01 SUPER POTENTE ACCESA")
print("===================================")
print(f"Memoria: {stats()}")
print("\nComandi:")
print(" - scrivi normale per parlare con NOVA")
print(" - 'ricordi' per vedere ultimi ricordi")
print(" - 'cerca parola' per cercare in memoria")
print(" - 'stats' per vedere quanti ricordi")
print(" - 'cancella' per resettare memoria")
print(" - 'esci' per chiudere")
print("===================================\n")

while True:
    try:
        domanda = input("Tu: ").strip()
        
        if not domanda:
            continue

        if domanda.lower() == "esci":
            print("\nNOVA: A dopo Boss! Spengo.")
            break

        if domanda.lower() == "ricordi":
            print(f"\n--- MEMORIA ---\n{leggi(30)}\n")
            continue

        if domanda.lower().startswith("cerca "):
            parola = domanda[6:]
            print(f"\n--- CERCO '{parola}' ---\n{cerca(parola)}\n")
            continue

        if domanda.lower() == "stats":
            print(f"\n{stats()}\n")
            continue

        if domanda.lower() == "cancella":
            conferma = input("Sicuro? (si/no): ")
            if conferma.lower() == "si":
                from memoria import cancella
                print(cancella())
            continue

        # === QUI SUCCEDE LA MAGIA ===
        # 1. Prende memoria
        contesto = leggi_tutto()
        # 2. Chiede al cervello super potente
        print("\nNOVA sta pensando...")
        risposta = pensa(domanda, contesto)
        print(f"\nNOVA: {risposta}\n")

        # 3. Salva tutto in memoria potente
        salva(f"Tu: {domanda}", "dialogo")
        salva(f"NOVA: {risposta}", "dialogo")

    except KeyboardInterrupt:
        print("\nChiusura...")
        break
    except Exception as e:
        print(f"Errore: {e}")