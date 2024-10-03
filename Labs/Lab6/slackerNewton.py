import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    x0 = np.array([1, 0])
    
    Nmax = 100
    tol = 1e-10
    
    [xstar,ier,its, d] =  SlackerNewton(x0,tol,Nmax, 0.128)
    print(xstar)
    print('Slacker Newton: the error message reads:',ier) 
    print('Slacker Netwon: number of iterations is:',its)
    print('Slacker Netwon: itterartion diffs is:', d[:8])
     
    [xstar,ier,its] =  LazyNewton(x0,tol,Nmax)
    print(xstar)
    print('Lazy Newton: the error message reads:',ier)
    print('Netwon: number of iterations is:',its)
     
  
     
def evalF(x): 

    F = np.zeros(2)
    
    F[0] = 4*x[0]**2 + x[1]**2 - 4
    F[1] = x[0] + x[1] - np.sin(x[0] - x[1])
    return F
    
def evalJ(x): 
    J = np.array([[8*x[0], x[1]**2],
                  [1-np.cos(x[0] - x[1]), 1+np.cos(x[0] - x[1])]])
    return J



def LazyNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

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

def SlackerNewton(x0,tol,Nmax, jTol):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = inv(J)
    d = np.zeros(Nmax)
    
    for its in range(Nmax):
       d[its] = norm(J - evalJ(x0))

       if(d[its] > jTol):
           J = evalJ(x0)
           Jinv = inv(J)
           
           
           
       
       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its, d]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its, d]   

    

        
driver()       