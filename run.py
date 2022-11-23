# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 15:08
# @Author  : LCQ
# @FileName: run.py

import pytest,os
if __name__ == '__main__':
    allure_path=os.path.join(os.path.dirname(__file__),'allure_report')
    pytest.main()
    os.system('allure serve %s'%allure_path)