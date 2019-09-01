#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/12 9:32
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : yamlop.py
import yaml
with open(file='haha.yaml',encoding='utf-8') as fb:
    date=yaml.load(fb,Loader=yaml.FullLoader)
    print(date)


def a():
    def b():
        c= 2+1
        return c
    print('a函数')
    return b

print(a()())