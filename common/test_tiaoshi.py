from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.cnblogs.com/yoyoketang")

#滚动底部
time.sleep(4)
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)

time.sleep(3)
#滚到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)

time.sleep(3)
#滚动到元素出现的位置
ele = driver.find_element_by_link_text("新车")
driver.execute_script("arguments[0].scrollIntoView();",ele)