import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def main():
    x0 = np.array([1, 1])
    
    K = np.array([[1/6,1/18],
                   [0  , 1/6]])
 
    
    Nmax = 100
    tol = 1e-10
    
    [xstar,ier,its] =  iteration(x0, K,tol,Nmax)
    print("xstar:", xstar)
    print("evaluate:", evalF(xstar))
    print('the error message reads:',ier) 
    print('number of iterations is:',its)


def evalF(x): 

    F = np.zeros(2)
    # print(x)
    
    F[0] = 3 *x[0]**2 - x[1]**2
    F[1] = 3 * x[0]*x[1]**2-x[0]**3 -1
    return F

def iteration(x0, K, tol,Nmax):
    
    for its in range(Nmax):
       F = evalF(x0)
       x1 = x0 - K.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]   

main()


    