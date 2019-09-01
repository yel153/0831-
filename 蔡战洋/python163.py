#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/18 19:43
# @Author : "Darcy J"
# @Email : cc524997199@163.com
# @File : python163.py

import smtplib,os,base64
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class mail_163(object):

    def __init__(self,mail_host,mail_name,mail_passwd,
                 mail_recv,mail_subject,mail_connect,
                 mail_text=None,mail_file=None,mail_image=None,
                 mail_ssl=False,port=25,ssl_port=465):
        self.mail_host=mail_host
        self.mail_name=mail_name
        self.mail_passwd=mail_passwd
        self.mail_recv=mail_recv
        self.mail_subject=mail_subject
        self.mail_connect=mail_connect
        self.mail_text=mail_text
        self.mail_file=mail_file
        self.mail_image=mail_image
        self.mail_ssl = mail_ssl
        self.port=port
        self.ssl_port=ssl_port
    def write_mail(self): #写邮间，添加附件
        msg=MIMEMultipart()
        if self.mail_connect: #邮件正文内容
            try:
                part_con=MIMEText(self.mail_connect)
            except:
                print("读取邮件内容出错")
            else:
                msg.attach(part_con)#,'plain','utf-8')
        if self.mail_text:
            txt_Name=os.path.split(self.mail_text)[-1]
            try:
                with open(self.mail_text,'r',encoding='utf-8') as fa:
                    part_txt=fa.read()
            except:
                print('读取附件文本错误')
            else:
                part_txt=MIMEApplication(part_txt)
                part_txt.add_header('Content-Disposition', 'attachment', filename=txt_Name)
                msg.attach(part_txt)
        if self.mail_image: #图片附件
            image_Name=os.path.split(self.mail_image)[-1]
            try:
                with open(self.mail_image,'rb') as fb:
                    image_file=fb.read()
            except:
                print("读取邮件图片错误")
            else:
                part_image=MIMEImage(image_file,image_Name.split('.')[-1])
                part_image.add_header('Content-Disposition', 'attachment', filename=image_Name)
                msg.attach(part_image)
        if self.mail_file: #邮件附件内容
            flie_Name = os.path.split(self.mail_file)[-1]
            try:
                with open(self.mail_file,'rb') as fc:
                    xls_file=fc.read()
            except:
                print('读取邮件表格出错类')
            else:
                part_xls=MIMEApplication(xls_file)
                part_xls.add_header('Content-Disposition', 'attachment', filename=flie_Name)
                msg.attach(part_xls)
        msg['from'] = Header(self.mail_name)  # 发送方信息
        msg['To'] = Header(str(";".join(self.mail_recv)))  # 接收方信息
        msg['Subject'] = Header(self.mail_subject)
        return msg
    def send_mail(self):
        if self.mail_ssl:
            set_smtp=smtplib.SMTP_SSL(host=self.mail_host,port=self.ssl_port)
        else:
            set_smtp=smtplib.SMTP(host=self.mail_host,port=self.port)
        try:
            set_smtp.login(self.mail_name,password=self.mail_passwd)
            set_smtp.sendmail(self.mail_name,self.mail_recv,self.write_mail().as_string())
            print('邮件发送ok')
            set_smtp.quit()
        except:
            print('发送失败')

if __name__ == '__main__':
    m=mail_163(
        mail_host='smtp.163.com',  #邮箱服务器
        mail_name='cc524997199@163.com', #自己的邮箱
        mail_passwd='qaz123',    #自己邮箱密码，或者授权码
        mail_recv=["734351303@qq.com","18237820536@163.com","cc524997199@163.com" ],   #接收方 邮箱
        mail_subject='python测试邮件',  #邮件主题
        mail_connect='这是我用python发送的第一封邮件，收到请回复',    #邮件内容
        mail_text=r'C:\Users\Darcy\Desktop\蔡战洋\xlstext\文本文档.txt',#邮件附件。txt绝对路径
        mail_file=r'C:\Users\Darcy\Desktop\蔡战洋\xlstext\js.txt',  #邮件附件
        mail_image=r'E:\猫\猫.jpg', #邮件附件图片
        mail_ssl=True  #是否为安全连接，是ture否flase
    )
    m.send_mail()





# flie_name = os.path.split(r'C:\Users\Darcy\Desktop\蔡战洋\xlstext\51job.xls')
# with open(r'C:\Users\Darcy\Desktop\蔡战洋\xlstext\51job.xls',mode='r', encoding='utf8') as fc:
#     xls_file = fc.read()
#     # asd=MIMEText(xls_file,base64,'utf-8')
#     print(xls_file)
