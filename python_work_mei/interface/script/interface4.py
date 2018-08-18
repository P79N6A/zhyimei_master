# coding:utf-8
import requests
import unittest
import json
class test_wuye4(unittest.TestCase):
    def setUp(self):
        print(u"开始")
    def test_interface4(self):
        lp4={"communityId":"1","token":"e10adc3949ba59abbe56e057f20f8824","username":"13000000000"}
        rd4=requests.get("http://172.16.4.120/wuye/public/index.php/index/index//buildingInfoList?",params=lp4)
        data=json.loads(rd4.text)
        self.assertEqual("success",data["message"])
    def tearDown(self):
        print(u"结束")
if __name__ == '__main__':
    unittest.main