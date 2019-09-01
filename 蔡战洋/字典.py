#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/12 21:17
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : 字典.py

import random,numpy
from python_main import d
from mysql import sqlserver


# class excel(object):
#     def open_excel(self):
#         pass


class py_class(object):

    def suan_99(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print("{}*{}={}\t".format(i,j,i*j),end="")
            print()

    def hui_wen(self):
        a= input("判断回文，请输入一个字符串：")
        a1 = len(a)//2
        for i in range(a1):
            if a[i] != a[-(i+1)]:
                print("{}不是回文".format(a))
                break
        else:
            print(f"{a}是个回文")

    def zhi_shu(self):
        a=0
        for i in range(2,100):
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                a += i
        print(a)

    def jie_cheng(self):
        a,b=1,0
        for i in range(1,10):
            a *= i
            b += a
        print(b)

    def yin_shu(self):
        for i in range(1,1001):
            a = 0
            for j in range(1,i):
                if i % j == 0:
                    a += j
            else:
                if a == i:
                    print(i)

    def shuixain_hua(self):
        for i in range(100,1000):
            a,a1,a2=i//100,i//10%10,i%10
            if a**3 + a1**3 + a2**3 == i :
                print(i)

    def zifu_cuan(self):
        a=input("请输入一组字符，以空格分开：")
        a1 = a.split()
        a2,a3=0,0
        for i in a1:
            if i.isdigit():
                a2 += 1
            elif i.istitle():
                a3 += 1
        print(f"这段话里首字母大写的有{a3}个,全数字的有{a2}个")

    def mao_pao(self):
        a = input("请输入一个数组，空格分开：")
        a1 = a.split()
        a2 = len(a1)-1
        for i in range(len(a1)):
            for j in  range(a2):
                if int(a1[j]) < int(a1[j+1]):
                    a1[j],a1[j+1]=a1[j+1],a1[j]
        print(a1)

    def xuan_ze(self):
        a = input("请输入一个数组，空格分开：")
        a1 = a.split()
        a2 = len(a1)
        for i in range(a2):
            for j in range(i+1):
                if int(a1[j]) < int(a1[i]):
                    a1[j], a1[i] = a1[i], a1[j]
        print(a1)

    def qu_chong(self):
        a = [1,2,3,4,5,6,7,8,4,5,6]
        b= set(a)
        print(list(b))

    def differ_shu(self):
        a = 0
        for i in range(1,10):
            for j in range(0,10):
                for k in range(0,10):
                    if i != j != k and i != k:
                        a += 1
        print(a)

    def str_int(self):
        a = input("请输入一个数字：")
        a1,a2=0,a[::-1]
        for i,j in enumerate(a2):
            for k in range(10):
                if str(k) == j:
                    a1 = k * (10**i) + a1
        print(a1)

    def country_count(self):
        a = d["data"]["msg"]
        a1=[]
        for i in a:
            if i["country"] not in a1:
                a1.append(i["country"])
        print(a1)

    def height_count(self):
        a = d["data"]["msg"]
        a1,a2 = [],1
        for i in a:
            a3 = "s_"+str(a2) #a3 =f"s_{a2}"
            a1.append(i[a3][-1])
            a2 += 1
        a1.sort()
        print(f"所有学生身高范围在{a1[0]}-{a1[-1]}之间")

    def sex_count(self):
        a = d["data"]["msg"]
        a1= []
        for i in a:
            a2,a3=i.keys()
            a1.append(i[a2][1])
        a4,a5 = a1.count("男"),a1.count("女")
        print("学生的男女比例为{}:{}".format(a4,a5))

    def avg_height(self):
        a = d["data"]["msg"]
        a1 = []
        for i in a:
            a2, a3 = i.keys()
            a4=i[a2][-1].rstrip('cm')
            a1.append(int(a4))
        a5= numpy.mean(a1)
        print(f"平均身高：{a5}cm")

    def height_170_180(self):
        a = d["data"]["msg"]
        a1 = []
        for i in a:
            a2, a3 = i.keys()
            a4 = i[a2][-1]
            if '170cm' <= a4 <= '180cm':
                a1.append(i[a2][0])
        print(a1)

    def print_1_4(self):
        for i in range(1,10):
            print('*' * i)
        else:
            a = i-1
            while a>0:
                print('*' * a)
                a -= 1

    def san_jiao_xing(self):
        a = int(input("请输入一条边"))
        a1 = int(input("请输入一条边"))
        a2 = int(input("请输入一条边"))
        if a + a1 > a2 and a - a1 < a2:
               if a**2 + a1**2 == a2**2 or a2**2 + a**2 == a1**2 or a1**2 + a2**2 == a**2:
                   print("直角三角形")
               elif a1**2 + a2**2 < a**2 or a**2 + a1**2 < a2**2 or a**2 + a2**2 < a1**2:
                   print("钝角三角形")
               elif a**2 + a1**2 > a2**2 or a2**2 + a1**2 > a**2 or a2**2 + a**2 > a1**2:
                   print("锐角三角形")
        else:
            print("输入的边构不成三角形")

    def cai_shu(self):
        a = input('猜数字0-9之间，三次机会，请输入一个数字：')
        a1 = random.randint(0,10)
        # print(a1)
        a2 = 3
        while a2 > 1:
            a2 -= 1
            if a ==  str(a1):
                print(f'恭喜你猜对了随机数：{a1}')
                break
            else:
                a = input(f'猜错了，还有{a2}次机会，请输入一个数字：')

    def py_19(self):
        a = 0
        for i in range(1,100):
            for j in range(1,100):
                if i - 0.5 * j == 0 and 100-i-j > 0:
                    a += 1
                    print(f'公鸡：{i}母鸡:{100-i-j}小鸡：{j}')
        print(f'共有{a}种购买方式')


    def max_1_2(self):
        a = [1,2,3,7,5,6,7]
        print(max(a))

    def print_1_3(self):
        a = 1
        while a<=10:
            b=1
            while b <= a:
                print('*',end="")
                b+=1
            print()
            a+=1
        while a>0:
            a-=1
            print('*' * a)

if __name__ == '__main__':
    # adc=spider_mysql()
    # adc.new_main_table()
    pass
    # adc = py_class()
    # adc.py_19()


# print(a.strip('j'))







class spider_mysql(object):
    # sqlserver('192.168.10.32',3306,'root','123456')
    def new_main(self):
        a1 = input('是否要新建库，输入任意字符新建，输入N不建：')
        if a1 != 'N':
            sqlserver('192.168.10.32',3306,'root','123456').create_database('spider')

    def new_main_table(self):
        self.curs = sqlserver('192.168.10.32', 3306, 'root', '123456').connect.cursor()
        a = input('是否要建表，输入任意新建，输入n不建：')
        if a != 'n':
            a1 = input('使用库名：')
            a2 = input('新建表名：')
            a3 = input('字段名，字段类型')
            sql1 = f' use {a1}'
            sql2 = f'create table {a2} ({a3})'
            self.curs.execute(sql1)
            self.curs.execute(sql2)
  #           职位 varchar(100),公司链接 varchar(100),公司名称 varchar(100),薪资 varchar(100),地点 varchar(100)
  #
  #
  # 职位 varchar(100),公司链接 varchar(100),公司名称 varchar(100),薪资 varchar(100),地点 varchar(100)





a = {"w":1,"e":2}
a["o"]=2
print(type(a))



