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

$\frac{||r^{(k)}||}{||b||} < tol$

Dove $r^{(k)}$ è il residuo alla k-esima iterazione calcolato come $r^{(k)}=Ax^{(k)} − b$

Sono state controllate volta per volta 4 **tolleranze** diverse, ovvero:
$tol = [10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}]$

Inoltre viene fatto un controllo sul **numero massimo di iterazioni** che se superato viene segnalata la mancata convergenza $(k>maxIter)$ dove $maxIter = 2000$

## Metodo di Jacobi

### Pseudocodice

1. $x^{(k+1)} = x^{(k)} + P^{-1}r^{(k)}$

Dove $P^{-1}$ è una matrice diagonale costruita nel seguente modo:

$$
P^{-1}:=\left[\begin{array}{cccc}
1 / a_{1,1} & 0 & \cdots & 0 \\
0 & 1 / a_{2,2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1 / a_{n, n}
\end{array}\right]
$$

## Metodo di Gauß-Seidel

### Idea alla base

$x^{(k+1)}_i =\frac{1}{a_{i,i}} ( b_i – a_{i,1}x^{(k+1)}_1 − \cdots  – a_{i,i−1} x^{(k+1)}_{i−1}  − a_{i,i+1} x^{(k)}_{i+1}  − \cdots – a_{i,n}x^{(k)}_n)$

### Psudocodice

1. $r^{(k)} = b − Ax^{(k)}$
2. Sostituzione in avanti $Py = r^{(k)}$
3. $x^{(k+1)} = y^{(k)} + y$

Dove la matrice $P$ è costruita nel seguente modo:

$$
P:=\left[\begin{array}{cccc}
a_{1,1} & 0 & \cdots & 0 \\
a_{2,1} & a_{2,2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
a_{n, 1} & a_{n, 2} & \cdots & a_{n, n}
\end{array}\right]
$$

## Metodo del Gradiente

### Psudocodice

1. $r^{(k)} = b -Ax^{(k)}$
2. $y^{(k)} = Ar^{(k)}$
3. $a = (r^{(k)})^tr^{(k)}$
4. $b = (r^{(k)})^ty^{(k)}$
5. $\alpha_k = a/b$
6. $x^{(k+1)} = r^{(k)} \alpha_kr^{(k)}$

## Metodo del Gradiente coniugato

### Pseudocode

1. $r^{(k)}=b−Ax^{(k)}$
2. $y^{(k)} = Ad^{(k)}$
3. $z^{(k)} = Ar^{(k)}$
4. $\alpha_k = (d^{(k)} · r^{(k)})/(d^{(k)} · y^{(k)})$
5. $x^{(k+1)} = x^{(k)} + \alpha_kd^{(k)}$
6. $r^{(k+1)}=b−Ax^{(k+1)}$
7. $w^{(k)} = Ar^{(k+1)}$
8. $\beta_k = (d^{(k)} · w^{(k)})/(d^{(k)} · y^{(k)})$
9. $d^{(k+1)} = r^{(k+1)} − \beta_kd^{(k)}$

## Descrizione rapida dei file

- `README.md`
  - Descrizione tecnica del progetto
- `jacoby.py`
  - Implementazione dell’algoritmo risolutivo di Jacoby
- `gauss_seidel.py`
  - Implementazione dell’algoritmo risolutivo di Gauß-Seidel
- `gradiente.py`
  - Implementazione dell’algoritmo risolutivo del Gradiente
- `gradiente_coniugato.py`
  - Implementazione dell’algoritmo risolutivo del Gradiente Coniugato
- `control.py`
  - Definizione di diverse funzioni di usate per effettuare dei controlli nei diversi algoritmi realizzati
- `main.py`
  - File eseguibile dove vengono calcolati i vettori soluzione richiesti e si salvano i risultati
- `Progetto_MCS.ipynb`
  - Notebook in cui vengono esaminate le matrici usate e analizzati i risultati ottenuti
- `utils.py`
  - Definizione di funzioni utili all’analisi dei risultati


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

Aggiornato a 27/05/2023

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
- [x] Istogramma del numero di iterazioni per una data tolleranza di ogni metodo
- [x] Istogramma dei tempi per una data tolleranza di ogni metodo
- [x] Istogramma dell'errore relatico per una data tolleranza di ogni metodo
- [x] Decrescita dell'errore relativo
- [x] Residuo
