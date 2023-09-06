'''
Author: Misaki
Date: 2023-09-06 22:02:54
LastEditTime: 2023-09-06 22:04:48
LastEditors: Misaki
Description: 
'''

# -*- coding: utf-8 -*-
# @File : yaml_util.py
import yaml

class Yaml_Util:
    def __init__(self, yaml_path):
        '''
        初始化时 传入yaml文件路径
        :param yaml_file:
        '''
        self.yaml_path = yaml_path

    def yaml_read(self):
        '''
        yaml文件的读取
        :return:
        '''
        with open(self.yaml_path, 'r', encoding='utf-8') as f:
            ym = yaml.load(f, Loader=yaml.FullLoader)
        return ym