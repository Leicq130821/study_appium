# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 9:10
# @Author  : LCQ
# @FileName: public_locator.py

class PublicLocator():

    # 根据文本查找元素
    text_element='//*[normalize-space(@text)="{}"]'
    # 根据包含文本查找元素
    contains_text_element='//*[contains(@text,"{}")]'
    # 根据id查找元素
    id_element='//*[@resource-id="{}"]'
    # 根据content-desc/description查找元素
    content_element='//*[normalize-space(@content-desc)="{}"]'
    # 根据包含content-desc/description查找元素
    contains_content_element='//*[contains(@content-desc,"{}")]'
    # 根据class查找元素
    class_element='//{}'
    # 根据包含class查找元素
    contains_class_element='//*[contains(@class,"{}")]'
    # 跟着文本的编辑框
    follow_text_edit_text='//*[normalize-space(@text)="{}"]/following-sibling::android.widget.EditText'
    # 文本下的图片
    down_text_image='//*[normalize-space(@text)="{}"]//android.widget.Image'
    # 取消
    cancel='//*[normalize-space(@text)="取消"]'
    # 确定
    confirm='//*[normalize-space(@text)="确定"]'