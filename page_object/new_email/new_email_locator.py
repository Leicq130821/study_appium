# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 19:11
# @Author  : LCQ
# @FileName: new_email_locator.py

class NewEmailLocator():

    new_email=('新邮件','//*[normalize-space(@text)="新邮件"]')
    subject_edit_text=('主题编辑框','//*[normalize-space(@text)="主题 :"]/following-sibling::android.widget.EditText')
    add_recipient_icon=('添加收件人图标','//*[normalize-space(@text)="收件人 :"]//android.widget.Image')
    customer_contact_search_edit_text=('客户联系人搜索编辑框','//*[normalize-space(@text)="客户联系人"]/following-sibling::android.widget.EditText')
    added_recipient=('添加的收件人','//android.widget.TextView[@text="收件人 :"]/following-sibling::*//android.widget.TextView')
    email_content_edit_text=('邮件正文编辑框','//*[@resource-id="cke_ckeditor"]//android.widget.EditText')
    email_attach_icon=('邮件附件图标','//*[@text="主题 :"]//android.widget.Image')