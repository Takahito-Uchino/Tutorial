import matplotlib.pyplot as plt
import numpy as np

a = range(0, 7)
b = [55, 21, 61, 98, 85, 52, 99]
plt.bar(a, b)
# plt.barh(a, b) 横棒グラフ
plt.show()

# 棒グラフ
m = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
y_pos = np.arange(len(m))
sales = [10, 18, 32, 54, 65, 96, 120, 140, 145, 162, 188, 202]

plt.bar(y_pos, sales, alpha=0.5)
plt.ylabel('Usage')
plt.title('Sales Trends')
plt.show()

a = range(0, 7)
b = [55, 21, 61, 98, 85, 52, 99]
plt.barh(a, b)
plt.show()
