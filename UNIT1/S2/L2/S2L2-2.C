//Si scriva un programma in linguaggio C che legga due valori interi e visualizzi la loro media aritmetica.
#include <stdio.h>

int main() {
     int numero1, numero2;              //Dichiarazione delle variabili, in questo caso ci servono per la media di due numeri, quindi numero 1 e numero 2
     float media;                       //Dichiarazione della variabile media
     

     printf("Calcolo della media fra due numeri\n");


     printf("Inserire il primo numero:  ");
     scanf("%d", &numero1);             //In questa fase viene chiesto all'utente di inserire il primo numero per la media che poi tramite la funzione scan verrà richiamato come numero 1


     printf("Inserire il secondo numero:  ");
     scanf("%d", &numero2);             //In questa seconda fase proprio come sopra viene chiesto all'utente di inserire il secondo numero per la media che viene sempre richiamato tramite la funzione di scan ma in questo caso richiamiamo il numero 2
     
     media = (numero1 + numero2) /2;      //In questa fase calcoliamo la media e quindi addizioniamo i due numeri e poi dividiamo per 2.
    

     printf("La media dei due numeri è:  %.2f\n",media);      //In questa fase viene mostrato a schermo tramite il printf il risultato della media fra i due numeri


     printf("Buona giornata :) ");


     return 0;

}