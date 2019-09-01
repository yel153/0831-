#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/16 17:24
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : qqmima.py


with open(file=r'C:\Users\Darcy\Desktop\QQ\AndroidQQ\Date\mima.txt',encoding='utf-8') as fb:
  dates=fb.read().split(';')
  s=[]
  for i in dates:
    lik=i.replace('\n','').split(',')
    s.append(tuple(lik))


class ClassTest(object):
  __num = 0

  @classmethod
  def addNum(cls):
    cls.__num += 1

  @classmethod
  def getNum(cls):
    return cls.__num

  # 这里我用到魔术方法__new__，主要是为了在创建实例的时候调用累加方法。
  def __new__(self):
    ClassTest.addNum()
    return super().__new__(self)


class Student(ClassTest):
  def __init__(self):
    self.name = ''


# a = Student()
# b = Student()
# print(ClassTest.getNum())



class classstu():
  __ko=0

  @classmethod
  def addko(cls):
    cls.__ko+=1

  @classmethod
  def getko(cls):
    return cls.__ko

  def __new__(self):
    classstu.addko()
    return super().__new__(self)

class student(classstu):
  def __init__(self):
    self.nae='yuqwr'



class name:
  def __init__(self,a,b,c):
    self.a=a
    self.b=b
    self.c=c
  def print_num(self):
    print(self.c)

class stu(name):
  def __init__(self,q,w,e,r,t):
    name.__init__(self,q,w,e)
    self.r=r
    self.t=t
  def print_stu(self):
    print(self.r)
    self.print_num()
  def __new__(cls, *args, **kwargs):
    print('hello')


"---------------------------------------------------------------------------------------------------"
"-------------------------------------------------------------------------------------------"
"-------------------------------------------------------------------------------"
"------------------------------------------------------------------"
"----------------------------------------------------"
"---------------------------------------"
"----------------------------"
"------------------"
"---------"
