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

def result(all):
    r = [] #判断全部被选中

    for i in all:
        if i.is_selected():
            pass
        else:
            i.click()
            r.append(i.is_selected())

        # if not i.is_selected():
        #     i.click()
        #     r.append(i.is_selected())   #将结果放到列表r中
        # else:
        #     r.append(i.is_selected())

    return r
    print(r)

rrrr = result(all)
print(rrrr)

for i in rrrr:
    assert i == True
