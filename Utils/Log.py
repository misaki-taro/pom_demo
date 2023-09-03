'''
Author: Misaki
Date: 2023-09-02 19:56:05
LastEditTime: 2023-09-02 20:04:49
LastEditors: Misaki
Description: 
'''

from cmath import log
import logging
import time
import os

class Log(object):
    
    def __init__(self, logger=None) -> None:
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入指定文件
        """

        cur_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.join(os.path.dirname(cur_path), f'Logs')
        if not os.path.exists(log_path):
            os.mkdir(log_path)
            
        now_date = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
        now_log_path = os.path.join(log_path, f'{now_date}')
        if not os.path.exists(now_log_path):
            os.mkdir(now_log_path)
        
        # Create a logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        
        # 创建一个handler，用于写入日志文件
        now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
        log_name = os.path.join(now_log_path, f'{now_time}.log')
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 创建一个handler，用于控制台输出
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # 定义handler输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s %(filename)s [line:%(lineno)d]: %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    
    def get_log(self):
        return self.logger


