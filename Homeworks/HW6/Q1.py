import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    # x0 = np.array([1, 1])
    # x0 = np.array([1, -1])
    x0 = np.array([0, 0])
    
    Nmax = 100
    tol = 1e-10
    
    [xstar,ier,its] =  Newton(x0,tol,Nmax)
    print(xstar)
    print('Newton: the error message reads:',ier) 
    print('Netwon: number of iterations is:',its)
     
    [xstar,ier,its] =  LazyNewton(x0,tol,Nmax)
    print(xstar)
    print('Lazy Newton: the error message reads:',ier)
    print('Lazy Newton: number of iterations is:',its)
     
    [xstar,ier,its] = Broyden(x0, tol,Nmax)     
    print(xstar)
    print('Broyden: the error message reads:',ier)
    print('Broyden: number of iterations is:',its)
     
def evalF(x): 

    F = np.zeros(2)
    
    F[0] = x[0]**2 + x[1]**2 - 4
    F[1] = np.exp(x[0])+x[1] - 1
    return F
    
def evalJ(x): 

    
    J = np.array([[2*x[0], 2*x[1]],
                  [np.exp(x[0]), 1]])
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
           
def LazyNewton(x0,tol,Nmax):

    J = evalJ(x0)
    Jinv = inv(J)
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]   
    
def Broyden(x0,tol,Nmax):
    
    A0 = evalJ(x0)

    v = evalF(x0)
    A = np.linalg.inv(A0)

    s = -A.dot(v)
    xk = x0+s
    for  its in range(Nmax):
       '''(save v from previous step)'''
       w = v
       ''' create new v'''
       v = evalF(xk)
       '''y_k = F(xk)-F(xk-1)'''
       y = v-w;                   
       '''-A_{k-1}^{-1}y_k'''
       z = -A.dot(y)
       ''' p = s_k^tA_{k-1}^{-1}y_k'''
       p = -np.dot(s,z)                 
       u = np.dot(s,A) 
       ''' A = A_k^{-1} via Morrison formula'''
       tmp = s+z
       tmp2 = np.outer(tmp,u)
       A = A+1./p*tmp2
       ''' -A_k^{-1}F(x_k)'''
       s = -A.dot(v)
       xk = xk+s
       if (norm(s)<tol):
          alpha = xk
          ier = 0
          return[alpha,ier,its]
    alpha = xk
    ier = 1
    return[alpha,ier,its]
     
        
driver() 
