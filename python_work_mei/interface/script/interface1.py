# coding:utf-8
import requests
import unittest
import json
class test_wuye1(unittest.TestCase):
    def setUp(self):
        print(u"开始")
    def test_interface1(self):
        print(u"测试接口")
        lp1={"username":"13000000000"}
        rd1=requests.get("http://172.16.4.120/wuye/public/index.php/index/index//oauthAccount?",params=lp1)
        data=json.loads(rd1.text)
        self.assertEqual("success",data["message"])
    def tearDown(self):
        print(u"结束")
if __name__ == '__main__':
    unittest.main