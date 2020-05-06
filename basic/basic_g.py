
class TestGenerator():

    def def_gen(self):
        g = (x * x for x in range(10))
        # print(g)
        print(next(g))
        print(next(g))

        for i in g:
            print(i)

    def odd(self):
        print('step 1')
        yield
        print('step 2')
        print('step 3')

t = TestGenerator()
# t.def_gen()
o = t.odd()
for n in o:
    print(n)
