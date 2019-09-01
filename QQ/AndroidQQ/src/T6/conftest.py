#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/26 15:11
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : conftest.py

import pytest

@pytest.fixture()
def fun():
    print('我执行lconftest的fun级的')

@pytest.fixture(scope='class')
def cls():
    print('我执行了conftest的class级的')

@pytest.fixture(scope='module')
def mod():
    print('我执行了conftest的mod级的')

@pytest.fixture(scope='package')
def pkg():
    print('我执行lconftest的package级的')