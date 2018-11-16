# coding=utf-8
import unittest.case
import unittest.runner
import unittest.result
import unittest.suite
import HTMLTestRunner
import time
import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")
suit=unittest.TestSuite()
os.chdir("D:\Users\zhyimei\PycharmProjects\echo\case")
os.system("python excute.py")
print "测试结束"
now=time.strftime("%y-%m-%d-%H-%M-%S",time.localtime(time.time()))
report="D:\\测试报告\\"+now+".html"
fp=open(report,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告",description="echo_1.3.7")
runner.run(suit)