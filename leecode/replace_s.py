class TestReplace:

    def replace(self, str1, list1):

        result = []

        for i in range(len(str1)):
            if str1[i] == '%':
                if str1[i+1] == 's':
                    result.append(list1[0])
                    list1.pop(0)
                else:
                    result.append('%')
            else:
                result.append(str1[i])

        print("".join(result))


str1 = "A%sC%sE"
list1 = ['B','D','F']

sul = TestReplace()
sul.replace(str1,list1)


