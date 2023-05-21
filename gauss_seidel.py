import numpy as np
from scipy.sparse import tril
from scipy.sparse.linalg import spsolve_triangular
from datetime import datetime


def solve(mtxA, vectB, vectX, tol):
    start = datetime.now()
    # Variabili
    maxIter = 20000
    mtxP = tril(mtxA, format="csr")
    k = 0
    vectX1 = np.zeros(mtxA.shape[0])
    residual = vectB - mtxA.dot(vectX1)

    # Funzione
    while np.linalg.norm(residual)/np.linalg.norm(vectB) >= tol and k < maxIter:
        k += 1
        vectX1 = vectX1 + spsolve_triangular(mtxP, residual, lower=True)
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
