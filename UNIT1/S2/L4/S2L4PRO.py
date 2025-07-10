import math

def perimetro():
    print("Senti, questo aggeggio serve a calcolare il perimetro di una figura geometrica. Non è scienza missilistica, è solo un'operazione matematica di base. Metti dentro i dati e ti sputa fuori il risultato. Fine.")

    while True:  #implementazione funzione while
        print("""
   Quadrato
   Cerchio
   Rettangolo
""")

        print("Sì, ok, ma di quale figura vuoi calcolare il perimetro? Quadrato? Cerchio? Rettangolo? Dillo e basta...e magari muoviti")
        inpututente = input("-> ")

        if inpututente == 'Quadrato':
            print("Ok, allora hai scelto il quadrato. Adesso, dimmi quanto misura un lato. Non ho tutto il giorno...")
            lato = float(input("Dammi il lato, veloce:  "))
            print(f"Il perimetro del Quadrato è: {lato * 4}")

        elif inpututente == 'Cerchio':
            print("Ok, allora hai scelto il cerchio. Adesso, dimmi quanto misura il raggio. Non ho tutto il giorno...")
            raggio = float(input("Dammi il raggio, veloce:  "))
            print(f"Il perimetro del cerchio è: {2 * math.pi * raggio}")

        elif inpututente == 'Rettangolo':
            print("Ok, allora hai scelto il rettangolo. Adesso, dimmi quanto misurano i lati. Non ho tutto il giorno...")
            base = float(input("Daje dammi sta base su:  "))
            altezza = float(input("Daje dammi sta altezza su:  "))
            print(f"Il perimetro del rettangolo è: {base * 2 + altezza * 2}")

        else:
            print("Inserisci 'Quadrato', 'Cerchio' o 'Rettangolo', non altro... pirla.")

        # Chiediamo all'utente se vuole fare un altro calcolo, con l'aggiunta di lower in modo che se l'utente usa il maiuscolo a noi non interessa
        continua = input("Vuoi fare un altro calcolo? Scrivi 'si' o 'no', e sbrigati: ").lower()
        if continua != 'si':
            print("Finalmente! Ciao, e non tornare più.")
            break # Esce dal ciclo while True
perimetro()