# coding:utf-8
import re

result = []
with open(r"D:\robot\log\offlineLogs\821\kern.log", 'r') as f:
    for line in f:
        # print(line)
        # print(type(line))
        if re.match(r"[a-zA-Z]+[0-9a-zA-Z_]*(\.[a-zA-Z]+[0-9a-zA-Z_]*)*", line):
            result.append(list(line.strip('\n').split(',')))
        # print(line)

    for i in result:
         # if re.match(r"[a-zA-Z]+[0-9a-zA-Z_]*(\.[a-zA-Z]+[0-9a-zA-Z_]*)*",i):
             print(i)
    #     else:
    #         print(2)

    # print(f.read())

# [a-zA-Z]+[0-9a-zA-Z_]*(\.[a-zA-Z]+[0-9a-zA-Z_]*)*