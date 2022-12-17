# -*- coding: utf-8 -*-
# @Time    : 2022/11/22 20:19
# @Author  : LCQ
# @FileName: log.py

import os,logging,time

class Log():

    # 初始化
    def __init__(self):
        '''
        简单初始化
        fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
        log_file=os.path.join(os.path.dirname(os.path.dirname(__file__)),'logs','%s.log'%time.strftime('%Y-%m-%d'))
        logging.basicConfig(level=logging.INFO,format=fmt,filename=log_file,filemode='a')    # level级别默认为warning
        '''
        # 创建日志器
        self.loggger=logging.getLogger()
        # 设置日志级别
        self.loggger.setLevel(logging.INFO)
        # 创建控制台
        console_handler=logging.StreamHandler()
        # 创建文件控制器
        file_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs','%s.log' % time.strftime('%Y-%m-%d %H.%M,%S'))
        file_handler=logging.FileHandler(file_path, encoding='utf-8')
        # 创建格式器
        fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
        formatter=logging.Formatter(fmt)
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        self.loggger.addHandler(console_handler)
        self.loggger.addHandler(file_handler)

    # 消息级别
    def log_info(self,message):
        self.loggger.info(message)

    # 警告级别
    def log_warning(self,message):
        self.loggger.warning(message)

    # 错误级别
    def log_error(self,message):
        self.loggger.error(message)

    # 崩坏级别
    def log_critical(self,message):
        self.loggger.critical(message)