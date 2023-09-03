'''
Author: Misaki
Date: 2023-09-02 22:53:07
LastEditTime: 2023-09-02 23:12:51
LastEditors: Misaki
Description: 
'''

import os
import time
import pytest
from time import sleep
from selenium import webdriver

import sys

print(sys.path)

from PageObject.BaiduIndex import BaiduIndex

driver = webdriver.Edge()
baidu_index = BaiduIndex(driver)


@pytest.fixture(scope="class")
def init():
    # 打开浏览器,访问登录页面
    baidu_index.logger.info("\nWebDriver 正在初始化...")
    driver.get(baidu_index.baidu_index_url)
    baidu_index.logger.info(f"打开链接: {baidu_index.baidu_index_url}...")
    # 窗口最大化
    driver.maximize_window()
    # 隐式等待
    driver.implicitly_wait(10)
    baidu_index.logger.info("WebDriver 初始化完成！")
    yield
    driver.quit()
    baidu_index.logger.info("WebDriver 成功退出...")


class TestBaiduSearch:

    @pytest.mark.baidu_search
    @pytest.mark.parametrize("key_word", [
        "哈哈",
        "呵呵",
    ], )
    def test_search(self, init, key_word):
        # @pytest.mark.parametrize 参数化
        baidu_index.search_key(key_word)
        web_title = driver.title
        assert f"{key_word}_百度搜索" == web_title