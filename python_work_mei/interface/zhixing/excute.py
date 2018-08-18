# coding:utf-8
import unittest
import time
import sys
import HTMLTestRunner
reload(sys)
sys.setdefaultencoding("utf-8")
dir="D:\\python_work\\interface\\script\\"
suit=unittest.defaultTestLoader.discover(dir,"inter*.py")
now=time.strftime("%y-%m-%d-%H-%M-%S",time.localtime(time.time()))
report="D:\\baogao\\baogao1\\"+now+".html"
fp=open(report,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="wuyetestreport",description=u"物业测试报告")
runner.run(suit)
fp.close()


