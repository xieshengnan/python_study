def bubblesort(list1):
    len1 = len(list1)
    for i in range(len1-1):
        for j in range(len1-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]

    print(list1)



def senNum1(list1):
    list1.sort()
    print(list1[-2])

def senNum2(list2):
    max_num = list2[0]
    sen_num = list2[0]

    for i in list2:
        if i > max_num:
            sen_num = max_num
            max_num = i
        elif max_num > i > sen_num:
            sen_num = i
        else:
            pass

    print(sen_num)


list1 = [4,5,1,2,7,9,8,10,100]
# senNum1(list1)
senNum2(list1)
# bubblesort(list1)


