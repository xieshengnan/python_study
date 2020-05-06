# 集合
list1 = [1, 2, 3,4,2, 1]
set1 = set(list1)
set1.add(9)       # 添加元素，只能添加一个
# set1.clear()
set1.discard(5)   # 删除指定元素，没有也不会报错
set1.remove(4)    # 删除指定元素，没有会报错
set1.pop()        # 随机删除一个元素
set1.update([2,4,5])  # 更新元素，可以更新多个
print(set1)

set2 = {'hello'}
print(set2)
