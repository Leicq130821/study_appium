# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 19:12
# @Author  : LCQ
# @FileName: new_email_page.py

import allure,pytest,time
from appium.webdriver.extensions.android.nativekey import AndroidKey
from .new_email_locator import NewEmailLocator
from common.base_operate import BaseOperate

class NewEmailPage(BaseOperate,NewEmailLocator):

    def __init__(self,driver):
        super().__init__(driver)
        self.click_element(self.new_email)

    # 发送邮件
    def send_email(self):
        with allure.step('点击添加收件人图标，输入关键字搜索收件人。'):
            self.click_element(self.add_recipient_icon)
            self.element_send_keys(self.customer_contact_search_edit_text,'测试')
            self.driver.press_keycode(AndroidKey.ENTER)
            self.click_element(self.text_element.format('客户UI自动化测试 <testui@qq.com>'))
            self.get_screenshot()
        with allure.step('选择联系人，点击确定，将联系人带入到收件人中。'):
            self.click_element(self.confirm)
            added_recipients=self.get_element_text(self.added_recipient,-1)
            pytest.assume(added_recipients==['客户UI自动化测试<testui@qq.com>'],'添加的收件人不正确，请检查！')
            self.get_screenshot()
        with allure.step('填写邮件主题、正文，添加附件，进行发送邮件'):
            self.element_send_keys(self.subject_edit_text,'邮件主题：%s'%time.strftime('%H'))
            self.element_send_keys(self.email_content_edit_text,'邮件正文')