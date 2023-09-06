'''
Author: Misaki
Date: 2023-09-03 17:10:41
LastEditTime: 2023-09-05 16:45:33
LastEditors: Misaki
Description: 
'''
from re import search
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class MBugIndex(BasePage):
    index_url = 'http://127.0.0.1:8000/login/'
    user_input = (By.ID, 'id_username')
    password_input = (By.ID, 'id_password')
    code_input = (By.ID, 'id_code')
    button = (By.ID, 'btnSubmit')

    down_button = (By.CSS_SELECTOR, '#bs-example-navbar-collapse-1 > ul.nav.navbar-nav.navbar-right > li > a')
    logout_button = (By.XPATH, '/html/body/nav/div/div[2]/ul[2]/li/ul/li[3]/a')
    register_button = (By.XPATH, '/html/body/nav/div/div[2]/ul[2]/li[2]/a')

    
    def login(self, username, password, code):
        self.logger.info('[=====登录操作=====]')
        self.wait_eleVisable(self.user_input, model="用户名框")
        self.wait_eleVisable(self.password_input, model="密码框")
        self.wait_eleVisable(self.code_input, model="验证码框")

        
        self.clean_inputText(self.user_input, model="用户名框")
        self.clean_inputText(self.password_input, model="密码框")
        self.clean_inputText(self.code_input, model="验证码框")

        self.input_text(self.user_input, username, model='用户名框')
        self.input_text(self.password_input, password, model='密码框')
        self.input_text(self.code_input, code, model='验证码框')
        

        self.wait_eleVisable(self.button, model="登录按钮")
        self.click_element(self.button, model = "登录按钮")

        self.driver.implicitly_wait(10)
        sleep(3)
    
    
    def logout(self):
        self.logger.info('[=====登出操作=====]')

        # 下拉框
        self.wait_eleVisable(self.down_button, model="下拉框")
        self.click_element(self.down_button, "下拉框")

        # 登出按钮
        self.wait_eleVisable(self.logout_button, model='登出按钮')
        self.click_element(self.logout_button, '登出按钮')
