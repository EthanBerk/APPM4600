# import libraries
import numpy as np
    
def driver():

# test functions 
     Nmax1 = 20;
     f1 = lambda x: x- ((x**5-7)/(5 * x**4));

     tol = 1e-10
     x0 = 1

# test f1 '''
     [xstar,ier, count, x] = fixedpt(f1,x0,tol,Nmax1)
     print('the approximate fixed point is:',xstar)
     print('Iterations :', count)
     print('fixed points :', x[x != 0])
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    




# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    x = np.zeros((Nmax,1))
    x[0] = x0


    count = 0
    while (count < Nmax):
       count = count +1
       x1 = f(x0)
       x[count] = x1
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, count, x]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, count, x]
    

driver()