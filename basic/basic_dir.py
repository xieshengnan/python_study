import os
class DirTest():

    def dir_test(self):
        print(os.name)
        print(os.path.abspath('.'))
        print(os.path.split('D:/study/python_study/basic_dir.py'))
        print(os.path.splitext('D:/study/python_study/basic_dir.py'))
        dlist = [d for d in os.listdir('.')]
        print("dlist:", dlist)


d = DirTest()
d.dir_test()
