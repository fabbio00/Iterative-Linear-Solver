import numpy as np
from scipy.sparse import tril
from scipy.sparse.linalg import spsolve_triangular


def relative_error(x, xk1):
    return np.linalg.norm(np.subtract(xk1, x))/np.linalg.norm(x)

    # Risultato
    return charts


def jacobi(A, b, x, tol):
    charts = {
        "residual_chart": [],
        "errrel_chart": [],
    }
    niter = 0
    new_vector = np.asarray([0]*len(x))
    inverted_p_matrix = 1/A.diagonal()
    residual = b - A.dot(new_vector)
    while np.linalg.norm(residual)/np.linalg.norm(b) >= tol and niter <= 20000:
        new_vector = new_vector + (inverted_p_matrix * (residual))
        charts["residual_chart"].append(
            np.linalg.norm(residual)/np.linalg.norm(b))
        charts["errrel_chart"].append(relative_error(x, new_vector))
        residual = b - A.dot(new_vector)
        niter = niter + 1
#    return {"iter": niter, "err_rel": relative_error(x, new_vector)}
    if niter > 20000:
        if np.linalg.norm(residual)/np.linalg.norm(b) >= tol:
            print("superato il numero massimo di iterazioni")
    # Risultato
    return charts


def gauss_seidel(mtxA, vectB, vectX, tol):
    # Variabili
    charts = {
        "residual_chart": [],
        "errrel_chart": [],
    }
    maxIter = 20000
    mtxP = tril(mtxA, format="csr")
    k = 0
    vectX1 = np.zeros(mtxA.shape[0])
    residual = vectB - mtxA.dot(vectX1)

    # Funzione
    while np.linalg.norm(residual)/np.linalg.norm(vectB) >= tol and k <= maxIter:
        k += 1
        vectX1 = vectX1 + spsolve_triangular(mtxP, residual, lower=True)
        charts["residual_chart"].append(
            np.linalg.norm(residual)/np.linalg.norm(vectB))
        charts["errrel_chart"].append(relative_error(vectX, vectX1))
        residual = vectB - mtxA.dot(vectX1)

    if k > 20000:
        if np.linalg.norm(residual)/np.linalg.norm(vectB) > tol:
            print("superato il numero massimo di iterazioni")
    # Risultato
    return charts


def gradiente(mtxA, vectB, vectX, tol):
    charts = {
        "residual_chart": [],
        "errrel_chart": [],
    }
    # Variabili
    k = 0
    vectX1 = np.zeros(mtxA.shape[0])
    residual = vectB - mtxA.dot(vectX1)

    # Funzione
    while np.linalg.norm(residual)/np.linalg.norm(vectB) >= tol and k <= 20000:
        k += 1
        y = mtxA.dot(residual)
        a = residual.T.dot(residual)
        b = residual.T.dot(y)
        alpha = a/b

        vectX1 = vectX1 + alpha * residual
        charts["residual_chart"].append(
            np.linalg.norm(residual)/np.linalg.norm(vectB))
        charts["errrel_chart"].append(relative_error(vectX, vectX1))
        residual = vectB - mtxA.dot(vectX1)
    if k > 20000:
        if np.linalg.norm(residual)/np.linalg.norm(vectB) >= tol:
            print("superato il numero massimo di iterazioni")


def gradiente_coniugato(A, b, x, tol):
    charts = {
        "residual_chart": [],
        "errrel_chart": [],
    }
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
        charts["residual_chart"].append(
            np.linalg.norm(residual)/np.linalg.norm(b))
        charts["errrel_chart"].append(relative_error(x, new_vector))
        residual = b - A.dot(new_vector)
        niter = niter + 1

    if niter > 20000:
        if np.linalg.norm(residual)/np.linalg.norm(b) >= tol:
            print("superato il numero massimo di iterazioni")
    # Risultato
    return charts


def printTime(time):
    tmp = []
    tmp.append(time)  # microsecondi - tmp[0]
    tmp.append((int)(tmp[0]/1000))  # millisecondi - tmp[1]
    tmp.append((int)(tmp[1]/1000))  # secondi - tmp[2]
    tmp.append((int)(tmp[2]/60))  # minuti - tmp[3]

    tmp[0] = tmp[0] - (tmp[1] * 1000)
    tmp[1] = tmp[1] - (tmp[2] * 1000)
    tmp[2] = tmp[2] - (tmp[3] * 60)

    mu = "\u03BC"

    if tmp[3] != 0:
        res = str(tmp[3]) + "m " + str(tmp[2]) + "s"
    elif tmp[2] != 0:
        res = str(tmp[2]) + "." + str(round(tmp[1]/100)) + "s"
    elif tmp[1] != 0:
        res = str(tmp[1]) + "." + str(round(tmp[0]/100)) + "ms"
    else:
        res = str(tmp[0]) + "u03BCs"

    # print(str(tmp[3]) + " : " + str(tmp[2]) + " : " + str(tmp[1]) + " : " + str(tmp[0]))
    # print(res)
    return (res)
