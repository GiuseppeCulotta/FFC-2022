#Dicretizzare una derivata
Discretizzare una derivata significa approssimarla con un rapporto incrementale. La discretizzazione delle derivate è fndamentale per poter discretizzare le equazioni differenziali e per esprimere una approssimazione della funzione in prossimità di un punto del dominio.
Quando parliamo di "discretizzare" una derivata in un contesto numerico o computazionale, intendiamo sostituire la derivata continua di una funzione con un'approssimazione che utilizza valori discreti, cioè valori calcolati a intervalli finiti lungo il dominio.
In pratica,essendo la derivata il limite del rapporto incrementale, non possiamo calcolare il limite esatto nel computer, quindi approssimiamo la derivata utilizzando un intervallo finito Δx (detto anche PASSO o TIME-STEP). Esistono vari modi per discretizzare una derivata:
	1)Differenza in avanti (Forward Difference): questo
	è un metodo di approssimazione al primo ordine, cioè
	l'errore è proporzionale a Δx.
	2)Differenza all'indietro (Backward Difference):
	uguale al precedente
	3)Differenza centrale (Central Difference):
	Questa è un'approssimazione di secondo ordine,
	quindi l'errore è proporzionale a (Δx)^2,
	risultando più accurata rispetto ai metodi
	precedenti.

Quando discretizzi una derivata, stai trasformando un problema continuo (che può richiedere calcoli infinitesimali) in un problema numerico risolvibile su un computer. Questo è essenziale per tutti i metodi numerici (come, per esempio, Eulero-Cromer o Velocity-Verlet).

#Step per la discretizzazione
1) Divido l'intervallo di definizione della funzione (ovvero il dominio) in N sotto-intervalli di ampiezza h data da:
	h = (|b-a|)/N
chiamerò "griglia" gli estremi dei sotto-intervalli dove è definita la funzione. Avrò che:
	x_i = a + ih, con i = 0,1,2,...,N
	f_i = f(x_i)
	


