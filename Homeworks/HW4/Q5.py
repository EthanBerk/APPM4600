import numpy as np
import matplotlib.pyplot as plt

def driver():
    f = lambda x:  x**6 - x  -1
    fp = lambda x:  6*x**5 - 1
    
    p0 = 2
    p1 = 1
    Nmax = 100
    tol = 1.e-13
    ax = plt.gca()
    ax.set_aspect('equal')
    
    print("newton")
    (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % info)
    print('Number of iterations:', '%d' % it)
    print('The iterates are', p[p != 0]- pstar)
    p = p[p!= 0]
    diff1 = np.abs(p[1::]-pstar)
    diff2 = np.abs(p[0:-1]-pstar)
    plt.plot(np.log(diff2), np.log(diff1), '.', label = "newton")
    
    print("secant")
    (p,pstar,info,it) = secant(f, p0, p1,tol, Nmax)
    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % info)
    print('Number of iterations:', '%d' % it)
    print('The iterates are', p[p != 0]-pstar)
    p = p[p!= 0]
    diff1 = np.abs(p[1::]-pstar)
    diff2 = np.abs(p[0:-1]-pstar)
    plt.plot(np.log(diff2), np.log(diff1), '.',  label = "secant")
    
    
    plt.legend()
    plt.show()
    



def newton(f,fp,p0,tol,Nmax):
    p = np.zeros(Nmax+1);
    p[0] = p0
    for it in range(Nmax):
        p1 = p0-f(p0)/fp(p0)
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [p,pstar,info,it]
        p[it+1] = p1
        p0 = p1
    pstar = p1
    info = 1
    return [p,pstar,info,it]


def secant(f, p0, p1,tol,Nmax):
    
    p = np.zeros(Nmax+1);
    if(f(p0) - f(p1) == 0):
        info = 1 
        pstar = p1  
        return [p,pstar,info,0]

    p[0] = p0
    for it in range(Nmax):
        p2 = p1 - (f(p1) * ((p1-p0) / (f(p1) - f(p0))))
        if (abs(p2-p1) < tol):
            pstar = p2
            info = 0
            return [p,pstar,info,it]
        p[it+1] = p1
        p0 = p1
        p1 = p2
    pstar = p2
    info = 1
    return [p,pstar,info,it]

driver()