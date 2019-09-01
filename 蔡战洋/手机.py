#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/17 13:17
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : 手机.py

def suan_99():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{}*{}={}\t".format(i, j, i * j), end="")
        print()

suan_99()