#Errori di Round off
Quando calcolo un valore da una formula, incorro in tre tipi di errori detti di "round off":
	1) incertezze sui valori (o sulla loro misura) usati nella formula 
	2) incertezza sulla rappresentazione dei numeri: essi sonon rappresentati con una precisione finita fino all' n-esima cifra decimale (non all'infinito)
	3) aritmetica: errori dovuti all'implementazione approssimata delle operazioni
	4) errori di approssimazione dovuti alle approssimazioni utilizzate nel modello fisico analizzato (Es: l'isocronismo delle piccole oscillazioni per il modello fisico del pendolo armonico)
	5) errori algoritmici dovuti al modo in cui scegliamo di approssimare le operazioni di alto livello nella simulazione

A contribuire all'errore di round-off è anche la limitatezza della precisione della macchina el rappresentare i numeri. 

#Precisione della macchina
E' il minimo numero rappresentabile dalla mantissa

#Limitazione dell'errore
Dobbiamo calcolare un integrale tramite l'approssiamzione dei rettangoli di Riemann. Sappiamo che all'aumentare del numero degli intervalli N, aumenta la precisione con cui risolviamo l'integrale e quindi diminuisce la cosidetta "incertezza algoritmica". In un grafico log-log all'aumentare di N, l'errore algoritmico decresce. Raggiunto un certo valore di N (N = N-0), che dipende dal problema e dall'algoritmo, l'errore algoritmico è minore di quello di round-off. Ciò significa che L'ERRORE TOTALE HA UN MINIMO.
