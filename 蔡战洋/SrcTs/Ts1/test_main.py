#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/12 16:08
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : test_main.py


# 清理测试环境的一个机制：
# 第一步：再执行用例之前进行环境清理
# 第二部：再用例之后进行环境清理

# 脚本清理
# setup_module   用例执行之前的
# teardown_module   用例执行之后的
# module   本脚本所有用例执行前，后的操作仅执行一次
# setup_function   每个测试用例运行之前都要执行一次
# teardown_function   每个测试用例运行之后都要执行一次

# setup,teardown   在类的范围内使用
# setup    每个测试用例运行之前都要执行一次
# teardown     每个测试用例运行之后都要执行一次
# setup_class   在类中所有测试用例执行之前运行一次
# teardown_class    在类中所有测试用例执行之后运行一次
# setup_method    方法级别，每个测试用例运行之前都要执行一次
# teardown_method   每个测试用例运行之后都要执行一次


# conftest.py

"""
conftest.py:python文件，用来存放公共函数，被不同测试用例使用
test脚本下，只有以test开头的类，函数，方法
必须放在当前测试用例所在的目录下面，才能被使用

"""



import  pytest




# @pytest.fixture()
# def claen():
#     print('输入错误，重新输入')

"""
参数化：向测试用例中传入参数的过程
# 必须request，固定写法
# 作用：取出参数列表中每一个函数
# request.param 固定参数
# 与request联用，取出参数
"""


"""
# 一个参数

dd=[1,2,3,4,5,6,7]
@pytest.fixture(params=dd)
def read_data(request):
    print(f'当前传入的参数是{request.param}')
    return request.param

def test_0(read_data):
    t = read_data
    assert t < 6

# 传入两个参数:
d1=[(1,2,3),(2,3,None),(3,4,None)]
@pytest.mark.parametrize('y1,y2,y3',d1)
def test_1(y1,y2,y3):
    print(f'y1的值是{y1}，y2的值是{y2}')
    assert y1 == y2
"""

# @pytest.fixture(autouse=True)等价于pytestmark=pytest.mark.usefixtures('myfix')


@pytest.fixture()
def myfix():
    print('每个测试用例都要执行一次')

# pytestmark=pytest.mark.usefixtures('myfix')
# @pytest.mark.usefixtures('myfix')
def test_3():
    pass

def test_4():
    pass

def test_2():
    pass

def test_1():
    pass

def test_0():
    pass



"""
def test_0():
    print('测试1')

def test_1(claen):
    print('测试2')

def test_2():
    print('测试3')
"""



"""
@pytest.fixture(scope='module')
def start():
    print('所有测试用例之前，之后运行一次')

@pytest.fixture(scope='module')
def close():
    print('所有测试用例之前，之后运行一次')

def test_1():
    print('test1')

def test_2():
    print('test2')

class Testone(object):

    def test_3(self):
        print('用例三执行')
"""



"""
class Testone(object):

    @pytest.fixture(scope='class')
    def login(self):
        print('执行login开始')

    def test_4(self):
        print('执行测试用例四')

    def test_5(self):
        print('执行测试用例五')

    def test_6(self):
        print('执行测试用例六')
"""



"""
@pytest.fixture()
def login():
    print('login函数开始执行')

def test_1(login):
    print('用例一执行')

def test_2(login):
    print('用例二执行')

def test_3():
    print('用例三执行')
"""





"""
class Testone(object):

    def setup(self):
        print('执行setup')

    def teardown(self):
        print('执行teardown')

    def test_4(self):
        print('执行测试用例四')

    def test_5(self):
        print('执行测试用例五')

    def test_6(self):
        print('执行测试用例六')
"""



"""
class Testone(object):

    def setup_method(self):
        print('执行setup_method')

    def teardown_method(self):
        print('执行teardown_method')

    def test_4(self):
        print('执行测试用例四')

    def test_5(self):
        print('执行测试用例五')

    def test_6(self):
        print('执行测试用例六')
"""




"""
class Testone(object):

    def setup_class(self):
        print('执行setup_class')

    def teardown_class(self):
        print('执行teardown_class')

    def test_4(self):
        print('执行测试用例四')

    def test_5(self):
        print('执行测试用例五')

    def test_6(self):
        print('执行测试用例六')
"""



"""  
def setup_module():
    print('所有用例执行之前执行一次')

def test_1():
    print('用例一执行')

def test_2():
    print('用例二执行')

def test_3():
    print('用例三执行')

def teardown_module():
    print('所有用例执行之后执行一次')
"""




"""
def setup_function():
    print('每个用例执行之前执行一次')

def test_1():
    print('用例一执行')

def test_2():
    print('用例二执行')

def test_3():
    print('用例三执行')

def teardown_function():
    print('每个用例执行之后执行一次')
"""

