import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(0, 5, 5000)

F = np.sin(x)
T = x - (1/6) * x**3 + (1/120) * x**5
P33 = (x-(7/60)*x**3)/(1+ (1/20)*x**2)
P24= (x)/(1 + (1/6)*x**2 + (7/360)*x**4)

plt.title("Evaluation")
plt.plot(x, F, label = "Sin(x)")
plt.plot(x, T, label = "Taylor:6")
plt.plot(x, P33, label = "Pade:3/3")
plt.plot(x, P24, label = "Pade:2/4")
plt.legend()
plt.show()

#error 
plt.title("Error")
plt.plot(x, np.abs(T - F), label = "Taylor:6")
plt.plot(x, np.abs(P33 - F), label = "Pade:3/3")
plt.plot(x, np.abs(P24- F), label = "Pade:2/4")
plt.legend()
plt.show()