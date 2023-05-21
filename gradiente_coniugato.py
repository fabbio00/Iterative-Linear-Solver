import numpy as np
from scipy.sparse.linalg import eigsh
from datetime import datetime

def solve(A, b, x, tol):
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
    # Risultato
    res = {
        "vectX": new_vector,
        "nIter": niter,
        "time": int(delta.total_seconds() * 1e6),
        "eRel": relative_error(x, new_vector)
    }
    return res

def relative_error(x, xk1):
    return np.linalg.norm(np.subtract(xk1, x))/np.linalg.norm(x)

def convergenza(A):
    conv = True
    if(not np.allclose(A.toarray(), A.toarray().T)):
        conv = False
    if(not eigsh(A, k=1, which='LM')[0] > 0):
        conv = False
    return conv