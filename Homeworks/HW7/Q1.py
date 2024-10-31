import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 
import matplotlib.pyplot as plt

def driver():
    
    f = lambda x: 1/(1+(10*x)**2)
    N = 19;
    x = np.linspace(-1, 1, N)
    y = f(x)
    c = interpPoly(x, y, N)
    
    evalx = np.linspace(-1, 1, 1001)
    evalyp = np.zeros(1001)
    evalyf = f(evalx)
    for j in range(1001):
        evalyp[j] = evalPoly(evalx[j], c, N)
        
    plt.plot(evalx, evalyp, label = "poly N = "+  str(N));
    plt.plot(evalx, evalyf, label = "function");
    plt.plot(x, y, 'o');
    plt.legend()
    plt.show()
        
def evalPoly(x, c, N):
    y = 0;
    for i in range(N):
        y += c[i] * x**(N-i-1)
    return y
def interpPoly(x, y, n):
    V = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            V[i][j] = x[i]**(n-j-1)
    return inv(V).dot(y)
    
driver()