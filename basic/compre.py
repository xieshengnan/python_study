# 推导式
list1 = list(range(1, 10))
print(list1)

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

L = [x * x for x in range(1, 11)]
print(L)

# 筛选仅偶数的平方
L2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L2)

# 两层循环，全排列
L3 = [n + m for n in 'XY' for m in 'ab']
print(L3)

# 导出当前目录下的所有文件
import os
dir1 = [x for x in os.listdir()]
print(dir1)





