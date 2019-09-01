#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/17 9:34
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : qqlog.py



import logging
import datetime

# logging ----> python 定义日志的库

# 日志文件夹/目录
LOG_DIR= 'C:\\Users\\Darcy\\Desktop\\QQ\\AndroidQQ\\Log\\' # 大写变量代表一般不随意改动
a = LOG_DIR+str(datetime.datetime.now().date())+'.txt' # 时间类型变str


# 定义日志输出的格式
fomat=logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
datefmt='%d-%m-%Y:%H:%M:%S'
)
print(fomat)#内存地址

# logging的两种输出方式
#  第一种输出到pycharm控制台
c=logging.StreamHandler()
# 添加日志的样式
c.setFormatter(fomat)

# 第二种输出到文本
d=logging.FileHandler(a,encoding='utf-8')
# 添加到日志样式
d.setFormatter(fomat)

def get_logger(filename):
# 获取执行日志的脚本名字
    l = logging.getLogger(filename)
# 添加输出内容到控制台
    l.addHandler(c)
# 添加输出内容到文本
    l.addHandler(d)
# 定义日志等级 INFO-->最低等级
    l.setLevel(logging.INFO)
    return l


# log=get_logger()
# log.info('sfudiayf')
# log.error('fyuftfdtd')