from selenium import webdriver
import unittest
import time
from pages.login_pages import LoginPage
from pages.add_bug_pages import AddBugPage

my = "http://team.gm825.net/index.php?m=my&f=index"

class AddBugCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.bug = AddBugPage(cls.driver)
        a = LoginPage(cls.driver)
        a.login()

    def setUp(self):
        self.driver.get(my)


    def test_add_bug(self):
        #添加bug
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "测试提交bug"+timestr
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_success(title)
        print(result)

        self.assertTrue(result)     #断言失败了

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main()