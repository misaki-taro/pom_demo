'''
Author: Misaki
Date: 2023-09-03 17:02:13
LastEditTime: 2023-09-06 22:31:52
LastEditors: Misaki
Description: 
'''


import os
import time
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

from PageObject.MBugIndex import MBugIndex
from PageObject.MBugProjectList import MBugProjectList
from Utils.Yaml import Yaml_Util

driver = webdriver.Edge()
mbug_index = MBugIndex(driver)
mbug_project_list = MBugProjectList(driver)


login_data_path = os.path.join(os.getcwd(), os.pardir, 'Data/login.yaml')
import pdb
pdb.set_trace()
login_data = Yaml_Util(login_data_path).yaml_read()

@pytest.fixture(scope='class')
def init():
    # 打开浏览器,访问登录页面
    mbug_index.logger.info("\nWebDriver 正在初始化...")
    driver.get(mbug_index.index_url)
    mbug_index.logger.info(f"打开链接: {mbug_index.index_url}...")
    # 窗口最大化
    driver.maximize_window()
    # 隐式等待
    driver.implicitly_wait(10)
    mbug_index.logger.info("WebDriver 初始化完成！")
    yield
    driver.quit()
    mbug_index.logger.info("WebDriver 成功退出...")

@pytest.mark.login
class TestLogin:
    
    @pytest.mark.login_success
    # @pytest.mark.parametrize('username,password,code',
    #                          [
    #                              ('13713676304', '12345678', '1234'),
    #                              ('597234156@qq.com', '12345678', '1234'),
    #                          ])
    @pytest.mark.parametrize('username,password,code', login_data)
    def test_login(self, init, username, password, code):
        mbug_index.login(username, password, code)
        result_loc = (By.CSS_SELECTOR, '#bs-example-navbar-collapse-1 > ul.nav.navbar-nav.navbar-right > li > a')
        cur_url = mbug_index.driver.current_url 
        assert cur_url == 'http://127.0.0.1:8000/index/' 

        # 点击退出
        mbug_index.logout()
        assert mbug_index.get_text(mbug_index.register_button, '注册按钮') == '注 册'
    
        driver.get(mbug_index.index_url)
        sleep(3)


@pytest.mark.project
class TestProject:
    
    @pytest.mark.parametrize('name,color,desc', 
                             [
                                 ('bb', '1', 'bbbb')
                             ])
    def test_project_create(self, init, name, color, desc):
        mbug_index.login('597234156@qq.com', '12345678', '1234')
        
        mbug_project_list.driver.get(mbug_project_list.url)
        mbug_project_list.create_project(name, color, desc)
        
        assert False
