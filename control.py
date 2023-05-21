import numpy as np
from scipy.sparse.linalg import eigsh

def relative_error(x, xk1):
    return np.linalg.norm(np.subtract(xk1, x))/np.linalg.norm(x)

def row_diagonal_dominance(A):
    conv = True
    for i in range(A.shape[0]):
        if(abs(A[i, i]) <= np.sum(A[i,:i])+np.sum(A[i,i+1:])):
            conv = False
            break
    return conv


def is_sim_pos(A):
    return is_sim(A) and is_pos(A)

def is_sim(A):
    return np.allclose(A.toarray(), A.toarray().T)

def is_pos(A):
    return eigsh(A, k=1, which='LM')[0] > 0