# 主要统计总词汇数和每个词汇的数目

def wordcount(readtxt):
    dict = {}
    readlist = readtxt.split()
    for every_word in readlist:
        if every_word in dict:
            dict[every_word] += 1
        else:
            dict[every_word] = 1

