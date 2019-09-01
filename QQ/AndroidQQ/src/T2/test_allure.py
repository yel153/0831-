#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/19 9:24
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : test_allure.py

import allure,pytest

# feature: 标注测试用例是属于哪一个模块的
# story：对一个测试用例的详细描述
# severity：测试用例优先级
"""
Allure中对严重级别的定义：
1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）(阻塞)
2、 Critical级别：临界缺陷（ 功能点缺失）（严重）
3、 Normal级别：普通缺陷（数值计算错误）
4、 Minor级别：次要缺陷（界面错误与UI需求不符） （次要）
5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）（轻微）
"""
# step 记录测试用例中的一些元素，日志代码可以通过step记录到报告中
# issue：存放问题
# testcase：存放详细测试用例
# 对 issue 和 testcase 生成一个网址



@allure.feature('模块一')
def test_1():
    assert 0 == 0

@allure.feature('模块二')
@allure.story('这厮一个很垃圾的测试用例')
def test_2():
    assert 1 == 1

def test_3():
    assert 2 == 3

@allure.feature('模块二')
@allure.story('这厮一个很niu的测试用例')
def test_4():
    """
    这是对函数的参数，返回值的一个注释

    """
    # 测试用例的描述是是通过注释获取到的
    assert "good" in "hello world"

@allure.feature('模块三')
@allure.severity('blocker')
def test_5():
    assert 1==2

@allure.feature('模块三')
@allure.severity('critical')
def test_6():
    assert 2==2

@allure.feature('模块三')
@allure.severity('minor')
def test_7():
    assert 3==2


# isinstance(参数一，参数二)判断数据类型的类，参数一和参数二是不是同一类型
# 是的话--->true 不是--->false
@allure.step('字符串相加:{0},{1}')
def str_add(str1,str2):
    if not isinstance(str1,str):
        return f'{str1}不是字符串类型的'
    if not isinstance(str2,str):
        return f'{str2}不是字符串类型的'
    return str1 + str2

@allure.feature('模块四')
def test_8():
    str1='哈哈哈'
    str2='嘻嘻嘻'
    assert str_add(str1,str2)

@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('blocker')
@allure.issue("http://www.baidu.com")
@allure.testcase("http://www.testlink.com")
def test_case():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'

with open(file='E:\猫\猫.jpg',mode='rb') as fb:
     file=fb.read()
# @allure.attach('猫.jpg', file, 'jpg')
# def test_9():
#     str1='哈哈哈'
#     str2='嘻嘻嘻'
#     assert str1==str2

