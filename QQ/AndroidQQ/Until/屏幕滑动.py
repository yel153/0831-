#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/17 10:46
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : 屏幕滑动.py


# 获取手机屏幕大小
def swip_right(drive,t=500):
    a= drive.get_window_size()
    # 放缩屏幕
    x1= a['width']*0.5
    x2 = a['width']*0.75
    y1= a['height']*0.25
    drive.swipe(x2,y1,x1,y1,duration=t)

def swip_left(drive,t=500):
    a= drive.get_window_size()
    # 放缩屏幕
    x1= a['width']*0.5
    x2 = a['width']*0.75
    y1= a['height']*0.25
    drive.swipe(x1,y1,x2,y1,duration=t)

def swip_up(drive,t=500):
    a= drive.get_window_size()
    # 放缩屏幕
    x1= a['width']*0.5
    y1= a['height']*0.25
    y2=a['height']*0.5
    drive.swipe(x1,y1,x1,y2,duration=t)

def swip_down(drive,t=500):
    a= drive.get_window_size()
    # 放缩屏幕
    x1= a['width']*0.5
    y1= a['height']*0.25
    y2=a['height']*0.5
    drive.swipe(x1,y2,x1,y1,duration=t)


"""
# 左滑
dr.swipe(x2,y1,x1,y1,t=500)# 单位毫秒
# 右滑
dr.swipe(x1,y1,x2,y1,t=500)
# 上滑
dr.swipe(x1,y1,x1,y2,t=500)
# 下滑
dr.swipe(x1,y2,x1,y1,t=500)
"""




from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ta_phone = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "JTJ4C15C18001065",
    "appPackage": "com.vy.visvacn",
    "appActivity": "com.vy.visvacn.MainActivity",
    "noReset": "true"
    # "unicodeKeyboard": "true",
    # "resetkeKboard": "true"
}
dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=ta_phone)
dry = WebDriverWait(dr, 10).until(lambda y: dr.find_element(y))

class tazai(object):

    def jk(self):

       dry((By.ID,'com.vy.visvacn:id/v3')).click()

kl=tazai()
kl.jk()

