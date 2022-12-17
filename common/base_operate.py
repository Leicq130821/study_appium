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
from appium.webdriver.connectiontype import ConnectionType
from appium.webdriver.extensions.android.nativekey import AndroidKey

class BaseOperate(PublicLocator,CreateData,Log,OperateFile,ConnectionType,AndroidKey):

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
    查找可见的元素
    value-demo：//*[@resource-id="com.tal.kaoyan:id/kylogin_phone_input_phonenum"]
    value-demo：//android.widget.EditText
    value-demo：//*[@class="android.widget.EditText"]
    value-demo：//*[@text="请输入手机号"]
    value-demo：//*[@content-desc="登录账号"]
    '''
    def find_visible_element(self,locator,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,locator[1])))
            else:
                return self.wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,locator[1])))[index]
        except Exception:
            self.log_error('查找%s失败，请检查！xpath表达式为：%s'%(locator[0],locator[1]))
            assert False,'查找%s失败，请检查！xpath表达式为：%s'%(locator[0],locator[1])

    # 查找加载到XML里面的元素
    def find_presence_element(self,locator,index=0):
        try:
            if index==-1:
                return self.wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,locator[1])))
            else:
                return self.wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,locator[1])))[index]
        except Exception:
            self.log_error('查找%s失败，请检查！xpath表达式为：%s'%(locator[0],locator[1]))
            assert False,'查找%s失败，请检查！xpath表达式为：%s'%(locator[0],locator[1])

    # 判断元素是否存在
    def judge_element_exist(self,locator,time=5,type=1):
        wait=WebDriverWait(self.driver,time,0.5)
        try:
            if type==1:
                wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,locator[1])))
            else:
                wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,locator[1])))
        except Exception:
            return False
        else:
            return True

    # 点击元素
    def click_element(self,locator,index=0):
        element=self.find_visible_element(locator,index)
        try:
            element.click()
            self.log_info('点击%s'%locator[0])
        except Exception as error:
            self.log_error('点击%s失败，请检查！错误信息为：%s' % (locator[0], str(error)))
            assert False, '点击%s失败，请检查！错误信息为：%s' % (locator[0], str(error))

    # 输入内容
    def element_send_keys(self,locator,key,index=0,clear=1):
        element=self.find_visible_element(locator,index)
        try:
            if clear:
                element.clear()
                self.sleep(0.2)
            element.send_keys(str(key))
            self.log_info('%s输入值：%s'%(locator[0],str(key)))
        except Exception as error:
            self.log_error('%s输入值失败，请检查！错误信息为：%s' % (locator[0],str(error)))
            assert False, '%s输入值失败，请检查！错误信息为：%s' % (locator[0],str(error))

    # 获取元素文本
    def get_element_text(self,locator,index=0,type=1):
        if index==-1:
            if type==1:
                elements=self.find_visible_element(locator,index)
            else:
                elements=self.find_presence_element(locator,index)
            try:
                text_list=[element.text for element in elements]
                self.log_info('获取%s文本'%locator[0])
                return text_list
            except Exception as error:
                self.log_error('获取%s文本失败，请检查！错误信息为：%s' % (locator[0], str(error)))
                assert False,'获取%s文本失败，请检查！错误信息为：%s' % (locator[0], str(error))
        else:
            if type==1:
                element=self.find_visible_element(locator,index).text
            else:
                element=self.find_presence_element(locator,index).text
            try:
                text=element.text
                self.log_info('获取%s文本'%locator[0])
                return text
            except Exception as error:
                self.log_error('获取%s文本失败，请检查！错误信息为：%s' % (locator[0], str(error)))
                assert False,'获取%s文本失败，请检查！错误信息为：%s' % (locator[0], str(error))

    # 获取元素的属性
    def get_element_attribute(self,locator,attribute,index=0,type=1):
        if index==-1:
            if type==1:
                elements=self.find_visible_element(locator,index)
            else:
                elements=self.find_presence_element(locator,index)
            try:
                attribute_value_list=[element.get_attribute(attribute) for element in elements]
                self.log_info('获取%s的%s'%(locator[0],attribute))
                return attribute_value_list
            except Exception as error:
                self.log_error('获取%s的%s，请检查！错误信息为：%s' % (locator[0],attribute,str(error)))
                assert False,'获取%s的%s，请检查！错误信息为：%s' % (locator[0],attribute,str(error))
        else:
            if type==1:
                element=self.find_visible_element(locator,index)
            else:
                element=self.find_presence_element(locator,index)
            try:
                attribute_value=element.get_attribute(attribute)
                self.log_info('获取%s的%s' % (locator[0],attribute))
                return attribute_value
            except Exception as error:
                self.log_error('获取%s的%s，请检查！错误信息为：%s' % (locator[0],attribute,str(error)))
                assert False,'获取%s的%s，请检查！错误信息为：%s' % (locator[0],attribute,str(error))

    # 切换环境
    def switch_context(self,index):
        try:
            contexts=self.driver.contexts
            self.driver.switch_to.context(contexts[index])
            self.log_info('切换环境')
        except Exception as error:
            self.log_error('切换环境失败，请检查！错误信息为：%s' % str(error))
            assert False,'切换环境失败，请检查！错误信息为：%s' % str(error)

    # 执行JS
    def execute_js(self,js):
        try:
            self.driver.execute_script(js)
            self.log_info('执行js:%s'%js)
        except Exception as error:
            self.log_error('执行js:%s失败，请检查！错误信息为：%s' % (js,str(error)))
            assert False,'执行js:%s失败，请检查！错误信息为：%s' % (js,str(error))
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
        __swipe_dict={'up':'向上滑动屏幕',
                      'down':'向下滑动屏幕',
                      'left':'向左滑动屏幕',
                      'right':'向右滑动屏幕'}
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
            self.log_info(__swipe_dict[duration])
        except Exception as error:
            self.log_error('%s失败，错误信息为：%s，请检查！'%(__swipe_dict[duration],error))
            assert False,'%s失败，错误信息为：%s，请检查！'%(__swipe_dict[duration],error)

    # 缩放操作
    def zoom(self,type):
        __zoom_dict = {'in': '缩小',
                       'out': '放大'}
        try:
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
            self.log_info(__zoom_dict[type])
        except Exception as error:
            self.log_error('%s失败，错误信息为：%s，请检查！'%(__zoom_dict[type],error))
            assert False,'%s失败，错误信息为：%s，请检查！'%(__zoom_dict[type],error)

    # 触屏滑动
    def touch_screen_swipe(self,*point_tuple):
        try:
            self.action.w3c_actions.devices=[]
            finger=self.action.w3c_actions.add_pointer_input('touch','finger')
            finger.create_pointer_move(x=point_tuple[0]['x'],y=point_tuple[0]['y'])
            finger.create_pointer_down(x=MouseButton.LEFT)
            for point in point_tuple[1:]:
                finger.create_pointer_move(x=point['x'],y=point['y'])
                finger.create_pause(1)
            finger.create_pointer_up(MouseButton.LEFT)
            self.action.perform()
            self.log_info('触屏滑动')
        except Exception as error:
            self.log_error('触屏滑动失败，错误信息为：%s，请检查！'%error)
            assert False,'触屏滑动失败，错误信息为：%s，请检查！'%error

    # 移动到元素
    def move_to_element(self,locator):
        element=self.find_visible_element(locator)
        try:
            self.action.w3c_actions.devices=[]
            finger=self.action.w3c_actions.add_pointer_input('touch','finger')
            finger.create_pointer_move(origin=element)
            self.action.perform()
            self.log_info('移动到%s'%locator[0])
        except Exception as error:
            self.log_error('移动到%s失败，错误信息为：%s，请检查！'%(locator[0],error))
            assert False,'移动到%s失败，错误信息为：%s，请检查！'%(locator[0],error)

    # 移动到坐标
    def move_to_coord(self,x,y):
        try:
            self.action.w3c_actions.devices=[]
            finger=self.action.w3c_actions.add_pointer_input('touch','finger')
            finger.create_pointer_move(x=x,y=y)
            self.action.perform()
            self.log_info('移动到坐标(%s,%s)' % (x,y))
        except Exception as error:
            self.log_error('移动到坐标(%s,%s)失败，错误信息为：%s，请检查！'%(x,y,error))
            assert False,'移动到坐标(%s,%s)失败，错误信息为：%s，请检查！'%(x,y,error)

    # 长按
    def long_press(self,locator,duration):
        element=self.find_visible_element(locator)
        try:
            self.action.w3c_actions.devices=[]
            finger=self.action.w3c_actions.add_pointer_input('touch','finger')
            finger.create_pointer_move(origin=element)
            finger.create_pointer_down(x=MouseButton.LEFT)
            finger.create_pause(duration)
            finger.create_pointer_up(MouseButton.LEFT)
            self.action.perform()
            self.log_info('长按%s' % locator[0])
        except Exception as error:
            self.log_error('长按%s失败，错误信息为：%s，请检查！'%(locator[0],error))
            assert False,'长按%s失败，错误信息为：%s，请检查！'%(locator[0],error)

    '''
    先移动到一个元素，按下，然后移动至另外一个元素后释放，存在惯性滑动。
    '''
    def scroll(self,origin_locator,destination_locator,duration=600):
        origin_element=self.find_visible_element(origin_locator)
        destination_element=self.find_visible_element(destination_locator)
        try:
            self.driver.scroll(origin_element,destination_element,duration=duration)
            self.log_info('从%s移动到%s'%(origin_locator[0],destination_locator[0]))
        except Exception as error:
            self.log_error('从%s移动到%s失败，错误信息为：%s，请检查！'%(origin_element[0],destination_element[0],error))
            assert False,'从%s移动到%s失败，错误信息为：%s，请检查！'%(origin_element[0],destination_element[0],error)

    '''
    先移动到一个元素，按下，然后移动至另外一个元素后释放，不存在惯性滑动。
    '''
    def drag_and_drop(self,origin_locator,destination_locator):
        origin_element=self.find_visible_element(origin_locator)
        destination_element=self.find_visible_element(destination_locator)
        try:
            self.driver.drag_and_drop(origin_element,destination_element)
            self.log_info('从%s移动到%s并释放'%(origin_locator[0],destination_locator[0]))
        except Exception as error:
            self.log_error('从%s移动到%s并释放失败，错误信息为：%s，请检查！'%(origin_element[0],destination_element[0],error))
            assert False,'从%s移动到%s并释放失败，错误信息为：%s，请检查！'%(origin_element[0],destination_element[0],error)

    '''
    设置设备网络：使用ConnectionType类来进行设置
    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6
    '''
    def device_network(self,type):
        try:
            self.driver.set_network_connection(type)
            self.log_info('设置网络')
        except Exception as error:
            self.log_error('设置网络失败，错误信息为：%s，请检查！'%error)
            assert False,'设置网络失败，错误信息为：%s，请检查！'%error

    '''
    设备按键：使用AndroidKey类来进行设置
    '''
    def press_keycode(self,code):
        try:
            self.driver.press_keycode(code)
            self.log_info('操作设备按键')
        except Exception as error:
            self.log_error('操作设备按键失败，错误信息为：%s，请检查！'%error)
            assert False,'操作设备按键失败，错误信息为：%s，请检查！'%error