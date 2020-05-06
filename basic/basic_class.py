class Grade():

    def get_name(self):
        print('grade name')


class TestClass(Grade):

    name = 'grade_name'

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self, score):
        print("%s,%d" % (self.name, self.score))

    def welcome(self, name):
        print("welcome " + self.name)
        print('self', self)
        print('class', self.__class__)


t = TestClass('xiaoming', 98)
t.welcome(t.name)
t.print_info(t.score)
t.get_name()

# g = Grade()
# g.get_name()
# print(type(g))
# print(isinstance(t, Grade))
# print(isinstance(t, TestClass))
# print(dir(t))

