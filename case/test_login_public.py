#coding:utf-8
from selenium import webdriver
import unittest
import time
from case.test_login_01 import Login

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.Login = Login(cls.driver)

    def setUp(self):
        # self.driver =  webdriver.Firefox()
        # self.Login = Login(self.driver)
        self.driver.get("http://team.gm825.net/index.php?m=user&f=login")
        self.Login.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_01(self):
        time.sleep(2)
        self.Login.login_01()
        #判断是否登录成功
        time.sleep(3)
        t = self.Login.get_login_username()
        print("登录成功，登录用户名为：%s"%t)
        self.assertTrue(t == "邓君")

    def test_02(self):
        #测试登录失败的场景
        time.sleep(2)
        #输入正确账号、错误密码
        self.Login.login_01("dengjun","111")
        time.sleep(2)
        #判断是否登录成功
        t = self.Login.get_login_username()
        print("登录失败：%s"%t)
        self.assertTrue(t == "12")

    def tearDown(self):
        self.Login.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()