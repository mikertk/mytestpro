# coding=utf-8
from selenium import webdriver


class Login():

    # 登录
    def __init__(self):
        pass

    def user_login(self, driver):
        driver.switch_to.frame('x-URS-iframe')
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("username")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_id("dologin").click()
        driver.switch_to.default_content()

    # 退出
    def user_logout(self, driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()
