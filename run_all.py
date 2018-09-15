#coding=utf-8

import unittest
from common import HTMLTestRunner_cn

#用例的存放路径
casePath = "D:\\web_auto\\case"
rule = "test_login_public.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

#报告路径
reportpath = "D:\\web_auto\\report\\"+"result.html"

fp = open(reportpath,"wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                            title = "登录测试用例",
                                            description = "自动化测试执行情况",
                                            retry = 1)  #错误重跑机制
runner.run(discover)
fp.close()

