import numpy as np

"""
数组运算
"""

# 数组乘法／减法，对应元素相乘／相减。
arr = np.array([[1.0, 2.0, 3.0], [4., 5., 6.]])
print(arr * arr)
print(arr - arr)
print()

# 标量操作作用在数组的每个元素上
arr = np.array([[1.0, 2.0, 3.0], [4., 5., 6.]])
print(1 / arr)
print(arr ** 0.5)  # 开根号

# 不同维度数组 广播
arr_1 = np.array([[1, 2, 3], [1, 2, 3]])
arr_2 = np.array([2, 3, 4])
print(arr_1 - arr_2)

# 打印结果
"""
[[ 1.  4.  9.]
 [16. 25. 36.]]
[[0. 0. 0.]
 [0. 0. 0.]]

[[1.         0.5        0.33333333]
 [0.25       0.2        0.16666667]]
[[1.         1.41421356 1.73205081]
 [2.         2.23606798 2.44948974]]
[[-1 -1 -1]
 [-1 -1 -1]]
请按任意键继续. . .
"""