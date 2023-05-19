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

```JSON
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

```JSON
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