# coding:utf-8
import requests
import unittest

url = "http://127.0.0.1/biz/user-login-L2Jpei8=.html "
h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "http://127.0.0.1/biz/user-login-L2Jpei8=.html",
    # "Cookie":  # 头部没登录前不用传cookie，因为这里cookie就是保持登录的
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie":"lang=zh-cn; device=desktop; theme=default; zentaosid=n1en012q08i7d6n91ltj3kqqr5"
}

body = {"account": "admin",
        "password": "705d8374a6f83799ab5b70b9b6a48b3b",
        "keepLogin[]": "on",
        "referer": "/biz/"
        }

body1 = {"account": "admin111111",
         "password": "705d8374a6f83799ab5b70b9b6a48b3b",
         "keepLogin[]": "on",
         "referer": "/biz/"
         }

class TestLoginZenTao(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()

    def testZao_login(self):
        r = self.s.post(url, data=body, headers=h,verify=False)
        print(r.content)  # 打印结果看到location='http://127.0.0.1/zentao/my/'说明登录成功了
        # 访问登录后的页面
        r2 = self.s.get("http://127.0.0.1/biz/my/ ")
        print(r2.text)

    def testZao_login_Fail(self):
        print("")

if __name__=="__main__":
    unittest.main()