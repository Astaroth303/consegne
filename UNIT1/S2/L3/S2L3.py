#Scrivere un programma in Python che genera un nome per una band musicale utilizzando due input forniti dall'utente: la città di origine e il nome del proprio animale domestico.

#Richiesta di Input: Il programma deve chiedere all'utente di inserire: Il nome della città di origine. Il nome del proprio animale domestico.

cittaorigine = input ("Inserire il nome della propria città di origine:    ")

animaledomestico = input ("Inserire il nome del proprio animale domestico:   ")


#Generazione del nome band usando citta di origine e animale domestico, avrei potuto mettere trai due + un doppio apice per separare il nome ma preferisco averlo unito per scelta stilistica
nomeband = cittaorigine + animaledomestico

#Generazione del nome della band
print(f"Il nome della band combinando la tua città e il nome dell'animale è:{nomeband}")