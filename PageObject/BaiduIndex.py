'''
Author: Misaki
Date: 2023-09-02 22:39:42
LastEditTime: 2023-09-02 23:16:40
LastEditors: Misaki
Description: 
'''

from re import search
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class BaiduIndex(BasePage):
    """每一个函数就是对该页面的一系列逻辑操作

    Args:
        BasePage (_type_): _description_
    """

    baidu_index_url = 'http://www.baidu.com'
    search_input = (By.ID, 'kw')
    search_button = (By.ID, 'su')

    def search_key(self, sk):
        self.logger.info("【===搜索操作===】")
        # 等待用户名文本框元素出现
        self.wait_eleVisable(self.search_input, model='搜索框')
        # 输入内容
        self.input_text(self.search_input, "阿崔", model="搜索框")
        # 清除文本框内容
        self.clean_inputText(self.search_input, model='搜索框')
        # 输入用户名
        self.input_text(self.search_input, text=sk, model='搜索框')
        # 等待搜索按钮出现
        self.wait_eleVisable(self.search_button, model='"百度一下"搜索按钮')
        # 点击搜索按钮
        self.click_element(self.search_button, model='"百度一下"搜索按钮')
        # 搜索后等待界面加载完成
        self.driver.implicitly_wait(10)
        sleep(3)
        

    
