import numpy as np
def driver():
    f = lambda x:  np.exp(3*x) - 9* np.exp(2*x)*x**2 + 27* np.exp(x)*x**4 - 27*x**6
    fp = lambda x: 3*np.exp(3*x) - 18*np.exp(2*x)*x - 18*np.exp(2*x)*x**2 + 108*np.exp(x)*x**3 + 27*np.exp(x)*x**4 - 162*x**5
    fpp = lambda x: -18*np.exp(2*x) + 9*np.exp(3*x) - 72*np.exp(2*x)*x + 324*np.exp(x)*x**2 - 36*np.exp(2*x)*x**2 + 216*np.exp(x)*x**3 - 810*x**4 + 27*np.exp(x)*x**4
    
    m = 2;
    p0 = 3.7
    Nmax = 100
    tol = 1.e-4
    
    print("Newton")
    (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % info)
    print('Number of iterations:', '%d' % it)
    
    print("newtonModifiedClass")
    (p,pstar,info,it) = newtonModifiedClass(f,fp, fpp,p0,tol, Nmax)
    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % info)
    print('Number of iterations:', '%d' % it)
    
    print("newtonModifiedP2")
    (p,pstar,info,it) = newtonModifiedP2(f,fp,p0,tol, Nmax, m)
    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % info)
    print('Number of iterations:', '%d' % it)

 
 
 def newtonModifiedClass(f, fp, fpp,p0,tol,Nmax):
    p = np.zeros(Nmax+1);
    p[0] = p0
    for it in range(Nmax):
        p1 = p0 - ((f(p0)/fp(p0)) / ((f(p0)*fpp(p0))/(fp(p0)**2)))
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [p,pstar,info,it]
        p[it+1] = p1
        p0 = p1
    pstar = p1
    info = 1
    return [p,pstar,info,it]
    
def newtonModifiedP2(f,fp,p0,tol,Nmax, m):
    p = np.zeros(Nmax+1);
    p[0] = p0
    for it in range(Nmax):
        p1 = p0- m*(f(p0) /fp(p0))
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [p,pstar,info,it]
        p[it+1] = p1
        p0 = p1
    pstar = p1
    info = 1
    return [p,pstar,info,it]

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



driver()