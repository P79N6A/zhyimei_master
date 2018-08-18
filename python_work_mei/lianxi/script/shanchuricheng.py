# coding:utf-8
import time
import unittest

from selenium import webdriver

from lianxi.public.fuzhi1 import method


class del_richeng(unittest.TestCase):
    def setUp(self):
        print("开始登陆")
        global browser,denglu
        browser=webdriver.Firefox()
        denglu=method()
        denglu.login(browser)
    def test_richeng(self):
        print("开始删除日程")
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[6]/a").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/form/table/tbody/tr[1]/td[1]/input").click()
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"delete\"]").click()
        time.sleep(2)
        now=time.strftime("%y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        browser.get_screenshot_as_file("D:\\screenshot\\"+now+"xiansuo.png")
        time.sleep(2)
        browser.switch_to_alert().accept()
        print("删除日程结束")
    def tearDown(self):
        print("退出登录")
        denglu.logout(browser)
        time.sleep(2)
        browser.quit()
if __name__ == '__main__':
    unittest.main()