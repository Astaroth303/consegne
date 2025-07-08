//Si scriva un programma che esegua l'operazione di moltiplicazione tra due numeri inseriti dall'utente.
#include <stdio.h>

int main() {
     int numero1, numero2;              //Dichiarazione delle variabili, in questo caso moltiplicheremo due numeri, quindi numero 1 e numero 2
     int risultato;                     //Dichiarazione della variabile risultato, nel nostro caso in risultato della moltiplicazione
     

     printf("Calcolo di una moltiplicazione fra due numeri\n");


     printf("Inserire il primo numero:  ");
     scanf("%d", &numero1);             //In questa fase viene chiesto all'utente di inserire il primo numero per la moltiplicazione che poi tramite la funzione scan verrà richiamato come numero 1


     printf("Inserire il secondo numero:  ");
     scanf("%d", &numero2);             //In questa seconda fase proprio come sopra viene chiesto all'utente di inserire il secondo numero per la moltiplicazione che viene sempre richiamato tramite la funzione di scan ma in questo caso richiamiamo il numero 2

     
     risultato = numero1 * numero2;      //In questa fase calcoliamo il risultato della moltiplicazione
    

     printf("Il risultato della tua moltiplicazione è:  %d\n",risultato);      //In questa fase viene mostrato a schermo tramite il printf il risultato della moltiplicazione


     printf("Buona giornata :) ");


     return 0;

}

