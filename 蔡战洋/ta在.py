#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/15 20:05
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : ta在.py

from time import sleep
from appium import webdriver

ta= {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "5019682f",
  "appPackage": "com.vy.visvacn",
  "appActivity": "com.vy.visvacn.MainActivity",
  "noReset": "true",
    "unicodekeyboard":"true",
    'resetkeyboard':'true'
}

dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=ta)
dr.find_element_by_id('com.vy.visvacn:id/tv_register').click()


