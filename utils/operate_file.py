# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 14:05
# @Author  : LCQ
# @FileName: operate_file.py

import yaml,xlrd

# 操作文件类
class OperateFile():

    # 读取yaml文件
    def read_yaml(self,path):
        with open(path, 'r', encoding='utf8') as file:
            data = yaml.load(stream=file, Loader=yaml.FullLoader)
            return data

    # 读取txt文件
    def read_txt(self,path):
        with open(path, 'r', encoding='utf8') as file:
            return file.readlines()

    # 读取excel文件
    def read_excel(self,path,sheet_index):
        with xlrd.open_workbook(path) as workbook:
            return workbook.sheet_by_index(sheet_index)