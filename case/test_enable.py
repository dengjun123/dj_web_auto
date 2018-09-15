#coding:utf-8
#check 判断复选框    (以下案列未全部选中，稍后再看)

from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("file:///C:/Users/11948/Desktop/checkbox.html")

check = Base(driver)

# loc1 = ("id","c1")
# r1 = check.isSelected(loc1)
# print(r1)
#
# che1 = check.click(loc1)
# r2 = check.isSelected(loc1)
# print(r2)

#复选框全部选中(复数定位)

loc_all = ("xpath",'.//*[@type="checkbox"]')
all  = check.findElements(loc_all)
print(all)  #list对象

for i in all:
    print(i.is_enable())