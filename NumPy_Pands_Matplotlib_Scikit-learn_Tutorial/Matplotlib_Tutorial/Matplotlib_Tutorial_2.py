import matplotlib.pyplot as plt

data = [2, 4, 6, 3, 5, 8, 4, 5]
plt.plot(data)
plt.show()

# r--は赤の点線 b--は青の点線 g--は緑の点線
plt.plot([1, 2, 3, 4], [1, 5, 10, 15], 'r--')
plt.show()
