from selenium import webdriver
import unittest
from pages.login_pages import LoginPage,login_url
import ddt
from common.read_excel import ExcelUtil
import os



'''
1.输入dengjun，输入密码oPe8*aVPWTySmSzo  点登录
2.输入dengjun，输入密码  点登录
3.输入dengjun111，输入密码oPe8*aVPWTySmSzo 点记住密码  点登录

'''

#测试数据源
# testdates = [
#     {"user":"dengjun","psw":"oPe8*aVPWTySmSzo","expect":"邓君"},
#     {"user":"dengjun","psw":"","expect":""},
#     {"user":"dengjun111","psw":"oPe8*aVPWTySmSzo","expect":""},
# ]


propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath = os.path.join(propath,"common","datas.xlsx")
print(filepath)

# filepath = "D:\\web_auto\\common\\datas.xlsx"  #路径不能写死
data = ExcelUtil(filepath)
testdates = data.dict_data()
print(testdates)


@ddt.ddt
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

    def login_case(self,user,psw,expect):
        self.loginp.login(user,psw)
        # self.loginp.input_user(user)
        # self.loginp.input_psw(psw)
        # self.loginp.click_login_button()
        ressult = self.loginp.get_login_name()
        print("测试结果：%s" % ressult )
        #断言
        self.assertTrue(ressult == expect)

    @ddt.data(*testdates)   #将testdates中的参数分开传入
    def test_01(self,data):
        # 输入账户，输入密码，点击登录
        print("-------开始测试：test_01-------" )
        # data1 = testdates[0]
        print("测试数据：%s" % data)
        self.login_case(data["user"],data["psw"],data["expect"])
        print("-------结束测试：pass-------" )


    # def test_02(self):
    #     #输入账户，输入密码，点击登录
    #     print("-------开始测试：test_02-------" )
    #     data2 = testdates[1]
    #     print("测试数据：%s" % data2)
    #     self.login_case(data2["user"],data2["psw"],data2["expect"])
    #     print("-------结束测试：pass-------" )

    # def test_03(self):
    #     #输入账户，输入密码，记住密码，点击登录
    #     print("-------开始测试：test_03-------" )
    #     data3 = testdates[2]
    #     print("测试数据：%s" % data3)
    #     self.login_case(data3["user"],data3["psw"],data3["expect"])
    #     print("-------结束测试：pass-------" )


    #如果最后运行弹框有问题，就将setUp里面的方法放到tearDown中

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
