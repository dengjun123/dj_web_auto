#coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://bj.ganji.com/")

time.sleep(2)

driver.find_element_by_link_text("租房").click()
time.sleep(2)

#隐式等待  全局的
driver.implicitly_wait(10)  #10 最大的等待时间  定位元素的时候有作用

t = driver.title
print(t)

#切换到新的窗口 handle

#获取当前窗口的handle
h1 = driver.current_window_handle
print(h1)

#获取所有窗口的handle,返回list对象
all = driver.window_handles
print(all)

#获取新窗口的handle
new_handle = all[-1]
#切换到新窗口的handle上
driver.switch_to.window(new_handle)
t2 = driver.title
print(t2)

#回到第一个窗口
driver.switch_to.window(h1)

#关掉新开的窗口
driver.close()

