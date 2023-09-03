import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(x)
# array()は、Pythonのリストを渡すことでNumPy用の配列(numpy.ndarray)を生成する。

x = np.array([1, 2, 3])
print(x)  # [1 2 3]
print(type(x))  # <class 'numpy.ndarray'>

my_list1 = [1, 2, 3, 4, 5]
my_array1 = np.array(my_list1)  # NumPyのarrayを作る。
print(my_array1)

my_list2 = [10, 20, 30, 40, 50]
my_lists = [my_list1, my_list2]  # リストのリストを作る。
print(my_lists)

# my_listsを使ってNumPyのアレイを作る。（多次元配列を作る。）
my_array2 = np.array(my_lists)
print(my_array2)

# タプルを複数渡すとエラーになってしまう。
np.array((1, 2, 3), (4, 5, 6))
