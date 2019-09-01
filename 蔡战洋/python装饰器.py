#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/12 15:07
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : python装饰器.py



import  pytest
# python 装饰器
# 作用：将函数作为参数进行返回给别的函数使用
# 函数执行规则：函数名（）

# 测试夹具fixture
# @pytest.fixture


"""
scope:装饰器的作用范围
    function:方法级别，默认
    class：类级别的
    module：脚本级别，所有的测试用例执行之前，之后运行一次（定义两个，之前和之后）
    package：包级别,目录级别的
    session：会话级别
"""


"""
def foo(func):
    print('执行foo函数开始')
    func()
    print('执行foo函数结束')

def koo():
    print('执行了koo函数')

foo(koo)
"""

def out1(fun):
    print('函数out1')
    def inne():
        fun()
        print('inne out1结束')
    return inne

def out(func):
    print('开始执行out函数')
    def inner():
        func()
        print('inner函数结束')
    return inner
# @：python的语法糖 @out 使用out这个装饰器
@out
@out1 #等价于  say_hello=out(out1(say_hello)) 执行顺序从里往外
def say_hello():
    print('hello,装饰器')
say_hello()





