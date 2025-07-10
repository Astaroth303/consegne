
import math #spiego successivamente perche ho importato la libreria math, ci servirà più avanti
def perimetro():
    print("Questo programma calcola il perimetro di una figura geometrica!")
    print("""
   Quadrato -> 1
   Cerchio -> 2
   Rettangolo -> 3
""")

    print("Di quale figura vuoi calcolare il perimetro? ")
    inpututente = int(input("-> "))

    if inpututente == 1:
        print("Hai scelto il quadrato, ora devi darmi le misure...")
        lato = float(input("Inserisci il lato del quadrato:  "))
        print(f"Il perimetro del Quadrato è: {lato * 4}")

    elif inpututente == 2:  # Ora questa è la sezione del Cerchio
        print("Hai scelto il cerchio, ora devi darmi le misure...")
        raggio = float(input("Inserisci il raggio:  "))
        # Uso la librea math.pi per una maggiore precisione rispetto a scrivere 3.14
        print(f"Il perimetro del cerchio è: {2 * math.pi * raggio}")

    elif inpututente == 3:  # Ora questa è la sezione del Rettangolo
        print("Hai scelto il rettangolo, ora devi darmi le misure...")
        base = float(input("Inserisci la grandezza della base:  "))
        altezza = float(input("Inserisci l'altezza:  "))
        print(f"Il perimetro del rettangolo è: {base * 2 + altezza * 2}")

    else:
        print("Inserisci un numero da 1 a 3, non altri...pirla")

# Richiamiamo la funzione perimetro per avviare il programma
perimetro()