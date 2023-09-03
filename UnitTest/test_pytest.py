'''
Author: Misaki
Date: 2023-09-02 19:20:46
LastEditTime: 2023-09-02 19:44:22
LastEditors: Misaki
Description: 
'''

import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

@pytest.mark.parametrize(
    'search_key,expected',
    [
        ('abcd', 'abcd_百度搜索'),
        ('bbb', 'bbb_百度搜索')
    ]
)
def test_baidu_search(search_key, expected):
    driver = webdriver.Edge()
    driver.get('http://www.baidu.com')
    driver.implicitly_wait(10)
    
    driver.find_element(By.ID, 'kw').send_keys(search_key)
    driver.find_element(By.ID, 'su').click()
    sleep(3)
    
    web_title = driver.title
    assert expected == web_title
    
    driver.quit()
