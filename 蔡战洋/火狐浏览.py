#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/15 11:07
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : 火狐浏览.py

from time import sleep
from selenium import webdriver

"""
def login_qq():
    fox_dr=webdriver.Firefox()
    sleep(10)
    fox_dr.get('https://mail.qq.com/cgi-bin/loginpage')
    sleep(10)
    fox_dr.find_element_by_id('switcher_plogin').click()
    sleep(1)
    fox_dr.find_element_by_id('uin_tips').clear()
    fox_dr.find_element_by_id('uin_tips').send_keys('734351303')
    sleep(10) 
"""

"""
def login_163(foo):
    sleep(5)
    fox_dr.get('https://www.baidu.com/')
    sleep(2)
    input_search=fox_dr.find_element_by_id('kw')
    input_search.send_keys('163邮箱')
    fox_dr.find_element_by_id('su').click()
    sleep(2)
    fox_dr.find_element_by_id('op_email3_username').send_keys('cc524997199')
    sleep(2)
    fox_dr.find_element_by_class_name('op_email3_password').send_keys('0.00.0')
    sleep(2)
    fox_dr.find_element_by_class_name('op_email3_submit').click()
    sleep(30)
    fox_dr.find_element_by_xpath('//*[@id="_mail_component_24_24"]').click()
    sleep(0.5)
    fox_dr.find_element_by_id('_mail_emailcontainer_0_199').send_keys('734351303@qq.com')
    sleep(0.5)
    fox_dr.find_element_by_id('1565857491665_subjectInput').send_keys('python test')
    sleep(1)
    fox_dr.find_element_by_class_name('APP-editor-iframe').send_keys('hello moon-python test')
    sleep(1)
    fox_dr.find_element_by_id('_mail_icon_35_182').click()
    print('ok')


if __name__ == '__main__':
    login_qq()
"""



class makeHtmlTagClass(object):

    def __init__(self, tag, css_class=''):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
            if css_class != "" else ""

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class + ">" \
                   + fn(*args, **kwargs) + "</" + self._tag + ">"

        return wrapped


@makeHtmlTagClass(tag="b", css_class="bold_css")
@makeHtmlTagClass(tag="i", css_class="italic_css")
# @makeHtmlTagClass(tag="h", css_class="tilo_css")
def hello(name):
    return "Hello, {}".format(name)

print (hello("Hao Chen"))

# <b class='bold_css'><i classg='italic_css'>Hello, Hao Chen</i></b>