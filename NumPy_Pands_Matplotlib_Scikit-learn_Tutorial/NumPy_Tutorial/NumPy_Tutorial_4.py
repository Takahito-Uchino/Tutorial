import numpy as np
sample_array = np.arange(10)
print(sample_array)

# reshapeを使って配列の形状を指定
sample_array2 = sample_array.reshape(2, 5)
print(sample_array2)  # array(([0, 1, 2, 3, 4],[5, 6, 7, 8, 9]))

# concatenateを使って、データの結合する(axisで行方向か、縦方向かを指定可能)
sample_array3 = np.array([[1, 2, 3], [4, 5, 6]])
sample_array4 = np.array([[7, 8, 9], [10, 11, 12]])

# 行方向に結合 axis=1 で行方向
print(np.concatenate([sample_array3, sample_array4], axis=1))

# hstackでも行方向の結合が可能
print(np.hstack((sample_array3, sample_array4)))

# axis=0 なので列方向
print(np.concatenate([sample_array3, sample_array4], axis=0))

# vstackで列方向の結合が可能
print(np.vstack((sample_array3, sample_array4)))
