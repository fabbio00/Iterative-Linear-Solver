import numpy as np
from datetime import datetime
import control as cr


def solve(A, b, x, tol):
    if (cr.is_sim_pos(A)):
        print("La matrice A è simmetrica e definita positiva, quindi converge in al più " +
              str(A.shape[0]) + " iterazioni")
    else:
        print("La matrice A non è simmetrica o definita positiva")
    start = datetime.now()
    niter = 0
    new_vector = np.asarray([0]*len(x))
    residual = b - A.dot(new_vector)
    dir = residual.copy()
    while np.linalg.norm(residual)/np.linalg.norm(b) >= tol and niter <= 20000:
        y = A.dot(dir)
        z = A.dot(residual)
        ak = (np.dot(dir, residual)) / (np.dot(dir, y))
        new_vector = new_vector + (ak * dir)
        residual = b - A.dot(new_vector)
        w = A.dot(residual)
        bk = (np.dot(dir, w)) / (np.dot(dir, y))
        dir = residual - (bk*dir)

        residual = b - A.dot(new_vector)
        niter = niter + 1

    end = datetime.now()
    delta = end - start
    if niter > 20000:
        if np.linalg.norm(residual)/np.linalg.norm(b) >= tol:
            print("superato il numero massimo di iterazioni")
    # Risultato
    res = {
        "vectX": new_vector,
        "nIter": niter,
        "time": int(delta.total_seconds() * 1e6),
        "eRel": cr.relative_error(x, new_vector)
    }
    return res
