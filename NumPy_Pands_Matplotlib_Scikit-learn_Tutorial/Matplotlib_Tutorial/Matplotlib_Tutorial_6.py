import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
data = [54, 32, 18, 44, 29]
ex = [0.1, 0, 0, 0, 0]
"""
autopct='%1.1f%%'は小数点の表示桁数になる。1.1で１つ、１．２で２つ。
explodeオプションで１つ目の要素を10%ずらしている。これにより少し目立たせることができる。
counterclockオプションでFalseにするとリストの定義した順に表示される
Trueになると反時計回りに円グラフの要素が構成される。
"""
plt.pie(data, explode=ex, labels=labels, autopct='%1.1f%%', counterclock=False)
plt.show()

labels = ['Python', 'Ruby', 'Java', 'C++', 'PHP']
sizes = [40, 12, 24, 16, 9]
colors = ['navy', 'yellow', 'blue', 'gold', 'tomato']
plt.pie(sizes, labels=labels, colors=colors)
plt.axis('equal')  # 綺麗な円グラフが描けます
plt.show()
