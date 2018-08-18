# coding:utf-8
import time
import unittest

from selenium import webdriver

from lianxi.public.fuzhi1 import method


class cre_richeng(unittest.TestCase):
    def setUp(self):
        print("开始登陆")
        global browser,denglu
        browser=webdriver.Firefox()
        denglu=method()
        denglu.login(browser)
        print("登录结束")
    def test_richeng(self):
        print("开始新建日程")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[6]/a").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/a").click()
        browser.find_element_by_xpath("//*[@id=\"subject\"]").send_keys(u"小龙虾")
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"owner_name\"]").clear()
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"owner_name\"]").send_keys("meizhengyi1")
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"start_date\"]").send_keys("2017-11-30")
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"end_date\"]").send_keys("2017-12-01")
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id=\"venue\"]").send_keys(u"乐科")
        time.sleep(2)
        browser.find_element_by_css_selector("#select1 > option:nth-child(2)").click()
        time.sleep(2)
        browser.find_element_by_css_selector("#module_name").send_keys("meizhengyi")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[6]/td[2]/textarea").send_keys(u"好气啊")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td[2]/input[1]").click()
        print("新建日程结束")
    def tearDown(self):
        print("退出登录")
        denglu.logout(browser)
        time.sleep(2)
        browser.quit()