# coding:utf-8
import time
import unittest

from selenium import webdriver

from lianxi.public.fuzhi1 import method


class del_xiansuo(unittest.TestCase):
    def setUp(self):
        print("开始登陆")
        global browser,n
        browser=webdriver.Firefox()
        n=method()
        n.login(browser)
    def test_xiansuo(self):
        print("开始删除线索")
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/form/table/tbody/tr[1]/td[1]/input").click()
        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/form/table/tbody/tr[2]/td[1]/input").click()
        time.sleep(2)
        browser.find_element_by_css_selector("div.pull-left:nth-child(1) > a:nth-child(1)").click()
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"delete\"]").click()
        time.sleep(3)
        browser.switch_to_alert().accept()
        # 确认提示框
        now=time.strftime("%y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        # 时间
        browser.get_screenshot_as_file("D:\\screenshot\\"+now+"delete_leads.png")
        # 截图时间
        time.sleep(3)
        print("删除线索结束")
    def tearDown(self):
        print("退出登录")
        n.logout(browser)
        time.sleep(3)
        browser.quit()
if __name__ == '__main__':
    unittest.main()