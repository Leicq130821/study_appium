# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 19:11
# @Author  : LCQ
# @FileName: new_email_locator.py

class NewEmailLocator():

    new_email=('新邮件','//*[normalize-space(@text)="新邮件"]')
    subject_edit_text=('主题编辑框','//*[normalize-space(@text)="主题 :"]/following-sibling::android.widget.EditText')
    add_recipient_icon=('添加收件人图标','//*[normalize-space(@text)="收件人 :"]//android.widget.Image')
    customer_contact_search_edit_text=('客户联系人搜索编辑框','//*[normalize-space(@text)="客户联系人"]/following-sibling::android.widget.EditText')
    customer_contact=('客户联系人','//*[@text="客户UI自动化测试 <testui@qq.com>"]')
    added_recipient=('添加的收件人','//android.widget.TextView[@text="收件人 :"]/following-sibling::*//android.widget.TextView')
    email_content_edit_text=('邮件正文编辑框','//*[@resource-id="cke_ckeditor"]//android.widget.EditText')
    email_attach_icon=('邮件附件图标','//*[@text="主题 :"]//android.widget.Image')
    attach_icon=('文件图标','//*[@text="文件"]')
    attach=('附件','//*[@text="icon.png"]')
    attach_is_processing=('文件正在处理中','//*[contains(@text,"文件正在处理中")]')
    send=('发送','//*[@text="发送"]')
    save_as_draft=('存为草稿','//*[contains(@text,"iKusSsimz")]')
    back_icon=('退回按钮','//*[@text="收件箱"]/../preceding-sibling::*')