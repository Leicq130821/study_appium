# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 16:59
# @Author  : LCQ
# @FileName: base_operate.py

import time,os,allure
from common.log import Log
from utils.create_data import CreateData
from utils.operate_file import OperateFile
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.public_locator import PublicLocator

class BaseOperate(PublicLocator,CreateData,Log,OperateFile):

    def __init__(self,driver):
        super().__init__()
        super(CreateData,self).__init__()
        self.driver=driver
        self.wait=WebDriverWait(driver=self.driver,timeout=30,poll_frequency=0.5)
        self.project_dir=os.path.dirname(os.path.dirname(__file__))
        self.config_path=os.path.join(self.project_dir,'config')
        self.download_path=os.path.join(self.project_dir,'download')
        self.file_path=os.path.join(self.project_dir,'file')

    '''
    通过xpath定位元素，对应app的resource-id属性
    value-demo：//*[@resource-id="com.tal.kaoyan:id/kylogin_phone_input_phonenum"]
    value-demo：//android.widget.EditText
    value-demo：//*[@class="android.widget.EditText"]
    value-demo：//*[@text="请输入手机号"]
    value-demo：//*[@content-desc="登录账号"]
    '''
    def find_visible_element(self,xpath,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,xpath)))
            else:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,xpath)))[index]
        except Exception:
            assert False,'查找元素失败，请检查！xpath表达式为：%s'%str(xpath)

    '''
    通过id定位元素，对应app的resource-id属性
    value-demo：com.tal.kaoyan:id/kylogin_phone_input_phonenum
    '''
    def find_element_by_id(self,value,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.ID,value)))
            else:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.ID,value)))[index]
        except Exception:
            assert False,'查找元素失败，请检查！元素的id为：%s'%str(value)

    '''
    通过class定位元素，对应app的class属性
    value-demo：android.widget.EditText
    '''
    def find_element_by_class(self,value,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.CLASS_NAME,value)))
            else:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.CLASS_NAME,value)))[index]
        except Exception:
            assert False,'查找元素失败，请检查！元素的class为：%s'%str(value)

    '''
    通过描述定位元素，对应app的content-desc/description属性
    value-demo：登录账号
    '''
    def find_element_by_accessibility_id(self,value,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.ACCESSIBILITY_ID,value)))
            else:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.ACCESSIBILITY_ID,value)))[index]
        except Exception:
            assert False,'查找元素失败，请检查！元素的accessibility_id为：%s'%str(value)

    '''
    通过UiSelector类定位元素：https://www.apiref.com/android-zh/android/support/test/uiautomator/UiSelector.html
    value-demo：new UiSelector().className("android.widget.EditText").text("请输入手机号").resourceId("com.tal.kaoyan:id/kylogin_phone_input_phonenum").description("登录账号") 
    '''
    def find_element_by_android_uiautomator(self,value,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.ANDROID_UIAUTOMATOR,value)))
            else:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.ANDROID_UIAUTOMATOR,value)))[index]
        except Exception:
            assert False,'查找元素失败，请检查！元素的accessibility_id为：%s'%str(value)

    '''
    滑屏操作
    滑屏操作需要四个坐标参数：start_x（开始滑时x坐标），end_x（结束滑时x坐标），
                              start_y（开始滑时y坐标），end_y（结束滑时y坐标）。
    先获取到屏幕的尺寸，然后利用比例确定x,y数值，这种是万能方法。
    '''
    def swipe(self,direction='left',duration=1000):
        window_size=self.driver.get_window_size()
        x=window_size['width']
        y=window_size['height']
        if direction=='up':
            self.driver.swipe(start_x=0.5*x,start_y=0.8*y,end_x=0.5*x,end_y=0.2*y,duration=duration)
        elif direction=='down':
            self.driver.swipe(start_x=0.5*x,start_y=0.2*y,end_x=0.5*x,end_y=0.8*y,duration=duration)
        elif direction=='left':
            self.driver.swipe(start_x=0.8*x,start_y=0.5*y,end_x=0.2*x,end_y=0.5*y,duration=duration)
        elif direction=='right':
            self.driver.swipe(start_x=0.2*x,start_y=0.5*y,end_x=0.8*x,end_y=0.5*y,duration=duration)

    # 查找加载到XML里面的元素
    def find_presence_element(self,xpath,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,xpath)))
            else:
                return self.wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,xpath)))[index]
        except Exception:
            assert False,'查找元素失败，请检查！xpath表达式为：%s'%str(xpath)

    # 判断元素是否存在
    def judge_element_exist(self,xpath,time=5,type=1):
        wait=WebDriverWait(self.driver,time,0.5)
        try:
            if type==1:
                wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,xpath)))
            else:
                wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,xpath)))
        except Exception:
            return False
        else:
            return True

    # 滚动元素到指定位置
    def scroll_to_element(self,xpath,index=0,type=1):
        pass
        # if type==1:
        #     element=self.find_visible_element(xpath,index)
        # else:
        #     element=self.find_visible_element(xpath,index)
        # JS="arguments[0].scrollIntoView();"
        # self.driver.execute_script(JS,element)

    # 点击元素
    def click_element(self,xpath,index=0,scroll=1):
        if scroll:
            self.scroll_to_element(xpath,index)
            self.sleep(0.5)
        self.find_visible_element(xpath,index).click()

    # 输入内容
    def element_send_keys(self,xpath,key,clear=1,scroll=1,index=0):
        if scroll:
            self.scroll_to_element(xpath,index)
            self.sleep(0.5)
        if clear:
            self.find_visible_element(xpath,index).clear()
            self.sleep(0.5)
        self.find_visible_element(xpath,index).send_keys(str(key))

    # 获取元素文本
    def get_element_text(self,xpath,index=0,scroll=0,type=1):
        if index==-1:
            if type==1:
                elements=self.find_visible_element(xpath,index)
            else:
                elements=self.find_presence_element(xpath,index)
            return [element.text for element in elements]
        else:
            if scroll:
                self.scroll_to_element(xpath,index,type)
                self.sleep(0.5)
            if type==1:
                return self.find_visible_element(xpath,index).text
            else:
                return self.find_presence_element(xpath,index).text

    # 获取元素的属性
    def get_element_attribute(self,xpath,attribute,index=0,type=1):
        if index==-1:
            if type==1:
                elements=self.find_visible_element(xpath,index)
            else:
                elements=self.find_presence_element(xpath,index)
            return [element.get_attribute(attribute) for element in elements]
        else:
            if type==1:
                element=self.find_visible_element(xpath,index)
            else:
                element=self.find_presence_element(xpath,index)
            return element.get_attribute(attribute)

    # 添加元素属性
    def element_add_attribute(self,xpath,attribute,value,index=0,type=1):
        if type==1:
            element=self.find_visible_element(xpath,index)
        else:
            element=self.find_presence_element(xpath,index)
        self.driver.execute_script('arguments[0].%s=arguments[1]'%attribute,element,value)

    # 设置元素属性
    def element_set_attribute(self,xpath,attribute,value,index=0,type=1):
        if type==1:
            element=self.find_visible_element(xpath,index)
        else:
            element=self.find_presence_element(xpath,index)
        self.driver.execute_script('arguments[0].setAttribute(arguments[1],arguments[2])',element,attribute,value)

    # 删除元素属性
    def element_del_attribute(self,xpath,attribute,index=0,type=1):
        if type==1:
            element=self.find_visible_element(xpath,index)
        else:
            element=self.find_presence_element(xpath,index)
        self.driver.execute_script('arguments[0].removeAttribute(arguments[1])',element,attribute)

    # 获取元素的CSS样式
    def get_element_css(self,xpath,CSS,index=0,type=1):
        if index==-1:
            if type==1:
                elements=self.find_visible_element(xpath,index)
            else:
                elements=self.find_presence_element(xpath,index)
            return [element.value_of_css_property(CSS) for element in elements]
        else:
            if type==1:
                element=self.find_visible_element(xpath,index)
            else:
                element=self.find_presence_element(xpath,index)
            return element.value_of_css_property(CSS)

    # 切换frame
    def switch_frame(self,xpath,index=0,type=1):
        if type==1:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.find_visible_element(xpath,index)))
        else:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.find_presence_element(xpath,index)))

    # 切回父frame
    def switch_parent_frame(self):
        self.driver.switch_to.parent_frame()

    # 切回主文档
    def switch_main_page(self):
        self.driver.switch_to.default_content()

    # 执行JS
    def execute_js(self,JS):
        self.driver.execute_script(JS)

    # 等待
    def sleep(self,s):
        time.sleep(s)

    # 截图
    def get_screenshot(self,title='截图'):
        allure.attach(self.driver.get_screenshot_as_png(),title,allure.attachment_type.PNG)