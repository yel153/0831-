#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/17 16:37
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : test_ta.py

import pytest,appium
from time import sleep
from AndroidQQ.Until.qqmima import s
from AndroidQQ.Until.屏幕滑动 import *
from selenium.webdriver.common.by import By
from AndroidQQ.Until.qqlog import get_logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log=get_logger(filename='test_ta.py')


class Testta(object):


    def test_lo(self,el):
        sleep(3)
        # WebDriverWait(dr,30,0.5).until(EC.presence_of_element_located((By.ID,'com.vy.visvacn:id/tv_register'))).click()
        dr.find_element_by_id(el['phone']).click()
        sleep(2)
        dr.find_element_by_id(el['phoneother']).click()

    @pytest.mark.parametrize('mi,ma',s)
    def test_login(self,dr,el,mi,ma):

        log.info(f"账号是:{mi},密码是:{ma}")
        sleep(3)
        dr.find_element_by_id(el['zuceiptphone']).send_keys(mi)
        sleep(1)
        dr.find_element_by_id(el['phoneiptmima']).send_keys(ma)
        sleep(1)
        dr.find_element_by_id(el['zucebtn']).click()
        sleep(2)
        try:
            assert dr.find_element_by_id(el['zucebtn']).text == '登陆' #断言错误账号登陆失败
        except:
            print('切换登陆测试')

    def test_login_sy(self,el):

        sleep(2)
        dr.find_element_by_id(el['zucetuichu']).click()
        sleep(3)
        dr.find_element_by_id(el['phone']).click()
        sleep(3)
        dr.find_element_by_id(el['phonebtn']).click()
        sleep(2)
        try:
            sleep(2)
            assert dr.find_element_by_id(el['ciq']) == dr.find_element_by_id(el['ciq'])  #断言登陆成功
        except:
            print('登陆失败')
        try:
            # sleep(2)
            dr.find_element_by_id(el['sycontent']).click()
        except:
            pass
        else:
            sleep(2)
            dr.find_element_by_id(el['syweiguanhd']).send_keys('哈哈哈哈哈')
            sleep(2)
            dr.find_element_by_id(el['syweiguanfb']).click()
            sleep(2)
            dr.find_element_by_id(el['zucetuichu']).click()
        assert dr.find_element_by_id(el['sycontent']).text=='哈哈哈哈哈'


    def test_sy_nr(self,dr,el):

        sleep(2)
        for i in range(3):
            sleep(0.5)
            swip_down(dr)
        sleep(3)
        dr.find_element_by_id(el['syneirong']).find_elements_by_class(el['syneirong1'])[0].click()
        sleep(0.5)
        dr.find_element_by_id(el['syneirongpl1']).send_keys('嘻嘻嘻')
        sleep(0.5)
        dr.find_element_by_id(el['syneirongfs']).click()
        sleep(0.5)
        assert dr.find_element_by_id(el['syneirongwd']).text=='嘻嘻嘻'

    def sy_zan(self):
        ww=dr.find_element_by_id('com.vy.visvacn:id/rcv').find_elements_by_class_name\
            ('android.widget.LinearLayout')
        for i in ww:
            i.click()
            sleep(2)
            dr.find_element_by_id('com.vy.visvacn:id/rl_left').click()

    def sy_ping_lun(self):
        wait=WebDriverWait(dr,15)
        cc=wait.until(lambda x:x.find_element_by_name())
        cc.click()









# gg=Testta()
# gg.sy_zan()








