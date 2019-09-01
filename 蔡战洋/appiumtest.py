#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/14 15:17
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : appiumtest.py

import appium
from time import sleep
from appium import webdriver

# python代码客服端连接手机所需要新的信息
contect_date= {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "5019682f",
  "appPackage": "com.tencent.mobileqq",
  "appActivity": ".activity.SplashActivity",
  "noReset": "true",
    "unicodekeyboard":"true"
}
# 步骤一：与手机建立手机
# 127.0.0.1=localhost
"""
将手机信息发送到appium服务器，使服务器和手机建立一个session
appium 与python客服端建立一个连接
"""

dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=contect_date)

# appium 运行步骤
"""
1，python客户端与appium服务器建立一个链接
2，python代码中的命令由appium服务器转发
3，手机中bootstrap.jar 服务器接收转发的命令
4，处理转发命令，将命令下发给uiautomator【手机自带测试框架：执行类似与adb命令】
5，uiautomator生成一个执行之后的结果
6，结果转发个bootstrap.jar微服务器
7，一直转发到python到客户端，appium库解析结果
8，将结果输出
"""

# appium 定位元素
"""
id：一般是唯一的，标记一个元素
class：标记一组元素，一般多个
text:是否可以获取文字，有文字代表可以获取
clickable：判断是否可以被点击，true可以被点击，false不可以
"""

# 执行操作
"""
1，id不唯一，使用class定位
解决方法：
    向上一级,或上上一级查找id唯一，class唯一
    在使用class进行定位
"""
# 先找唯一的id，再找class
# 联系人，看点，动态 三个组成的列表【1，2，3】


# s = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# s = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.TextView')
# for i in s:
#     sleep(2)
#     i.click()

# dr.find_element_by_id('android:id/tabs').find_element_by_class_name('android.widget.RelativeLayout').click()




"""
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=contect_date)
dr.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').send_keys('1971065714')
touch_name=dr.find_element_by_id('com.tencent.mobileqq:id/recent_chat_list').find_elements_by_class_name('android.widget.LinearLayout')
mes_list=[2,3,4]
for i in mes_list:
    sleep(2)
    touch_name[i].click()
    sleep(0.1)
    dr.find_element_by_id('com.tencent.mobileqq:id/input').send_keys('hello sun - python test')
    sleep(0.1)
    dr.find_element_by_id('com.tencent.mobileqq:id/fun_btn').click()
    sleep(0.1)
    dr.find_element_by_id('返回消息').click()
"""

