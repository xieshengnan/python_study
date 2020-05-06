# 一个数字和字符串混合的列表，数字排在字符串前面，排序输出

list1 = ['10086', 'joe', 'male', 95]

def cmp(x):
    if type(x) is not str:
        return '0'
    else:
        return x

list1.sort(key=cmp)
print(list1)
