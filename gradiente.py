import numpy as np
from datetime import datetime


def solve(mtxA, vectB, vectX, tol):
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

        # Compressed version
        # vectX = vectX + (residual.T.dot(residual) / residual.T.dot(mtxA.dot(residual))) * residual

        residual = vectB - mtxA.dot(vectX1)

    end = datetime.now()
    delta = end - start
    # Risultato
    res = {
        "vectX": vectX1,
        "nIter": k,
        "time": int(delta.total_seconds() * 1e6),
        "eRel": np.linalg.norm(np.subtract(vectX1, vectX))/np.linalg.norm(vectX)
    }
    return res
