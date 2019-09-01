#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 19:07
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : web_ta.py


import requests,pytest
from selenium import webdriver
from AndroidQQ.Until.qqmima import s
from selenium.webdriver.support.wait import WebDriverWait


# class Testlolo():
#
#     dr=webdriver.Firefox()
#     wait=WebDriverWait(dr,15)
#     def test_ta_home(self):
#         print('hahha')



@pytest.fixture(scope='module')
def date(s):
    cc,gh=[],[]
    for i in s:
        cc.append(i[0:2])
        gh.append(i[2:4])
    print('执行了一次')
    return cc,gh

print(date(s)[0])

class Test_zai():

    @pytest.mark.parametrize
    def test_is_pictuer(self):
        pass

    def test_count_op(self):
        pass

    def test_is_coumiute(self):
        pass





# import requests
#
# def test_main_point():
#
#     url = "http://apis.juhe.cn/geo/"
#     querystring = {"key":"825b6cbe0a6f7a84ff8fa7852aa0b751","type":"1","lng":"108.4152","lat":"34.1152"}
#     headers = {
#         'User-Agent': "PostmanRuntime/7.15.2",
#         'Accept': "*/*",
#         'Cache-Control': "no-cache",
#         'Postman-Token': "0e0e7120-c62a-4cd6-adaa-b99c23a7efb4,38998c86-f1ca-4675-aefb-723d5aac3c7c",
#         'Host': "apis.juhe.cn",
#         'Cookie': "aliyungf_tc=AQAAADratGwcFAEAmZWePfA5dTYIOYd0",
#         'Accept-Encoding': "gzip, deflate",
#         'Connection': "keep-alive",
#         'cache-control': "no-cache"
#         }
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     print(response.text)

def test_ta():
    print('web自动化')