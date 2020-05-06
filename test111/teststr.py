def teststr(str1):
    len1 = len(str1)

    for i in range(0, len1):
        if str1[i] != str1[len1-1-i]:
            return False

    return True


str1 = "123454321"
re = teststr(str1)
print(re)