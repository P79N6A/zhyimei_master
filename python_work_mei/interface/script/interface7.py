# coding:utf-8
import requests
import unittest
import json
class test_wuye6(unittest.TestCase):
    def setUp(self):
        print(u"开始")
    def test_interface6(self):
        lp6={"houseId":"1","token":"e10adc3949ba59abbe56e057f20f8824","username":"13000000000"}
        rd6=requests.get("http://172.16.4.120/wuye/public/index.php/index/index//houseInfo?",params=lp6)
        print(rd6.status_code)
        print(rd6.url)
        print(rd6.text)
        data=json.loads(rd6.text)
        self.assertEqual("success",data["message"])
    def tearDown(self):
        print(u"结束")
if __name__ == '__main__':
    unittest.main