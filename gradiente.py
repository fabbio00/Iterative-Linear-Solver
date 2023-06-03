import numpy as np
from datetime import datetime
import control as cr


def solve(A, b, x, tol):
    if (cr.is_sim_pos(A)):
        print("La matrice A è simmetrica e definita positiva, quindi converge per ogni valore del vettore iniziale")
    else:
        print("La matrice A non è simmetrica o definita positiva")
    start = datetime.now()

    # Variabili
    k = 0
    vectX1 = np.zeros(A.shape[0])
    residual = b - A.dot(vectX1)

    # Funzione
    while np.linalg.norm(residual)/np.linalg.norm(b) >= tol and k <= 20000:
        k += 1
        y = A.dot(residual)
        a = residual.T.dot(residual)
        b = residual.T.dot(y)
        alpha = a/b

        vectX1 = vectX1 + alpha * residual

        residual = b - A.dot(vectX1)

    end = datetime.now()
    delta = end - start
    if k > 20000:
        if np.linalg.norm(residual)/np.linalg.norm(b) >= tol:
            print("superato il numero massimo di iterazioni")
    # Risultato
    res = {
        "x": vectX1,
        "nIter": k,
        "time": int(delta.total_seconds() * 1e6),
        "eRel": cr.relative_error(x, vectX1)
    }
    return res
