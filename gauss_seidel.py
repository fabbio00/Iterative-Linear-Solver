import numpy as np
import control as cr
from scipy.sparse import tril
from scipy.sparse.linalg import spsolve_triangular
from datetime import datetime


def solve(mtxA, vectB, vectX, tol):
    if(cr.row_diagonal_dominance(mtxA)):
        print("La matrice A è a dominanza diagonale per righe, quindi converge")
    else:
        print("La matrice A non è a dominanza diagonale per righe, quindi non è detto che converga")
    start = datetime.now()
    # Variabili
    maxIter = 20000
    mtxP = tril(mtxA, format="csr")
    k = 0
    vectX1 = np.zeros(mtxA.shape[0])
    residual = vectB - mtxA.dot(vectX1)

    # Funzione
    while np.linalg.norm(residual)/np.linalg.norm(vectB) >= tol and k <= maxIter:
        k += 1
        vectX1 = vectX1 + spsolve_triangular(mtxP, residual, lower=True)
        residual = vectB - mtxA.dot(vectX1)

    end = datetime.now()
    delta = end - start
    if k > 20000:
        if np.linalg.norm(residual)/np.linalg.norm(vectB) > tol:
            print("superato il numero massimo di iterazioni")
    # Risultato
    res = {
        "vectX": vectX1,
        "nIter": k,
        "time": int(delta.total_seconds() * 1e6),
        "eRel": cr.relative_error(vectX, vectX1)
    }
    return res
