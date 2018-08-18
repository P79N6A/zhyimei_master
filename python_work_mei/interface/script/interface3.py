# coding:utf-8
import requests
import unittest
import json
class test_wuye3(unittest.TestCase):
    def setUp(self):
        print(u"开始")
    def test_interface3(self):
        lp3={"username":"13000000000","token":"e10adc3949ba59abbe56e057f20f8824","communityId":"1","pageNum":"1","pageSize":"2"}
        rd3=requests.get("http://172.16.4.120/wuye/public/index.php/index/index//taskInfoListByCondition?",params=lp3)
        print(rd3.status_code)
        print(rd3.url)
        print(rd3.text)
        data=json.loads(rd3.text)
        self.assertEqual("success",data["message"])
    def tearDown(self):
        print(u"结束")
if __name__ == '__main__':
    unittest.main