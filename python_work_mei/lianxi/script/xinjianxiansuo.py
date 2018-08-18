# coding:utf-8
import time
import unittest

from selenium import webdriver

from lianxi.public.fuzhi1 import method


class cre_xiansuo(unittest.TestCase):
    def setUp(self):
        global browser,xx
        browser =webdriver.Chrome()
        xx=method()
        xx.login(browser)
        print("登录结束")
        username=browser.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/div/div[1]/div[2]/p[1]").text
        if username =="meizhengyi1":
            print("OK")
        # browser.get("http://172.16.4.120/5kcrm/index.php?m=user&a=login")
        # browser.find_element_by_name("name").send_keys(u"梅正义")
        # browser.find_element_by_name("password").send_keys("meizhengyi")
        # browser.find_element_by_name("submit").click()
        time.sleep(2)
    def test_count(self):
        print("新建线索开始")
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/a").click()
        time.sleep(2)
        browser.find_element_by_id("owner_name").clear()
        browser.find_element_by_id("owner_name").send_keys(u"梅正义")
        time.sleep(2)
        browser.find_element_by_id("name").send_keys(u"乐科")
        # browser.maximize_window()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id=\"source\"]/option[2]").click()
        time.sleep(1)
        browser.find_element_by_id("contacts_name").send_keys(u"谢小妹")
        time.sleep(1)
        browser.find_element_by_id("position").send_keys("CEO")
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id=\"saltname\"]/option[2]").click()
        time.sleep(1)
        browser.find_element_by_id("mobile").send_keys("13866666666")
        time.sleep(1)
        browser.find_element_by_id("email").send_keys(u"11111111@qq.com")
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id=\"form1\"]/table/tbody/tr[6]/td[2]/select[1]/option[2]").click()
        browser.find_element_by_xpath("//*[@id=\"form1\"]/table/tbody/tr[6]/td[2]/select[2]/option[2]").click()
        browser.find_element_by_xpath("//*[@id=\"form1\"]/table/tbody/tr[6]/td[2]/select[3]/option[2]").click()
        browser.find_element_by_name("address['street']").send_keys(u"不输了")
        time.sleep(1)
        browser.find_element_by_id("nextstep_time").send_keys(u"2017-11-08 16:23")
        time.sleep(1)
        browser.find_element_by_id("nextstep").send_keys(u"试试看")
        time.sleep(2)
        browser.find_element_by_id("description").send_keys(u"无聊")
        js ="var q=document.documentElement.scrollTop=10000"
        browser.execute_script(js)
        time.sleep(2)
        browser.find_element_by_name("submit").click()
        time.sleep(3)
        now=time.strftime("%y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        browser.get_screenshot_as_file("D:\\screenshot\\"+now+"xiansuo.png")
        print("新建线索结束")
        time.sleep(2)
    def tearDown(self):
        print("退出登录")
        xx.logout(browser)
        # browser.find_element_by_css_selector(".avatar").click()
        # browser.find_element_by_css_selector("li.dropdown:nth-child(6) > ul:nth-child(2) > li:nth-child(12) > a:nth-child(1)").click()
        browser.quit()
if __name__ == '__main__':
    unittest.main()