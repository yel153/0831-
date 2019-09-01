#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/17 16:38
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : conftest.py


import yaml,pytest
from time import sleep
from appium import webdriver
from AndroidQQ.Until.qqmima import s
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def dr():
  ta_phone = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "emulator-5554",#5019682f
    "appPackage": "com.vy.visvacn",
    "appActivity": "com.vy.visvacn.MainActivity",
    "noReset": "true",
    "unicodeKeyboard": "true",
    "resetkeKboard": "true"
  }
  dr_ta = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=ta_phone)
  # wd=WebDriverWait(dr_ta,10).until(lambda x:EC.presence_of_element_located(x))
  sleep(2)
  return dr_ta


@pytest.fixture(scope='module')
def el():
  with open( file=r'C:\Users\Darcy\Desktop\QQ\AndroidQQ\Element\tazai.yaml',encoding='utf-8') as fb:
    dates= yaml.load(fb,Loader=yaml.FullLoader)
    return dates


