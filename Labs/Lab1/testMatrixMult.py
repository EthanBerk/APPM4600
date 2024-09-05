import numpy as np
import numpy.linalg as la
import math
def driver():
    m = 4
    n = 5
    p = 4
    x = np.random.rand(m,n)
    y = np.random.rand(n,p)

    # evaluate the dot product of y and w
    dp = matrixVectMult(x, y, m, n, p)
    # print the output
    print('matrix vector multplication is : ', dp)
    return
def matrixVectMult(x, y, m, n, p):
    # Computes matrix vector multplication beetween matrix x(m, n) and matrix y(n,p) 

    f = np.empty((m,p));
    for i in range(p):
        for j in range(m):
            f[i, j] = dotProduct(x[j, 0:], y[0:, i], n)
    return f

def dotProduct(x,y,n):
    # Computes the dot product of the n x 1 vectors x and y
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]
    return dp
driver()