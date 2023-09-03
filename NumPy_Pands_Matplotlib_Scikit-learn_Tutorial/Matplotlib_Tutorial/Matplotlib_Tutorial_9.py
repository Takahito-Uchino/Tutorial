import matplotlib.pyplot as plt

math = [82, 75, 50, 73, 65, 95, 78, 93, 71, 83]
english = [77, 92, 62, 77, 64, 45, 28, 60, 37, 86]

# 点数のタプル
points = (math, english)

fig, ax = plt.subplots()

bp = ax.boxplot(points)  # 複数指定するときはタプルを渡す
ax.set_xticklabels(['math', 'english'])

plt.title('exam')
plt.grid()
plt.show()
