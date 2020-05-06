# info = ['joe', 'man', 98]
# score = [89, 90, 100]
# info1 = []
# info1.append('may')
# print(info1)
#
# stu_info = [
#     ['joe', 'male', 99],
#     ['may', 'female', 100]
# ]
# print("%s的成绩是%d" % (stu_info[1][0], stu_info[1][2]))
#
# stu = [0] * 3
# print("stu:", stu)
# stu[0] = "may"
# stu[1] = "female"
# stu[2] = 99
# print("newstu", stu)
# print("stu[-1]:", stu[-1])
#
# # 定义二维列表
# stu1 = [([0] * 3) for i in range(4)]
# print("stu1", stu1)

boy = ['gary', 'man', 13]
boy.append('good')
print("appen", boy)

girl = ['lily', 'woman', 13]
boy.extend(girl)
print("extend", boy)

print("index2:13", boy.index(13))

print("count13", boy.count(13))

boy.insert(0, 'head')
print("insert", boy)

boy.pop(-1)
print("pop(-1)", boy)

print("boy+girl", boy+girl)
print("boy*2", boy*2)
print("john in boy :", 'john' in boy)

boy.remove('lily')
print("remove-1", boy)

boy.reverse()
print("reverse", boy)

# print("sort", boy.sort())

# print("len", len(boy))
# print("max", max(boy))
# print("min", min(boy))

boy.clear()
print("clear", boy)

del girl[-1]
print("del", girl)

# del girl
# print("del all", girl)







