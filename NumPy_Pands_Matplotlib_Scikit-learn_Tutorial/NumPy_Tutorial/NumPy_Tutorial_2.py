import numpy as np

a = np.array([1, 2, 3, 4])
a.shape  # (4, )が出力される。一次元かつ、４要素であることを意味する。
print(a.shape)

b = np.array([[1, 2], [3, 4]])
b.shape  # (2, 2)これは行列で、２行２列を意味する。
print(b.shape)
