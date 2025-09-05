#include <stdio.h>
#include <stdlib.h>

int main() {
    int vector[10], i, j, k;                           // Array di 10 elementi, variabili di controllo
    int swap_var;                                      // Variabile per scambio nel bubble sort
    int num_elementi;                                  // Numero di elementi da inserire (MODIFICATO)
    int modalita;                                      // Scelta modalità: sicura o vulnerabile
    
    // MENU PRINCIPALE
    printf("PROGRAMMA DI ORDINAMENTO CON GESTIONE BUFFER OVERFLOW\n");
    printf("=======================================================\n");
    printf("Scegli la modalità di esecuzione:\n\n");
    printf("1. Modalità SICURA (con controlli di input)\n");
    printf("2. Modalità VULNERABILE (senza controlli - possibile SEGFAULT)\n");
    printf("3. Esci\n\n");
    printf("Inserisci la tua scelta (1-3): ");
    
    scanf("%d", &modalita);                           // Legge scelta modalità
    printf("\n");
    
    // Gestione scelta modalità
    switch(modalita) {
        case 1:
            printf("=== MODALITÀ SICURA ATTIVATA ===\n");
            printf("I controlli di input prevengono buffer overflow\n\n");
            
            // CONTROLLI DI INPUT ATTIVI - Validazione numero elementi
            do {
                printf("Quanti interi vuoi inserire (1-10)? ");
                scanf("%d", &num_elementi);            // Legge numero con controllo
                
                if (num_elementi < 1 || num_elementi > 10) {
                    printf("ERRORE: Il numero deve essere tra 1 e 10!\n");  // Messaggio errore
                }
            } while (num_elementi < 1 || num_elementi > 10);  // Ripete finché valido
            
            break;
            
        case 2:
            printf("=== MODALITÀ VULNERABILE ATTIVATA ===\n");
            printf("*** ATTENZIONE: NESSUN CONTROLLO DI INPUT ***\n");
            printf("Inserire più di 10 elementi causerà BUFFER OVERFLOW!\n\n");
            
            // NESSUN CONTROLLO - Accetta qualsiasi numero (VULNERABILE)
            printf("Quanti interi vuoi inserire? ");   // PUNTO CRITICO: nessuna validazione
            scanf("%d", &num_elementi);               // Legge senza controlli
            
            break;
            
        case 3:
            printf("Programma terminato.\n");
            return 0;                                  // Esce dal programma
            
        default:
            printf("Scelta non valida!\n");
            return 1;                                  // Esce con errore
    }
    
    printf("Inserire %d interi:\n", num_elementi);    // Mostra quanti elementi inserire

    // CICLO DI INPUT - Può causare buffer overflow se num_elementi > 10
    for (i = 0; i < num_elementi; i++) {              // VULNERABILITÀ: può superare array[10]
        int c = i + 1;                                 // Converte indice per visualizzazione
        printf("[%d]:", c);                           // Mostra posizione corrente
        
        if (modalita == 1) {
            // MODALITÀ SICURA: Controllo input numerico
            while (scanf("%d", &vector[i]) != 1) {    // Verifica che sia un numero
                printf("ERRORE: Inserire un numero intero!\n");
                printf("[%d]:", c);                   // Richiede nuovamente
                while (getchar() != '\n');            // Pulisce buffer input
            }
        } else {
            // MODALITÀ VULNERABILE: Nessun controllo input
            scanf("%d", &vector[i]);                  // Legge direttamente senza controlli
        }
    }

    // STAMPA VETTORE INSERITO
    printf("\nIl vettore inserito e':\n");
    for (i = 0; i < num_elementi; i++) {              // Può leggere memoria non valida
        int t = i + 1;                                 // Conversione per display
        printf("[%d]: %d", t, vector[i]);             // ACCESSO ILLEGALE se i >= 10
        printf("\n");                                  // Nuova riga
    }

    // ALGORITMO BUBBLE SORT - Può operare su memoria corrotta
    for (j = 0; j < num_elementi - 1; j++) {          // Ciclo esterno: n-1 passate
        for (k = 0; k < num_elementi - j - 1; k++) {  // Ciclo interno: confronti adiacenti
            if (vector[k] > vector[k+1]) {            // Confronto elementi (può essere illegale)
                // Scambio elementi
                swap_var = vector[k];                  // Salva elemento corrente
                vector[k] = vector[k+1];              // Sposta elemento minore
                vector[k+1] = swap_var;               // Posiziona elemento maggiore
            }
        }
    }

    // STAMPA VETTORE ORDINATO
    printf("\nIl vettore ordinato e':\n");
    for (j = 0; j < num_elementi; j++) {              // Può stampare memoria corrotta
        int g = j + 1;                                 // Conversione per display
        printf("[%d]:", g);                           // Stampa posizione
        printf("%d\n", vector[j]);                    // ACCESSO ILLEGALE se j >= 10
    }
    
    // MESSAGGIO FINALE BASATO SULLA MODALITÀ
    if (modalita == 1) {
        printf("\n✅ Operazione completata in sicurezza!\n");
    }

    return 0;                                          // Termina programma
}

/*
SPIEGAZIONE DELLA MODIFICA AL PROGRAMMA ORIGINALE:

PROGRAMMA ORIGINALE (dalla traccia):
- Ciclo fisso: for (i = 0; i < 10; i++)
- Input sempre limitato a 10 elementi
- Completamente sicuro

MODIFICA APPLICATA:
- Aggiunta variabile: int num_elementi
- Aggiunto input: scanf("%d", &num_elementi) 
- Ciclo modificato: for (i = 0; i < num_elementi; i++)
- VULNERABILITÀ: se num_elementi > 10, si scrive oltre vector[10]

PUNTO CRITICO DELLA VULNERABILITÀ:
Il controllo dell'input utente è il punto dove si concentra la vulnerabilità.
Nella modalità vulnerabile, l'utente può inserire qualsiasi numero,
anche maggiore di 10, causando scrittura oltre i limiti dell'array.

ISTRUZIONI PER TESTARE:
1. Compilare: gcc -o program programma.c
2. Eseguire: ./program  
3. Scegliere modalità 2 (Vulnerabile)
4. Inserire numero > 10 (es: 15, 25, 50)
5. Inserire i valori richiesti
6. Osservare comportamento anomalo o segmentation fault

La vulnerabilità deriva dalla mancanza di controllo sull'input dell'utente
rispetto alla capienza del vettore di destinazione (10 elementi).
*/