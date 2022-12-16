# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 19:11
# @Author  : LCQ
# @FileName: new_email_locator.py

from common.public_locator import PublicLocator

class NewEmailLocator(PublicLocator):

    # 新邮件
    new_email=PublicLocator.text_element.format('新邮件')
    # 主题编辑框
    subject_edit_text=PublicLocator.follow_text_edit_text.format('主题 :')
    # 添加收件人图标
    add_recipient_icon=PublicLocator.down_text_image.format('收件人 :')
    # 客户联系人搜索编辑框
    customer_contact_search_edit_text=PublicLocator.follow_text_edit_text.format('客户联系人')
    # 添加的收件人
    added_recipient='//android.widget.TextView[@text="收件人 :"]/following-sibling::*//android.widget.TextView'
    # 邮件正文编辑框
    email_content_edit_text='//*[@resource-id="cke_ckeditor"]//android.widget.EditText'