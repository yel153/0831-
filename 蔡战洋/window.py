#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/19 21:11
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : window.py

import os,pyperclip,time,win32api,win32gui,win32con
from pymouse import *
from pykeyboard import PyKeyboard
m=PyMouse()
k=PyKeyboard()
# pyperclip.copy('网易邮箱')
# # # # os.startfile(r'C:\Users\Darcy\AppData\Local\Google\Chrome\Application\chrome.exe')
# os.startfile(r"D:\Program Files\Mozilla Firefox\firefox.exe")
# # # # os.startfile(r'C:\Users\Darcy\Desktop\命令.txt')
# time.sleep(10)
# # m.move(567,690)#鼠标移动
# # m.click(567,690,button=2,n=1) #.click鼠标点击(两个坐边，button鼠标左右键，以及滑鼠，n=点击次数)
# # # 模拟键盘点击ctrl+v
# # x_dim,y_dim = m.screen_size() #–获得屏幕尺寸
# # print(x_dim,y_dim)
# # pyperclip.paste()
# k.press_key(k.control_key)
# k.tap_key('v')
# k.release_key(k.control_key)
# time.sleep(1)
# k.tap_key(k.enter_key)
# time.sleep(5)
# m.click(263,285,button=1,n=1)
# pyperclip.copy('cc524997199')
# time.sleep(1)
# k.press_key(k.control_key)
# k.tap_key('v')
# k.release_key(k.control_key)
# time.sleep(1)
# k.tap_key(k.tab_key)
# pyperclip.copy('0.00.0')
# # k.tap_key(k.tab_key)
# k.press_key(k.control_key)
# k.tap_key('v')
# k.release_key(k.control_key)
# time.sleep(1)
# k.tap_key(k.tab_key,n=2)
# k.tap_key(k.enter_key)
# k.press_keys()
# m.move(683,384)#鼠标移动
# m.scroll(vertical=-10)
# k.press_key(k.enter_key)
# k.type_string('Hello, World!') #–模拟键盘输入字符串
# k.press_key('H') #–模拟键盘按H键
# k.release_key('H')# –模拟键盘松开H键
# k.tap_key('H') #–模拟点击H键
# k.tap_key('H',n=2,interval=5) #–模拟点击H键，2次，每次间隔5秒
# k.tap_key(k.function_keys[5]) #–点击功能键F5
# k.tap_key(k.numpad_keys[5],3) #–点击小键盘5,3次
#联合按键模拟
#例如同时按alt+tab键盘
# k.press_key(k.alt_key) #–按住alt键
# k.tap_key(k.tab_key) #–点击tab键
# k.release_key(k.alt_key) #–松开alt键
# # 模拟键盘点击ctrl+v
# k.press_key(k.control_key)
# k.tap_key('v')
# k.release_key(k.control_key)


""""""

"""
pyperclip.copy('网易邮箱')
os.startfile(r"D:\Program Files\Mozilla Firefox\firefox.exe")
time.sleep(10)
k.press_key(k.control_key)
k.tap_key('v')
k.release_key(k.control_key)
time.sleep(1)
k.tap_key(k.enter_key)
time.sleep(5)
m.click(263,285,button=1,n=1)
pyperclip.copy('cc524997199')
time.sleep(1)
k.press_key(k.control_key)
k.tap_key('v')
k.release_key(k.control_key)
time.sleep(1)
k.tap_key(k.tab_key)
pyperclip.copy('0.00.0')
k.press_key(k.control_key)
k.tap_key('v')
k.release_key(k.control_key)
time.sleep(1)
k.tap_key(k.tab_key,n=2)
k.tap_key(k.enter_key)
"""

"""
os.startfile(r"D:\Program Files\Mozilla Firefox\firefox.exe")
time.sleep(10)
pyperclip.copy('hello')
k.press_keys([k.control_key,'v'])
time.sleep(1)
k.tap_key(k.enter_key)
time.sleep(5)
m.click(666,356,button=3,n=1)
m.move(666,386)
"""




# b='0123456789'
# c=0
# for i in a:
#     if i in b:
#         c+=1
# if c==len(a):
#     print('全是数字')
# else:
#     print('不是全数字')

# os.startfile(r'"D:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe"')
# time.sleep(2)



# def c (a=None):
#     if a:
#         print("json")
#     else:
#         print('john')


from selenium import webdriver
from time import *
import socket,threading
# print(ctime())
class serve(object):
    def __init__(self):
        ip_port = ('127.0.0.1', 9789)  # 指定服务器的ip地址，监听端口号
        self.s1 = socket.socket()  # 建立一个套字节，客服端与服务器传输信息
        self.s1.bind(ip_port)  # 绑定服务地址和端口号
        self.s1.listen(5)  # 设置最大连接数
        print('启动socket服务，等待客服端连接...')
        self.a1, address = self.s1.accept()  # socket 自动处理拥
    def servermsg(self):
        # ip_port = ('127.0.0.1', 9789)  # 指定服务器的ip地址，监听端口号
        # s1 = socket.socket()  # 建立一个套字节，客服端与服务器传输信息
        # s1.bind(ip_port)  # 绑定服务地址和端口号
        # s1.listen(5)  # 设置最大连接数
        # print('启动socket服务，等待客服端连接...')
        # a1, address = s1.accept()  # socket 自动处理拥塞控制 accept(),持续开启一直到手动关闭
        # a2 = a1.recv(1024).decode('utf-8')   #第一步接收客服端发送的请求 recv()设置发送数据大小
        # print(a2)
        # a3 = input('请输入发送内容:')
        # s1.sendall(a3.encode())
        while True:
            a2 = self.a1.recv(1024).decode('utf-8')
            # print(f'客服端向服务器发送的消息:{a2}')
            if a2 == '0':
                break
            else:
                print(a2)
        self.s1.close()
    def serversend(self):
        while True:
            # a2 = self.a1.recv(1024).decode('utf-8')
            # print(f'客服端向服务器发送的消息:{a2}')
            a3 = input('请输入发送客服端内容:')
            if a3 == "1":
                break
            else:
                # 发送信息给客服端
                # 1.先找到客服端
                # 2.使用sendall
                self.a1.sendall(a3.encode('utf-8'))
        self.s1.close()

# gg=serve()
# t2=threading.Thread(target=gg.servermsg)
# t3=threading.Thread(target=gg.serversend)
# t2.start()
# t3.start()




"""
web=webdriver.Firefox()
sleep(10)
url='https://www.baidu.com/'
web.get(url)
web.find_element_by_xpath('//*[@id="kw"]').send_keys("博客园")
web.find_element_by_id('su').click()
sleep(10)
web.close()
"""


def jie_cheng():
    a,b,c=1,1,1
    while a<=5:
        b *= a
        a += 1
        c += b
    print(c)
jie_cheng()