#coding:utf-8

import unittest
import requests

m = "添加留言aa-3"
url_login = "http://www.ablesky.com/login.do?"

headers_login = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie": "showPublicImg3=false; tencentSig=2870733824; __root_domain_v=.ablesky.com; _qddaz=QD.f8x14a.lmds6l.j0rk0yul; Hm_lvt_9790880dab91acdee4b1a752a45fd21a=1513663890; UM_distinctid=1606d6601da844-0d7a6cfa46d76a-b7a103e-1fa400-1606d6601db72a; CNZZDATA1260967758=525642747-1513663889-http%253A%252F%252Fwww.ablesky.com%252F%7C1513666559; forpaysecurity=3be7cd04-ac1f-443c-a68e-0347866d7b1e; Hm_lvt_a8bcd4708d6047971e1bf0d843eec6a5=1514018704; freshIdc=0; Hm_lvt_cd6c8acf1994c677daf5f506e7b66e2d=1515204108; Hm_lvt_d2ccd9166d14caf4f88f65c3c0cee399=1515204109; AUI_EC=%7B%22ablesky_chapterKnow%22%3Atrue%2C%22SA%22%3A%22aa-1%22%7D; as=d06dc01291efdf3fdaa9189cb2d47f46; Hm_lvt_2c3784f03626d6f26635da62b9bfad4f=1516846041,1517018951,1517044730,1517190025; se=67dcf79252da9fee319c1e230a27dbec; SA=aa-1; Hm_lpvt_2c3784f03626d6f26635da62b9bfad4f=1517196365; AUI_SC=%7B%22oauth2_ref%22%3A%22http%3A%2F%2Fwww.ablesky.com%2F%22%7D; AUSS=YWEtMToxNTE5Nzg4MzcwNzE5OjNkMjQ2NzRkMTg2ZTc0YjZlNTMxYzAxNGY5YzQwZTg3; RM=rm; ASUSS=QUI0MUNFMUNBRjY3RkIxOENDNThFRTk5ODJBNDcwMEEucGFzc3BvcnQwbWQuYnAxLmFibGVza3kuY29tOjE5Mi4xNjguMjAyLjIwOjExMjExOjYxMzMwNzA6YWEtMToxNTE3MTk2MzcwNzIzOk16RTJZemczWmpjMU0yUTRaakptWXpCbVpESmtNV1JtTkRnNU5XRTNaRGM9; JSESSIONID=C5C5ABE27E6E8A540F4677FE4F5E81A5.se1md.bp1"
}
gossip_url = "http://www.ablesky.com/ajax/account/gossip/add"

body = {
    "userName":"aa-1",
    "showPublic":"true",
    "content":"%s"%m,
    "gossipId":""
}

class TestLoginAblesky(unittest.TestCase):
    u'''ablesky登录测试'''
    def setUp(self):
        self.s = requests.session()

    def testLogin(self):
        u'''ablesky登录'''
        re_login = self.s.get(url=url_login,headers = headers_login,verify = False)
        print(re_login.content)
        # 验证是否登录成功
    def testReportadd(self):
        u'''ablesky发布留言'''
        re_post = self.s.post(url=gossip_url,data=body,headers = headers_login,verify = False)
        result1 = re_post.json()
        print("字典转换成json：" % result1)
        print(type(result1))
        print(result1["result"])
        print(result1["result"]["gossiperUserName"])
        str1 = result1["result"]["gossiperUserName"]
        if "mingzhutest" in str1:
            print("发布成功")
        else:
            print("发布失败")

if __name__ == '__main__':
    unittest.main()
