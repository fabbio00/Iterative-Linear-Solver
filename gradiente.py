import numpy as np
from datetime import datetime
import control as cr

def solve(mtxA, vectB, vectX, tol):
    if(cr.is_sim_pos(mtxA)):
        print("La matrice A è simmetrica e definita positiva, quindi converge per ogni valore del vettore iniziale")
    else:
        print("La matrice A non è simmetrica o definita positiva")
    start = datetime.now()

    # Variabili
    k = 0
    vectX1 = np.zeros(mtxA.shape[0])
    residual = vectB - mtxA.dot(vectX1)

    # Funzione
    while np.linalg.norm(residual)/np.linalg.norm(vectB) >= tol and k < 20000:
        k += 1
        y = mtxA.dot(residual)
        a = residual.T.dot(residual)
        b = residual.T.dot(y)
        alpha = a/b

        vectX1 = vectX1 + alpha * residual

        residual = vectB - mtxA.dot(vectX1)

    end = datetime.now()
    delta = end - start
    # Risultato
    res = {
        "vectX": vectX1,
        "nIter": k,
        "time": int(delta.total_seconds() * 1e6),
        "eRel": cr.relative_error(vectX, vectX1)
    }
    return res
