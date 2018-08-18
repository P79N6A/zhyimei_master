# coding:utf-8
from selenium import webdriver
from time import sleep
class method():
    def login(self,name,password):
        browser =webdriver.Chrome()
        browser.get("http://172.16.4.120/5kcrm/index.php?m=user&a=login")
        browser.find_element_by_name("name").send_keys(name)
        browser.find_element_by_name("password").send_keys(password)
        browser.find_element_by_name("submit").click()
if __name__ == '__main__':
    print(__name__)

    m=method()
    m.login(u"梅正义","meizhengyi")