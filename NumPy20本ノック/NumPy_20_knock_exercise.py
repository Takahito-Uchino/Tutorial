import numpy as np
import matplotlib.pyplot as plt

A = np.array([[-10, -8, -6], [-4, -2, 0], [2, 4, 6], [8, 10, 12]])
B = np.array([[-1, -2, -2, -2], [-2, -1, -2, -2], [-2, -2, -1, -2]])

print(A.shape, B.shape)
C = A @ B
print(C)

D = C[: 2, : 2]
print(D)
print(D.transpose())
print(np.linalg.inv(D))

x = np.random.randint(-100, 100, 300)
y = np.random.randint(-100, 100, 300)
plt.scatter(x, y)
plt.show()
