from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base():

    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElementNew(self, locator):
        '''定位到元素，返回元素对象，没定位到，Timeout异常'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele

    def findElement(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElements(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
                return eles
            except:
                return []

    def sendkeys(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()


    def is_title(self,_title):
        try:
            #返回bool值
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self,_title):
        try:
            #返回bool值
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
            return result
        except:
            return False


    def is_text_in_element(self,locator,_text):
        try:
            #返回bool值
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,
                                                                                                           _text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,_value):
        try:
            #返回bool值,value为空返回false
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,
                                                                                                           _value))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def isSelected(self,locator):
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self,locator):
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self,locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def get_text(self,locator):
        #获取文本
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回“”")
            return ""

    def move_to_element(self,locator):
        #鼠标悬停操作
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()

    def select_by_index(self,locator,index):
        #通过索引，index是索引第几个，从0开始，默认选第一个
        element = self.findElement(locator)  #定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        #通过value值定位
        element = self.findElement(locator)  #定位select这一栏
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        #通过value值定位
        element = self.findElement(locator)  #定位select这一栏
        Select(element).select_by_visible_text(text)


    def js_focus_element(self,locator):
        #聚焦元素
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)


    def js_scroll_top(self):
        #滚动到顶部
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)


    def js_scroll_end(self):
        #滚动到底部
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)



if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://team.gm825.net/index.php?m=my&f=index")
    a = Base(driver)
    loc1 = (By.ID,"account")
    loc2 = (By.NAME,"password")
    loc3 = (By.ID,"submit")

    a.sendkeys(loc1,"dengjun")
    a.sendkeys(loc2,"oPe8*aVPWTySmSzo")
    a.click(loc3)

    a.move_to_element()
