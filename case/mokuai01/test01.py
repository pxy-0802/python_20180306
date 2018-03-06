#coding:utf-8

import unittest
class Test(unittest.TestCase):

    u'''测试test01'''

    def testAdd(self):  # test method names begin with 'test'
        a = 1
        b = 2
        result = a+b  #测试结果
        ex = 3 #期望结果
        self.assertEqual(result,ex) #断言是测试结果与期望结果对比

        if result==ex:
            print("True")
        else:
            print("False")


    def testMultiply(self):
        a = 2
        b = 3
        result = a*b #实际结果
        self.assertEqual(result,5) #断言(检查点)pass or failed  result与期望结果6  之间的对比


if __name__ == '__main__':
    unittest.main()