#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 9:08
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : brower.py

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
dr=webdriver.Firefox()
# dr.switch_to.frame('login_frame')
dr.get('https://www.baidu.com')  #访问网址
print(dr.title)     #获取访问网址的标题  断言
print(dr.current_url)      # 获取访问的网址
# dr.set_window_size(400,400)  # 设置浏览器窗口的大小 长和宽
# dr.set_window_position(400,400) # 设置浏览器的位置
dr.maximize_window()  # 最大化浏览器
# dr.minimize_window() # 最小化浏览器
# sleep(2)
# dr.get('http://www.jd.com')
# sleep(2)
# dr.back()  # 回退到上一次的页面
# sleep(2)
# dr.forward() # 前进到上一次页面
dr.find_element_by_id('kw').send_keys('163邮箱')
dr.find_element_by_id('su').click()
sleep(2)
dr.find_element_by_id('op_email3_username').send_keys('cc524997199')
sleep(1)
dr.find_element_by_class_name('op_email3_password').send_keys('0.00.0')
sleep(1)'
dr.find_element_by_class_name('op_email3_submit').click()
# dr.switch_to.frame('login_frame')
# dr.find_element_by_link_text('登陆').click()
# dr.find_element_by_link_text('新闻').click()
# dr.find_element_by_xpath()
"""

# dr=webdriver.Chrome()
# dr.get('https://www.ctrip.com/')
# ww=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in ww:
#     i.click()
#     sleep(2)
# print(len(ww))

# dr=webdriver.Chrome()
# dr.get('https://www.jd.com/')
# dr.find_element_by_id('key').send_keys('macbook')
# dr.find_element_by_class_name('button').click()

"""
from appium import webdriver
ta_phone = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "emulator-5554",#5019682f
    "appPackage": "com.vy.visvacn",
    "appActivity": "com.vy.visvacn.MainActivity",
    "noReset": "true",
    "unicodeKeyboard": "true",
    "resetkeKboard": "true"
  }
dr= webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=ta_phone)
ww=dr.find_element_by_id('com.vy.visvacn:id/rcv').find_elements_by_class_name\
    ('android.widget.LinearLayout')
for i in ww:
    i.click()
    sleep(2)
    dr.find_element_by_id('com.vy.visvacn:id/rl_left').click()
"""

def fire_163():
    dr=webdriver.Firefox()
    dr.get('https://www.baidu.com')
    dr.find_element_by_id('kw').send_keys('163邮箱')
    dr.find_element_by_id('su').click()
    sleep(2)
    dr.find_element_by_id('op_email3_username').send_keys('cc524997199')
    sleep(1)
    dr.find_element_by_class_name('op_email3_password').send_keys('0.00.0')
    sleep(1)
    dr.find_element_by_class_name('op_email3_submit').click()
    sleep(5)
    dr.find_element_by_xpath('//*[@id="_mail_component_24_24"]').click()
    num=dr.window_handles
    dr.switch_to.window(num[1])
    dr.find_element_by_xpath('/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]').click()
    dd= dr.window_handles
    print(dd)
    dr.switch_to.window(num[1])
    print(dr.title)
    sleep(3)


def ifeng():
    dr=webdriver.Firefox()
    dr.get('https://www.ifeng.com/')
    sleep(3)
    dr.find_element_by_xpath('/html/body/button').click()
    sleep(1)
    ww=dr.switch_to.alert
    print(ww.text)
    sleep(1)
    ww.send_keys('嘻嘻嘻')
    sleep(1)
    ww.accept()
    dd=dr.find_element_by_link_text('证监会重磅：分拆上市来了！')
    dr.execute_script('arguments[0].scrollIntoView();',dd)
    sleep(5)
    for i in range(0,10000,200):
        js=f'var q=document.documentElement.scrollTop={i}'
        dr.execute_script(js)
        sleep(2)


def driver():
    dr=webdriver.Firefox()
    dr.get('https://www.baidu.com')
    return dr

def mail_163(gh):
    dr=gh()
    unti=WebDriverWait(dr,20)
    dr.find_element_by_id('kw').send_keys('163邮箱')
    dr.find_element_by_id('su').click()
    sleep(2)
    dr.find_element_by_id('op_email3_username').send_keys('cc524997199')
    sleep(1)
    dr.find_element_by_class_name('op_email3_password').send_keys('0.00.0')
    sleep(1)
    dr.find_element_by_class_name('op_email3_submit').click()
    sleep(2)
    ww=dr.window_handles
    dr.switch_to.window(ww[-1])
    write=unti.until(lambda x:x.find_element_by_xpath('/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]'))
    write.click()
    dr.find_element_by_class_name('nui-editableAddr-ipt').send_keys('524997199@qq.com')
    # rev=unti.until(lambda x:x.find_element_by_link_text('sunzl'))
    # rev.click()
    dr.find_element_by_xpath('//input[@class="nui-ipt-input" and @maxlength="256"]').send_keys('python selenium test')
    dr.switch_to.frame(dr.find_element_by_class_name('APP-editor-iframe'))
    sleep(3)
    dr.find_element_by_xpath('/html/body').send_keys('你好，这是一封测试邮件，看到后请立即回复。我是机器人')
    sleep(2)
    dr.switch_to.default_content()
    sleep(2)
    dr.find_element_by_xpath('//*[contains(@class,"js-component-button") and @role="button" and @tabindex="1"]').click()

def mail_qq(gh,fun):
    dr=gh()
    dr.find_element_by_id('kw').send_keys('qq邮箱')
    dr.find_element_by_id('su').click()
    unti=WebDriverWait(dr,15)
    result=unti.until(lambda x: x.find_element_by_xpath('//div[@id="1" and @class="result c-container "]//a'))
    result.click()
    sleep(3)
    ww=dr.window_handles
    dr.switch_to.window(ww[1])
    dr.switch_to.frame('login_frame')
    lo=unti.until(lambda x:x.find_element_by_xpath('//*[@id="switcher_plogin" and @class="switch_btn" and @tabindex="8"]'))
    lo.click()
    usr=unti.until(lambda x:x.find_element_by_id('u'))
    usr.send_keys('734351303')
    dr.find_element_by_id('p').send_keys('9601070.0')
    dr.find_element_by_id('login_button').click()
    try:
        fun(dr,unti)
    except:
        print('验证失败')
    else:
        dr.find_element_by_id('login_button').click()
    dr.switch_to.default_content()
    wte=unti.until(lambda x:x.find_element_by_xpath('//*[@id="composebtn_td" and contains(@class,"composepart")]'))
    wte.click()
    ifa=unti.until(lambda x:x.find_element_by_xpath('//*[@id="mainFrame" and @name="mainFrame"]'))
    dr.switch_to.frame(ifa)
    dr.find_element_by_xpath('/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input').send_keys('cc524997199@163.com')
    dr.find_element_by_xpath('//*[@id="subject" and @class=""]').send_keys('python test mail')
    sleep(2)
    ao=unti.until(lambda x:x.find_element_by_xpath('//*[@class="qmEditorIfrmEditArea" and @tabindex="3"]'))
    dr.switch_to.frame(ao)
    dr.find_element_by_xpath('/html/body').send_keys('lamda x:x.find_element_by_link_text(发送).click()')
    dr.switch_to.parent_frame()
    dr.find_element_by_link_text('发送').click()

def ta_zai(gh):
    dr=gh()
    wait=WebDriverWait(dr,15)
    dr.find_element_by_id('kw').send_keys('ta在')
    dr.find_element_by_id('su').click()
    result = wait.until(lambda x: x.find_element_by_xpath('//div[@id="1" and @class="result c-container "]//a'))
    result.click()
    ww=dr.window_handles
    dr.current_window_handle(ww[1])
    print(dr.title)
    # assert dr.title==''

def jd_sc():
    dr = webdriver.Firefox()
    dr.get('https://www.jd.com')
    unti = WebDriverWait(dr, 10)
    unti.until(lambda dr: dr.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[4]/ul[1]/li[1]/a').is_displayed())
    ww=dr.find_elements_by_class_name('cate_menu_item')
    for i in ww:
        ActionChains(dr).move_to_element(i).perform() #动作链：动作链控制鼠标移动到元素中心点(.perform动作开始执行)
        sleep(2)

def hua_dong_yan_zheng(dr,unti):
    dr.find_element_by_id('login_button').click()
    unti.until(lambda x:x.switch_to.frame('tcaptcha_iframe'))
    ww=unti.until(lambda x:x.find_element_by_id('tcaptcha_drag_button'))
    # ww=dr.find_element_by_id('tcaptcha_drag_button')
    ActionChains(dr).drag_and_drop_by_offset(ww,195,0).perform()

def main():
    gh=driver
    fun=hua_dong_yan_zheng
    ta_zai(gh)

if __name__ == '__main__':
    main()
