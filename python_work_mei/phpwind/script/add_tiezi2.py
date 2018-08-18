# coding:utf-8
from selenium import webdriver
import time
from phpwind.public.log import method
import unittest
class add_tiezi2(unittest.TestCase):
    def setUp(self):
        global browser,denglu
        browser=webdriver.Firefox()
        denglu=method()
        denglu.login(browser)
        time.sleep(2)
    def test_tiezi2(self):
        browser.find_element_by_id("fn_4").click()
        time.sleep(2)
        browser.find_element_by_id("td_post").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[8]/div/form[1]/div/div[3]/div[3]/div/img[7]").click()
        time.sleep(2)
        browser.find_element_by_css_selector("#atc_title").send_keys(u"咦惹")
        time.sleep(2)
        browser.find_element_by_css_selector("#menu_show > img:nth-child(3)").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html").send_keys(u"啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈")
        time.sleep(2)
        js ="var q=document.documentElement.scrollTop=10000"
        browser.execute_script(js)
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[8]/div/form[1]/div/table[2]/tbody/tr[4]/td[1]/div/input[1]").click()
        time.sleep(2)
    def tearDown(self):
        denglu.logout(browser)
        time.sleep(2)
        browser.quit()