import numpy as np
import matplotlib.pyplot as plt

# 平均10、標準偏差１０の正規乱数を１００件生成
x = np.random.normal(10, 10, 1000)
plt.hist(x)
plt.show()

# 引数にbins=数字でヒストグラムの棒の数を指定できる
# orientation='horizontalで横棒に
plt.hist(x, bins=16, orientation='horizontal')
plt.show()
