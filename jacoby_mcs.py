import numpy as np
from datetime import datetime
    
def solve(A, b, x, tol):
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
    for i in range(A.shape[0]):
        if(abs(A[i, i]) <= np.sum(A[i,:i])+np.sum(A[i,i+1:])):
            conv = False
            break
    return conv