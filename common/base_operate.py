# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 16:59
# @Author  : LCQ
# @FileName: base_operate.py

import time,os,allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.public_locator import PublicLocator

class BaseOperate(PublicLocator):

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver=self.driver,timeout=30,poll_frequency=0.5)
        self.project_dir=os.path.dirname(os.path.dirname(__file__))
        self.config_path=os.path.join(self.project_dir,'config')
        self.download_path=os.path.join(self.project_dir,'download')
        self.file_path=os.path.join(self.project_dir,'file')

    # 查找可交互的元素
    def findVisibleElement(self,locator,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,locator)))
            else:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,locator)))[index]
        except Exception:
            assert False,'查找元素失败，请检查！locator表达式为：%s'%str(locator)

    # 查找加载到XML里面的元素
    def findPresenceElement(self,locator,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,locator)))
            else:
                return self.wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,locator)))[index]
        except Exception:
            assert False,'查找元素失败，请检查！locator表达式为：%s'%str(locator)

    # 判断元素是否存在
    def judgeElementExist(self,locator,time=5,type=1):
        wait=WebDriverWait(self.driver,time,0.5)
        try:
            if type==1:
                wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,locator)))
            else:
                wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,locator)))
        except Exception:
            return False
        else:
            return True

    # 滚动元素到指定位置
    def scrollElement(self,locator,index=0,type=1):
        if type==1:
            element=self.findVisibleElement(locator,index)
        else:
            element=self.findPresenceElement(locator,index)
        JS="arguments[0].scrollIntoView();"
        self.driver.execute_script(JS,element)

    # 点击元素
    def clickElement(self,locator,index=0,scroll=1):
        if scroll:
            self.scrollElement(locator,index)
            self.sleep(0.5)
        self.findVisibleElement(locator,index).click()

    # 输入内容
    def elementSendKeys(self,locator,key,clear=1,scroll=1,index=0):
        if scroll:
            self.scrollElement(locator,index)
            self.sleep(0.5)
        if clear:
            self.findVisibleElement(locator,index).clear()
            self.sleep(0.5)
        self.findVisibleElement(locator,index).send_keys(str(key))

    # 获取元素文本
    def getElementText(self,locator,index=0,scroll=0,type=1):
        if index==-1:
            if type==1:
                elements=self.findVisibleElement(locator,index)
            else:
                elements=self.findPresenceElement(locator,index)
            return [element.text for element in elements]
        else:
            if scroll:
                self.scrollElement(locator,index,type)
                self.sleep(0.5)
            if type==1:
                return self.findVisibleElement(locator,index).text
            else:
                return self.findPresenceElement(locator,index).text

    # 获取元素的属性
    def getElementAttribute(self,locator,attribute,index=0,type=1):
        if index==-1:
            if type==1:
                elements=self.findVisibleElement(locator,index)
            else:
                elements=self.findPresenceElement(locator,index)
            return [element.get_attribute(attribute) for element in elements]
        else:
            if type==1:
                element=self.findVisibleElement(locator,index)
            else:
                element=self.findPresenceElement(locator,index)
            return element.get_attribute(attribute)

    # 添加元素属性
    def addElementAttribute(self,locator,attribute,value,index=0,type=1):
        if type==1:
            element=self.findVisibleElement(locator,index)
        else:
            element=self.findPresenceElement(locator,index)
        self.driver.execute_script('arguments[0].%s=arguments[1]'%attribute,element,value)

    # 设置元素属性
    def setElementAttribute(self,locator,attribute,value,index=0,type=1):
        if type==1:
            element=self.findVisibleElement(locator,index)
        else:
            element=self.findPresenceElement(locator,index)
        self.driver.execute_script('arguments[0].setAttribute(arguments[1],arguments[2])',element,attribute,value)

    # 删除元素属性
    def delElementAttribute(self,locator,attribute,index=0,type=1):
        if type==1:
            element=self.findVisibleElement(locator,index)
        else:
            element=self.findPresenceElement(locator,index)
        self.driver.execute_script('arguments[0].removeAttribute(arguments[1])',element,attribute)

    # 获取元素的CSS样式
    def getElementCSS(self,locator,CSS,index=0,type=1):
        if index==-1:
            if type==1:
                elements=self.findVisibleElement(locator,index)
            else:
                elements=self.findPresenceElement(locator,index)
            return [element.value_of_css_property(CSS) for element in elements]
        else:
            if type==1:
                element=self.findVisibleElement(locator,index)
            else:
                element=self.findPresenceElement(locator,index)
            return element.value_of_css_property(CSS)

    # 切换frame
    def switchFrame(self,locator,index=0,type=1):
        if type==1:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.findVisibleElement(locator,index)))
        else:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.findPresenceElement(locator,index)))

    # 切回父frame
    def switchParentFrame(self):
        self.driver.switch_to.parent_frame()

    # 切回主文档
    def switchMainPage(self):
        self.driver.switch_to.default_content()

    # 执行JS
    def executeJS(self,JS):
        self.driver.execute_script(JS)

    # 等待
    def sleep(self,s):
        time.sleep(s)

    # 截图
    def getScreenshot(self,title='截图'):
        allure.attach(self.driver.get_screenshot_as_png(),title,allure.attachment_type.PNG)