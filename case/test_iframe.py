#coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://mail.126.com/")

time.sleep(2)
# driver.switch_to.frame("x-URS-iframe")
# driver.find_element_by_name("email").send_keys("yoyoyo")

#如果没有ID、name就把他当成元素
frame = driver.find_elements_by_tag_name("iframe")[0]
driver.switch_to.frame(frame)
driver.find_element_by_name("email").send_keys("yoyoyo")

#如果多个iframe，就切换多次
# driver.switch_to.frame("第一次切")
# driver.switch_to.frame("第二次切")
#切完之后再定位


#通过索引定位
driver.switch_to.frame(2)  #iframe  导航栏索引定位

#切换到上一层，相当于back
driver.switch_to.parent_frame()


#操作完后切回来,直接回到主页面，相当于home
driver.switch_to.default_content()
