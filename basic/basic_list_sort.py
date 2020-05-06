L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
str1 = 'xieshengnan'
d = {'a': 1, 'b': 2, 'c': 3}


class MoreTest():

    # def __init__(self):
    #     self.L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    #     self.str1 = 'xieshengnan'

    def slice_test(self):
        print("L[0:3]:", L[0:3])
        print("L[:3]", L[0:3])
        print("L[-1]", L[-1])
        print("L[-2:-1]", L[-2:-1])
        print("L[-3:]", L[-3:])
        # print("L[:4:2]", L[:4:2])
        # print("L[::2]", L[::2])
        # print("L[:]", L[:])

    def iter_test(self):
        for i in L:
            print(i)

        for i in str1:
            print(i)

        for key in d:
            print(key)

        for value in d.values():
            print(value)

        for k, v in d.items():
            print(k, v)

    def comp(self):
        L = []
        # print(list(range(0, 10)))
        for x in range(0,10):
            L.append(x)
        print(L)
        L1 = [x*x for x in range(1, 10)]
        print("L1:", L1)

        L2 = [x*x for x in range(1, 11) if x%2 == 0]
        print("L2:", L2)

        L3 = [m + n for m in 'AB' for n in 'abc']
        print("L3", L3)

        L4 = [x if x%2 == 0 else -x for x in range(1, 11) if x%3 == 0]
        print("L4:", L4)

    def test(self):
        L1 = ['Hello', 'World', 18, 'Apple', None]
        L2 = [x.lower() for x in L1 if isinstance(x, str) == True ]
        print("L2:", L2)


m = MoreTest()
# print("--------------------slice--------")
# m.slice_test()
# print("--------------iter------------")
# m.iter_test()
# print(L)
# print("-------------------comp---------")
# m.comp()
m.test()
