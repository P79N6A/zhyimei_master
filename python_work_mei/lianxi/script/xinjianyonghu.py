# coding:utf-8
import time
import unittest
from random import Random

from selenium import webdriver

from lianxi.data.testexcel import a
from  lianxi.public.fuzhi1 import method


class cre_yonghu(unittest.TestCase):
    def setUp(self):
        print("开始登陆")
        global browser,nn
        browser =webdriver.Firefox()
        nn=method()
        nn.login(browser)
        print("登陆结束")
    def test_cre_yonghu(self):
        print("开始创建用户")
        r=Random()
        h=r.randint(1,280)
        # print(h)
        tt=a()
        ww=tt.yh(h)
        time.sleep(2)
        browser.find_element_by_class_name("avatar").click()
        browser.find_element_by_css_selector("li.dropdown:nth-child(6) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()
        time.sleep(2)
        # browser.implicitly_wait(3)
        browser.find_element_by_css_selector("a.btn:nth-child(3)").click()
        # print(ww[0],ww[1])
        browser.find_element_by_css_selector("table.table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)").send_keys(ww[0])
        browser.find_element_by_id("password").send_keys(ww[1])
        time.sleep(2)
        browser.find_element_by_css_selector("table.table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > select:nth-child(1) > option:nth-child(2)").click()
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/select/option[2]").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/select/option[2]").click()
        time.sleep(2)
        browser.find_element_by_css_selector("table.table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(2) > input:nth-child(1)").click()
        time.sleep(2)
        print("创建用户结束")
    def tearDown(self):
        print("退出登录")
        nn.logout(browser)
        time.sleep(2)
        browser.quit()
