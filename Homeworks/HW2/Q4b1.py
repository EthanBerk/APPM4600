import matplotlib.pyplot as plt
import numpy as np

R = 1.2
dr = 0.1
f = 15
p = 0


theta = np.linspace(0, 2 * np.pi, 400)

x = R * (1 + dr * np.sin(f * theta + p)) * np.cos(theta)
y = R * (1 + dr * np.sin(f * theta + p)) * np.sin(theta)

ax = plt.gca()
ax.set_aspect('equal')

plt.plot(x, y)
plt.show()
