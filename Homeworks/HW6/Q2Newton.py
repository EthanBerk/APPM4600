import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    # x0 = np.array([1, 1])
    # x0 = np.array([1, -1])
    x0 = np.array([0, 0, 0])
    
    Nmax = 100
    tol = 1e-6
    
    [xstar,ier,its] =  Newton(x0,tol,Nmax)
    print(xstar)
    print('Newton: the error message reads:',ier) 
    print('Netwon: number of iterations is:',its)
     
def evalF(x): 

    F = np.zeros(3)
    
    F[0] = x[0] + np.cos(x[0] * x[1] * x[2]) -1
    F[1] = (1- x[0])**(1/4) + x[1] + 0.05*x[2]**2 - 0.15 *x[2] -1
    F[2] = -x[0]**(2) - 0.1 *x[1] **2 + 0.01*x[1] + x[2] -1
    
    return F
    
def evalJ(x): 
    
    J = np.array([[1 - (x[1] * x[2] * np.sin(x[0] * x[1] * x[2])),-x[0] * x[2] * np.sin(x[0] * x[1] * x[2]), -x[0] * x[1] * np.sin(x[0] * x[1] * x[2])],
                  [-(1/4) * (1 - x[0])**(-3/4), 1, 0.1 * x[2] - 0.15],
                  [-2*x[0], -0.2 * x[1] + 0.01 , 1]])
    return J


def Newton(x0,tol,Nmax):

    for its in range(Nmax):
       J = evalJ(x0)
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]
        
driver() 
