# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 10:12
# @Author  : LCQ
# @FileName: init_app.py

import os
from appium import webdriver
from utils.operate_file import OperateFile

def init_app():
    # 加启动配置
    try:
        operate=OperateFile()
        project_dir=os.path.dirname(os.path.dirname(__file__))
        config_path=os.path.join(project_dir,'config')
        init_app_data=operate.read_yaml(os.path.join(config_path,'init_app.yaml'))
        driver=webdriver.Remote(init_app_data['url'],init_app_data['desired_caps'])
    except Exception as error:
        assert False,'初始化appium失败：%s'%error
    else:
        return driver