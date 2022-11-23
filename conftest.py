# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 15:08
# @Author  : LCQ
# @FileName: conftest.py

from common.init_app import init_driver
from selenium.webdriver.support import expected_conditions as EC
from common.base_operate import BaseOperate
import pytest,time,allure

# 登录
@pytest.fixture(scope='session')
def login():
    global driver
    driver=init_driver()
    operate = BaseOperate(driver)
    trade = operate.getElementText(operate.href_link.format('https://trade.joinf.com'))
    if trade == 'Trade':
        operate.clickElement(operate.id_div.format('switchGroup'))
        operate.clickElement(operate.switch_language.format('zh'))
    return driver

# 自动刷新
@pytest.fixture(scope="function",autouse=True)
def autoRefresh():
    driver.refresh()
    # 判断是否有弹窗
    time.sleep(1)
    alert=EC.alert_is_present()(driver)
    if alert:
        alert.accept()
    time.sleep(5)

# 用例失败添加截图
@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        with allure.step('用例失败截图'):
            allure.attach(driver.get_screenshot_as_png(),"截图",allure.attachment_type.PNG)

# 关闭浏览器
@pytest.fixture(scope="session",autouse=True)
def quitDriver():
    yield
    driver.quit()

# 用例名称中文编码格式
def pytest_collection_modifyitems(items):
    for item in items:
        item.name=item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid=item.nodeid.encode("utf-8").decode("unicode_escape")