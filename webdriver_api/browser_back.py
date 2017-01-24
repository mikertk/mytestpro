# coding=utf-8
"""
Author: 虫师
Date: 2016/11/22
Method:
  *  back()     后退
  *  forward()  前进
  *  refresh()  刷新
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# 访问百度首页
first_url = 'https://www.baidu.com'
print("now access %s" % first_url)
driver.get(first_url)

# 访问百科页面
second_url = 'https://baike.baidu.com'
print("now access %s" % second_url)
driver.get(second_url)

# 返回（后退）到百度首页
print("back to %s " % first_url)
driver.back()

# 前进到百科页
print("forward to %s" % second_url)
driver.forward()

# 刷新当前页面
print "refresh page"
driver.refresh()

driver.quit()
