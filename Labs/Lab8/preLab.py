import numpy as np


def linearInterpolation(f, x0, x1, a):
    return ((f(x1)-f(x0))/(x1-x0)) * (a -x0) + f(x0)

f  = lambda x: x

print(linearInterpolation(f, 0,1, 3))