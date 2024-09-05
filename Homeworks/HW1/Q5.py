import matplotlib.pyplot as plt
import numpy as np

b = float(10)**np.arange(-16, 1, 1);
x = 10**6

f1 = (np.cos(x+b) - np.cos(x)) - (-2* np.sin(( 2*x +b)/2) * np.sin(b/2))

x = np.pi
f2 = (np.cos(x+b) - np.cos(x)) - (-2* np.sin(( 2*x +b)/2) * np.sin(b/2))


plt.semilogx(b, f1, label = "Original - Modified (x = 10^6)")
plt.semilogx(b, f2, label = "Original - Modified (x = pi)")

plt.legend()

plt.show()


