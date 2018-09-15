#coding=utf-8

from selenium import webdriver
import unittest
import time

class LoginTest(unittest.TestCase):
    '''登录类的案列'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get("http://team.gm825.net/index.php?m=user&f=login")


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


    def test_login_01(self):
        "登陆成功的案例"
        time.sleep(3)
        self.driver.find_element_by_id("account").send_keys("dengjun")
        self.driver.find_element_by_name("password").send_keys("oPe8*aVPWTySmSzo")
        self.driver.find_element_by_id("submit").click()
        #判断是否登录成功
        time.sleep(3)
        t = self.get_login_username()
        print("获取结果：%s"%t)
        self.assertTrue(t=="邓君")


        #检查页面元素，看是否登录成功
    def get_login_username(self):
        try:
            t = self.driver.find_element_by_css_selector("#userMenu>a").text
            print(t)
            return t
        except:
            return ""


    #退出登录
    def tearDown(self):
        self.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

