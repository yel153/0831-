#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/17 14:59
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : python实践.py

import os,re,requests,pymysql,socket,smtplib,paramiko,xlrd,xlwt
from  xlutils.copy import copy
from email.header import Header
from email.mime.text import MIMEText

class shi_jian(object):

    def test_1(self,a):
        a1,a2=0,a[::-1]
        for i,k in enumerate(a2):
            for j in range(10):
                if int(k) == j:
                    a1 = j * (10 ** i) + a1
        print(a1)

    def test_2(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print(f'{j}*{i}={i*j}\t',end='')
            print()

    def test_3(self):
        # os.mkdir('aaa')
        # for i in range(5):
        #     with open('./aaa/a.txt',mode='a',encoding='utf-8') as fc:
        #         fc.write('hello world \n')
        # with open('./aaa/a.txt',encoding='utf-8') as fb:
        #     date = fb.read()
            # print(date)
        os.remove('aaa/a.txt')
        os.rmdir('aaa')

    def test_4_1(self):
        con=pymysql.connect(
            host='192.168.43.121',
            port=3306,
            user='root',
            password='123456',
            charset='utf8',
            database='spider',
        )
        self.cur=con.cursor()
    def test_4_2(self):
        self.test_4_1()
        sql_create= 'create table test_tab(id varchar(32),num varchar(32),nam varchar(32),age varchar(32)) '
        self.cur.execute(sql_create)
        a=[]
        with open('a.txt',encoding='utf-8') as fc:
            txt_date=fc.read()
            a.append(txt_date)
        txt_list=a[0].split()
        for i in txt_list:
            txt_list_1=i.split(',')
            sql_insert=f"insert into test_tab values {tuple(txt_list_1)}"
            self.cur.execute(sql_insert)

    def test_5(self):
        a=[1,2,3,4]
        b=0
        for i in a:
            for j in a:
                for k in a:
                    if i != j != k and i != k:
                        print(f'{i*(10**2)+j*10+k}')
                        b+=1
        print(f'共{b}个')

    def test_6_1(self):
        url = f'https://www.qiushibaike.com/text/'
        header={
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
                }
        html = requests.get(url=url,headers=header)
        date=html.content.decode('utf-8')
        # print(date)
        return date

    def test_6_2(self,):
        # self.test_6_1()
        re_6_1=re.compile('<div class="content">.*?<span>(.*?)</span>.*?</div>',re.S)
        re_6_2=re_6_1.findall(self.test_6_1())
        for i in re_6_2:
            a1 = i.strip()
            a2=a1.replace("<br/>","")
            print(a2)
            with open('糗事百科.txt',mode='a',encoding='utf-8')as fs:
                fs.write(f'{a2}\n')

    def test_7_1(self):
        url = 'https://www.zhipin.com/job_detail/?query=测试工程师&city=101210100'
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        html = requests.get(url=url, headers=header)
        date = html.content.decode('utf-8')
        print(date)
        return date
    def test_7_2(self):
        re_7_1= re.compile('ka=.*?target="_blank">(.*?)</a>.*?<div class="job-title">(.*?)</div>.*?<span class="red">(.*?)</span>.*?<p>(.*?)<em class="vline"></em>(.*?)<em class="vline"></em>(.*?)</p>',re.S)
        re_7_2=re_7_1.findall(self.test_7_1())
        return re_7_2
    def test_7_3(self):
        self.test_4_1()
        date_7_0=self.test_7_2()
        # self.cur.execute('create table bos(compy varchar(50),job varchar(50),pay varchar(32),jobcity varchar(50),expr varchar(20),educ varchar(20))')
        for i in date_7_0:
            print(i)
            # print(type(i))
            self.cur.execute(f'insert into boss values {i}')

    def test_8_1(self):
        ip_port=('127.0.0.1',9999)
        s_1=socket.socket()
        s_1.bind(ip_port)
        s_1.listen(5)
        print('等待客服端连接。。。')
        s_2,s_s=s_1.accept()
        while True:
            s_3=s_2.recv(1024).decode('utf8')
            print(s_3)
            s_4=input("发给客服端，1退出：")
            if s_4 != '1':
                s_2.sendall(s_4.encode())
            else:
                break
        s_1.close()
    def test_8_2(self):
        ip_port=('127.0.0.1',9999)
        c_1=socket.socket()
        c_1.connect(ip_port)
        while True:
            c_3=input('发给服务端，1退出：')
            c_1.sendall(c_3.encode())
            if c_3 != '1':
                c_4=c_1.recv(1024).decode('utf-8')
                print(c_4)
            else:
                break

    def test_9_1(self):
        mail_host = "smtp.163.com"
        mail_user = "cc524997199@163.com"
        mail_pass = "qaz123"
        mail_port = 465
        sender = "cc524997199@163.com"
        receviers = ["cc524997199@163.com"]
        subject = "python测试邮件"
        content = "这是我使用python发送的邮件"
        message = MIMEText(content, 'plain', 'utf-8')
        message['from'] = Header(sender)
        message['To'] = Header(str(";".join(receviers)))
        message['Subject'] = Header(subject)
        s1 = smtplib.SMTP_SSL(host=mail_host, port=mail_port)
        s1.login(user=mail_user, password=mail_pass)
        s1.sendmail(sender, receviers, message.as_string())
        s1.quit()
        print("ok")

    def test_10_1(self):
        date_10_11=[]
        with open('a.txt',encoding='utf-8') as fc:
            date_10_11.append(fc.read())
        # print(date_10_1)
        date_10_10=date_10_11[0].split()
        date_10_13=[]
        for i in date_10_10:
            date_10_12=i.split(',')
            date_10_13.append(date_10_12)
        return  date_10_13
    def test_10_2(self):
        try:
            date_10_20 = self.test_10_1()
            date_10_21 = xlrd.open_workbook('txt.xls')
            date_10_22 = copy(date_10_21)
            date_10_23 = date_10_22.add_sheet('txt内容')
            a=0
            for i in date_10_20:
                b=0
                for j in i:
                    date_10_23.write(a,b,j)
                    b+=1
                a+=1
            date_10_22.save('txt.xls')
            print('ok')
        except:
            date_10_20 = self.test_10_1()
            date_10_21 = xlwt.Workbook('txt.xls')
            date_10_22 = date_10_21.add_sheet('txt内容')
            a = 0
            for i in date_10_20:
                b = 0
                for j in i:
                    date_10_22.write(a, b, j)
                    b += 1
                a += 1
            date_10_21.save('txt.xls')
            print('ok')

    def test_11_1(self):
        s_11_0=paramiko.Transport('192.168.10.28',22)
        s_11_0.connect(username='root',password='123456')
        s_11_1=paramiko.SFTPClient.from_transport(s_11_0)
        s_11_2= '/home/qaz123/因数.sh'
        s_11_3= '/home/qaz123/选择.sh'
        s_11_1.get(s_11_2,'D:因数.sh')
        s_11_1.get(s_11_3,'D:选择.sh')



    def test_12_1(self,a1):
        a2, a3 = 0, 0
        for i in os.listdir(a1):
            # print(i)
            if os.path.isdir(f'{a1}\{i}'):
                a2 += 1
            elif os.path.isfile(f'{a1}\{i}'):
                a3 += 1
        print(f"目录{a2}个，文件{a3}个")






    def txt_1(self):
        for i in range(100):
            with open('a.txt', mode='a', encoding='utf-8') as fc:
                fc.write('zhe,shi,bowen,123\n')



if __name__ == '__main__':
    GG = shi_jian()
    # GG.test_7_3()


# with open('a.txt',encoding='utf-8') as fg:
#     pp = fg.read()
#     print(tuple(pp))

