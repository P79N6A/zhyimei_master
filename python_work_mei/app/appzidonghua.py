# coding:utf-8
from  appium import webdriver
import  time
desired_caps={
    "platformName":"Android",
    "deviceName":"7f0e043",
    "patformVerson":"6.0",
    "appPackage":"com.android.calculator2",
    "appActivity":"Calculator",
    "unicodeKeyboard":True,
    "resetKeyboard":True
}
driver=webdriver.Remote("http://127.0.0.1:4731/wd/hub",desired_caps)
time.sleep(2)
driver.find_element_by_id("com.android.calculator2:id/digit4").click()
time.sleep(2)
driver.find_element_by_id("com.android.calculator2:id/plus").click()
time.sleep(2)
driver.find_element_by_id("com.android.calculator2:id/digit3").click()
time.sleep(2)
driver.find_element_by_id("com.android.calculator2:id/equal").click()
time.sleep(2)
driver.quit()
