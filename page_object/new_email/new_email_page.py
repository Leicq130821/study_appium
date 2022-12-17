# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 19:12
# @Author  : LCQ
# @FileName: new_email_page.py

import allure,pytest,time
from .new_email_locator import NewEmailLocator
from common.base_operate import BaseOperate

class NewEmailPage(BaseOperate,NewEmailLocator):

    def __init__(self,driver,logger):
        super().__init__(driver,logger)
        self.click_element(self.new_email)

    # 发送邮件
    def send_email(self):
        with allure.step('点击添加收件人图标，输入关键字搜索收件人。'):
            self.click_element(self.add_recipient_icon)
            self.element_send_keys(self.customer_contact_search_edit_text,'测试')
            self.press_keycode(self.ENTER)
            self.click_element(self.customer_contact)
            self.get_screenshot()
        with allure.step('选择联系人，点击确定，将联系人带入到收件人中。'):
            self.click_element(self.confirm)
            added_recipients=self.get_element_text(self.added_recipient,-1)
            pytest.assume(added_recipients==['客户UI自动化测试<testui@qq.com>'],'添加的收件人不正确，请检查！')
            self.get_screenshot()
        with allure.step('填写邮件主题、正文，添加附件，进行发送邮件'):
            self.element_send_keys(self.subject_edit_text,'邮件主题：%s'%time.strftime('%Y%m%d %H.%M.%S'))
            self.element_send_keys(self.email_content_edit_text,'邮件正文')
            self.click_element(self.email_attach_icon)
            self.click_element(self.attach_icon)
            self.click_element(self.attach)
            while self.judge_element_exist(self.attach_is_processing,2):
                self.sleep(1)
            self.get_screenshot()
            self.click_element(self.send)
            self.click_element(self.back_icon)

    # 新邮件：存为草稿邮件
    def save_as_draft_email(self):
        with allure.step('点击添加收件人图标，输入关键字搜索收件人。'):
            self.click_element(self.add_recipient_icon)
            self.element_send_keys(self.customer_contact_search_edit_text,'测试')
            self.press_keycode(self.ENTER)
            self.click_element(self.customer_contact)
            self.get_screenshot()
        with allure.step('选择联系人，点击确定，将联系人带入到收件人中。'):
            self.click_element(self.confirm)
            added_recipients=self.get_element_text(self.added_recipient,-1)
            pytest.assume(added_recipients==['客户UI自动化测试<testui@qq.com>'],'添加的收件人不正确，请检查！')
            self.get_screenshot()
        with allure.step('填写邮件主题、正文，添加附件，存为草稿邮件'):
            self.element_send_keys(self.subject_edit_text,'邮件主题：%s'%time.strftime('%Y%m%d %H.%M.%S'))
            self.element_send_keys(self.email_content_edit_text,'邮件正文')
            self.click_element(self.email_attach_icon)
            self.click_element(self.attach_icon)
            self.click_element(self.attach)
            while self.judge_element_exist(self.attach_is_processing,2):
                self.sleep(1)
            self.get_screenshot()
            self.click_element(self.save_as_draft)