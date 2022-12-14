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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
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
        self.action=ActionChains(self.driver,duration=1000)

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
            self.log_error('查找元素失败，请检查！xpath表达式为：%s'%xpath)
            assert False,'查找元素失败，请检查！xpath表达式为：%s'%xpath

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

    # 查找加载到XML里面的元素
    def find_presence_element(self,xpath,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,xpath)))
            else:
                return self.wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,xpath)))[index]
        except Exception:
            assert False,'查找元素失败，请检查！xpath表达式为：%s'%xpath

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

    # 点击元素
    def click_element(self,xpath,index=0):
        self.find_visible_element(xpath,index).click()

    # 输入内容
    def element_send_keys(self,xpath,key,clear=1,index=0):
        if clear:
            self.find_visible_element(xpath,index).clear()
            self.sleep(0.5)
        self.find_visible_element(xpath,index).send_keys(str(key))

    # 获取元素文本
    def get_element_text(self,xpath,index=0,type=1):
        if index==-1:
            if type==1:
                elements=self.find_visible_element(xpath,index)
            else:
                elements=self.find_presence_element(xpath,index)
            return [element.text for element in elements]
        else:
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

    # 切换环境
    def switch_context(self,index):
        contexts=self.driver.contexts
        self.driver.switch_to.context(contexts[index])

    # 执行JS
    def execute_js(self,js):
        self.driver.execute_script(js)

    # 等待
    def sleep(self,s):
        time.sleep(s)

    # 截图
    def get_screenshot(self,title='截图'):
        allure.attach(self.driver.get_screenshot_as_png(),title,allure.attachment_type.PNG)

    '''
    滑屏操作
    滑屏操作需要四个坐标参数：start_x（开始滑时x坐标），end_x（结束滑时x坐标），
                              start_y（开始滑时y坐标），end_y（结束滑时y坐标）。
    先获取到屏幕的尺寸，然后利用比例确定x,y数值，这种是万能方法。
    '''
    def swipe_screen(self,direction='left',duration=1000):
        try:
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
        except Exception as error:
            self.log_error('滑屏操作失败，错误信息为：%s，请检查！'%error)
            assert False,'滑屏操作失败，错误信息为：%s，请检查！'%error

    # 缩放操作
    def zoom(self,type):
        self.action.w3c_actions.devices=[]
        finger_one=self.action.w3c_actions.add_pointer_input('touch','finger_one')
        finger_two=self.action.w3c_actions.add_pointer_input('touch','finger_two')
        window_size=self.driver.get_window_size()
        x=window_size['width']
        y=window_size['height']
        # 放大
        if type=='in':
            finger_one.create_pointer_move(x=0.4*x,y=0.4*y)
            finger_two.create_pointer_move(x=0.6*x,y=0.6*y)
        # 缩小
        else:
            finger_one.create_pointer_move(x=0.2*x,y=0.2*y)
            finger_two.create_pointer_move(x=0.8*x,y=0.8*y)
        finger_one.create_pointer_down(x=MouseButton.LEFT)
        finger_two.create_pointer_down(x=MouseButton.LEFT)
        if type=='in':
            finger_one.create_pointer_move(x=0.2*x,y=0.2*y)
            finger_two.create_pointer_move(x=0.8*x,y=0.8*y)
        else:
            finger_one.create_pointer_move(x=0.4*x,y=0.4*y)
            finger_two.create_pointer_move(x=0.6*x,y=0.6*y)
        finger_one.create_pointer_up(MouseButton.LEFT)
        finger_two.create_pointer_up(MouseButton.LEFT)
        self.action.perform()

    # 触屏滑动
    def touch_screen_swipe(self,*point_tuple):
        self.action.w3c_actions.devices=[]
        finger=self.action.w3c_actions.add_pointer_input('touch','finger')
        finger.create_pointer_move(x=point_tuple[0]['x'],y=point_tuple[0]['y'])
        finger.create_pointer_down(x=MouseButton.LEFT)
        for point in point_tuple[1:]:
            finger.create_pointer_move(x=point['x'],y=point['y'])
            finger.create_pause(1)
        finger.create_pointer_up(MouseButton.LEFT)
        self.action.perform()

    # 移动到元素
    def move_to_element(self,xpath):
        self.action.w3c_actions.devices=[]
        finger=self.action.w3c_actions.add_pointer_input('touch','finger')
        finger.create_pointer_move(origin=self.find_visible_element(xpath))
        self.action.perform()

    # 移动到坐标
    def move_to_coord(self,x,y):
        self.action.w3c_actions.devices=[]
        finger=self.action.w3c_actions.add_pointer_input('touch','finger')
        finger.create_pointer_move(x=x,y=y)
        self.action.perform()

    # 长按
    def long_press(self,xpath,duration):
        self.action.w3c_actions.devices=[]
        finger=self.action.w3c_actions.add_pointer_input('touch','finger')
        finger.create_pointer_move(origin=self.find_visible_element(xpath))
        finger.create_pointer_down(x=MouseButton.LEFT)
        finger.create_pause(duration)
        finger.create_pointer_up(MouseButton.LEFT)
        self.action.perform()

    '''
    先移动到一个元素，按下，然后移动至另外一个元素后释放，存在惯性滑动。
    '''
    def scroll(self,xpath_one,xpath_two,duration=600):
        origin_element=self.find_visible_element(xpath_one)
        destination_element=self.find_visible_element(xpath_two)
        self.driver.scroll(origin_element,destination_element,duration=duration)

    '''
    先移动到一个元素，按下，然后移动至另外一个元素后释放，不存在惯性滑动。
    '''
    def drag_and_drop(self,xpath_one,xpath_two):
        origin_element=self.find_visible_element(xpath_one)
        destination_element=self.find_visible_element(xpath_two)
        self.driver.drag_and_drop(origin_element,destination_element)

    '''
    设置设备网络
    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6
    '''
    def device_network(self,type):
        self.driver.set_network_connection(type)

    '''
    设备按键
    '''
    def device_press(self,code):
        self.driver.press_keycode(code)