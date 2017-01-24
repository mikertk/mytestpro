# coding=utf-8
import time
from selenium import webdriver


a = webdriver.Firefox()
a.get("https://www.baidu.com")
time.sleep(2)
a.quit()
