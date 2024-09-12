import matplotlib.pyplot as plt
import numpy as np

b = float(10)**np.arange(-16, 1, 1);
x = 10**6

f1 = (np.cos(x+b) - np.cos(x)) - (-b * np.sin(x))

x = np.pi
f2 = (np.cos(x+b) - np.cos(x)) - (-b * np.sin(x))


plt.semilogx(b, f1, label = "Original - Approximation (x = 10^6)")
# plt.semilogx(b, f2, label = "Original - Approximation (x = pi)")

plt.legend()

plt.show()


