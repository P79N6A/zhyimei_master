# coding:utf-8
import phpwind.script.add_tiezi1
import phpwind.script.add_tiezi2
from selenium import webdriver
import time
import unittest
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import HTMLTestRunner
# suit=unittest.TestSuite()
# suit.addTest(phpwind.script.add_tiezi1.add_tiezi1("test_tiezi1"))
# # suit.addTest(phpwind.script.add_tiezi2.add_tiezi2("test_tiezi2"))
# now=time.strftime("%y-%m-%d-%H-%M-%S",time.localtime(time.time()))
# report="D:\\baogao\\baogao1\\"+now+".html"
# fp=open(report,"wb")
# runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="phpwindtestreport",description=u"phpwind测试报告")
# runner.run(suit)
# fp.close()

dir="D:\\python_work\\phpwind\\script\\"
suit=unittest.defaultTestLoader.discover(dir,"add*.py")
# suit.addTest(phpwind.script.add_tiezi2.add_tiezi2("test_tiezi2"))
now=time.strftime("%y-%m-%d-%H-%M-%S",time.localtime(time.time()))
report="D:\\baogao\\baogao1\\"+now+".html"
fp=open(report,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="phpwindtestreport",description=u"phpwind测试报告")
runner.run(suit)
fp.close()
# runner=unittest.TextTestRunner()
# runner.run(suit)

