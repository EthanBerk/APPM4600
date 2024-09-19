import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2,6,100)
y = x - 4 * np.sin(2*x) -3


plt.axhline(linewidth= 1, ls = "--", color="r")

plt.plot(x,y)
plt.show()