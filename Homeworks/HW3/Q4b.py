# import libraries
import numpy as np

    
def driver():

# Function 
     f = lambda x: - np.sin(2*x) + (5*x /4) - (3/4);
     Nmax1 = 100;
# Tolerance
     tol = 1e-10

#find actual roots

# find fixed point 1 
     x1 = -.9
     [xstar,ier] = fixedpt(f,x1,tol,Nmax1)
     print('the approximate fixed point 1 is:',xstar)
     print('f(xstar):',f(xstar))
     print('Error message reads:',ier)
    
# find fixed point 2 
     x2 = -.5
     [xstar,ier] = fixedpt(f,x2,tol,Nmax1)
     print('the approximate fixed point 2 is:',xstar)
     print('f(xstar):',f(xstar))
     print('Error message reads:',ier)
     
# find fixed point 3 
     x3 = 1.7
     [xstar,ier] = fixedpt(f,x3,tol,Nmax1)
     print('the approximate fixed point 3 is:',xstar)
     print('f(xstar):',f(xstar))
     print('Error message reads:',ier)
     
# find fixed point 4 
     x4 = 4
     [xstar,ier] = fixedpt(f,x4,tol,Nmax1)
     print('the approximate fixed point 4 is:',xstar)
     print('f(xstar):',f(xstar))
     print('Error message reads:',ier)
# find fixed point 5 
     x4 = 5
     [xstar,ier] = fixedpt(f,x4,tol,Nmax1)
     print('the approximate fixed point 5 is:',xstar)
     print('f(xstar):',f(xstar))
     print('Error message reads:',ier)


# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count < Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
    

driver()