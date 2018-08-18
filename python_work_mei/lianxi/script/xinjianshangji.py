# coding:utf-8
from selenium import webdriver
import time
from lianxi.public.fuzhi1 import method
import unittest
class test_cre_shangji(unittest.TestCase):
    def setUp(self):
        global browser
        print("开始登陆")
        browser =webdriver.Firefox()
        browser.get("http://172.16.4.120/5kcrm/index.php?m=user&a=login")
        browser.find_element_by_name("name").send_keys(u"梅正义")
        browser.find_element_by_name("password").send_keys("meizhengyi")
        browser.find_element_by_name("submit").click()
        time.sleep(2)
    def test_shangji(self):
        print("开始新建商机")
        username=browser.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/div/div[1]/div[2]/p[1]").text
        print(username)
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[3]/a").click()
        time.sleep(2)
        browser.find_element_by_css_selector("a.btn-primary").click()
        time.sleep(2)
        browser.find_element_by_css_selector("#customer_name").click()
        time.sleep(2)
        browser.find_element_by_css_selector("#datas > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").click()
        time.sleep(2)
        browser.find_element_by_css_selector("div.ui-dialog:nth-child(17) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)").click()
        time.sleep(2)
        browser.find_element_by_id("total_price").send_keys("100000")
        time.sleep(2)
        browser.find_element_by_id("name").send_keys(u"乐科")
        time.sleep(2)
        browser.find_element_by_css_selector("select.input-medium:nth-child(2) > option:nth-child(2)").click()
        browser.find_element_by_css_selector("select.input-medium:nth-child(3) > option:nth-child(2)").click()
        browser.find_element_by_css_selector("select.input-medium:nth-child(4) > option:nth-child(2)").click()
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[5]/td[2]/input").click()
        browser.find_element_by_css_selector("#type > option:nth-child(2)").click()
        time.sleep(2)
        browser.find_element_by_css_selector("#origin > option:nth-child(2)").click()
        time.sleep(2)
        browser.find_element_by_css_selector(".input-large").send_keys("XXXXXXXXXXXXXXXXXXXXXXXX")
        browser.find_element_by_id("estimate_price").send_keys("1000000")
        browser.find_element_by_id("gain_rate").send_keys("80")
        time.sleep(2)
        browser.find_element_by_css_selector("#nextstep_time").send_keys("2017-11-14 20:59")
        time.sleep(2)
        browser.find_element_by_id("nextstep").send_keys("YYYYYYYYYYYYYYYYYYYYYY")
        browser.find_element_by_id("description").send_keys("hhhhhhhhhhhhhhhhhhhhhhhh")
        js ="var q=document.documentElement.scrollTop=10000"
        browser.execute_script(js)
        time.sleep(2)
        browser.find_element_by_css_selector("#form1 > table:nth-child(3) > tfoot:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").click()
        time.sleep(2)
        print("新建商机结束")
    def tearDown(self):
        mm=method()
        mm.login(browser)
        print("退出登录")
        browser.quit()