# coding=utf-8
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.number = input('Enter a number:')
        self.number = int(self.number)

    def test_case1(self):
        print(self.number)
        self.assertEqual(self.number, 10, msg='Your input is not 10')

    def test_case2(self):
        print(self.number)
        self.assertEqual(self.number, 20, msg='Your input is not 20')

    # @unittest.skip('暂时跳过用例3的测试')
    def test_case3(self):
        print(self.number)
        self.assertEqual(self.number, 30, msg='Your input is not 30')

    def tearDown(self):
        print('Test Over')


if __name__ == '__main__':
    # # 方案一如下：
    # unittest.main()

    # 方案二如下：
    # 8.2.1先构造测试集,实例化测试套件
    suite = unittest.TestSuite()
    # 8.2.1.2将测试用例加载到测试套件中。
    # 执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
    suite.addTest(Test('test_case3'))
    suite.addTest(Test('test_case2'))
    suite.addTest(Test('test_case1'))
    # 8.2.2执行测试用例，实例化TextTestRunner类
    runner = unittest.TextTestRunner()
    # 8.2.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(suite)
    #
    # # 方案三如下：
    # # 8.3.1构造测试集（简化了方案二中先要创建测试套件然后再依次加载测试用例）
    # # 执行顺序同方案一：执行顺序是命名顺序：先执行test_case1，再执行test_case2
    # test_dir = './'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # # 8.3.2执行测试用例，实例化TextTestRunner类
    # runner = unittest.TextTestRunner()
    # # 8.3.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    # runner.run(discover)