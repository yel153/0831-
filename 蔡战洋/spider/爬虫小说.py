# -*- coding: utf-8 -*-
# 有目的的获取网络中的资源


import requests, re

# s1 = {
#     "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
# # 1.发送url请求
# req = requests.get("https://www.fpzw.com/xiaoshuo/88/88413/", headers=s1)
# req.encoding= 'gbk'#.text的编码设置
# print(req.text)
# b= req.content.decode("gbk")
# print(b)
"""

try:
    s1 = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
    # 1.发送url请求
    req = requests.get("https://www.fpzw.com/xiaoshuo/88/88413/",headers=s1)
    # # 2.接收html文本
    req.encoding='gbk'
    res=req.text
    # res = req.content.decode("gbk")
    s2 = re.compile('<dd><a href="(.*?)">(.*?)</a></dd>')
    a1 = re.findall(s2,res)
    print(a1)
    # a2 = {}
    # for i in a1:
    #     a2[i[1]] = f"https://www.fpzw.com/xiaoshuo/88/88413/{i[0]}"
    # s5 = open(file="棋组.txt",mode="a",encoding="utf-8")
    # for j in a2:
    #     req1 = requests.get(f"{a2[j]}",headers=s1)
    #     res1 = req1.content.decode("gbk")
    #     s3 = re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*)</p>')
    #     a3 = re.findall(s3,res1)
    #     for h in a3:
    #         a4 = h.replace("<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;","")
    #         s5.write(f"{j}\n")
    #         s5.write(a4)
    #         print(f"{j}完成")
    #     s5.write("\n")
    # s5.close()
except:
    print("异常被处理啦！")
# s3 = re.compile('<h2>(.*?)</h2>')
# a2 = re.findall(s3,res)
# print(a2)
# s1 = re.compile('<title>\s*(.*)\s*</title>')
# a1 = re.findall(s1,res)
# print(a1)
"""
#
# f = open("agent.txt",encoding="utf-8")
# for i in f.read().split(","):
#     print(i)




# respose=requests.get('http://www.xiaohuar.com/v/')
# # print(respose.status_code)# 响应的状态码
# # print(respose.content)  #返回字节信息
# # print(respose.text)  #返回文本内容
# urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
# url=urls[5]
# result=requests.get(url)
# mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]
#
# video=requests.get(mp4_url)
#
# with open('b.mp4','wb') as f:
#     f.write(video.content)
#     print("ok")