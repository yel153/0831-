import socket
ip_port = ('127.0.0.1',9789)  #指定客服端ip，端口号
c = socket.socket()  #创建套接字，接收服务器发送的数据
c.connect(ip_port)  #连接服务器
# 发送数据到服务器，接收服务器数据
# t = input('输入发送数据：')
# 发送
# c.sendall(t.encode())   #发送所有数据到服务器 :sendall() encode()编码方式发送二进制
while True:
    t = input('请输入发送服务端内容:')
    if t == "1":
        print('关闭服务端')
        break
    else:
        # print("客服端向服务器发送的信息")
        c.sendall(t.encode())
        a1 = c.recv(1024).decode('utf-8')
        print(a1)
c.close()







