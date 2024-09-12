import matplotlib.pyplot as plt
import numpy as np

A = (1/2) *np.array([
    [1/2, 1/2],
    [1+10^-10, 1-10^-10]
])
Ai = np.array([
    [1-10^10, 10^10],
    [1+10^10, -10^10]
])

print("||A||_2 = ", np.linalg.svdvals(A)[0])
print("||A^{-1}||_2 = ", np.linalg.svdvals(Ai)[0])
print("||A||_2 * ||A^{-1}||_2 ", np.linalg.svdvals(A)[0] * np.linalg.svdvals(Ai)[0])