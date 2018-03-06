#coding:utf-8

from common import HTMLTestRunner

import unittest

casePath = "D:\\test\\pro_test\\case"  #用例路径
discover = unittest.defaultTestLoader.discover(casePath,pattern="test*.py")

print(discover)

#runner = unittest.TextTestRunner()
#runner.run(discover)

reportPath = "D:\\test\\pro_test\\report\\"+"report.html"

fp = open(reportPath,"wb") #以二进制写入

runner =HTMLTestRunner.HTMLTestRunner(fp,verbosity=2,
                                      title="测试报告",
                                      description="测试描述"
                                      )
runner.run(discover)

fp.close()