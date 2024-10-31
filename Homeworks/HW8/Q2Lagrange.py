import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import math
from numpy.linalg import norm


def driver():


    f = lambda x: 1./(1.+x**2)

    N = 21
    ''' interval'''
    a = -5
    b = 5
   
    N -= 1
    ''' create equispaced interpolation nodes'''
    xint = np.zeros(N+1)
    for i in range(N+1):
        xint[i] = (a+b)/2 + (b-a)/2 * np.cos(((2*i+1) * np.pi)/(2*(N+1)))
        
    ''' create interpolation data'''
    yint = np.zeros(N+1)
    for jj in range(N+1):
        yint[jj] = f(xint[jj])
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yevalL = np.zeros(Neval+1)
    for kk in range(Neval+1):
      yevalL[kk] = eval_lagrange(xeval[kk],xint,yint,N)

    ''' create vector with exact values'''
    fex = np.zeros(Neval+1)
    for kk in range(Neval+1):
        fex[kk] = f(xeval[kk])
    
    
    plt.figure()
    plt.plot(xeval,fex)
    plt.plot(xeval,yevalL,label='Lagrange') 
    plt.plot(xint, yint, 'o');
    plt.legend()

    plt.show()
         
    errL = abs(yevalL-fex)
    plt.figure()
    plt.semilogy(xeval,errL,'bs--',label='Lagrange')
    plt.show()  
    nerr = norm(fex-yevalL)
    print('nerr = ', nerr)            



def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  
    

       
driver()