import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

x = np.linspace(0,1,100)
y = sp.special.erf(x / (2 * np.sqrt(0.138e-6 * 5.184e6)))*(35) - 15 


plt.axhline(linewidth= 1, ls = "--", color="r")

plt.plot(x,y, label="f(x)")
plt.legend()
plt.show()