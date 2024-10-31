import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 
import matplotlib.pyplot as plt
import operator
from functools import reduce 
def prod(factors):
    return reduce(operator.mul, factors, 1)


def driver(): 
    f = lambda x: 1/(1+(10*x)**2)
    N = 21;
    x = np.linspace(-1, 1, N)
    y = f(x)
    
    evalx = np.linspace(-1, 1, 1001)
    evalyp = np.zeros(1001)
    evalyf = f(evalx)
    

    for j in range(1001):
        evalyp[j] = barycentricEval(x, y, N, evalx[j])
        
    plt.plot(evalx, evalyp, label = "Barry poly N = "+  str(N));
    plt.plot(evalx, evalyf, label = "function");
    plt.plot(x, y, 'o');
    plt.legend()
    plt.show()

    
    
def barycentricEval(x, y, n, xeval):
    if xeval in x :
        return y[np.where(x == xeval)[0]]
    
    xdif = xeval - x
    
    w = np.ones(n);
    phi = prod(xdif);
    
    yeval = 0;
    
    for j in range(n):
        for i in range(n):
            if(i!=j):
                w[j] *= 1 /(x[j]-x[i])
        if(xeval - x[j] != 0):   
            yeval += phi * (w[j]/(xeval - x[j])) * y[j]
        
    return yeval
        
                
                
            
    
    
    
driver()