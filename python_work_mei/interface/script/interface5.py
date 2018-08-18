# coding:utf-8
import requests
import unittest
import json
class test_wuye5(unittest.TestCase):
    def setUp(self):
        print(u"开始")
    def test_baocun(self):
        lp5={"token":"e10adc3949ba59abbe56e057f20f8824","username":"13000000000","houseId":"1","createorName":"clark","residentName":"dy","telephone":"13888888888","content":"测试工单"}
        rd5=requests.post(url="http://172.16.4.120/wuye/public/index.php/index/index//taskInfo?",params=lp5)
        print(rd5.url)
        data1=json.loads(rd5.text)
        self.assertEqual(u"保存工单成功",data1["message"])
    def tearDown(self):
        print(u"结束")
if __name__ == '__main__':
    unittest.main