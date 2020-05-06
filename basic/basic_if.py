num1 = int(input("enter a year number:"))

if num1%100 == 0:
    if num1%400 == 0:
        print("ruinian")
    else:
        print("no")
else:
    if num1%4 ==0:
        if num1%100 !=0:
            print("ruinian")

    else:
        print("no")


def choice():
    if num1 == 1:
        print("输入的是1")
    elif num1 == 2:
        print("输入的是2")
    else:
        print("输入的是其他的")

choice()