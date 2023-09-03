import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

"""
x = np.arange(10)
y = np.random.randint(-10, 10, 10)
plt.plot(x, y)
plt.show()
"""
"""
x1 = np.random.randint(10, 20, 20)
x2 = np.random.randint(20, 30, 20)
y1 = np.random.randint(50, 100, 20)
y2 = np.random.randint(0, 40, 20)
plt.scatter(x1, y1)
plt.scatter(x2, y2)
plt.show()
"""
"""
data = np.random.randint(0, 10, 10)
plt.hist(data, bins=15)
plt.show()
"""
"""
x = ['Sam', 'John', 'Kevin', 'Adam']
y = np.random.randint(0, 200, 4)
plt.bar(x, y)
plt.show()
"""
"""
x = np.arange(10)
y = np.random.randint(-10, 10, 10)
plt.plot(x, y)
plt.title('Result')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
"""
"""
x1 = np.random.randint(10, 20, 20)
x2 = np.random.randint(20, 30, 20)
y1 = np.random.randint(50, 100, 20)
y2 = np.random.randint(0, 40, 20)
plt.scatter(x1, y1)
plt.scatter(x2, y2)
plt.xlim([0, 40])
plt.ylim([0, 120])
plt.show()
"""
"""
x = np.linspace(0, 10, 500)
y = np.exp(x)
plt.plot(x, y)
plt.yscale('log')
plt.show()
"""
"""
x = np.linspace(0, 2*np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')
plt.legend(loc=2)
plt.ylim(-2, 2)
plt.show()
"""
"""
x1 = np.random.randint(10, 35, 20)
x2 = np.random.randint(5, 45, 20)
x3 = np.random.randint(0, 40, 20)
y1 = np.random.randint(50, 100, 20)
y2 = np.random.randint(0, 40, 20)
y3 = np.random.randint(20, 80, 20)
plt.scatter(x1, y1, marker='*', s=80)
plt.scatter(x2, y2, marker='^', s=60)
plt.scatter(x3, y3, marker='x', s=30)
plt.show()
"""
"""
data = [5, 3, 4, 2, 0, 3, 2, 1, 4, 6, 8, 5]
plt.plot(data)
plt.annotate('min value', xy = (4, 0),xytext = (9, 1), arrowprops = dict(facecolor = 'black', shrink = 0.05))
plt.xticks(np.arange(0, 12, 1))
plt.yticks(np.arange(0, 9, 2))
plt.show()
"""
"""
data = [5, 3, 4, 2, 0, 3, 2, 1, 4, 6, 8, 5]
plt.plot(data)
plt.grid()
plt.show()
"""
"""
names = ['Sam', 'John', 'Kevin', 'Adam']
values = [60, 170, 10, 120]
#plt.rcParams['figure.figsize'] = (9, 3)
plt.figure(figsize = (9, 3))
plt.subplot(1, 3, 1)
plt.bar(names, values)
plt.subplot(1, 3, 2)
plt.scatter(names, values)
plt.subplot(1, 3, 3)
plt.plot(names, values)
plt.show()
"""
"""
data = np.random.rand(10, 10)
plt.imshow(data, cmap = 'Blues')
plt.colorbar()
plt.show()
"""
"""
theta = np.linspace(-4*np.pi, 4*np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
#plt.subplot(projection = '3d')
#plt.scatter(x, y, z)
#plt.show()
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.plot(x, y, z, label = '3D Curve')
ax.legend()
plt.show()
"""
"""
x = np.array([100, 200, 300, 400, 500])
labels = ['Apple', 'Banana', 'Orange', 'Grape', 'Strawberry']
colors = ['red', 'yellow', 'orange', 'purple', 'pink']
plt.pie(x, labels = labels, colors = colors, counterclock = False, startangle = 90)
plt.show()
"""
"""
fig = plt.figure(figsize = (8, 6))
ax = fig.add_subplot(111, facecolor = '#FFFFCC')

x, y = 4 * (np.random.rand(2, 100) - .5)
ax.plot(x, y, 'o')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
cursor = Cursor(ax, useblit = True, color = 'red', linewidth = 2)
plt.show()
"""
"""
x = np.arange(10)
y = np.random.randint(-10, 10, 10)
plt.figure(figsize = (9, 6))
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title('Result')
plt.xlabel('x axis')
plt.ylabel('y axis')

x = ['Sam', 'John', 'Kevin', 'Adam']
y = np.random.randint(0, 200, 4)
plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.show()
"""
"""
x = np.arange(10)
y = np.random.randint(-10, 10, 10)
fig = plt.figure(figsize = (9, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x, y)
ax1.title('Result')
ax1.xlabel('x axis')
ax1.ylabel('y axis')

x = ['Sam', 'John', 'Kevin', 'Adam']
y = np.random.randint(0, 200, 4)
ax2 = fig.add_subplot(1, 2, 2)
ax2.bar(x, y)
plt.show()
"""
"""
labels = ['Chips', 'Hotdogs', 'Cookies', 'Chocolates']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels = labels, counterclock = True, shadow = True, startangle = 90, explode = [0, 0.1, 0, 0], autopct ='%1.1f%%')
plt.axis('equal')
plt.show()
"""

mu1, sigma1 = 100, 15
mu2, sigma2 = 90, 20
mu3, sigma3 = 110, 10
x1 = mu1 + sigma1 * np.random.randn(10000)
x2 = mu2 + sigma2 * np.random.randn(10000)
x3 = mu3 + sigma3 * np.random.randn(10000)
plt.hist([x1, x2, x3], bins = 10, density = True, color = ['yellow', 'skyblue', 'blue'], label = ['x1', 'x2', 'x3'], stacked = True)
plt.title('histgram')
plt.xlabel('x')
plt.ylabel('frequency')
plt.grid(True)
plt.legend(loc = 'upper left')
plt.show()