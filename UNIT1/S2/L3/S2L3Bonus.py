import re

def conta_parole():
    """
    Chiede all'utente una stringa di testo, la analizza e restituisce un dizionario
    con il conteggio delle occorrenze di ciascuna parola, ignorando la punteggiatura
    e la distinzione tra maiuscole e minuscole.
    """
    # Chiede all'utente di inserire il testo o la singola parola
    testo = input("Inserire il testo da analizzare: ")

    # Converte il testo in minuscolo
    testo = testo.lower()

    # Spiegazione dettagliata del funzionamento di re.sub:
    # re.sub è un metodo del modulo 're' che usa la funzione 'sub' (substitute).
    # Cerca le limitazioni che noi gli diamo (il pattern) e le sostituisce
    # con qualcosa che forniamo, nel nostro caso con uno spazio.
    # 'r' davanti alla stringa si riferisce a una "raw string" e previene problemi
    # con i caratteri speciali di escape come '\n' o '\t'.
    # '[]' indica una classe di caratteri, corrispondendo a qualsiasi carattere al suo interno.
    # '^' all'interno delle parentesi quadre fa da negazione, indicando "qualsiasi carattere TRANNE quelli successivi".
    # '\w' indica tutti i caratteri alfanumerici (lettere dalla 'a' alla 'z', dalla 'A' alla 'Z', numeri dallo '0' al '9') e l'underscore '_'.
    # '\s' indica gli spazi bianchi (spazi, tabulazioni, a capo, ecc.).
    # In sintesi, '[^\w\s]' cerca qualsiasi carattere che non sia un carattere di parola
    # (alfanumerico o underscore) e non sia uno spazio. Trova quindi punteggiatura o simboli speciali.
    testo_pulito = re.sub(r'[^\w\s]', ' ', testo)

    # Divide il testo pulito in una lista di parole singole
    parole = testo_pulito.split()

    # Inizializza un dizionario vuoto per tenere conto delle occorrenze delle parole
    conteggio_parole = {}

    # Itera su ciascuna parola nella lista e aggiorna il conteggio
    for parola in parole:
        if parola:
            # Se la parola è già nel dizionario, incrementa il suo conteggio
            if parola in conteggio_parole:
                conteggio_parole[parola] += 1
            # Se la parola non è ancora nel dizionario, viene aggiunta con +1
            else:
                conteggio_parole[parola] = 1

    # Restituisce il dizionario finale con i conteggi delle parole contando anche le parole ripetute più volte
    return conteggio_parole
risultato = conta_parole()
print(risultato)