# coding:utf-8
from random import Random

from lianxi.data.testexcel import a


# 随机登录脚本
class method():
    def login(self,browser):
        ran =Random()
        user=a()
        ff=user.f(ran.randint(1,30))
        print(ff)
        # browser =webdriver.Chrome()
        browser.get("http://172.16.4.120/5kcrm/index.php?m=user&a=login")
        browser.find_element_by_name("name").send_keys(ff[0])
        browser.find_element_by_name("password").send_keys(ff[1])
        browser.find_element_by_name("submit").click()
    def logout(self,browser):
        browser.find_element_by_css_selector(".avatar").click()
        browser.find_element_by_css_selector("li.dropdown:nth-child(6) > ul:nth-child(2) > li:nth-child(12) > a:nth-child(1)").click()

# if __name__ == '__main__':
#
#
#     yyy =webdriver.Chrome()
#     m=method()
#     m.login(yyy)
    # m.logout(yyy)
