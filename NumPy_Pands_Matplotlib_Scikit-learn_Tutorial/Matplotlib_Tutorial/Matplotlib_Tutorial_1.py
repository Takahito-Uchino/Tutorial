import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)  # -5から５まで0.1区切りで配列を作る
y = np.sin(x)  # 配列xの値に関してそれぞれsin(x)を求めてy軸の配列を生成

plt.plot(x, y)  # plot関数の第１引数xがx軸に対応し、第２引数yがy軸に対応している
plt.show()
