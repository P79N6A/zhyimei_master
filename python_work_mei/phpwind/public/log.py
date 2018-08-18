# coding:utf-8
from selenium import webdriver
import time
class method():
    def login(self,browser):
        # browser=webdriver.Firefox()
        browser.get("http://172.16.4.120/wind/login.php")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[6]/div/form/div/table/tbody/tr[2]/td/div/dl[1]/dd/input").send_keys("meizhengyi")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[6]/div/form/div/table/tbody/tr[2]/td/div/dl[2]/dd/input").send_keys("meizhengyi")
        time.sleep(2)
        browser.find_element_by_name("hideid").click()
        time.sleep(2)
        browser.find_element_by_name("cktime").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[6]/div/form/div/table/tbody/tr[2]/td/div/dl[5]/dd/input").click()
    def logout(self,browser):
        browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/table/tbody/tr/td[4]/a[3]").click()
        time.sleep(2)
        browser.quit()