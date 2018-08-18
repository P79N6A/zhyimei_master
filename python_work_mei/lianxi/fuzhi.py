# coding:utf-8
from random import Random

from selenium import webdriver

from lianxi.data.testexcel import a


class method():
    def login(self):
        ran =Random()
        user=a()
        ff=user.f(ran.randint(1,10))
        # print(ff)
        browser =webdriver.Chrome()
        browser.get("http://172.16.4.120/5kcrm/index.php?m=user&a=login")
        browser.find_element_by_name("name").send_keys(ff[0])
        browser.find_element_by_name("password").send_keys(ff[1])
        browser.find_element_by_name("submit").click()
        print(ff[0],ff[1])
        # username=browser.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/div/div[1]/div[2]/p[1]").text
        # if username ==ff[0]:
        #     print(ff[0])
        #     print("OK")
if __name__ == '__main__':


    m=method()
    m.login()