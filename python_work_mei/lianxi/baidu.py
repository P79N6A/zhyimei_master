# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
liulanqi=webdriver.Chrome()
liulanqi.get("https://www.baidu.com/")
sleep(2)
ele = liulanqi.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[8]")
print(ele)
sleep(2)
ActionChains(liulanqi).move_to_element(ele).perform()
# 悬停
sleep(5)
liulanqi.find_element_by_css_selector(".bdpfmenu > a:nth-child(5)").click()
liulanqi.find_element_by_id("kw").send_keys(u"是过得好快")
sleep(2)
liulanqi.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
sleep(2)
liulanqi.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")
sleep(2)
liulanqi.find_element_by_id("kw").send_keys(Keys.CONTROL,"v")
sleep(2)
print(liulanqi.title)
print(liulanqi.current_url)

# liulanqi.switch_to_alert().accept()
# liulanqi.switch_to_alert().dismiss()
# alert_test =liulanqi.switch_to_alert().text
