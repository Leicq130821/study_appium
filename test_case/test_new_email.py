# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 19:58
# @Author  : LCQ
# @FileName: test_new_email.py

import pytest,allure
from page_object.new_email.new_email_page import NewEmailPage

@allure.feature('新邮件')
class TestNewEmail():

    @allure.story('新邮件：发送邮件')
    def test_send_email(self,login):
        self.new_email_page=NewEmailPage(login)
        self.new_email_page.send_email()

if __name__ == '__main__':
    pytest.main(['-s','-v'])