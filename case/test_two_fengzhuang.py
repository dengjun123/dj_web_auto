#coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://team.gm825.net/index.php?m=my&f=index")

# driver.find_element(By.ID,"account")
# driver.find_element_by_id(By.NAME,"password")
# driver.find_element(By.ID,"submit")

#定位器

def findelement(driver,locator,timeout=10,t=0.5):
    ele = WebDriverWait(driver,timeout,t).until(lambda x: x.find_element(*locator))
    #返回的是元素对象
    return ele

loc1 = (By.ID,"account")
loc2 = (By.NAME,"password")
loc3 = (By.ID,"submit")

findelement(driver,loc1).send_keys("dengjun")
findelement(driver,loc2).send_keys("oPe8*aVPWTySmSzo")
findelement(driver,loc3).click()

# ele1.send_keys("dengjun")
#
# ele2 = WebDriverWait(driver,5,1).until(lambda x: x.find_element_by_name("password"))
# print(ele2)
#
# ele2.send_keys("oPe8*aVPWTySmSzo")
#
# ele3 =  WebDriverWait(driver,5,1).until(lambda x: x.find_element_by_id("submit"))
# ele3.click()