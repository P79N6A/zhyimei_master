# coding:utf-8
from selenium import webdriver
import time
haha =webdriver.Chrome()
haha.get("http://172.16.4.120/5kcrm/index.php?m=user&a=login")
haha.find_element_by_name("name").send_keys(u"梅正义")
haha.find_element_by_name("password").send_keys("meizhengyi")
haha.find_element_by_name("submit").click()
time.sleep(2)