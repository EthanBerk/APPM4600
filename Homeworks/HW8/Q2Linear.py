import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm



def driver():
    
    f = lambda x: 1./(1.+x**2)

    N = 21
    ''' interval'''
    a = -5
    b = 5
   
    ''' create equispaced interpolation nodes'''
    N -= 1
    xint = np.zeros(N+1)
    for i in range(N-1):
        xint[i+1] = -((a+b)/2 + (b-a)/2 * np.cos(((2*(i)+1) * np.pi)/(2*(N-1))))
    xint[0] = a;
    xint[N] = b;
    
        
    ''' create interpolation data'''
    yint = np.zeros(N+1)
    for jj in range(N+1):
        yint[jj] = f(xint[jj])
    
      
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yevalL = np.zeros(Neval+1)
    for kk in range(Neval+1):
      yevalL[kk] = eval_lin_spline(xeval[kk],xint,yint,N+1)

    ''' create vector with exact values'''
    fex = np.zeros(Neval+1)
    for kk in range(Neval+1):
        fex[kk] = f(xeval[kk])
    
    
    plt.figure()
    plt.plot(xeval,fex)
    plt.plot(xeval,yevalL,label='Linear') 
    plt.plot(xint, yint, 'o');
    plt.legend()

    plt.show()
         
    errL = abs(yevalL-fex)
    plt.figure()
    plt.semilogy(xeval,errL,'bs--',label='Linear')
    plt.show()  
    nerr = norm(fex-yevalL)
    print('nerr = ', nerr)  
     
     
              

    
    
def  eval_lin_spline(xeval, xint,yint,N):
    for jint in range(N):
        if(xint[jint] <= xeval and xeval <= xint[jint+1]):
            x0 = xint[jint]
            x1 = xint[jint+1]
            y0 = yint[jint]
            y1 = yint[jint+1]
            print(x0)
            
            break
        
    return linearInterpolation(xeval, x0, x1, y0, y1)
        
def linearInterpolation(x, x0, x1, y0, y1):
    return ((y1-y0)/(x1-x0)) * (x - x0) + y0

driver()