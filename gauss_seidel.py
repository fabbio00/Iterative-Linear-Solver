import numpy as np
import control as cr
from scipy.sparse import tril
from scipy.sparse.linalg import spsolve_triangular
from datetime import datetime


def solve(A, b, x, tol):
    if (cr.row_diagonal_dominance(A)):
        print("La matrice A è a dominanza diagonale per righe, quindi converge")
    else:
        print("La matrice A non è a dominanza diagonale per righe, quindi non è detto che converga")
    start = datetime.now()
    # Variabili
    maxIter = 20000
    mtxP = tril(A, format="csr")
    k = 0
    vectX1 = np.zeros(A.shape[0])
    residual = b - A.dot(vectX1)

    # Funzione
    while np.linalg.norm(residual)/np.linalg.norm(b) >= tol and k <= maxIter:
        k += 1
        vectX1 = vectX1 + spsolve_triangular(mtxP, residual, lower=True)
        residual = b - A.dot(vectX1)

    end = datetime.now()
    delta = end - start
    if k > 20000:
        if np.linalg.norm(residual)/np.linalg.norm(b) > tol:
            print("superato il numero massimo di iterazioni")
    # Risultato
    res = {
        "x": vectX1,
        "nIter": k,
        "time": int(delta.total_seconds() * 1e6),
        "eRel": cr.relative_error(x, vectX1)
    }
    return res
