import numpy as np


def solve(self, mtxA, vectB, tol, maxIter):
    # Creating utils variable
    mtxP = mtxA.copy()
    mtxN = mtxA.copy()
    for i in range(len(mtxA)):
        for j in range(len(mtxA)):
            if (i <= j):
                mtxN[i][j] = 0
            else:
                mtxN[i][j] = -mtxN[i][j]
                mtxP[i][j] = 0

    k = 0
    vectX = np.random.rand(mtxA.shape[1])
    residual = np.subtract(vectB, mtxA.dot(vectX))

    while (np.linalg.norm(residual) > tol) and k < maxIter:
        k += 1
        for i in range(len(vectX)):
            xi = vectB[i]
            for j in range(len(vectX)):
                xi -= mtxA[i][j] * vectX[j]
            vectX[i] = xi/mtxA[i][i]
        residual = np.subtract(vectB, mtxA.dot(vectX))
        if k % 100 == 0:
            print(k, end="\t")
        if k % 1000 == 0:
            print()
            print(np.linalg.norm(residual))

    if (np.linalg.norm(residual) > tol):
        print("CIAO")
    else:
        print(tol)
        print(np.linalg.norm(residual))
