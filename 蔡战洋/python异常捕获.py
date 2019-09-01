# -*- coding: utf-8 -*-
# python异常处理
# 1.错误
# python 语法错误：书写格式class，缩进
# 代码逻辑：python解释器无法使用编译解释，导致python错误
# 2.异常
# 处理错误的过程被称为异常处理
# try...except 最简单的异常捕获




try:
    a = 1 / 0
    print(a)
except (ZeroDivisionError,AssertionError): #多个异常条件添加
    print("异常被处理哈啦啦！")
except ImportError:  # 多个except书写
    print("ImportError异常被处理啦啦！")


# try ...except...finally
try:
    a = 1 / 0
    print(a)
# except (ZeroDivisionError,AssertionError): #多个异常条件添加
    print("异常被处理啦啦！")
except :  # 多个except书写
    print("ImportError异常被处理啦啦！")
finally:
    print("无论异常是否被处理，都会输出finally下面的代码")

# try...except...else
try:
    a = 1 / 1
    print(a)
except (ZeroDivisionError,AssertionError): #多个异常条件添加
    print("异常被处理啦啦！")
except ImportError:  # 多个except书写
    print("ImportError异常被处理啦啦！")
else:
    print(a)



