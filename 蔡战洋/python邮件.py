


# python 发送电子邮件
# 使用到的模块 smtplip,email

import smtplib
from email.mime.text import  MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage



# 设置服务器所需要的信息
mail_host = "smtp.163.com"      #邮件服务器的地址
mail_user= "cc524997199@163.com"    #邮箱用户名
mail_pass = "qaz123"    #邮箱有第三方授权密码，填授权码，没有可以填本身密码
mail_port = 465     #https协议加密端口465，不加密25
sender = "cc524997199@163.com"      # 发送方
receviers = ["734351303@qq.com","18237820536@163.com"]    #接收方

# 填写邮件内容
subject = "python测试邮件"  # 邮件主题
# 添加一个MIMEultipart类，处理正文及附件添加到附件里
message = MIMEMultipart()
message['from'] = Header(sender)    #发送方信息
message['To'] = Header(str(";".join(receviers)))    #接收方信息
message['Subject'] = Header(subject)       #邮件主题绑定
# 使用html格式的正文内容，添加附件
with open('abc.html','r',encoding='utf-8') as f:
    connect=f.read()
part = MIMEText(connect,'html','utf-8')  #设置html格式参数
# 一下是附件代码
with open('a.txt','r',encoding='utf-8') as  h:
    connect1=h.read()
part1 = MIMEText(connect1,'plain','utf-8') #设置txt参数
# 附件设置内容类型，方便起见，设置为二进制流
part1['Content-Type'] = 'application/octet-stream'
#设置附件头，添加文件名
part1['Content-Disposition'] = 'attachment;filename="a.txt"'
with open('捕获.png','rb') as fb:
    picture = MIMEImage(fb.read()) # MIMEImge 加载二进制图片，用于固件传输
picture['Content-Type'] = 'application/octet-stream'
picture['Content-Disposition'] = 'attachment;filename="捕获.png"'
# 将内容附件添加到邮件主题中，attach(添加的内容)
message.attach(part)
message.attach(part1)
message.attach(picture)

try:
#      第一种  #  无授权码的发
#     smtpobj = smtplib.SMTP()
#     连接服务器
#     smtpobj.connect(mail_host,25)
#     第二种 有授权码送
#     输入密码登陆邮箱
    s1 = smtplib.SMTP_SSL(host=mail_host,port=mail_port)  #链接额服务器
    s1.login(user=mail_user,password=mail_pass)     #登陆邮箱
    s1.sendmail(sender,receviers,message.as_string())   #以字符串形式发送出去
    s1.quit()   #退出
    print("ok")
except smtplib.SMTPException as e:
    print("err",e)


"""
content = "这是我使用python发送的邮件"    #邮件正文
message = MIMEText(content,'plain','utf-8')     #三个参数，第一个发送内容content,第二个plain设置文本格式，第三个编码方式

# 发送邮件是填写收件人，发件人，邮件主题
# header() 填写邮件主题

message['from'] = Header(sender)    #发送方信息
message['To'] = Header(str(";".join(receviers)))    #接收方信息
message['Subject'] = Header(subject)       #邮件主题

# 登陆并发送邮件
try:
#      第一种  #  无授权码的发
#     smtpobj = smtplib.SMTP()
#     连接服务器
#     smtpobj.connect(mail_host,25)
#     第二种 有授权码送
#     输入密码登陆邮箱
    s1 = smtplib.SMTP_SSL(host=mail_host,port=mail_port)  #链接额服务器
    s1.login(user=mail_user,password=mail_pass)     #登陆邮箱
    s1.sendmail(sender,receviers,message.as_string())   #以字符串形式发送出去
    s1.quit()   #退出
    print("ok")
except smtplib.SMTPException as e:
    print("err",e)





class smtp_1(object):
    def set_smtp(self,a1,a2,a3,a4,a5,a6):
        self.mail_host = a1  # 邮件服务器的地址
        self.mail_user = a2  # 邮箱用户名
        self.mail_pass = a3  # 邮箱有第三方授权密码，填授权码，没有可以填本身密码
        self.mail_port = a4  # https协议加密端口465，不加密25
        self.sender = a5  # 发送方
        self.receviers = a6  # 接收方
    def write_message(self,b1,b2):
        # 填写邮件内容
        subject = b1  # 邮件主题
        content = b2  # 邮件正文
        self.message = MIMEText(content, 'plain', 'utf-8')  # 三个参数，第一个发送内容content,第二个plain设置文本格式，第三个编码方式
        self.message['from'] = Header(self.sender)  # 发送方信息
        self.message['To'] = Header(str(";".join(self.receviers)))  # 接收方信息
        self.message['Subject'] = Header(subject)  # 邮件主题
    def login_send(self):
        try:
            s1 = smtplib.SMTP_SSL(host=self.mail_host, port=self.mail_port)  # 链接额服务器
            s1.login(user=self.mail_user, password=self.mail_pass)  # 登陆邮箱
            s1.sendmail(self.sender, self.receviers, self.message.as_string())  # 以字符串形式发送出去
            s1.quit()  # 退出
            print("ok")
        except smtplib.SMTPException as e:
            print("err", e)

"""
if __name__=='__main__':
    s= ["734351303@qq.com","18237820536@163.com","w18003827633@163.com"]
    gg=smtp_1()
    gg.set_smtp("smtp.163.com","cc524997199@163.com","qaz123",465,"cc524997199@163.com",s)
    gg.write_message("python发送邮件","这是我用python发送的邮件，收到请回复")
    gg.login_send()





