import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def eval_legendre(x, n):
    p = np.zeros(n + 1)
    p[0] = 1
    p[1] = x
    for i in range(2, n + 1):
        p[i] = (1/i)*((2*n +1) * x * p[i-1] - n * p[n-2])
    return p;

print(eval_legendre(2, 5))
    
