#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/17 11:17
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : test_01.py

from AndroidQQ.Until.屏幕滑动 import *
from time import sleep

def test_0(dr):
    for i in range(10):
        sleep(1)
        swip_down(dr)

