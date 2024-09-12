import matplotlib.pyplot as plt
import numpy as np
import math

t = np.arange(0, np.pi, np.pi/30);
y = np.cos(t);

S = 0;
for tVal, yVal in zip(t, y):
    S += tVal*yVal

print("The sum is: ", S)

