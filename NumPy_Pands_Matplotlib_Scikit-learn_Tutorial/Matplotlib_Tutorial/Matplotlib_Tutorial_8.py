import numpy as np
import matplotlib.pyplot as plt

math = [162, 168, 172, 181, 176, 168, 173, 175, 162, 169]
x = np.array(math)
plt.title('height')
plt.grid()  # 横線ラインを入れる
plt.boxplot(x)
plt.show()

# 下記コードでも同様に描画可能
fig, ax = plt.subplots()
bp = ax.boxplot(math)
plt.title('height')
plt.grid()
plt.show()
