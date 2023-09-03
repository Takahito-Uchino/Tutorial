import numpy as np
# データの準備
# 等間隔の数字
# 0から9までの数字（配列）を生成
x = np.arange(10)
print(x)

# reshape()は配列を形状に変換する。
x = np.arange(1, 10).reshape(3, 3)  # 3x3の多次元配列に変換
y = np.arange(1, 10)
y = np.reshape(y, (3, 3))  # 3x3の多次元配列に変換

print(x)
print(y)

print(x + y)
print(x - y)
print(x * y)
