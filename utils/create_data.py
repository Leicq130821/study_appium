# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 14:12
# @Author  : LCQ
# @FileName: create_data.py

import random
from faker import Faker
from random_words import RandomWords

# 生成数据
class CreateData():

    def __init__(self):
        self.rw = RandomWords()
        self.fake = Faker(locale='zh_CN')
    # 文本
    def text(self,num=10):
        return self.fake.text(max_nb_chars=num).strip('.')
    # 整数
    @property
    def int(self):
        return random.randint(1,99999999)
    # 小数
    @property
    def float(self):
        return round(random.uniform(1,100),2)
    # 公司名称
    @property
    def company_name(self):
        return self.fake.company()
    # 手机
    @property
    def mobile(self):
        heads = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '157', '183', '159', '187', '181', '180', '182']
        return random.choice(heads) + ''.join(str(i) for i in random.sample(range(0, 10), 8))
    # 邮件
    @property
    def email(self):
        suffix = ['@163.com', '@qq.com', '@126.com', '@aliyun.com', '@sina.com', '@yahoo.com', '@hotmail.com']
        return ''.join(str(i) for i in random.sample(range(1, 10), 9)) + random.choice(suffix)
    # 邮编
    @property
    def post_code(self):
        return self.fake.postcode()
    # 银行卡号
    @property
    def bank_card_code(self):
        return range(6227007201360049787,6227007201360049987)[random.randint(0,len(range(6227007201360049787,6227007201360049987))-1)]
    # 职业
    @property
    def job(self):
        return self.fake.job()
    # 电话
    @property
    def telephone(self):
        heads = ['010-', '022-', '0571-', '0577-', '021-', '020-', '0755-', '0592-', '027-', '023-', '028-', '025-','0512-', '0371-', '0532-']
        return random.choice(heads) + ''.join(str(i) for i in random.sample(range(1, 10), 8))
    # 用户名
    @property
    def user_name(self):
        return self.fake.user_name()
    # 网址
    @property
    def url(self):
        return 'www.' + self.rw.random_word() + self.rw.random_word() + '.com'
    # 地址
    @property
    def address(self):
        return self.fake.address()
    # QQ
    @property
    def qq(self):
        return ''.join(str(i) for i in random.sample(range(1, 10), 9))
    # 名字
    @property
    def name(self):
        return self.fake.name()
    # 自动编码
    def auto_code(self,num):
        return ''.join(str(i) for i in random.sample(range(0,9),num))
    # 单词
    @property
    def word(self):
        return self.rw.random_word()
    # 文件名
    @property
    def file_name(self):
        return self.fake.file_name()