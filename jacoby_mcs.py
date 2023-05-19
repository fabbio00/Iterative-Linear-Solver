import numpy as np
class Jacoby:
    def __init__(self):
        pass
        
    def execute(self, A, b, x, tol):
        niter = 0
        new_vector = np.asarray([0]*len(x))
        inverted_p_matrix = 1/A.diagonal()
        residual = b - A.dot(new_vector)
        while np.linalg.norm(residual)/np.linalg.norm(b) >= tol and niter <= 20000:
            new_vector = new_vector + (inverted_p_matrix * (residual))
            residual = b - A.dot(new_vector)
            niter = niter +1
        return {"iter": niter, "err_rel": self.relative_error(x, new_vector)}
    
    def relative_error(self, x, xk1):
        return np.linalg.norm(np.subtract(xk1, x))/np.linalg.norm(x)
    
    def convergenza(A):
        conv = True
        for i in A:
            if(abs(A[i][i]) <= sum(A[i,:i])+sum(A[i,i+1:])):
                conv = False
                break
        return conv