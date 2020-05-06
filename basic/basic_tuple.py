# 元组一旦定义，元组内的元素不可变
tup1 = ('10086', 'male', 'joe')
print('type:', type(tup1))

tup2 = '10010', 'female', 'lily'
print('type:', type(tup2))

print("tup1[1]:", tup1[1])

print('tup1[:-1]', tup1[:-1])

print('tup1.count:', tup1.count('10086'))

print('tup1.index:', tup1.index('10086'))

# del tup1
# print("del", tup1)

print("max", max(tup1))
print("min", min(tup1))
print("len", len(tup1))

print("tup1+tup2", tup1+tup2)
print("tup1*3", tup1*3)
print("10086 in tup1", '10086' in tup1)

tup_list = list(tup1)
print("转换为列表后的tup1", tup1)
print("转到到的list", tup_list)


