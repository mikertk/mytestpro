# coding=utf-8
"""
Author: 虫师
Date: 2016/12/1
Method:
  * text：返回 alert/confirm/prompt 中的文字信息。
  * accept()：接受现有警告框。
  * dismiss()：解散现有警告框。
  * send_keys(keysToSend)： 发送文本至警告框。 keysToSend：将文本发送至警告框。
"""
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")

driver.find_element_by_link_text("设置").click()
driver.find_element_by_class_name("setpref").click()
time.sleep(1)

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(1)

# 接受警告框
driver.switch_to_alert().accept()

driver.quit()
