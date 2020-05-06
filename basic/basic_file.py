class file():
    def ReadFile(self):
        try:
            f = open('D:\study\estfile.txt', 'r')
            print(f.read())
        finally:
            if f:
                f.close()

    def Readnewfile(self):

        with open('D:\study\estfile.txt', 'r') as f2:
            for line in f2:
                print(line.strip())

    def Writefile(self):

        with open('D:\study\estfile.txt', 'w') as f:
            f.write("xin xieru de ")

f1 = file()
# f1.ReadFile()
f1.Readnewfile()
f1.Writefile()