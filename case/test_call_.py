from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from common.base import Base

driver = webdriver.Firefox()
# driver.get("https://www.baidu.com")
# #期望结果与实际结果相等
# r1 = EC.title_is("百度一下，你就知道")(driver)
# print (r1)
#
# #包含在实际结果中
# r2 = EC.title_contains("百度一下")(driver)
# print(r2)

driver.get("http://team.gm825.net/index.php?m=my&f=index")

# loc1 = ("xpath",".//*[text()='忘记密码']")
# r1 = EC.presence_of_element_located(loc1)(driver)
# print(r1)  #返回WebElement元素对象

# time.sleep(3)
# loc2 = ("xpath",".//*[@id='login-form']/form/table/tbody/tr[4]/td")
# r2 = EC.text_to_be_present_in_element(loc2)(driver)
# print(r2)

loc2 = ("xpath",".//*[@id='login-form']/form/table/tbody/tr[4]/td")

chandao = Base(driver)
r1 = chandao.is_title("用户登录-禅道")
print(r1)
r2 = chandao.is_title_contains("11禅道")
print(r2)
r3 = chandao.is_text_in_element(loc2,"忘记密码")
print(r3)


# class hello():
#
#     def __init__(self,a):
#         print(a)
#
#
#     def __call__(self,b):
#         print(b)
#
#
#
#
# if __name__ == "__main__":
#     h = hello("hello")
#     h("hello world")