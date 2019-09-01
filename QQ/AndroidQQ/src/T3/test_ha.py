#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/19 17:42
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : test_ha.py


# import pytest,appium
# from time import sleep
# from AndroidQQ.Until.qqmima import s
# from AndroidQQ.Until.屏幕滑动 import *
# from selenium.webdriver.common.by import By
# from AndroidQQ.Until.qqlog import get_logger
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class Testone(object):
#
#     def test_click(self,dr,el):
#         pass

def ha():
    return 5+3


def xi(lo):
    return lo()+3

def main(lp,ha):
    return lp(ha)
if __name__ == '__main__':
    print(main(xi))
