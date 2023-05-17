import numpy as np
class GradC:
    def __init__(self):
        pass
        
    def execute(self, A, b, x, tol):
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
        return {"iter": niter, "err_rel": self.relative_error(x, new_vector)}
    
    def relative_error(self, x, xk1):
        return np.linalg.norm(np.subtract(xk1, x))/np.linalg.norm(x)