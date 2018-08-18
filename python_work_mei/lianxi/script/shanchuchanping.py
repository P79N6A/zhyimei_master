# coding:utf-8
import time
import unittest

from selenium import webdriver

from lianxi.public.fuzhi1 import method


class del_chanping(unittest.TestCase):
    def setUp(self):
        print("开始登陆")
        global browser,hh
        browser=webdriver.Firefox()
        hh=method()
        hh.login(browser)
        print("登录结束")
    def test_chanping(self):
        print("开始删除产品")
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[4]/a").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/form/table/tbody/tr[1]/td[1]/input").click()
        time.sleep(2)
        # browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/form/table/tbody/tr[2]/td[1]/input").click()
        # time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"delete\"]").click()
        time.sleep(2)
        browser.switch_to_alert().accept()
        print("删除产品结束")
    def tearDown(self):
        print("退出登录")
        hh.logout(browser)
        browser.quit()
if __name__ == '__main__':
    unittest.main()