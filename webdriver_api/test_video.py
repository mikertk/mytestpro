# coding=utf-8
"""
Author: 虫师
Date: 2016/12/1
Method:
  * execute_script() 调用JavaScript操作Web。
"""
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://videojs.com/")

# 播放视频
print "play"
driver.find_element_by_id("preview-player").click()

# 播放 15 秒钟
sleep(15)

# 暂停视频
print("stop")
driver.find_element_by_id("preview-player").click()
driver.quit()
