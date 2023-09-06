'''
Author: Misaki
Date: 2023-09-03 17:10:41
LastEditTime: 2023-09-05 19:19:27
LastEditors: Misaki
Description: 
'''
from re import search
from Common.BasePage import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

class MBugProjectList(BasePage):
    url = 'http://127.0.0.1:8000/project/list/'
    create_button = (By.XPATH, '/html/body/div[1]/a')
    project_name = (By.ID, 'id_name')
    project_desc = (By.ID, 'id_desc')

    ele2model = {
        create_button: '新建项目',
        project_name: '项目名称',
        project_desc: '项目描述'
    }
    
    
    def create_project(self, name, color, desc):
        # 创建项目按钮
        self.wait_eleVisable(self.create_button, model=self.ele2model[self.create_button])
        self.click_element(self.create_button, self.ele2model[self.create_button])
        
        # 项目名
        self.wait_eleVisable(self.project_name, model=self.ele2model[self.project_name])
        self.input_text(self.project_name, name, self.ele2model[self.project_name])

        color_loc = (By.XPATH, '/html/body/div[3]/div[3]/div/div/div[2]/form/div[2]/div/label[1]/span')
        # color_loc = (By.ID, 'id_color_1')
        # color_ele = self.find_element(color_loc, '颜色1')
        # ActionChains(self.driver).move_to_element(color_ele).click().perform()
        # # self.driver.execute_script("arguments[0].click", color_ele)
        
        # color_ele = self.find_element(color_loc, '颜色1')
        # color_ele = self.find_element(color_loc, '颜色1')
        # # self.click_element(color_loc, '颜色{0}'.format(str(color)))

        color_option_xpath = "//label[@for='id_color_1']"  # 例如，选择第二个颜色
        color_option = self.driver.find_element(By.XPATH, color_option_xpath)
        color_option.click()

        projects_xpath = '//a[@class="title"]'
        projects = self.driver.find_element(By.XPATH, projects_xpath)
        
        print(projects)
        
        self.input_text(self.project_desc, desc, self.ele2model[self.project_desc])