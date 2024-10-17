import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 


def driver():
    
    f = lambda x: math.exp(x)
    a = 0
    b = 1
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval)
    
    ''' number of intervals'''
    Nint = 4
    
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for i in range(Neval):
      fex[i] = f(xeval[i])
    
    plt.figure()
    plt.plot(xeval,fex)
    plt.plot(xeval,yeval)
    plt.legend()
   
    
    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.show()
     
     
              

    
    
def  eval_lin_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)
   
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval) 
    
    for jint in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        '''let n denote the length of ind'''
        
        '''temporarily store your info for creating a line in the interval of 
         interest'''
         
        a1= xeval[findX(jint, Neval, Nint)]
        b1 = xeval[findX(jint + 1, Neval, Nint)]
        # fa1 = f(a1)
        # fb1 = f(b1)
        
        for a in range(findX(jint, Neval, Nint), findX(jint+1, Neval, Nint) + 1):
          
          yeval[a] = linearInterpolation(f, a1, b1, xeval[a])
          print(a)
        
          '''use your line evaluator to evaluate the lines at each of the points 
           in the interval'''
          '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with 
           the points (a1,fa1) and (b1,fb1)'''
           
    return yeval
           
def findX(jint, Neval, Nint):
    return min(int(jint * (Neval/Nint)), Neval-1) 


  
  
def linearInterpolation(f, x0, x1, a):
    return ((f(x1)-f(x0))/(x1-x0)) * (a -x0) + f(x0)

driver()