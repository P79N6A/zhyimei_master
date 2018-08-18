# coding:utf-8
import time
import unittest
from random import Random

from selenium import webdriver

from lianxi.data.testexcel import a
from lianxi.public.fuzhi1 import method


class cre_kehu(unittest.TestCase):
    def setUp(self):
        global browser,hhh
        print("开始登陆")
        browser = webdriver.Firefox()
        hhh=method()
        hhh.login(browser)
    def test_kehu(self):
        print("开始创建客户")
        r=Random()
        yyy=r.randint(1,200)
        kkhh=a()
        kehuming=kkhh.kehu(yyy)
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/a").click()
        time.sleep(2)
        browser.find_element_by_id("owner_name").clear()
        time.sleep(2)
        browser.find_element_by_id("owner_name").send_keys(u"梅正义")
        browser.find_element_by_id("name").send_keys(kehuming[0])
        time.sleep(2)
        browser.find_element_by_css_selector("#industry > option:nth-child(2)").click()
        browser.find_element_by_css_selector("#origin > option:nth-child(2)").click()
        browser.find_element_by_xpath("//*[@id=\"ownership2\"]").click()
        browser.find_element_by_id("zip_code").send_keys("666666")
        browser.find_element_by_css_selector("#annual_revenue > option:nth-child(3)").click()
        time.sleep(2)
        browser.find_element_by_id("rating1").click()
        time.sleep(2)
        browser.find_element_by_css_selector("select.input-medium:nth-child(2) > option:nth-child(2)").click()
        time.sleep(2)
        browser.find_element_by_css_selector("select.input-medium:nth-child(3) > option:nth-child(2)").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[6]/td[2]/select[3]/option[2]").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[6]/td[2]/input").send_keys(u"啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[8]/td[2]/input").send_keys("meizhengyi")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[8]/td[4]/input").send_keys(u"大大")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[9]/td[2]/input").send_keys("11111111@qq.com")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[9]/td[4]/input").send_keys("CEO")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[10]/td[2]/input").send_keys("11111111")
        time.sleep(2)
        js ="var q=document.documentElement.scrollTop=10000"
        browser.execute_script(js)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[10]/td[4]/input").send_keys("13666666666")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tbody/tr[11]/td[2]/textarea").send_keys(u"额鹅鹅鹅鹅鹅鹅鹅鹅鹅")
        time.sleep(2)
        browser.find_element_by_css_selector("#no_of_employees > option:nth-child(2)").click()
        time.sleep(2)
        browser.find_element_by_id("description").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td/input[1]").click()
        time.sleep(3)
        now=time.strftime("%y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        # 时间
        browser.get_screenshot_as_file("D:\\screenshot\\"+now+"add_cust.png")
        print("创建客户结束")
        haha=browser.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/form/table/tbody/tr[1]/td[3]/a/span").text
        print(kehuming[0])
        print(haha)
        self.assertEqual(kehuming[0],haha)
    def tearDown(self):
        hhh.logout(browser)
        time.sleep(2)
        browser.quit()
if __name__ == '__main__':
    unittest.main()