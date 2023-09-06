'''
Author: Misaki
Date: 2023-09-03 16:15:30
LastEditTime: 2023-09-03 17:24:30
LastEditors: Misaki
Description: 
'''


import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


# 测试登录功能

@pytest.mark.login
def test_login_001():
    driver = webdriver.Edge()
    driver.get('http://127.0.0.1:8000/login/')
    driver.implicitly_wait(10)
    
    driver.find_element(By.ID, 'id_username').send_keys('13713676304')
    driver.find_element(By.ID, 'id_password').send_keys('12345678')
    driver.find_element(By.ID, 'id_code').send_keys('1234')
    driver.find_element(By.ID, 'btnSubmit').click()
    
    driver.implicitly_wait(10)
    sleep(3)
    
    name = driver.find_element(By.CSS_SELECTOR, '#bs-example-navbar-collapse-1 > ul.nav.navbar-nav.navbar-right > li > a').text
    assert name == 'misaki'

    



