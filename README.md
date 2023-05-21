# Progetto Metodi del Calcolo Scientifico

Costruzione di una libreria per la risoluzione di sistemi lineari tramite metodi iterativi

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
Aggiornato a 19/05/2023

### Generico

- [x] Restituire i tempi di calcolo 
- [ ] Errore assoluto (se serve)
- [ ] Grafici sui risultati
- [ ] Metodo preliminare per i metodi che lo hanno (es. jacobi che dice subito se la matrice è risolvibile o meno )
- [ ] Fare file di python eseguibile
- [x] Sistemare e capire come raggruppare il codice

### Teoremi

- [ ] File controll
- [ ] capire come fare le varie print

### Grafici

- [ ] Grafici sulle matrici usate (per far capire quanto sono sparse)
- [ ] Istogramma del numero di iterazioni per una data tolleranza
- [ ] Istogramma dei tempi per una data tolleranza
- [ ] decrescita dell'errore relativo 