import matplotlib.pyplot as plt

x1, y1 = range(0, 5), [10, 41, 44, 29, 85]
x2, y2 = range(0, 5), [59, 55, 77, 15, 47]

fig = plt.figure()

# １行２列の１番目
a1 = fig.add_subplot(1, 2, 1)  # 第３引数の1は左を意味する
a1.bar(x1, y1)
a1.set_title('A')

a2 = fig.add_subplot(1, 2, 2)  # 第３引数の２は右を意味する
a2.bar(x2, y2)
a2.set_title('B')

plt.show()
