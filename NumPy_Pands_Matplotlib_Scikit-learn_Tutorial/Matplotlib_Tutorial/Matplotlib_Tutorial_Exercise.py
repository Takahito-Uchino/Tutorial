import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y1 = np.sin(x)
plt.plot(x, y1)

y2 = np.cos(x)
plt.plot(x, y2)
plt.show()
