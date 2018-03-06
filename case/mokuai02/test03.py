#coding:utf-8

import unittest

class LoginCase(unittest.TestCase):

    u'''test03测试用例'''
    def setUp(self): #前置，每个用例都会先执行这个
        print("setUp:前置，每个用例都会先执行这个")
        self.Login()  #先走用例


    def tearDown(self):   #清空数据，或者退出登录
        print("tearDown:后置，每次用例执行完，都会执行这个")


    def Login(self): #没有以Test开头的不是用例，只是登录的一个方法
        print("走登录流程，登录了Login")


    def test04(self):  #测试用例
        print("04测试发帖：testReport")

    def test01(self):
        u'''test03下面的01测试'''
        print("test01")

    def test02(self):
        u'''test03下面的02测试'''
        print("test02")

    def test03(self):
        u'''test03下面的03测试'''
        print("test03")

if __name__ == '__main__':
    unittest.main()