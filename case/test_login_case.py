from selenium import webdriver
import unittest
from pages.login_pages import LoginPage,login_url



'''
1.输入dengjun，输入密码oPe8*aVPWTySmSzo  点登录
2.输入dengjun，输入密码  点登录
3.输入dengjun，输入密码oPe8*aVPWTySmSzo 点记住密码  点登录
4.点击忘记密码
'''

class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_01(self):
        #输入账户，输入密码，点击登录
        self.loginp.input_user("dengjun")
        self.loginp.input_psw("oPe8*aVPWTySmSzo")
        self.loginp.click_login_button()
        ressult = self.loginp.get_login_name()
        #断言
        self.assertTrue(ressult == "邓君")

    def test_02(self):
        #输入账户，输入密码，点击登录
        self.loginp.input_user("dengjun")
        self.loginp.click_login_button()
        ressult = self.loginp.get_login_name()
        #断言
        self.assertTrue(ressult == "")

    def test_03(self):
        #输入账户，输入密码，记住密码，点击登录
        self.loginp.input_user("dengjun")
        self.loginp.input_psw("oPe8*aVPWTySmSzo")
        self.loginp.click_keep_login()
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        #断言
        self.assertTrue(result == "邓君")

    def test_04(self):
        #忘记密码
        self.loginp.click_forget_psw()
        result = self.loginp.is_refresh_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
