#Programma per il calcolo dei perimetri di quadrato, cerchio e rettangolo MA SCORBUTICO

import math #spiego successivamente perche ho importato la libreria math, ci servirà più avanti
def perimetro():
    print("Senti, questo aggeggio serve a calcolare il perimetro di una figura geometrica. Non è scienza missilistica, è solo un'operazione matematica di base. Metti dentro i dati e ti sputa fuori il risultato. Fine.")
    print("""
   Quadrato 
   Cerchio 
   Rettangolo 
""")

    print("Sì, ok, ma di quale figura vuoi calcolare il perimetro? Quadrato? Triangolo? Cerchio? Dillo e basta...e magari muoviti")
    inpututente = input ("-> ")

    if inpututente == 'Quadrato':
        print("Ok, allora hai scelto il quadrato. Adesso, dimmi quanto misura un lato. Non ho tutto il giorno...")
        lato = float(input("Dammi il lato, veloce:  "))
        print(f"Il perimetro del Quadrato è: {lato * 4}")

    elif inpututente == 'Cerchio':  # Ora questa è la sezione del Cerchio
        print("Ok, allora hai scelto il cerchio. Adesso, dimmi quanto misura un lato. Non ho tutto il giorno...")
        raggio = float(input("Dammi il raggio, veloce:  "))
        # Uso la librea math.pi per una maggiore precisione rispetto a scrivere 3.14
        print(f"Il perimetro del cerchio è: {2 * math.pi * raggio}")

    elif inpututente == 'Rettangolo':  # Ora questa è la sezione del Rettangolo
        print("Ok, allora hai scelto il rettangolo. Adesso, dimmi quanto misura un lato. Non ho tutto il giorno...")
        base = float(input("Daje dammi sta base su:  "))
        altezza = float(input("Daje dammi sta altezza su:  "))
        print(f"Il perimetro del rettangolo è: {base * 2 + altezza * 2}")

    else:
        print("Inserisci un numero da 1 a 3, non altri...pirla")

# Richiamiamo la funzione perimetro per avviare il programma
perimetro()