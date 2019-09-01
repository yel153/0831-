#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/17 15:10
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : waitapp.py




# aapium三种等待方式
# 1，sleep：强制等待  工作的线程会停止等待一段时间
# 2，隐形等待：implicitly_wait(time_to_wait=10)
#  设置最大等待时间，关键字参数：time_to_wait=10，超过最大等待时间后则会抛出异常,设置以后全局有效，每个dr默认等待这个时间
# 3,安卓独有 --- wait_activity():
# 等待某个activity出现，设置最大等待时间，超出最大等待时间爱，就会抛出异常
# self.dr.wait_activity(activity=".activity.SplashActivity'', timeout=10)
# 4，智能等待 --- WebDriverWait()：
# 在指定的时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait   #等待某个元素加载出来
from selenium.webdriver.support import expected_conditions as EC   # expected_conditions  selenium 的异常处理类
from selenium.webdriver.common.by import By  # By 指的是通过什么方式定位的，例如  By.id--->通过id定位的
WebDriverWait('参数1','参数2','参数3').until(EC.presence_of_all_elements_located('参数4'))

"""
参数1:我们与手机建立的会话---》dr
参数2：最大等待时间，单位s
参数3：刷新页面的时间间隔，单位s 
until(EC.presence_of_all_elements_located('参数4'))
直到某个元素被找到，停止等待
参数四:一个由定位方法，和元素组成的元组。例如：（By.id,'元素'）
"""



# def find_elt(*loc,dr):
#   """
#   定位元素,定位正确后返回元素的信息,外部调用传入元组参数必须有*,
#   例如:
#   find_element(*self.native_caixun)
#   :param loc: 元组类型,结构必须是(By.NAME, u'财讯')
#   :return: element
#   """
#   try:
#     element = WebDriverWait(dr,30).until(lambda x: x.find_element(*loc))
#     return element
#   except NoSuchElementException as e:
#     print('Error details :%s' % (e.args[0]))
#
#
# def find_elements(dr,*loc):
#   """
#   定位元素,定位正确后返回元素的信息,外部调用传入元组参数必须有*,
#   例如:
#   find_elements(*self.native_caixun)
#   :param loc: 元组类型,结构必须是(By.NAME, u'财讯')
#   :return: elements
#   """
#   try:
#     # return self.driver.find_elements(*loc)
#     elements = WebDriverWait(dr, 10).until(lambda x: x.find_elements(*loc))
#     return elements
#   except NoSuchElementException as e:
#     print  ( 'Error details :%s' % (e.args[0]))
#
#  find_elt(*(By.XPATH,'//android.widget.Button[@content-desc="帐户及设置"]'))