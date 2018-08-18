# coding:utf-8
import time
import unittest

from selenium import webdriver

from lianxi.public.fuzhi1 import method


class del_kehu(unittest.TestCase):
    def setUp(self):
        print("开始登陆")
        global browser,hhh
        browser = webdriver.Chrome()
        hhh=method()
        hhh.login(browser)
    def test_kehu(self):
        print("开始删除客户")
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(2)
        browser.find_element_by_name("customer_id[]").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/ul/div/a").click()
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"delete\"]").click()
        time.sleep(2)
        browser.switch_to_alert().accept()
        print("删除客户结束")
    def tearDown(self):
        print("退出登录")
        hhh.logout(browser)
        browser.quit()
if __name__ == '__main__':
    unittest.main()