# 套接字 抽象
# 完成两个应用程序之间的数据传输
# 模块 socket

import socket

ip_port = ('127.0.0.1',9789)  #指定服务器的ip地址，监听端口号
s1 = socket.socket()  #建立一个套字节，客服端与服务器传输信息
s1.bind(ip_port)    #绑定服务地址和端口号
s1.listen(5)   #设置最大连接数
print('启动socket服务，等待客服端连接...')
a1,address = s1.accept()  #socket 自动处理拥塞控制 accept(),持续开启一直到手动关闭
# a2 = a1.recv(1024).decode('utf-8')   #第一步接收客服端发送的请求 recv()设置发送数据大小
# print(a2)
# a3 = input('请输入发送内容:')
# s1.sendall(a3.encode())
while True:
    a2 = a1.recv(1024).decode('utf-8')
    print(f'客服端向服务器发送的消息:{a2}')
    a3 = input('请输入发送客服端内容:')
    if a3 == "1":
        break
    else:
        # 发送信息给客服端
        # 1.先找到客服端
        # 2.使用sendall
        a1.sendall(a3.encode())
s1.close()

# print(adress)




