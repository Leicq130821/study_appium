# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 15:08
# @Author  : LCQ
# @FileName: conftest.py

from common.init_app import init_app
from utils.log import get_logger
from common.base_operate import BaseOperate
import pytest,allure,time

# 登录
@pytest.fixture(scope='session')
def login():
    driver=init_app()
    global base_operate
    logger=get_logger(time.strftime('登录：%Y%m%d %Y%m%d %H.%M'))
    base_operate=BaseOperate(driver,logger)
    base_operate.click_element(('允许','//*[@text="允许"]'))
    base_operate.element_send_keys(('账号输入框','//android.widget.EditText'),'lcq_ui_test')
    base_operate.element_send_keys(('密码输入框','//android.widget.EditText'),'123456',index=1)
    base_operate.click_element(('登录','//*[@text="登录"]'))
    return driver

# 用例失败添加截图
@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        with allure.step('用例失败截图'):
            base_operate.get_screenshot()

# 关闭浏览器
@pytest.fixture(scope="session",autouse=True)
def quitDriver(login):
    yield
    driver=login
    driver.quit()

# 用例名称中文编码格式
def pytest_collection_modifyitems(items):
    for item in items:
        item.name=item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid=item.nodeid.encode("utf-8").decode("unicode_escape")