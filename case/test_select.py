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

#方法一，通用，先展开再选项
driver.find_element_by_id("nr").click()
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='nr']/option[3]").click()


#方法二，通过索引
el = driver.find_element_by_id("nr")
# # Select(el).select_by_index(1)
# #收回选项框
# el.click()

#通过value值
# Select(el).select_by_value("50")
# el.click()


Select(el).select_by_visible_text("每页显示10条")
el.click()
