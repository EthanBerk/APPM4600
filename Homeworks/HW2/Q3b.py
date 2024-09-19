import math

def f(x):
    y = math.e**x
    return y - 1

print(f(9.999999995000000 * 10.0**-10.0))