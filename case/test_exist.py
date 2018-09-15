#coding:utf-8
#check 判断复选框    (以下案列未全部选中，稍后再看)

from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("file:///C:/Users/11948/Desktop/checkbox.html")

check = Base(driver)

loc1 = ("id","c1---")
r1 = check.isElementExist(loc1)
print(r1)



loc_all = ("xpath",'.//*[@type="checkbox"]')
r2 = check.isElementExist2(loc_all)
print(r2)
