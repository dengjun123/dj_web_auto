#coding=utf-8

from selenium import webdriver
import time
import unittest

driver = webdriver.Firefox()
driver.get("http://www.maiziedu.com/")
#窗口最大化
driver.maximize_window()
time.sleep(3)

class Login_maizi():
    def __init__(self,driver):
        self.driver = driver
        time.sleep(4)

    def test_click_login_button(self,username,password):
        #点击关闭浮层
        self.driver.find_element_by_class_name("close-windows-btn7").click()
        time.sleep(3)
        #点击登录按钮
        self.driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div/a[2]").click()

    #判断登录框是否存在
    def is_alert_on(self):
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert   # 切换到alert弹框
            text = alert.text #获取弹框上的文本
            alert.accept()
            return text
        except:
            return ""

    #登录
    def test_login_ture(self):
        self.driver.find_element_by_id("id_account_l").sendkeys("15011462598")
        self.driver.find_element_by_id("id_password_l").sendkeys("Zhen8023")
        self.driver.find_element_by_id("login_btn").click()



if __name__ =="__main__":
    unittest.main()
    Login = Login_maizi()
    Login.test_login_ture()

