#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/16 10:02
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : test_00.py

import pytest
from time import sleep
from AndroidQQ.Until.qqmima import s
from  appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from AndroidQQ.Until.qqlog import get_logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

log=get_logger(filename='test_1.py')

# def elem():
#   with open(file=r'C:\Users\Darcy\Desktop\QQ\AndroidQQ\Date\用户密码.yaml',encoding='utf-8') as fb:
#     qq_elem = yaml.load(fb, Loader=yaml.FullLoader)
#     return qq_elem
# ad=elem()
#
# for i,k in ad.items():
#   print(i,k)
#   for _ in k:
#     print(_)

# uswd=[('734351303','9601070.0'),('484083158','0.00.0')]


qq_phone = {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "5019682f",
  "appPackage": "com.tencent.mobileqq",
  "appActivity": ".activity.SplashActivity",
  "noReset": "true"
  # "unicodeKeyboard": "true",
  # "resetkeKboard": "true"
}
dr_qq = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=qq_phone)
# sleep(5)
# dfg=dr_qq.find_element_by_id('com.tencent.mobileqq:id/ivTitleName')
# print(dfg)

# FG=(By.XPATH,'com.tencent.mobileqq:id/settings')


# class Testlogin(object):
#
#   def test_lgn(dr,elem):
#
#     dr.find_element_by_xpath(elem['touxiang']).click()
#     sleep(0.5)
#     dr .find_element_by_id(elem['seting']).click()
#     sleep(0.5)
#     dr.find_element_by_id(elem['zhanghao']).click()
#     sleep(0.5)
#     dr.find_element_by_id(elem['tuichu']).click()
#     sleep(0.5)
#     dr.find_element_by_id(elem['queren']).click()
#     sleep(0.5)
#     assert dr.find_element_by_accessibility_id(elem['newuser']).text == '用户注册'
#
#   @pytest.mark.parametrize('ue,ma', s)
#   def test_check(self,ue,ma,elem,dr):
#
#     log.info(f'账号:{ue},密码:{ma}')
#     dr.find_element_by_id(elem['inputusr']).clear()
#     sleep(0.5)
#     dr.find_element_by_id(elem['inputusr']).send_keys(ue)
#     sleep(0.5)
#     dr.find_element_by_id(elem['inputpwd']).clear()
#     sleep(0.5)
#     dr.find_element_by_id(elem['inputpwd']).send_keys(ma)
#     sleep(0.5)
#     dr.find_element_by_id(elem['loginbtn']).click()
#     sleep(1)
#     try:
#       dr.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()  # 捕获登陆失败弹框确认
#     except :
#       sleep(1)
#       try:
#         dr.find_element_by_id('com.tencent.mobileqq:id/ivTitleName').text == '消息'  #捕获登陆成功信息
#       except :
#         assert dr.find_element_by_accessibility_id(elem['newuser']).text == '用户注册'  #断言错误账号密码登陆失败（无弹框）
#       else:
#         assert dr.find_element_by_id('com.tencent.mobileqq:id/ivTitleName').text == '消息' # 断言正确账号登陆成功
#     else:
#       sleep(2)
#       assert dr.find_element_by_accessibility_id(elem['newuser']).text == '用户注册'  # 断言错误账号登陆失败（有弹框）
#
#
#    def test_login(self,elem,dr):
#
#      dr.find_element_by_id(elem['inputusr']).clear()
#      sleep(0.5)
#      dr.find_element_by_id(elem['inputusr']).send_keys('484083158')
#      sleep(0.5)
#      dr.find_element_by_id(elem['inputpwd']).clear()
#      sleep(0.5)
#      dr.find_element_by_id(elem['inputpwd']).send_keys('0.00.0')
#      sleep(0.5)
#      dr.find_element_by_id(elem['loginbtn']).click()