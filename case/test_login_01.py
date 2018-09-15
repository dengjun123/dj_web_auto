#coding=utf-8
from selenium import webdriver

import time

class Login():

    def __init__(self,driver):
        self.driver = driver

    def login_01(self,user="dengjun",psw="oPe8*aVPWTySmSzo"):

        self.driver.get("http://team.gm825.net/index.php?m=user&f=login")
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("submit").click()

    #检查登录成功后页面元素
    def get_login_username(self):
        try:
            t = self.driver.find_element_by_css_selector("#userMenu>a").text
            print(t)
            return t
        except:
            return ""

    #判断登录框是否存在
    def is_alert_exist(self):
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except:
            return ""


if __name__ == "__main__":
    driver = webdriver.Firefox()
    Login = Login(driver)
    Login.login_01()