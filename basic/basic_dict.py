# 字典中键是不可变的，键也是唯一的

dict1 = {'学号': '10086', '性别': 'male', '性别':'female', "成绩":[98, 90, 23]}
dict1['学号'] = '10010'
print(dict1)
print(dict1['学号'])

# 字典浅拷贝的尝试
dict2 = dict1
dict2['学号'] = '100'
print("dict2:", dict2)
print("dict1:", dict1)


dict3 = dict1.copy()
dict3['学号'] = '1111'
print("dict3:", dict3)
print("dict1:", dict1)

# dict5.formkeys(seq[1,2])

print("dict1学号：" + dict1.get('学号'))

if "姓名" in dict1:
    print(dict1["姓名"])
else:
    print(dict1["学号"])

print("dict key:", dict1.keys())
print("dict value:", dict1.values())
print("get:", dict1.get('学号'))
print("item:", dict1.items())
dict1.update({'地址': '猎豹移动'})
print(dict1)
print('dict.value:', dict1.values())


