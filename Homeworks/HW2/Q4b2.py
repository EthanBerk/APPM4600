import matplotlib.pyplot as plt
import numpy as np

dr = 0.05
f = 15
p = np.random.uniform(0, 2)


ax = plt.gca()
ax.set_aspect('equal')

theta = np.linspace(0, 2 * np.pi, 400)


for i in range(10):
    R = i
    f = 2 + i
    
    y = R * (1 + dr * np.sin(f * theta + p)) * np.sin(theta)
    x = R * (1 + dr * np.sin(f * theta + p)) * np.cos(theta)
    plt.plot(x, y)




plt.show()
