import numpy as np



def computeOrder(x, xstar):
     diff1 = np.abs(x[1::]-xstar)
     diff2 = np.abs(x[0:-1]-xstar)
     fit = np.polyfit(np.log(diff2.flatten()), np.log(diff1.flatten()), 1)
     
     _lambda = np.exp(fit[1])
     alpha = fit[0]
     return alpha
 
 
h = 0.01 * 2. **(-np.arange(0, 10))
s = np.pi/2
fd = (np.cos(s+h) - np.cos(s))/h
cd = (np.cos(s+h) - np.cos(s-h))/(2*h)
t = -1 #true value

print("fd:",np.abs(fd - t))
print("cd:",np.abs(cd - t))
print("fd order:",computeOrder(fd, t))
print("cd order:",computeOrder(cd, t))