#coding:utf-8

from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
import time

login_url = "http://team.gm825.net/index.php?m=user&f=login&referer=L2luZGV4LnBocD9tPW15JmY9aW5kZXg="
class LoginPage(Base): #继承
    #定位登录
    loc1_user = (By.ID,"account")
    loc2_psw= (By.NAME,"password")
    loc3_button = (By.ID,"submit")
    loc4_keep = ("id","keepLoginon")
    loc5_forget_psw = ("link text","忘记密码")
    loc6_get_user = ("css selector","#userMenu>a")
    loc7_forget_psw_page = ("css selector",".btn")

    def input_user(self,text=''):
        self.sendkeys(self.loc1_user,text)

    def input_psw(self,text=''):
        self.sendkeys(self.loc2_psw,text)

    def click_login_button(self):
        self.click(self.loc3_button)

    def click_keep_login(self):
        self.click(self.loc4_keep)

    def click_forget_psw(self):
        self.click(self.loc5_forget_psw)



    def get_login_name(self):
        user = self.get_text(self.loc6_get_user)
        return user

    def get_login_result(self,user):
        result = self.is_text_in_element(self.loc6_get_user,user)

        return result


    def is_alert_exist(self):
        #判断alert是否存在
        a = self.is_alert()
        if a:
            print(a)
            a.accept()

    def is_refresh_exist(self):
        #判断忘记密码页面刷新按钮是否存在
        r = self.isElementExist(self.loc7_forget_psw_page)
        return r


    def login(self,user="dengjun",password="oPe8*aVPWTySmSzo",keep_login=False):
        #登录流程
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(password)
        if keep_login:
            self.click_keep_login()

        self.click_login_button()



if __name__ == "__main__":
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    login_page.login(keep_login=True)

    # driver.get(login_url)
    # login_page.input_user("dengjun")
    # login_page.input_psw("oPe8*aVPWTySmSzo")
    # login_page.click_keep_login()
    # login_page.click_login_button()
