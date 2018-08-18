# coding:utf-8
import time
import unittest

from selenium import webdriver

from lianxi.public.fuzhi1 import method


class cre_renwu(unittest.TestCase):
    def setUp(self):
        global browser,denglu
        browser=webdriver.Firefox()
        print("开始登陆")
        denglu=method()
        denglu.login(browser)
        print("登录结束")
    def test_renwu(self):
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[5]/a").click()
        time.sleep(2)
        print("开始新建任务")
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/a").click()
        time.sleep(2)
        browser.find_element_by_id("subject").send_keys(u"大闸蟹")
        time.sleep(2)
        browser.find_element_by_id("owner_name").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/span[13]/input").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/button[1]").click()
        time.sleep(2)
        browser.find_element_by_id("about_roles_name").send_keys(u"李四")
        time.sleep(2)
        browser.find_element_by_css_selector("#select1 > option:nth-child(2)").click()
        time.sleep(2)
        browser.find_element_by_css_selector("#module_name").send_keys("meizhengyi")
        time.sleep(2)
        browser.find_element_by_css_selector("#due_date").send_keys("2017-11-30 17:52")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[6]/td[2]/select/option[2]").click()
        time.sleep(2)
        browser.find_element_by_css_selector(".table > tbody:nth-child(3) > tr:nth-child(6) > td:nth-child(4) > select:nth-child(1) > option:nth-child(2)").click()
        time.sleep(2)
        # browser.find_element_by_xpath("/html/body").send_keys("666666666666666666666")
        time.sleep(2)
        browser.find_element_by_css_selector(".table > tfoot:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)").click()
        print("新建任务结束")
    def tearDown(self):
        print("退出登录")
        denglu.logout(browser)
        browser.quit()
if __name__ == '__main__':
    unittest.main()


