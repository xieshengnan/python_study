stu1 = ['john', 'male', '10011', 98]
num = 100
def test_for():
    global num
    for i in stu1:
        if type(i) == int:
            stu1[3] = 100
        if type(i) == str:
            pass
    print(stu1)
    num = 300
    print(num)
    #
    # for j in range(6):
    #     print(j)
test_for()
print(stu1)
print(num)

def getnine():
    list = []
    for i in range(1,10):
        for j in range(1,i+1):
            list.append(str(i)+"*"+str(j)+"="+str(i*j))

    print(list)

