import numpy as np
import numpy.random as np_random

"""
索引与切片
"""

# 通过索引访问二维数组某一行或某个元素
print('通过索引访问二维数组某一行或某个元素')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[2])
print(arr[0][2])
print(arr[0, 2]) # 普通Python数组不能用。

# 取arr四个角位置元素，输出一维数组
rows = np.array([0, 0, 2, 2]) 
cols = np.array([0, 2, 0, 2])
print(arr[rows, cols])
# 取arr四个角位置元素，输出二维数组
rows = np.array([[0,0],[2,2]]) 
cols = np.array([[0,2],[0,2]])
print(arr[rows, cols]) # 
print()

# 对更高维数组的访问和操作
print('对更高维数组的访问和操作')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # 3维
print(arr) # 3维数组
print(arr[0])  # 结果是个2维数组
print(arr[1, 0]) # 结果是个1维数组
print(arr[[0, 0, 1], [1, 0, 0]]) # 打印arr[0,1]、arr[0,0]、arr[1,0]
print(arr[[0, 0, 1], [1, 0, 0], [0, 1, 1]]) # 输出arr[0,1,0]、arr[0,0,1]、arr[1,0,1]位置元素
old_values = arr[0].copy()  # 复制arr[0]的值
arr[0] = 42 # 把arr[0]所有的元素都设置为同一个值
print(arr)
arr[0] = old_values # 把原来的数组写回去
print(arr)
print()

print('使用布尔数组作为索引')
name_arr = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
rnd_arr = np_random.randn(7, 4) # 随机7*4数组
print(rnd_arr)
print(name_arr == 'Bob') # 返回布尔数组，元素等于'Bob'为True，否则False。
print(rnd_arr[name_arr == 'Bob'])  # 利用布尔数组选择行
print(rnd_arr[name_arr == 'Bob', :2])  # 增加限制打印列的范围
print(rnd_arr[~(name_arr == 'Bob')]) # 对布尔数组的内容取反
mask_arr = (name_arr == 'Bob') | (name_arr == 'Will') # 逻辑运算混合结果
print(rnd_arr[mask_arr])
rnd_arr[name_arr != 'Joe'] = 7  # 先布尔数组选择行，然后把每行的元素设置为7。
print(rnd_arr)

print('使用切片访问和操作数组')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s = slice(1, 6, 1) # 参数分别为起始、结束、步长
print(arr[s])
print(arr[1:6:1]) # 打印元素arr[1]到arr[5]，与slice方法效果相同
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[:2]) # 打印第1、2行
print(arr[:2, 1:]) # 打印第1、2行，第2、3列.同arr[:2, [1,2]]
print(arr[:, :1])  # 打印第一列的所有元素
arr[:2, 1:] = 0 # 第1、2行，第2、3列的元素设置为0
print(arr)

print('使用布尔数组作为索引')
name_arr = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
rnd_arr = np_random.randn(7, 4) # 随机7*4数组
print(rnd_arr)
print(name_arr == 'Bob') # 返回布尔数组，元素等于'Bob'为True，否则False。
print(rnd_arr[name_arr == 'Bob'])  # 利用布尔数组选择行
print(rnd_arr[name_arr == 'Bob', :2])  # 增加限制打印列的范围
print(rnd_arr[~(name_arr == 'Bob')]) # 对布尔数组的内容取反
mask_arr = (name_arr == 'Bob') | (name_arr == 'Will') # 逻辑运算混合结果
print(rnd_arr[mask_arr])
arr = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print(arr > 5)
print(arr[arr >  5])

# 打印结果
"""
通过索引访问二维数组某一行或某个元素
[7 8 9]
3
3
[1 3 7 9]
[[1 3]
 [7 9]]

对更高维数组的访问和操作
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
[[1 2 3]
 [4 5 6]]
[7 8 9]
[[4 5 6]
 [1 2 3]
 [7 8 9]]
[4 2 8]
[[[42 42 42]
  [42 42 42]]

 [[ 7  8  9]
  [10 11 12]]]
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]

使用布尔数组作为索引
[[ 0.20801525  0.65769691  0.89611338 -0.47413773]
 [-0.68038952  0.8700822   1.34140597 -0.39905413]
 [-0.3283722   0.04633543  0.19166468  1.35796122]
 [-0.47608994  0.27653884  0.817753    2.36501838]
 [-0.02186801 -0.46063505 -0.45436928  0.56087996]
 [-0.36182397  0.54252233 -1.29304264  1.26791408]
 [ 0.86871186 -0.14727845 -0.92266399  0.81630381]]
[ True False False  True False False False]
[[ 0.20801525  0.65769691  0.89611338 -0.47413773]
 [-0.47608994  0.27653884  0.817753    2.36501838]]
[[ 0.20801525  0.65769691]
 [-0.47608994  0.27653884]]
[[-0.68038952  0.8700822   1.34140597 -0.39905413]
 [-0.3283722   0.04633543  0.19166468  1.35796122]
 [-0.02186801 -0.46063505 -0.45436928  0.56087996]
 [-0.36182397  0.54252233 -1.29304264  1.26791408]
 [ 0.86871186 -0.14727845 -0.92266399  0.81630381]]
[[ 0.20801525  0.65769691  0.89611338 -0.47413773]
 [-0.3283722   0.04633543  0.19166468  1.35796122]
 [-0.47608994  0.27653884  0.817753    2.36501838]
 [-0.02186801 -0.46063505 -0.45436928  0.56087996]]
[[ 7.          7.          7.          7.        ]
 [-0.68038952  0.8700822   1.34140597 -0.39905413]
 [ 7.          7.          7.          7.        ]
 [ 7.          7.          7.          7.        ]
 [ 7.          7.          7.          7.        ]
 [-0.36182397  0.54252233 -1.29304264  1.26791408]
 [ 0.86871186 -0.14727845 -0.92266399  0.81630381]]
使用切片访问和操作数组
[2 3 4 5 6]
[2 3 4 5 6]
[[1 2 3]
 [4 5 6]]
[[2 3]
 [5 6]]
[[1]
 [4]
 [7]]
[[1 0 0]
 [4 0 0]
 [7 8 9]]
使用布尔数组作为索引
[[-0.41652817 -1.9083364  -0.42638188 -0.52257586]
 [ 0.70882161 -1.45983665  0.48044276 -1.28032139]
 [ 0.04655583  0.28168593  0.46636532 -0.87500408]
 [-0.23686776  0.0671876  -0.62824434  0.53654728]
 [ 2.2841548   0.71917568  0.77087353  0.04137966]
 [ 0.44497083 -1.43376175  1.80849996 -0.86061081]
 [-0.35023255 -0.09871832  0.1764426   0.14621878]]
[ True False False  True False False False]
[[-0.41652817 -1.9083364  -0.42638188 -0.52257586]
 [-0.23686776  0.0671876  -0.62824434  0.53654728]]
[[-0.41652817 -1.9083364 ]
 [-0.23686776  0.0671876 ]]
[[ 0.70882161 -1.45983665  0.48044276 -1.28032139]
 [ 0.04655583  0.28168593  0.46636532 -0.87500408]
 [ 2.2841548   0.71917568  0.77087353  0.04137966]
 [ 0.44497083 -1.43376175  1.80849996 -0.86061081]
 [-0.35023255 -0.09871832  0.1764426   0.14621878]]
[[-0.41652817 -1.9083364  -0.42638188 -0.52257586]
 [ 0.04655583  0.28168593  0.46636532 -0.87500408]
 [-0.23686776  0.0671876  -0.62824434  0.53654728]
 [ 2.2841548   0.71917568  0.77087353  0.04137966]]
[[False False False]
 [False False False]
 [ True  True  True]
 [ True  True  True]]
[ 6  7  8  9 10 11]
请按任意键继续. . .
"""