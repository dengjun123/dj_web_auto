#coding:utf-8

from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
import time

class AddBugPage(Base): #继承
    #定位登录
    # loc1 = (By.ID,"account")
    # loc2 = (By.NAME,"password")
    # loc3 = (By.ID,"submit")

    #添加bug
    loc_test = ("link text","测试")
    loc_bug = ("link text","Bug")
    loc_addbug = ("xpath",".//*[@id='createActionMenu']/a")
    loc_truck = ("xpath",".//*[@id='openedBuild_chosen']/ul/li/input")
    loc_truck_add = ("xpath",".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_input_title = ("id","title")
    #需要先切换
    # loc_frame = ("class name","ke-edit-iframe")
    loc_input_body = ("class name","article-content")
    loc_save = ("css selector","#submit")

    #新增的列表
    loc_new = ("xpath",".//*[@id='bugList']/thead/tr/th[4]/div/a")

    # def __init__(self,driver):
    #     self.driver = driver
    #     self.chandao = Base(self.driver)

    # def login(self,user="dengjun",password="oPe8*aVPWTySmSzo"):
    #     self.driver.get("http://team.gm825.net/index.php?m=my&f=index")
    #     self.sendkeys(self.loc1,user)
    #     self.sendkeys(self.loc2,password)
    #     self.click(self.loc3)

    def add_bug(self,title="测试提交bug"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)

        self.sendkeys(self.loc_input_title,title)

        time.sleep(3)
        frame = self.findElement(("class name","ke-edit-iframe"))
        #切换iframe
        self.driver.switch_to.frame(frame)
        #副文本不能clear
        body = '''[测试步骤]
        [结果]
        [期望结果]
        '''
        self.sendkeys(self.loc_input_body,body)
        self.driver.switch_to.default_content()
        self.click(self.loc_save)

    def is_add_bug_success(self,_text):
        return self.is_text_in_element(self.loc_new,_text)


if __name__ == "__main__":
    driver = webdriver.Firefox()
    bug = AddBugPage(driver)
    from pages.login_pages import LoginPage
    a = LoginPage(driver)
    a.login()



    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "测试提交bug"+timestr
    bug.add_bug(title)

    result = bug.is_add_bug_success(title)
    print(result)
