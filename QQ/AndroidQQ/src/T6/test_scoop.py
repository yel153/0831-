#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/26 15:12
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : test_scoop.py


# @pytest.fixture(scope='function')
# def setup_function():
#     # request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
#     print('setup_function called.')
#
# def teardown_function():
#     print("teardown_function called.")
# @pytest.fixture(scope='module')

# def setup_class():
#     # request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
#     print('setup called.')
#
# def teardown_class():
#     print("teardown called.")
# # @pytest.fixture(scope='module')


# def setup_method():
#     # request.addfinalizer(teardown_module)
#     print('setup_module called.')
#
# def teardown_method():
#     print("teardown_module called.")


def test_00():
    print('测试用例一执行')

def test_01():
    print('测试用例二执行')

def test_02(fun):
    print('测试用例三执行')

def test_03():
    print('测试用例四执行')

def test_04(fun):
    print('测试用例五执行')

class Testone():

    # def setup(self):
    #     # request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
    #     print('setup_function called.')
    #
    # def teardown(self):
    #     print("teardown_function called.")

    # def setup_method(self):
    #     # request.addfinalizer(teardown_module)
    #     print('setup_module called.')

    # def teardown_method(self):
    #     print("teardown_module called.")

    def test_05(self):
        print('测试用例六执行')

    def test_06(self):
        print('测试用例七执行')

    def test_07(self,fun):
        print('测试用例八执行')

    def test_08(self):
        print('测试用例九执行')







