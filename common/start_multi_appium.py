# -*- coding: utf-8 -*-
# @Time    : 2022/12/15 19:11
# @Author  : LCQ
# @FileName: start_multi_appium.py


import subprocess
import time


def start(host,port):

    #指定bp端口号
    bootstrap_port = str(port+1)
    #把在cmd弹窗输入的命令，直接写到这里
    cmd = 'start /b appium -a ' + host+' -p '+str(port) +' -bp '+ str(bootstrap_port)
    #去掉 “/b”，即可以打开cmd弹窗运行
    #cmd = 'start  appium -a ' + host+' -p '+str(port) +' -bp '+ str(bootstrap_port)
    # 打印输入的cmd命令，及时间
    print("%s at %s " %(cmd,time.ctime()))
    subprocess.Popen(cmd,shell=True,stdout=open('./appium_log/'+str(port)+'.log','a'),stderr=subprocess.STDOUT)
if __name__ == '__main__':
    host = '127.0.0.1'
    for i in range(2):
        port = 4723 + 2*1
        start(host,port)
