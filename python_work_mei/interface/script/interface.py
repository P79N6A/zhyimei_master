# coding:utf-8
import json
import requests
import unittest
class test_wuye(unittest.TestCase):
    def setUp(self):
        print("接口测试开始")
    def test_login(self):
        lp={"username":"13000000000","password":"123456"}
        rd=requests.get("http://172.16.4.120/wuye/public/index.php/index/index//login?",params=lp)
        data=json.loads(rd.text)
        self.assertEqual("success",data["message"])
    def tearDown(self):
        print("接口测试结束")
if __name__ == '__main__':
    unittest.main