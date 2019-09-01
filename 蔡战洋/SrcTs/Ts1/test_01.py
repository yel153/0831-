#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/12 10:04
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : test_01.py

import pytest
def test_0():
    n = 0
    for i in range(1,101):
        n += i
# 断言指的是：拿实际结果与预期结果进行对比的过程
    assert n == 5051

"""

# 执行测试用例：pytest -v 测试文件
# 1、py.test test_01.py --alluredir ./result/    执行测试用例，并生成测试报告数据，保存到result目录下
# 2、allure generate ./result/ -o ./report/ --clean   将测试报告数据生成allure网页报告
# 3、allure open -h 127.0.0.1 -p 8083 ./report/     打开allure网页测试报告

"""




"""
# pytest:查找当前目录下，所有文件或目录，找包含test目录或者文件，如果找到test目录，类似于cd
# 执行包含test开头的文件，搜索test开头所有的函数
# 当整个当前目录下没有包含test开头的目录文件和文件：
# _____ERROR collecting test session ____
"""




"""
# pytest
 -v 使输出的信息更加详细
 -q 简化输出信息
 -k 指定关键字运行
 -s 输出测试用例中的print内的信息
 脚本名::用例名字  运行执行脚本中的具体用例
"""

