# coding=utf-8
"""
Author: 虫师
Date: 2016/11/22
Method:
  * perform() 执行所有 ActionChains 中存储的行为；
  * context_click() 右击；
  * double_click() 双击；
  * drag_and_drop() 拖动；
  * move_to_element() 鼠标悬停。
"""
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 定位到要鼠标悬停的元素
above = driver.find_element_by_link_text("设置")
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()

# ...

'''
# 鼠标拖放操作
# 定位元素的原位置
element = driver.find_element_by_id("xx")
# 定位元素要移动到的目标位置
target = driver.find_element_by_id("xx")
ActionChains(driver).drag_and_drop(element, target).perform()
'''