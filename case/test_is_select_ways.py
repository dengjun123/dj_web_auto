#coding:utf-8
#is_selected 是判断下拉框内容是否被选中

from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

baidu = Base(driver)

loc1 = ("link text","设置")
mouse = baidu.findelement(loc1)
ActionChains(driver).move_to_element(mouse).perform()

loc2 = ("link text","搜索设置")
baidu.click(loc2)

loc3 = ("xpath",".//*[@id='nr']/option[3]")
r1 = baidu.findelement(loc3).is_selected()
print(r1)  #没有被选中


loc4 = ("id","nr")
select = baidu.findelement(loc4)
Select(select).select_by_index(2)

r2 = baidu.findelement(loc3).is_selected()
print(r2)  #被选中了，返回True




