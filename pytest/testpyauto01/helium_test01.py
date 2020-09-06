"""
Author:wanglu,管理员用户
Time:2020/9/6，系统时间
"""
from helium import *
from selenium.webdriver import ChromeOptions

options=ChromeOptions()
options.add_argument("--start-maximized")
driver=start_chrome("www.baidu.com",options=options)