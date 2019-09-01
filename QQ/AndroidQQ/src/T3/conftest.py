#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/17 16:38
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : conftest.py


import yaml,pytest
from time import sleep
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def dr():
  ta_phone = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "5019682f",
    "appPackage": "com.vy.visvacn",
    "appActivity": "com.vy.visvacn.MainActivity",
    "noReset": "true",
    "unicodeKeyboard": "true",
    "resetkeKboard": "true"
  }
  dr_ta = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=ta_phone)
  return dr_ta




@pytest.fixture(scope='module')
def el():
  with open( file=r'C:\Users\Darcy\Desktop\QQ\AndroidQQ\Element\tazai.yaml',encoding='utf-8') as fb:
    dates= yaml.load(fb,Loader=yaml.FullLoader)
    return dates

