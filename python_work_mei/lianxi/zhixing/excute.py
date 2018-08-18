# coding:utf-8
import sys
import time
import unittest
import lianxi.script.xinjianshangji
import lianxi.script.shanchukehu
import lianxi.script.shanchuricheng
import lianxi.script.shanchuxiansuo
import lianxi.script.xinjianchanping
import lianxi.script.xinjiankehu
import lianxi.script.xinjianricheng
import lianxi.script.xinjianxiansuo
import lianxi.script.xinjianyonghu

from lianxi.script import shanchuchanping, xinjianrenwu

reload(sys)#无法生成报告，重载
sys.setdefaultencoding("utf-8")
import HTMLTestRunner
suit=unittest.TestSuite()
suit.addTest(lianxi.script.xinjianchanping.cre_chanping("test_chanping"))
suit.addTest(lianxi.script.xinjianxiansuo.cre_xiansuo("test_count"))
# suit.addTest(lianxi.script.xinjianshangji)
suit.addTest(lianxi.script.xinjianyonghu.cre_yonghu("test_cre_yonghu"))
suit.addTest(lianxi.script.xinjiankehu.cre_kehu("test_kehu"))
suit.addTest(lianxi.script.xinjianricheng.cre_richeng("test_richeng"))
suit.addTest(xinjianrenwu.cre_renwu("test_renwu"))
suit.addTest(shanchuchanping.del_chanping("test_chanping"))
suit.addTest(lianxi.script.shanchukehu.del_kehu("test_kehu"))
suit.addTest(lianxi.script.shanchuricheng.del_richeng("test_richeng"))
suit.addTest(lianxi.script.shanchuxiansuo.del_xiansuo("test_xiansuo"))
now=time.strftime("%y-%m-%d-%H-%M-%S",time.localtime(time.time()))
report="D:\\baogao\\"+now+".html"
fp=open(report,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="testreport",description="我的第一个测试报告")
# runner=unittest.TextTestRunner()
runner.run(suit)
fp.close()