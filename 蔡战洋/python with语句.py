# -*- coding: utf-8 -*-
# python with
# 应用场合：主要是操作系统资源，建立连接，python线程，进程的关闭释放
# 一种概念：上下文管理



# with...as
with open("a.txt",encoding="utf-8") as s1:
    a1 = s1.read()
print(a1)

