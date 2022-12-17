# -*- coding: utf-8 -*-
# @Time    : 2022/11/22 20:19
# @Author  : LCQ
# @FileName: log.py

import os,logging

def get_logger(name):
    '''
    简单初始化
    fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
    log_file=os.path.join(os.path.dirname(os.path.dirname(__file__)),'logs','%s.log'%time.strftime('%Y-%m-%d'))
    logging.basicConfig(level=logging.INFO,format=fmt,filename=log_file,filemode='a')    # level级别默认为warning
    '''
    # 创建日志器
    loggger=logging.getLogger(name)
    # 设置日志级别
    loggger.setLevel(logging.INFO)
    # 创建控制台
    console_handler=logging.StreamHandler()
    # 创建文件控制器
    log_file=os.path.join(os.path.dirname(os.path.dirname(__file__)),'logs',name)
    file_handler=logging.FileHandler(log_file+'.log', encoding='utf-8')
    # 创建格式器
    fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
    formatter=logging.Formatter(fmt)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    loggger.addHandler(console_handler)
    loggger.addHandler(file_handler)
    return loggger