#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/16 15:00
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : conftest.py

import pytest,yaml
from time import sleep
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope='module')
def elem():
  with open(file=r'C:\Users\Darcy\Desktop\QQ\AndroidQQ\Element\login.yaml',encoding='utf-8') as fb:
    qq_elem = yaml.load(fb, Loader=yaml.FullLoader)
    return qq_elem



@pytest.fixture(scope='module')
def dr():
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
  sleep(2)
  print('我执行了dr')
  return dr_qq


