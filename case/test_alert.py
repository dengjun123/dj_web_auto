#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver = webdriver.Firefox()
url = "https://www.baidu.com/"
driver.get(url)
driver.implicitly_wait(10) #隐式等待

#鼠标移动到设置按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)

el = driver.find_element_by_id("nr")
Select(el).select_by_value("50")
el.click()

#点击保存设置
driver.find_element_by_link_text("保存设置").click()
time.sleep(3)


#alert弹窗处理
t = driver.switch_to.alert  #切换到alert

def is_alert_on(self):
    try:
        a = t.text  #获取弹窗上的文本
        return True
    except:
        return False

if is_alert_on():
    print("有弹窗 %s"%t.text)
    t.accept()  #点确定   点击取消  t.dismiss  t.test  t.sendkeys("输入内容")
else:
    print("没弹出框，不做处理")
    pass

