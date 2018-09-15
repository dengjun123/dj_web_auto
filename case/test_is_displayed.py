#coding:utf-8

from common.base import Base
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://team.gm825.net/index.php?m=my&f=index")
chandao = Base(driver)
loc1 = ("id","account")
el1 = chandao.findelement(loc1)

#判断显示元素
r1 = el1.is_displayed()
print(r1)  #返回bool值  True

#隐藏元素
loc2 = ("id","hiddenwin")
el2 = chandao.findelement(loc2)
r2 = el2.is_displayed()
print(r2)

#元素不存在
loc3 = ("id","XXX")
el3 = chandao.findelement(loc3)
r3 = el3.is_displayed()
print(r3)

