#coding:utf-8
#radio 也是平常见到的单选，一定药看到type=“radio”

from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

baidu1 = Base(driver)

loc1 = ("link text","设置")
mouse = baidu1.findelement(loc1)
ActionChains(driver).move_to_element(mouse).perform()

loc2 = ("link text","搜索设置")
baidu1.click(loc2)

# loc3 = ("id","s1_1")
loc4 = ("id","s1_2")
baidu1.click(loc4)

# r1 = baidu.isSelected(loc3)
# print(r1)
r2 = baidu1.isSelected(loc4)
print(r2)