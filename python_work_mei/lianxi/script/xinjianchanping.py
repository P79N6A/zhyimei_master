# coding:utf-8
import time
import unittest
from random import Random

from selenium import webdriver

from lianxi.data.testexcel import a
from  lianxi.public.fuzhi1 import method


class cre_chanping(unittest.TestCase):
    def setUp(self):
        print("登陆开始")
        global browser,hhh
        browser=webdriver.Chrome()
        hhh=method()
        hhh.login(browser)
    def test_chanping(self):
        print("开始新建产品")
        r=Random()
        t=r.randint(1,200)
        chanp=a()
        chanpingming=chanp.cp(t)
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[4]/a").click()
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[2]/a").click()
        browser.find_element_by_id("name").send_keys(chanpingming)
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"category_id\"]/option").click()
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"development_time\"]").send_keys("2017-11-30")
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"link\"]").clear()
        browser.find_element_by_xpath("//*[@id=\"link\"]").send_keys("http://666.com")
        browser.find_element_by_xpath("//*[@id=\"development_team\"]").send_keys(u"大辣椒")
        time.sleep(2)
        browser.find_element_by_id("cost_price").send_keys("100000")
        browser.find_element_by_id("suggested_price").send_keys("1000000")
        js ="var q=document.documentElement.scrollTop=10000"
        browser.execute_script(js)
        browser.find_element_by_xpath("//*[@id=\"main_pic\"]").send_keys("D:\\screenshot\\17-11-09_15-26-11add_cust.png")
        browser.find_element_by_xpath("//*[@id=\"description\"]").send_keys(u"哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈")
        browser.find_element_by_xpath("//*[@id=\"form1\"]/table/tfoot/tr/td/input[1]").click()
        print("新建产品结束")
        haha=browser.find_element_by_xpath("//*[@id=\"form1\"]/table/tbody/tr[1]/td[4]/a/span").text
        self.assertEqual("http://666.com",haha)
    def tearDown(self):
        print("开始退出")
        hhh.logout(browser)
        browser.quit()
if __name__ == '__main__':
    unittest.main()