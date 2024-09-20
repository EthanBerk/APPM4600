# import libraries
import numpy as np
    
def driver():

# test functions 
     Nmax1 = 50;
     f1 = lambda x: (10/(x+4))**(1/2);

     tol = 1e-10
     x0 = 1.5

# test f1 '''
     [xstar,ier, count, x] = fixedpt(f1,x0,tol,Nmax1)
     [alpha, _lambda] = computeOrder(x[x != 0], xstar)
     print('the approximate fixed point is:',xstar)
     print('Iterations :', count)
     # print('fixed points :', x[x != 0])
     print('order of convergence :', alpha)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    


def computeOrder(x, xstar):
     diff1 = np.abs(x[1::]-xstar)
     diff2 = np.abs(x[0:-1]-xstar)
     fit = np.polyfit(np.log(diff2.flatten()), np.log(diff1.flatten()), 1)
     
     _lambda = np.exp(fit[1])
     alpha = fit[0]
     return [alpha, _lambda]

# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    x = np.zeros((Nmax,1))
    


    count = 0
    while (count < Nmax):
       x[count] = x0
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, count, x]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, count, x]
    

driver()