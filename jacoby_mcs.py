import numpy as np
import control as cr
from datetime import datetime
    
def solve(A, b, x, tol):
    if(cr.row_diagonal_dominance(A)):
        print("La matrice A è a dominanza diagonale per righe, quindi converge")
    else:
        print("La matrice A non è a dominanza diagonale per righe, quindi non è detto che converga")
    start = datetime.now()
    niter = 0
    new_vector = np.asarray([0]*len(x))
    inverted_p_matrix = 1/A.diagonal()
    residual = b - A.dot(new_vector)
    while np.linalg.norm(residual)/np.linalg.norm(b) >= tol and niter <= 20000:
        new_vector = new_vector + (inverted_p_matrix * (residual))
        residual = b - A.dot(new_vector)
        niter = niter +1
#    return {"iter": niter, "err_rel": relative_error(x, new_vector)}

    end = datetime.now()
    delta = end - start
    if niter > 20000:
        if np.linalg.norm(residual)/np.linalg.norm(b) > tol:
            print("superato il numero massimo di iterazioni")
    # Risultato
    res = {
        "vectX": new_vector,
        "nIter": niter,
        "time": int(delta.total_seconds() * 1e6),
        "eRel": cr.relative_error(x, new_vector)
    }
    return res