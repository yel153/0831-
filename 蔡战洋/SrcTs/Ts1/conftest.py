#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/13 9:36
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : conftest.py


import pytest

@pytest.fixture()
def clean():
    print('测试用例之前执行前')