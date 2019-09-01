
# python -- 操作linux
# 需要导入模块  paramiko



import paramiko
"""
# 连接unix系统
s1 =paramiko.SSHClient()  #第一步，创造一个sshclien对象
s1.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #建立连接第二部，信任linux的主机，类似xshell第一次连接的保存信息
s1.connect(
    hostname="192.168.10.26",
    port=22,
    username="qaz123",
    password="123"
) #第三步使用connect()连接linux主机
# stdin,stdout,stderr = s1.exec_command('ls -al')     # 执行linux命令 exec_command() ，stdin：代表输入命令 stdout：命令输出结果 stderr：内容接收变量
# print(stdout.read().decode())  # 查看内容    输出变量.read().decode()

# sftp = paramiko.SFTPClient(s1)  #创建一个文件传输通道  SFTPClient(参数)：SFTPClient sftp客服端方法，参数 之前建立的连接
# a1 = 'js.sh'  # 传输的文件
# a2 = './'   # 保存的位置
# sftp.get(a1,a2)   #执行命令




x1 = paramiko.Transport(("192.168.10.26",22)) #第二种连接方式 Transport(()):端口号连接linux系统，ip地址，端口号元组
x1.connect(username="qaz123",password="123")  #
# sftp = paramiko.SFTPClient.from_transport(x1)  #SFTPClient.from_transport(x1):sftp客服端方法
# a1 = 'js.sh'  # 传输的文件
# a2 = 'js.txt'   # 保存的位置     第二种：r'保存文件路径' 必须要加保存后的文件名
# sftp.get(a1,a2)   #执行命令  get（远程文件，本地文件）下载    put（本地文件，远程文件）上传
x1.close()
s1.close()

"""

class linux_1(object):
    def __init__(self,a1,a2,a3,a4):
        self.b1 = paramiko.Transport((a1,a2))
        self.b1.connect(username=a3,password=a4)
    def linux_2(self):
        stdin,stdout,stderr = self.b1.exec_command('ls -al')     # 执行linux命令 exec_command() ，stdin：代表输入命令 stdout：命令输出结果 stderr：内容接收变量
        print(stdout.read().decode())  # 查看内容    输出变量.read().decode()
        self.b1.close()
    def linux_3(self,b3,b4):
        b2 = paramiko.SFTPClient.from_transport(self.b1)
        b2.get(b3,b4)
        self.b1.close()
# cx = linux_1("192.168.10.26",22,"qaz123","123")
# cx.linux_2()


# import pyperclip
# pyperclip.copy('hello world')  #复制
# print(pyperclip.paste())   #粘贴

# # python 与系统交互 window，mac，uninx
# # python的内置模块 ，os库
#
# import os
# # os.startfile('.exe的绝对路径') 打开一个应用程序
# print(os.getcwd()) # 获取当前目录
# os.chdir('A')#  os.chdir(目录名字) 切换到指定目录
# print(os.getcwd())
# # 返回目录：os.curdir 代表一个点  os.pardir 代表两个点
# os.chdir('./')
# a = os.getcwd()
# print(a)
# a = os.name #获取操作系统的类型  nt window ，posix linux
# os.makedirs("aaaa/aaa/aa")# 创建多级目录
# os.mkdir("aaa")#创建一个目录
# os.removedirs("aaa")#删除多个目录
# os.rmdir("aaa")#删除一个空目录 知删除空目录
# a = os.listdir('D:\安装包') #查看当前目录下所有文件，目录，包括隐藏  绝对路径 ,返回元组
# os.rename('/Users/Darcy/Desktop/文件/aaaa','/Users/Darcy/Desktop/文件/aaab')
# print(os.popen('dir'))  #执行系统命令
# for a,b,c in os.walk('/Users/Darcy/Desktop/文件'):  #目录树
#     print(b)
#
#
# os.path 类
# print(os.path.abspath("A")) #返回文件绝对路径
# print(os.path.dirname(r'\Users\Darcy\Desktop\文件'))  #返回文件的上一级目录
# print(os.path.basename(r'\Users\Darcy\Desktop\文件'))  #返回文件
# print(os.path.exists(r'\Users\Darcy\Desktop\文件')) #判断文件是否存在，返回布尔值
# print(os.path.isdir('路径'))  #判断是否为目录
# print(os.path.isfile(r'\Users\Darcy\Desktop\文件'))  #判断是否为文件
# print(os.path.islink(r'\Users\Darcy\Desktop\文件')) #判断文件是否为连接文件
# print(os.path.join('/Users/','fdslf'))  #文件路径拼接
# print(os.path.split(r'\Users\Darcy\Desktop\文件'))  #文件路径分离，返回一个元组，路径与最后一个文件分隔
# print(os.path.splitext(r'\Users\Darcy\Desktop\文件'))  #分隔文件后缀名,返回一个元组





"""统计目录下有多少文件，目录"""
class any(object):
    def __init__(self,a1):
        self.a1 = a1
    def count_list(self):
        a2,a3 = 0,0
        for i in os.listdir(self.a1):
            print(i)
            if os.path.isdir(f'{self.a1}\{i}'):
                a2 += 1
            elif os.path.isfile(f'{self.a1}\{i}'):
                a3 += 1
        print(f"目录{a2}个，文件{a3}个")
# asd = any(r'D:\安装包')
# asd.count_list()




import time
# python 时间

# time.sleep(4)# 睡眠 浮点数，整数，单位秒
# print(time.clock()) #cpu执行一段代码的时间
# print(time.ctime()) #打印当前时间
# print(time.asctime())
# print(time.localtime())
# print(time.strftime("%a %d %B %H:%M:%S"))  #输出为字符串
# print(time.strptime("30 Nov 00", "%d %b %y"))# 根据格式解析表示时间的字符串
# print(time.time()) # 距离计算机元年过去的时间
#
#
# from datetime import *
# print(datetime.now())# 获取当前时间，日期
# print(datetime(1994,11,9,9,1,1))# 获取指定的时间，日期
# print(datetime.strptime('1994-11-09 09:01:01','%Y-%m-%d %H:%M:%S'))# 字符串时间转datetime日期
# print(datetime.now().strftime("%a %d %B %H:%M:%S")) #日期转字符串
# now = datetime.now()
# print(now + timedelta(hours=5))  #日期加减
# print(date.today()) #只获取当前日期
# print(date.today()-timedelta(days=2))  #日期加减
