Per creare una calcolatrice scientifica con un'interfaccia grafica moderna in Python, possiamo utilizzare la libreria `tkinter` per l'interfaccia grafica e `math` per le funzioni matematiche. Di seguito ti fornisco il codice Python e il comando per installare le librerie necessarie.

### Comando per installare le librerie:
Non è necessario installare librerie aggiuntive oltre a quelle standard di Python, poiché `tkinter` e `math` sono incluse di default.

### Codice Python:

((CODICE NON COPIATO PER MOTIVI DI SPAZIO, DISPONIBILE SINGOLARMENTE IN QUESTA CARTELLA))

### Spiegazione del Codice:
1. **Interfaccia Grafica**: Utilizziamo `tkinter` per creare l'interfaccia grafica. La finestra della calcolatrice ha una dimensione di 400x600 pixel e un colore di sfondo moderno (`#2E3440`).

2. **Display**: Il display è un `Entry` widget che mostra l'equazione corrente e il risultato. È di sola lettura e ha un font grande per una migliore visibilità.

3. **Pulsanti**: I pulsanti sono disposti in una griglia e includono tutte le operazioni di base, funzioni scientifiche come seno, coseno, tangente, logaritmi, radici quadrate, potenze, e costanti come π e e.

4. **Funzionalità**: Quando un pulsante viene premuto, il valore viene aggiunto all'equazione corrente. Se viene premuto `=`, l'equazione viene valutata e il risultato viene mostrato nel display. I pulsanti `C` e `AC` consentono rispettivamente di cancellare l'ultimo carattere e di resettare completamente l'equazione.

5. **Gestione degli Errori**: Se l'equazione non è valida, viene mostrato un messaggio di errore.

### Esecuzione:
1. Copia e incolla il codice in un file Python (ad esempio, `calcolatrice.py`).
2. Esegui il file con Python:
   ```bash
   python calcolatrice.py
   ```

Questo codice creerà una calcolatrice scientifica con un'interfaccia grafica moderna e funzionalità complete.
