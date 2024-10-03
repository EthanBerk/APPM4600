import numpy as np
import math
import time
from numpy.linalg import norm 

def main():
    f = lambda x: x[0]**2 + (4*x[1]**2) + (4*x[2]**2) - 16
    
    fx = lambda x: 2 * x[0]
    fy = lambda x: 8 * x[1]
    fz = lambda x: 8 * x[2]
    
    d = lambda x: f(x)/(fx(x)**2 +fy(x)**2 + fz(x)**2)
    
    Nmax = 100
    tol = 1e-10
    x0 = np.array([1,1,1])
    
    [xcurve,ier,its, p] =  iteration(x0, d, fx, fy, fz, tol, Nmax)
    print("xcurve:", xcurve)
    print("evaluate:", f(xcurve))
    print('the error message reads:',ier) 
    print('number of iterations is:',its)
    
    
def iteration(x0, d, fx, fy, fz, tol, Nmax):
    
    p = np.zeros(Nmax+1);

    for its in range(Nmax):
       x1 = x0 - d(x0) * np.array([fx(x0), fy(x0), fz(x0)])
       
       if (norm(x1-x0) < tol):
           xcurve = x1
           ier = 0
           return[xcurve, ier,its, p]
           
       x0 = x1
    
    xcurve = x1
    ier = 1
    return[xcurve,ier,its, []]   
main()