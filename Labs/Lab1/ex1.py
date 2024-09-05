import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.920, 2.08, 0.001);

p1 = x**9 -18*x**8 + 144*x**7 -672*x**6 + 2016*x**5 -4032*x**4 + 5376*x**3 -4608*x**2 + 2304*x - 512
p2 = (x-2)**9

plt.plot(x, p1, label = "p1(x)")
plt.plot(x, p2, label = "p2(x)")

plt.legend()

plt.show()


