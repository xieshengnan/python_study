# 判断一个列表中是否有字符‘b’，如果有输出它的位置
list1 = [1, 'a', 2, 'b', 3, 'b']
num1 = list1.count('b')
if num1 > 0:
    print("有b，有%d个, b的位置是%d" % (num1, list1.index('b')))



