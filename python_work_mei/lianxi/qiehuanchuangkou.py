# coding:utf-8
from selenium import webdriver
import  time
browser=webdriver.Firefox()
time.sleep(2)
browser.get("file:///C:/Users/Administrator/Desktop/jx3/jiansan.html")
browser.find_element_by_xpath("/html/body/ul/li[1]/a").click()
time.sleep(2)
# handle1=browser.current_window_handle
# print(handle1)
browser.find_element_by_xpath("/html/body/ul/li[2]/a").click()
time.sleep(2)
# handle2=browser.current_window_handle
# print(handle2)
handles=browser.window_handles
print(handles)
time.sleep(2)
browser.switch_to_window(handles[0])
time.sleep(2)
browser.switch_to_window(handles[1])
time.sleep(2)
browser.switch_to_window(handles[2])
browser.switch_to_window(handles[1])
browser.find_element_by_xpath("//*[@id=\"key_S\"]").send_keys("haha")