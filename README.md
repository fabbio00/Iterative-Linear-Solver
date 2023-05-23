# Progetto Metodi del Calcolo Scientifico

Costruzione di una libreria per la risoluzione di sistemi lineari tramite i seguenti metodi iterativi:

- Metodo di Jacobi
- Metodo di Gauß-Seidel
- Metodo del Gradiente
- Metodo del Gradiente coniugato

La **matrice A** viene acquisita leggendo i  dati da un file `.mtx`

Il **vettore soluzione x** è un vettore composto da tutti $1$

Il **vettore b** viene calcolato dal vettore soluzione x col seguente calcolo $b=Ax$ 

Il **vettore x di partenza** usato da tutti i metodi è un vettore della stessa grandezza della matrice A e con tutti i valori a zero

I metodi si e arrestarsi qualora la k-esima iterata $x^{(k)}$ soddisfa il seguente **criterio di arresto**:

$\frac{||Ax^{(k)} − b||}{||b||} < tol$

Sono state controllate volta per volta 4 **tolleranze** diverse, ovvero:
$tol = [10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}]$

Inoltre viene fatto un controllo sul **numero massimo di iterazioni** che se superato viene segnalata la mancata convergenza $(k>maxIter)$ dove $maxIter = 2000$


## Metodo di Jacobi

## Metodo di Gauß-Seidel

### Psudocodice

1. $r^{(k)} = b − Ax^{(k)}$
2. Sostituzione in avanti Py = r^{(k)}
3. $x^{(k+1)} = y^{(k)} + y$

## Metodo del Gradiente

### Psudocodice

1. $r^{(k)} = b -Ax^{(k)}$
2. $y^{(k)} = Ar^{(k)}$
3. $a = (r^{(k)})^tr^{(k)}$
4. $b = (r^{(k)})^ty^{(k)}$
5. $\alpha_k = a/b$
6. $x^{(k+1)} = r^{(k)} \alpha_kr^{(k)}$

## Metodo del Gradiente coniugato

## Risultati

### Risultati di ogni funzione

Dizionario contenente

- Vettore X calcolato `"vectX"`
- Numero di iterazioni fatte `"nIter"`
- Tempo impeigato in mirosecondi `"time"`
- Errore relativo `"eRel"`

Esempio:

```python
res = {
    "vectX" : [],
    "nIter" : 150,
    "time" : 1654545,
    "eRel" : 0.0000001 
}
```

### Risulati finali

Dizionario suddiviso per ogni ogni metodo usato, ognuno di questi conterrà un ulteriore dizionario per ogni matrice in input che conterrà i risultati ottenuti per ogni tolleranza testata

Esempio:

```python
resTot = {
    "Jacoby" : {
        "spa1" : [
            {
                "tol" : 0.0001,
                "nIter" : 150,
                "time" : 1654545,
                "eRel" : 0.0000001 
            }
        ]
    }
}
```


## ToDo
Aggiornato a 21/05/2023

### Generico

- [x] Restituire i tempi di calcolo
- [ ] Grafici sui risultati
- [x] Metodo preliminare per i metodi che lo hanno (es. jacobi che dice subito se la matrice è risolvibile o meno )
- [ ] Fare file di python eseguibile
- [x] Sistemare e capire come raggruppare il codice

### Teoremi & Controlli

- [x] File controll
- [x] capire come fare le varie print

### Grafici

- [x] Grafici sulle matrici usate (per far capire quanto sono sparse)
- [x] Istogramma del numero di iterazioni per una data tolleranza di ogni matrice
- [x] Istogramma dei tempi per una data tolleranza di ogni matrice
- [x] Istogramma dell'errore relatico per una data tolleranza di ogni matrice
- [ ] Istogramma del numero di iterazioni per una data tolleranza di ogni metodo
- [ ] Istogramma dei tempi per una data tolleranza di ogni metodo
- [ ] Istogramma dell'errore relatico per una data tolleranza di ogni metodo
- [ ] Decrescita dell'errore relativo 