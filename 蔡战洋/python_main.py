# -*- coding: utf-8 -*-
# c = True
# a = False
# name = input("请输入用户名：")
# passwd = input("请输入密码：")
# if name =="cai":
#    if passwd =="123456" :
#           print("登陆成功")
#    else:
#        print("密码错误")
# else:
#    print("用户名或者密码错误")


# 运算符
# nu_1 = 10
# nu_2 = 20

# t = nu_1 + nu_2
# print(t)
# h = nu_1 - nu_2
# print(h)
# i = nu_1 * nu_2
# print(i)
# j= nu_2 / nu_1
# print(j)
# k = nu_2 % nu_1
# print(k)
# print(nu_1 ** nu_2)
# l = nu_2 // nu_1
# print(l)


# 运算符计算器
# q = int(input("请输入数字:"))
# a = int(input("请输入数字:"))
# z = input("请输入计算方式:")
# if z == "加":
#    w = q + a
#    print(w)
# elif z == "减":
#    s = q - a
#    print(s)
# elif z == "乘":
#    x = q * a
#    print(x)
# elif z == "除":
#    e = q / a
#    print(e)


# 判断成绩
# a = int(input("请输入成绩哦"))
# if 90 <= a:
#    print("优秀")
# elif 80 <= a < 90:
#    print("良好")
# elif 60 <= a < 80:
#    print("及格")
# elif  a < 60:
#    print("还要努力！不及格")


# 赋值运算符
# a = 2
# a += 126
# print(a)
# a -= 126
# print(a)
# a *= 126
# print(a)
# a /= 126
# print(a)
# a %= 126
# print(a)
# a **= 126
# print(a)
# a //= 126
# print(a)


# a = 3
# b = 2
# c = 1
# if  not c > b:
#    print("a最大")
# else:
#    print("假")









# 判断三角形
# a = int(input("请输入边"))
# b = int(input("请输入边"))
# c = int(input("请输入边"))
# if c + b > a and c - b < a:
#    if b**2 + c**2 == a**2 or b**2 + a**2 == c**2 or a**2 + c**2 == b**2:
#        print("直角三角形")
#    elif b**2 + c**2 < a**2 or a**2 + c**2 < b**2 or b**2 + a**2 < c**2:
#        print("钝角三角形")
#    elif b**2 + c**2 > a**2 or a**2 + c**2 > b**2 or b**2 + a**2 > c**2:
#        print("锐角三角形")
# else:
#    print("输入的边构不成三角形")





# 三个数字排序
# a = int(input("请输入数"))
# b = int(input("请输入数"))
# c = int(input("请输入数"))
# if a > b > c :
#    print(a,b,c)
# elif a > c > b :
#    print(a,c,b)
# elif b > c > a :
#    print(b,c,a)
# elif b > a > c :
#    print(b,a,c)
# elif c > a > b:
#    print(c,a,b)
# elif c > b > a :
#    print(c,b,a)


# a = "1234567890"
# b = "23"
# if b in a:
#    print("zhen")


# a = ""
# if a:
#    print("a")
# else:
#    print("abs")
# b = len(a)
# print(b)


# c="abc"
# d="def"
# e=c + d
# print(e * 5)


# find()查找字符串中的子字符串，如果找到，返回子字符串的第一个字符索引值，找不到结果是-1
# rfind()查找字符串中的子字符串，如果找到，返回子字符串的第一个字符索引值，找不到结果是-1(从右往左)
# a="hello"
# b="j"
# print(a.find(b))
# index()查找字符串中的子字符串，如果找到，返回子字符串的第一个字符索引值，找不到抛出异常
# rindex()查找字符串中的子字符串，如果找到，返回子字符串的第一个字符索引值，找不到抛出异常(从右往左)
# print(a.index(b))
# 异常报错的关注点
# 最后一行指的是报错类型，报错内容
# 上边一行显示报错位置


# title() 将英文字母单词首字母大写，其他字母小写
# a="hello world"
# print(a.title())

# upper() 将所有英文小写字母转换成大写字母
# print(a.upper())

# swapcase() 大写转小写,小写变大写。本身互换格式
# a="SDFGHJK TUI"
# print(a.swapcase())

# count() 统计子字符串在字符串中出现的次数，返回结果是数字
# a = "1234567891234567891234567890"
# c = "9"
# print(a.count(c)

# startswith() 判断字符串是否以某个子字符串开头，是的话返回布尔值true，不是返回false
# print(a.startswith("12"))

# endswith() 判断字符串是否以某个子字符串结尾，是的话返回布尔值true，不是返回false
# print(a.endswith("0"))

# max()求字符串中的最大值，返回的是根据字符的编码方式 ascii码 对应的最大值字符
# a = "12345678azsxdcfv"
# print(max(a))
#
# min()求字符串中的最大值，返回的是根据字符的编码方式 ascii码 对应的最大值字符
# print(min(a))


# 格式化字符串输出
# 1.f"字符串{变量名}"
# 2."字符串{}".format(变量名)
# a = "bowen"
# b = f"banji{a}"
# print(f"jiwen{a}")


# split()：切割字符串，指定字符或者字符串进行切割，返回一个表，指定切割次数,指定字符不能为空
# a = input("请输入单词,以空格分开")
# b = a.split(" ")
# print(f"最后一个单词的长度是：{len(b[-1])}")
#
#
# lstrip() 删除字符串中的指定字符，不指定默认删除空格，左侧开头开始，指定字符不存在就不删除
# a = " studit good studay jikl"
# print(f"原始字符：{a}")
# print(f"删除后：{a.lstrip()}")
#
# rstrip() 删除字符串中的指定字符，不指定默认删除空格，右侧开头开始，指定字符不存在就不删除
# strip() 删除字符串中的指定字符，不指定默认删除空格，两边同时开始，指定字符不存在就不删除
#
#
# replace() 替换字符串中的字符或子字符串，第一个是原始字符，第二个新的字符.如果原始字符不存在，就不替换原样输出
# a = "what are you saying"
# print(a.replace(" ",","))
#
#
# join() 将列表中的元素拼接成字符串，第一个变量是字符串，第二个必须是列表
# a = "_"
# b = ["1","2","3"]
# print(a.join(b))


# isdigit()判断字符串是否全部是数字，如果是返回true，否则返回false
# a = "123k"
# print(a.isdigit())
#
# istitle()判断字符串是否为标题，如果是返回true，否则返回false
# isupper()判断字符串中的字母是否全部是大写，如果是返回true，否则返回false
# islower()判断字符串中的字母是否全部是小写，如果是返回true，否则返回false
# isalnum()判断字符串中所有字符是否有数字或者字母组成，如果是返回true，否则返回false
# a = "hjk\n"
# print(a.isalpha())
# isalpha() 判断字符串中所有的字符全部是字母，如果是返回true，否则返回false
# isspace()判断字符串中只包含空白字符，如果是返回true，否则返回false 空白字符包含 \n \r \t
# isdecimal()判断字符串中是否只包含十进制的数字，如果是的话返回true，否则返回fals
# 0o（数字0，字母o）代表八进制



# 列表的组成
# 1.英文的中括号
# 2.列表里可以放字符串，数字，列表，元组，字典，集合
# 3.有序的，可以变得数据容器【列表的定义】
# 4.每个元素以英文的逗号分割

# 定义一个列表
# a = ["abc","1",["hello","2019"]]
# print(a)
# 定义一个空列表，返回false
# a = []  0，空字符串，空列表，空元组，空字典，空集合，在if条件判断下返回false

# 当列表只取一个元素时返回该元素本身的数据类型
# type()：用来判断数据类型
# print(type(a[0]))

# 提取列表中列表的元素
# b = a[-1]
# print(b[0]) == print(a[-1][0])

# 替换列表的元素
# a[0] = "hello"
# print(a)

# 向列表添加元素，append(需要添加的元素)，在列表尾部添加元素
# a.append("world")
# print(a)

# 列表支持拼接
# a = [1,2,3]
# b = ["a","b","c"]
# c = a + b
# print(c)

# 支持重复输出，将重复输出的元素放到一个列表内
# print(a * 2)

# 列表反转
# print(a[::-1])
#
# count()：统计列表中某个元素出现的次数，返回数值
# print(a.count("a"))
#
# extend(需要添加的元素)：向列表中添加多个元素，默认在尾部。可以是列表，元组，集合，字典
# a = [123,3,45,123]
# b = [134.67,90]
# a.extend(b)
# print(a)

# index(需要查找的元素)：如果找的到返回该元素对应的索引值，找不到抛出异常
# a = ["123","567"]
# print(a.index("123"))

# insert(index,需要添加的元素)：向列表内的指定位置添加元素
# index：指的是索引值
# a = [1,2,3]
# a.insert(1,87)
# print(a)

# pop(索引值)：删除列表中的元素，当索引值不写，默认删除最后一个元素
# a = [1,2,3,4,5,6,7,8,9]
# print(a.pop())#显示被删除的元素
# print(a)

# remove(指定需要删除的元素)：输出列表的元素,删除一次
# a = [1,2,3,4,1,6,7]
# a.remove(2)
# print(a)

# reverse():反转列表中的元素
# a = [1,2,3,4,5]
# a.reverse()
# print(a)

# sort(reverse=false):对列表中的元素进行排序，按照ascii码排序，默认是升序.不能有多种类型数据
# reverse = true 降序
# a = [1,2,98,4,45]
# a.sort(reverse=1)
# print(a)

# clear()：清空列表
# a.clear()
# print(a)

# copy()：复制列表。浅copy
# b = a.copy
# print(b)

# len()求列表长度
# print(a.len())

# max()求列表中的最大值
# print(max(a))
# min()求列表中的最小值
# print(min(a))

# list()：将非列表类型转换为列表类型
# a = "12345"
# print(list(a))

# enumerate(列表名)：列表元祖转换成有序的序列
# a = [1,2,3,4,5]
# for h,i in enumerate(a):
#     print(h,i)


# python 基本数据类型--字典
# 以键值对的形式保存数据
# 键必须是唯一的
# 值可以是一个或者多个
# 值可以是数值类型，字符串类型，元组类型，集合类型，列表类型，字典类型
# d = {
#     "a":123,
#     "b":["lieiao","shangp",123],
#     "c":{"1":23,"2":["e","f"]}
# }
# print(d.values())
# a=1
# a=2
# print(a)




# seq = [1,2,3]
# b = dict.fromkeys(seq,"一百")
# print(b)
#
# c = d.items()
# print(c)
# for e in d.items():
#     print(e)
# a = {1:2,2:3}


# if 0:
#     print("o")


# for循环  for 变量（起始值） in 可迭代对象:
#              可执行语句块
# 可迭代对象： 字符串，列表，元祖，集合


# s = "hello world"
# for i in s:
# print(f"子字符是{}")


# python内置函数 range（）范围









# 九九乘法表
# for i in range(1,10):
#     for h in  range(1,i + 1):
#         print(f"{h} * {i} = {i * h}\t",end="")
#     print("")








# 判断输入字符是否为回文
# a = input("请输入字符：")
# b = len(a)
# c = 0
# for i in  range(b):
#     if a[i] == a[-(i+1)]:
#         pass
#     else:
#         c = c + 1
#     if c == 0:
#         print("这是回文")
#     else:
#         print("这不是回文")









# 判断回文
# a = input("请输入字符")
# b = len(a)
# c = 0
# if b <= 1:
#     print("你输入的字符过短!请重新输入")
# else:
#     for i in range(b):
#         if a[i] == a[-i-1]:
#             c = c + 1
#     if c == b :
#         print("这是回文")
#     else:
#         print("这不是回文")









# 质数之和
# a = 0
# for i in range(2,100):
#     for h in range(2,i + 1):
#         if i % h == 0 :
#             break
#     if i == h:
#         a = a + h
# print(a)









# 阶乘之和
# b = 0
# a = 1
# for i in range(1,11):
#     a = a * i
#     b = a + b
# print(b)










# 因数之和
# for i in range(1,1001):
#     a = 0
#     for h in range(1,i + 1):
#         if i % h == 0 and h < i:
#             a = a + h
#     if a == i:
#         print(i)










# 水仙花数
# for i in range(100,1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     if i == a ** 3 + b ** 3 + c ** 3:
#         print(i)










# 杨辉三角
# a = int(input("请输入行数："))


# a = input("请输入一段话")
# b = a.split(" ")
# e = 0
# f = 0
# for i in  range(0,len(list(b))):
#     if list(b)[i].isdigit():
#         f = f + 1
#     elif list(b)[i].istitle():
#         e = e + 1
# print(f"这段话里首字母大写的有{e}个,全数字的有{f}个")











# 商品价格
# a = input("请输入你购买的商品名：")
# n = int(input("请输入购买量："))
# b = ["矿泉水","方便面","面包","辣条","西瓜"]
# c = [3,5,10,4,30]
# for k,l in enumerate(list(b)):
#     if a == l:
#         print(f"{l}")
#         print(f"商品单价：{c[k]}")
#         print(f"总价：{c[k] * n}")
#     else:
#         print("此商品无货")










# 冒泡
# a = input("排序,输入多组数据空格隔开：")
# b = a.split()
# for h in range(0,len(b)):
#     for i in  range(0,len(b)-1):
#         if int(b[i]) > int(b[i+1]):
#             b[i],b[i + 1] = b[i+1],b[i]
# print(b)












# 选择
# a = input("排序,输入多组数据空格隔开：")
# b = a.split()
# for h in range(len(b)):
#     for i in  range(h):
#         if int(b[h]) > int(b[i]):
#             b[h],b[i] = b[i],b[h]
# print(b)









# for i in range(0):
#     print(i)
# print("ok")










# 多种商品价格
# a = input("请输入你购买的商品名：")
# n = input("请输入购买量：")
# b = ["矿泉水","方便面","面包","辣条","西瓜"]
# c = [3,5,10,4,30]
# x = a.split()
# y = n.split()
# h = 0
# for o in range(0, len(x)):
#     e = 0
#     d = 0
#     for k, l in enumerate(list(b)):
#         if x[o] == l:
#             print(f"{l}  商品单价：{c[k]}  购买数量：{y[o]}")
#             e = int(c[k]) * int(y[o]) + e
#         else:
#             d = d + 1
#     h = e + h
#     if x[o] != l and d == 5:
#         print(f"{x[o]}:此商品无货")
# print(f"总价{h}")









# # 去重
# a = [1,2,2,3,4,3,4,4]
# b = set()
# for i in a:
#     b.add(i)
# print(b
#
# # 去重 字典
# a = [1,2,3,4,2,3,4]
# b =dict.fromkeys(a)
# c=[]
# for i in b:
#     c.append(i)
# print(c)
#
# # 去重
# a = [1,2,2,3,4,3,4,4]
# b = []
# for i in  a:
#     if i not in b:
#         b.append(i)
# print(b)











# 多个字符
# a = input("亲输入字符，空格分开：")
# b = input("请输入字符，空格分开：")
# c = a.split()
# d = b.split()
# e = {}
# if len(c) >= len(d):
#     for f in range(len(c)):
#         if len(d) - 1 >= f:
#             e.setdefault(c[f],d[f])
#         else:
#             e.setdefault(c[f])
#     print(e)
# else:
#     for g in range(len(d)):
#         if g >= len(c):
#             # e["bowen"] = d[g]
#             e.setdefault("bowen",d[g])
#         else:
#             e.setdefault(c[g],d[g])
#     print(e)













# 单个字符
# a = list(input("输入a："))
# d = list(input("输入d："))
# b = len(a)
# e = len(d)
# c = {}
# if b >= e:
#     for i in range(0, b):
#         if i <= e-1:
#             c.setdefault(a[i], d[i])
#         else:
#             c.setdefault(a[i])
#     print(c)
# else:
#     for i in range(0, b):
#         c.setdefault(a[i], d[i])
#     print(c)











# s = {
#     "key1": [1000, 2000, 3000],
#     2019: [
#         "hello",
#         {"python": ['py2.x', 'py2.x']},
#     ],
# }

# 1、求 key1 对应value的和
# 2、求 python 对应的值，并将每个版本的首字符大写、尾字符大写输出


# 1
# a = 0
# for i in range(len(s["key1"])):
#     a = s["key1"][i] + a
# s["key1"] = a

# 2
# b = []
# for h in s[2019][-1]["python"]:
#     b.append(h.title())
# s[2019][-1]["python"] = b
# print(s)










# s = '[Description("衣物挑战5kg")]@        /medal/201906/24/Cloth_Single_5.png         @        /medal/201906/24/Cloth_Single_5_Get.png     @            [Description("衣物挑战10kg")]@        /medal/201906/24/Cloth_Single_10.png        @        /medal/201906/24/Cloth_Single_10_Get.png    @            [Description("衣物挑战15kg")]@        /medal/201906/24/Cloth_Single_15.png       @        /medal/201906/24/Cloth_Single_15_Get.png   @            [Description("衣物挑战20kg")]@        /medal/201906/24/Cloth_Single_20.png       @        /medal/201906/24/Cloth_Single_20_Get.png    @           [Description("衣物挑战25kg以上")]@        /medal/201906/24/Cloth_Single_25.png        @        /medal/201906/24/Cloth_Single_25_Get.png   @            [Description("衣物累计50kg")]@        /medal/201906/24/Cloth_Sum_50.png           @        /medal/201906/24/Cloth_Sum_50_Get.png'

# 题目要求
# 将类似/medal/201906/24/Cloth_Single_5.png的放到一个列表内
# 将类似/medal/201906/24/Cloth_Single_5_Get.png的放到一个列表内

# a = s.split("@")
# b = []
# c = []
# d = []
# for i in a:
#     c.append(i.strip())
# for h in range(len(c)):
#     if c[h].endswith("Get.png"):
#         b.append(c[h])
#     elif c[h].endswith(".png"):
#         d.append(c[h])
# print(b)
# print(d)











# A = (56,"zxvci",[76],{1:789,2:3629},(1,2,3))
# B = (89,90,678)
# print(((A + B) * 3).count(76))
#
# a =["abc","wsx"]
# b = []
# for i in a:
#     b.append(i[::-1].title()[::-1])
# print(b)










# a = {1,2,3,"jkl"}
# print(a.pop())
# print(a)


# a = {1,2,3,4,5,6}
# b = {3,4,5,6,7,8}
# c = a.difference(b)
# print(c)
# a.difference_update(b)
# print(a)
# d = a.intersection(b)
# print(d)
# a.intersection_update(b)
# print(a)
# print(a.isdisjoint(b))
# print(a.issubset())
# issubset()










# import random
# a = random.randint(0,1000) #随机生成数字0到1000
# print(a)
# b = []
# for i in range(10):
#     import random
#     a = random.randint(0, 1000)
#     b.append(a)
# print(set(b))











# 三位数不相等的个数
# a = 0
# for i in range(1,10):
#     for h in range(0,10):
#         for j in range(0,10):
#             if i != h != j and i != j:
#                 print(i,h,j)
#                 a = a + 1
# print(f"这样的数共有{a}")












# (a+b=c)的平方
# for i in range(1,100):
#     for j in range(1,i):
#         for h in range(1,j):
#             if (j ** 2 + h ** 2) == i ** 2:








# a = int(input("请输入一个数："))
# if a > 0:
#     if a % 2 == 0:
#         print(f"{a} 是个偶数")
#     else:
#         print(f"{a} 是一个奇数")
# else:
#     print("请输入一个大于0的数")








# a,b = 0.00008,0
# while a < 8848:
#     a = a * 2
#     # print(a)
#     b += 1
# print(b)


# a = 0
# for i in range(10):
#     a += 1
# print(a)








# 不使用int将一个数字字符转换为int
# a = input("请输入一个数字:")
# b = 0
# c = a[::-1]
# for i,j in  enumerate(c):
#     for h in range(10):
#         if str(h) == j:
#             b = h * (10 ** i) + b
# print(b)
# print(type(b))







# a = input("输入数")
# b=0
# while True:
#     b += 1
#     if str(b) == a:
#         print(b)
#         break








# a = eval(input("请输入一个数字："))
# print(a)
# print(type(a))

# a = input("输入数字")
# print(a)
# print(type(a))









# select name from score left join score a on a.name=score.name and a.kemu="语文" left join score b on b.name=score.name and b.kemu="数学" where a.score>80 and b.score>80;


# a = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         a -= i
#     else:
#         a += i
# print(a)













# 统计字符串长度大于5的
# 将e全部替换成博文
# 截取第一个逗号前的所有单词，并将首字符大写
# 删除除包含英文o的单词


# a = Then one day the mother eagle appeared at the top of the mountain cliff, with a big bowl of delicious food and she looked down at her baby. The baby looked up at the mother and cried "Why did you abandon me? I'm going to die any minute. How could you do this to me?
# b = a.split()
# c = 0
# 4
# for i in b:
#     if i.find("o") != -1:
#         b.remove(i)
# print(b)

# 1
# for i in  b:
#     if len(i)>5:
#         c += 1
# print(c)

# 2
# for i in range(len(b)):
#     if b[i].find("e") != -1:
#         b[i] = b[i].replace("e","bowen")
# print(b)

# 3
# for i in range(len(b)):
#      if b[i].find(",") != -1:
#          d = b.index(b[i])
#          for h in range(d):
#             b[h] = b[h].title()
# print(b)








d = {
    "data": {
        "msg":
        [
            {
                "s_1": ["Jim", "男",  19, "175cm"],
                "country": "美国"
            },
            {
                "s_2": ["Kity", "女",  17, "165cm"],
                "country": "法国"
            },
            {
                "s_3": ["Tom", "男",  19, "173cm"],
                "country": "美国"
            },
            {
                "s_4": ["拖拉斯基", "男",  18, "180cm"],
                "country": "俄罗斯"
            },
            {
                "s_5": ["阿卡丽", "女",  17, "175cm"],
                "country": "乌克兰"
            },
            {
                "s_6": ["牙买稻子", "女",  18, "161cm"],
                "country": "日本"
            },
            {
                "s_7": ["龟田一郎", "男",  19, "175cm"],
                "country": "日本"
            },
            {
                "s_8": ["张三", "男",  20, "180cm"],
                "country": "中国"
            },
            {
                "s_9": ["李秀琴", "女",  19, "175cm"],
                "country": "中国"
            },
            {
                "s_10": ["宋仲基", "女",  19, "175cm"],
                "country": "韩国"
            },
            {
                "s_11": ["金正鞋", "男",  19, "168cm"],
                "country": "朝鲜"
            },
            {
                "s_12": ["卡列夫斯基", "男",  21, "190cm"],
                "country": "俄罗斯"
            },
        ]
    },
}

"""
# 求国家个数
# 求所有学生的身高范围
# 求统计男女比例
# 求平均身高
# 查询身高在170到180之间的学生名字



# 1
# a = d["data"]["msg"])
# a = []
# for i in d["data"]["msg"]:
#     a.append(i["country"])
# print(set(a))






# 2
# e = []
# # for i in d["data"]["msg"]:
# for i in d["data"]["msg"]:
#     a,c=i.keys()
#     for b in range(1,13):
#         if "s_" + str(b) == a:
#             e.append(i["s_" + str(b)][-1])
                break
# e.sort()
# print(f"身高范围{e[0]}-{e[-1]}")





# 3
e = []
# for i in d["data"]["msg"]:
#     a,c=i.keys()
#     for b in range(1,13):
#         if "s_" + str(b) == a:
#             e.append(i["s_" + str(b)][1])
# # print(e)
# m = e.count("男") / e.count("女")
# print(f"男女比列{m}")




# 4
# e = []
# for i in d["data"]["msg"]:
#     a,c=i.keys()
#     for b in range(1,13):
#         if "s_" + str(b) == a:
#             e.append(i["s_" + str(b)][-1])
# # print(e)
# # g = []
# h = 0
# for m in e:
#    h = int(m.rstrip("cm")) + h
# g = h / len(e)
# print(f"平均身高{g}cm")





# 5
# e = []
# for i in d["data"]["msg"]:
#     a,c=i.keys()
#     for b in range(1,13):
#         if "s_" + str(b) == a:
#             # e.append(i["s_" + str(b)][-1])
#             if  170 <= int(i["s_" + str(b)][-1].rstrip("cm")) <=180:
#                 print(i["s_" + str(b)][0],i["s_" + str(b)][-1])
"""


"""
# 购物车2.0
# import time
# a = {1:["啤酒",50,150],
#      2:["饮料",30,190],
#      3:["开水",20,240],
#      4:["花生",20,180],
#      5:["瓜子",15,210],
#      6:["板凳",30,300]
# }
# k = {666:2050,
#      111:3678,
#      777:8000,
#      999:2000,
#      2333:17900
# }
# 
# print(f" 编号\t           商品\t            单价\t           库存")
# for b in range(1,7):
#     print(f" {b}\t               {a[b][0]}\t            {a[b][1]}\t               {a[b][2]}")
# while True:
#     c = input("是否要购买商品，购买输入Y,退出输入B：")
#     if c == "Y" :
#         d = input("请输入购买的编号：")
#         while  int(d) > 6  or int(d) < 1:
#             d = input("商品不存在，请输入有效编号：")
#         e = input("请输入购买数量：")
#         if a[int(d)][2] == 0:
#             print(f"{a[int(d)][0]}商品库存:{a[int(d)][-1]}，返回购物系统中...")
#             continue
#         while int(e) > a[int(d)][2] or int(e) <= 0:
#             e = input(f"{a[int(d)][0]}库存:{a[int(d)][-1]}\t请重新输入:")
#         g = input("结账中，请输入你的会员卡号，没有请按N:")
#         h = a[int(d)][1] * int(e)
#         a[int(d)][-1] = a[int(d)][-1] - int(e)
#         if g == "N":
#             print(f"你购买了:{a[int(d)][0]} 数量:{e} 应付金额:{h} 剩余库存:{a[int(d)][-1]}")#
#             i = int(input("请付款："))
#             while i < h:
#                 i = int(input("你钱不够，请重新付款："))
#             print(f"收你{i}  找零{i - h} ")
#         else:
#             l = 0
#             while int(g) not in k.keys():
#                 g = input("卡号错误，请重新输入，超过5次返回购买系统:")
#                 l += 1
#                 if l == 4:
#                     break
#             if l < 4:
#                 if h * 0.8 > k[int(g)]:
#                     print(f"卡内余额不足，应支付{h * 0.8},卡内余额{k[int(g)]}")
#                     print(f"会员卡号:{g}，购买商品:{a[int(d)][0]} 数量:{e} 剩余库存:{a[int(d)][-1]} 应付金额:{h} 八折优惠,实付:{h * 0.8} 卡内余额:{k[int(g)]} ")#
#                     i = int(input(f"请补足付款{h * 0.8 - k[int(g)]}:"))
#                     while i < h * 0.8 - k[int(g)]:
#                         i = int(input("你钱不够，请重新补足余款："))
#                     print(f" 收你{i}  找零{i - (h * 0.8 - k[int(g)])} ")
#                     k[int(g)] = 0  #
#                 else:
#                     k[int(g)] = k[int(g)] - (h * 0.8)
#                     print(f"会员卡号:{g}\t购买了:{a[int(d)][0]}\t数量:{e}\t剩余库存:{a[int(d)][-1]}\t应付金额:{h}，八折优惠,实付:{h * 0.8}\t卡内余额:{k[int(g)]} ")#
#             else:
#                 pass
#     elif c == "B":
#         break
"""



"""
# 购物车 1.0
# a = {1:["香蕉",11,123],
#      2:["苹果",25,120],
#      3:["橘子",17,243],
#      4:["西瓜",10,178],
#      5:["桃子",15,210],
#      6:["葡萄",13,188]
# }
# k = {666:2000,
#      111:3678,
#      777:8000,
#      999:20000,
#      2333:17900
# }
# # a = ["香蕉","苹果","橘子","西瓜","桃子","葡萄"]
# # b = [11,25,17,10,15,13]
# # c = [123,120,243,178,210,188]
# # e = [1,2,3,4,5,6]
# # print(a[1])
# # while True:
# print(f" 编号\t           商品\t            单价\t           库存")
# for b in range(1,7):
#     print(f" {b}\t               {a[b][0]}\t            {a[b][1]}\t               {a[b][2]}")
# while True:
#     c = input("是否要购买商品，是的输入Y,退出输入B：")
#     if c == "Y" :
#         d = input("请输入购买的编号：")
#         while  int(d) > 6  or int(d) < 1:
#             d = input("商品不存在，请输入有效编号：")
#         e = input("请输入购买数量：")
#         while int(e) > a[int(d)][2] and int(e) > 0:
#             e = input("你输入数量超过库存，请重新购买")
#         g = input("结账，会员输入卡号，不是请输入N:")
#         h = a[int(d)][1] * int(e)
#         if g == "N":
#             print(f"你购买了:{a[int(d)][0]} 数量:{e} 应付金额:{h} 剩余库存:{a[int(d)][-1] - int(e)}")
#             i = int(input("请付款："))
#             while i <= h:
#                 i = int(input("你钱不够，请重新付款："))
#             print(f"找零{i - h} ")
#         else:
#             l = 0
#             while int(g) not in k.keys():
#                 g = input("错误卡号，请重新输入，超过5次退出系统:")
#                 l += 1
#                 if l == 4:
#                     break
#             if l < 4:
#                 if h * 0.8 > k[int(g)]:
#                     print(f"卡内余额不足，应支付{h * 0.8},卡内余额{k[int(g)]}")
#                     print(f"会员卡号:{g}，购买商品:{a[int(d)][0]} 数量:{e} 剩余库存:{a[int(d)][-1] - int(e)} 应付金额:{h} 八折优惠,实付:{h * 0.8} 卡内余额:{k[int(g)]} ")
#                     i = int(input(f"请补足付款{h * 0.8 - k[int(g)]}:"))
#                     while i < h * 0.8 - k[int(g)]:
#                         i = int(input("你钱不够，请重新补足余款："))
#                     print(f"找零{i - (h * 0.8 - k[int(g)])} ")
#                 else:
#                     print(f"会员卡号:{g}\t购买了:{a[int(d)][0]}\t数量:{e}\t剩余库存:{a[int(d)][-1] - int(e)}\t应付金额:{h}，八折优惠,实付:{h * 0.8}\t卡内余额:{k[int(g)] - (h * 0.8)} ")
#             else:
#                 pass
#     elif c == "B":
#         break
"""





"""
# 购物车3.0(....)
import time
a = {1:["啤酒",50,150],
     2:["饮料",30,190],
     3:["开水",20,240],
     4:["花生",20,180],
     5:["瓜子",15,210],
     6:["板凳",30,300]
}
k = {666:[2050,"大众会员",95],
     111:[3678,"白银会员",95],
     777:[8000,"黄金会员",85],
     999:[2000,"铂金会员",85],
     2333:[17900,"钻石会员",75]
}

print(f" 编号\t           商品\t            单价\t           库存")
for b in range(1,7):
    print(f" {b}\t               {a[b][0]}\t            {a[b][1]}\t               {a[b][2]}")
while True:
    c = input("是否要购买商品,退出输入Y：")
    if c != "Y" :
        d = input("请输入购买的编号：")
        while  int(d) > 6  or int(d) < 1:                #           判断输入有效编号
            d = input("商品不存在，请输入有效编号：")
        e = input("请输入购买数量：")
        if a[int(d)][2] == 0:                          #   判断购买商品库存
            print(f"{a[int(d)][0]}商品库存:{a[int(d)][-1]}，返回购物系统中...")
            continue
        while int(e) > a[int(d)][2] or int(e) <= 0:
            e = input(f"{a[int(d)][0]}库存:{a[int(d)][-1]}\t请重新输入:")
        g = input("结账中，请输入你的会员卡号，没有请按N:")
        h = a[int(d)][1] * int(e)
        a[int(d)][-1] = a[int(d)][-1] - int(e)
        if g == "N":
            print(f"你购买了:{a[int(d)][0]} 数量:{e} 应付金额:{h} 剩余库存:{a[int(d)][-1]}")#
            i = int(input("请付款："))
            while i < h:
                i = int(input("你钱不够，请重新付款："))
            print(f"收你{i}  找零{i - h} ")
        else:
            l = 0
            while int(g) not in k.keys():
                g = input("卡号错误，请重新输入，超过5次返回购买系统:")
                l += 1
                if l == 4:
                    break
            if l < 4:
                if h * k[int(g)][2] / 100 > k[int(g)][0]:                      #判断会员等级，折扣，卡内余额
                    print(f"卡内余额不足，应支付{h * k[int(g)][2] / 100},卡内余额{k[int(g)][0]}")
                    print(f"会员卡号:{g}，{k[int(g)][1]}  {k[int(g)][2]}折 购买商品:{a[int(d)][0]} 数量:{e} 剩余库存:{a[int(d)][-1]} 应付金额:{h} 实付:{h * k[int(g)][2] / 100} 卡内余额:{k[int(g)][0]} ")#
                    i = int(input(f"请补足付款{h * k[int(g)][2] / 100 - k[int(g)][0]}:"))        #卡内余额不足，现金补款
                    while i < h * k[int(g)][2] / 100 - k[int(g)][0]:                #判断你付钱
                        i = int(input("你钱不够，请重新补足余款："))
                    print(f" 收你{i}  找零{i - (h * k[int(g)][2] / 100 - k[int(g)][0])} ")
                    k[int(g)][0] = 0  #
                else:
                    k[int(g)][0] = k[int(g)][0] - (h * k[int(g)][2] / 100)
                    print(f"会员卡号:{g} {k[int(g)][1]}\t{k[int(g)][2]}折  购买了:{a[int(d)][0]}\t数量:{e}\t剩余库存:{a[int(d)][-1]}\t应付金额:{h}，实付:{h *  k[int(g)][2] / 100}\t卡内余额:{k[int(g)][0]} ")#
            else:
                pass
    else:
        break
"""



"""
# def add(x):
#     b = 0
#     for i in range(x):
#         b += i
#     print(b)
#     # return b #返回b的结果
# # add(200)
# print(add(200))





a = "GG"


# def jb():
#     b = "局部变量"
#     print(b)
#     return b
# 
# jb()
# # print(jb())




# def fool():
#     c = 100 #局部变量
#     global c   #变全局变量
#     print(c)
#
# print( c + 100)


# pycharm 调试：
# def k(x,y):
#     c = x + y
#     print(c)
#     return c
# 
# k(100,120)






#阶乘之和 函数
# def jc(a):
#     c = 0
#     b = 1
#     for i in range(1,a + 1):
#         b *= i
#         c += b
#     print(c)
# 
# jc(7)
"""



"""
# 元组
# def k(*argrs): #argrs 只是一个变量命名，可以是其他
#     a = "x_"
#     for b,c in enumerate(argrs):
#         d = a + str(b)
#         print(f"{d}：{c}")
# k(100,23,34,[89,67,9],56,21,"ghjsagfja")






# def k():
#     global p #p代表全局变量
#     p = 100
# k()
# print(p)




# 修改全局变量的数据类型
# g = "全局变量"
# def k():
#     global g
#     g = 100000
#     print(g)
# # k()
# print(g)



# #字典
# def k(**kwargs):
#     print(kwargs)
# #写法一
# k(c=1,b=2,a=3)
# #写法二
# n = {"33":231,"22":234,"11":12}
# k(**n)
"""


"""
# 排序函数
# def k(*b):
#     x = list(b)
#     for i in range(len(x)):
#         for h in range(len(x) - 1):
#             if int(x[h]) < int(x[h+1]):
#                 x[h],x[h+1]=x[h+1],x[h]
#     return x
# print(k(1.2,34,90,23,10,-1))

# def l(d):
#     c=d.split()
#     for i in range(0,len(c)):
#         for j in range(i+1,len(c)):
#             if int(c[j])<int(c[i]):
#                 c[j],c[i]=c[i],c[j]
#     return c
# print(l("45678 121 12141 12521 521 2 1 4 5 2 9 567 -1"))
"""





"""
#1.0
# def k():
# def zhma(a,b):
#     c = []
#     d = []
#     for i in range(len(a)):
#         if 8 >= len(a[i]) >= 5 and 9 >= len(b[i]) >= 6:
#             c.append(a[i])
#             d.append(b[i])
#     print (f"{len(d)}个账号可用")
#     for h in range(len(d)):
#         print (f"账号{c[h]},密码{d[h]}")


# n = ["qaxzx","tryqwf6","gfhsha","qwe","gfyua76","gysa324"]
# m = ["15361318","hfha","yufa67","rufa46","truwq68","hfu32"]
# zhma(n,m)
"""


"""
#2.0
# def a():
#     while True:
#         h = input("账号检测，输入任意字符开始，N结束：")
#         if h != "N":
#             b = input("请输入账号，空格分开:")
#             c = input("请输入密码，空格分开:")
#             d = b.split()
#             e = c.split()
#             if len(d) == len(e):
#                 for g in range(len(d)):
#                     if 8 >= len(d[g]) >= 5 and 9 >= len(e[g]) >= 6:
#                         print(f"第{g + 1}个账号可用{d[g]},密码{e[g]}")
#                     else:
#                         print(f"第{g + 1}个不可用")
#             else:
#                 print("账号和密码输入不一致,重新开始程序")
#         else:
#             break
# a()
"""




"""
#3.0
# def a():
#     while True:
#         h = input("账号检测，输入任意字符开始，N结束：")
#         if h != "N":
#             b = input("请输入账号，空格分开:")
#             d = b.split()
#             c = input("请输入密码，空格分开:")
#             e = c.split()
#             while len(e) != len(d):
#                 c = input("账号和密码输入不一致,请重新输入密码:")
#                 e = c.split()
#             for g in range(len(d)):
#                 if 8 >= len(d[g]) >= 5 and 9 >= len(e[g]) >= 6:
#                     print(f"第{g + 1}个账号可用{d[g]},密码{e[g]}")
#                 else:
#                     print(f"第{g + 1}个账号不可用")
#         else:
#             break
# a()
"""




"""
# if a[666][2]  / 100 > a[777][0]:
#     print("ok")
# else:
#     print("no")
# for i in enumerate(a,20):
#     print(i)
"""




"""
# 1
# def k():
#     return "函数k"
# def a():
#     print("函数a")
#     print(k())
# a()




# def a():
#     x = 100
#     def b():
#         c = x * 10
#         return c
#     return b

# print(a()()) #执行嵌套函数

# import random
# a = lambda n:random.randint(1,10) * n  #匿名函数
# print(a(5))
"""




"""
# print([i for i in range(5)])  #python 列表推导式

# a = [lambda i:i + 10  for i in range(1,11) if i > 5]  #python 列表推导式



# b = [b.append(b[i][g]) for i in range(len(b)) for g in range(len(b[i]))]
# print(b)


# a = [[1,2,6,3],[3,4],[5,6,7]]
# 
# a = [x for y in a for x in y  ]
# print(a)
"""




# open 操作文档
"""
# f =open("a.txt",mode="a",encoding="utf-8")
# 
# # write():写入 传入字符串
# a = input("输入，空格分隔:")
# b = a.split()
# for i in b:
#     f.write(f"{i}\n")
# f.close()
"""






"""
# def x(g):
#     f = open(g, mode="w", encoding="utf-8")
# 
#     # write():写入 传入字符串
#     a = input("#创建文件并显示文件内容：输入你想写的内容，空格分隔:")
#     b = a.split()
#     for i in b:
#         f.write(f"{i}\n")
#     f.close()
#     f =open( g ,encoding="utf-8")
#     # read 读取文件中所有的内容
#     # a =f.read() #a = f.readlines(2)  返回的是一个列表，返回2行
#     a = f.read()
#     return a
#     # a = f.readlines()
#     # b = []
#     # for i in a:
#     #     b.append(i.strip())
#     # return b
#     # f.close()

# print(x("a.txt"))
"""







# f =open("a.txt",encoding="utf-8")
# # read 读取文件中所有的内容
# a =f.read()
# print(a)
# f.close()




# 人生若只如初见，何事秋风悲画扇 等闲变却故人心，却道故人心易变 骊山语罢清宵半，泪雨霖铃终不怨 何如薄幸锦衣郎，比翼连枝当日愿




"""

import time

class Student(object):
    # 类的属性
    height = 170
    weight = 130
    def name(self,x):
        weight = 130 #局部变量 【实例属性】
        print(f"姓名 {x} 体重 {self.weight} 身高 {self.height}")

#类的使用
# s1 = Student() #被称为对象/类的实例
# 类的实例使用类的方法
Student().name("蔡战洋")

"""

"""
class Su(object):
    a = int(input("请输入你的成绩"))
    b = int(input("请输入你的成绩"))
    def lo(self,h,g):
        d = f"{h}#Ahce#"
        e = f"{g}#鸡蛋#"
        if self.a  > self.b :
            return d
        else:
            return e
print(Su().lo("sanmu","sherli"))

"""


"""
class Su(object):
    nianji = "2"
    __sex = "1"  #类的私有属性
    def __init__(self,name,age): #类的构造方法 在类执行时，自动执行 __init__
        # 如果定义了init方法，再创造对象的时候，必须传入参数
        self.age = age
        self.name = name
        self.__g = "sdx" #对象的私有属性
    def show(self):
        print(f"{self.name} {self.age} {self.nianji}")
a = Su("宏",20)# 这是创造对象的过程
# a.show() # 对象使用类的方法，类的方法只有类的对象才能用
"""

# print(Su.nianji)  # 类的公有属性可以直接使用类名.属性名
# 类的私有属性不能在类的外面通过类名.属性名的方式使用
# 对象公有属性，通过对象名.属性名的方式使用
# 对象私有属性，不能再类外部通过对象名.属性名的方式使用
# 类名.对象的属性是不可以使用


class shuxing(object):
    __sek=12
    def df(self):
        print(shuxing.__sek)

#  类的属性 ： 私有 共有
#  实例属性 ： 私有 共有
#  区分类的属性和对象属性
#  类的属性：定义在类的内部，方法的外部
#  对象属性：定义在init方法内部

# 公有和私有：
# 私有是以双下划线开头：__sex = "1"
# 私有属性在定义之后，不希望被修改，可以通过：self.__变量名/self._类名__变量名的方式使用它



"""
class Ning(object):
    a = "21"
    __b = "171"
    def op(self,i):
        nianji = "2"
        __a = "china"
        print(f"{i} {__a} {self.a} {self.__b} {nianji}")
        print()

    def show(self):
        print("普通方法")
    @staticmethod
    def foo():#静态方法
        print("类的静态方法")
    @classmethod
    def koo(cls):#类方法 cls和self的作用一致
        print("类的类方法")
    def __siyou(self):
        print("类中的私有方法")
    def a(self):
        self.__siyou()
        #在类的方法中使用其他方法的方式 self.方法名


Ning().__siyou()
"""


# 类中的普通方法不能被类名.方法名的方式使用
# 对象名.普通方法名 ---》使用普通方法
# 对象名.静态方法名 ---》使用静态方法
# 对象名.类方法名 ---》使用类方法
# 私有方法不可以在类的外部使用
# 类名.类方法名，类名.静态方法名；可以使用类方法，静态方法

# staticmethod 将普通方法转为静态方法装饰器
# classmethod 将普通方法转变为类方法的装饰器


# 方法
# 静态方法 普通方法 私有方法

"""
class B(object):
    def __init__(self, name, age):  # 类的构造方法 在类执行时，自动执行 __init__
        # 如果定义了init方法，再创造对象的时候，必须传入参数
        self.age = age
        self.name = name
        self.__g = "sdx"  # 对象的私有属性
    def say(self):
        print(f"B类中不同方法")
        return self.age ,self.name
# (类名) 继承于xx类
class C(B):
    def gg(self):
        res = super().say()
        # res = self.say()
        print(res)
    # 多态，重写方法
    def say(self):
        print("c的方法")


# c = C("zz",30)
# # c.gg()
# # c.say()

# 多态 继承类对被继承的方法的重写【方法名一样，语句块不一样】
# 使用super（）.被继承类的方法
"""




"""
# python插入 mysql
import pymysql

# 1.连接数据库
class sqlserver():
    def __init__(self,hosts,ports,users,passwords):
        self.connect = pymysql.connect(
            host = hosts,# 数据库所在的主机ip地址/域名【云服务器---mysql数据库】
            port = ports, # mysql 端口号
            user = users,  # mysql用户名
            password = passwords, # 密码
            charset = "utf8", #编码方式 默认utf8
        # database = "库名"  # 指定数据库，不写，默认所有数据库
        )
        self.cur = self.connect.cursor()
    def create_database(self,i):# 建库
        sql = f"create database {i} default character set utf8 collate utf8_general_ci"
        self.cur.execute(sql)
    def create_table(self): # 建表
        a = input("请输入你要建的表名")
        b = input("表名所在库")
        sql1 = f" use {b}"
        sql2 = f"create  table {a}(name varchar(16),sex char(16),age int,class varchar(16),countery varchar(16))"
        self.cur.execute(sql1)
        self.cur.execute(sql2)
    # def insert_intos(self):
    #     while True:
    #         a = input("退出写入请按N：")
    #         if a != "N":
    #             c = input("输入你要写数据的表")
    #             b = input("表名所在库")
    #             d = input(f"请输入你要写入的数据")
    #             sql0 = f"desc {c} "
    #             sql = f"use {b}"
    #             sql1 = f"insert into {c} values ({d})"
    #             self.cur.execute(sql)
    #             self.cur.execute(sql1)
    #             # self.connect.commit()  #保存数据库
    #         else:
    #             break
    def insert_into(self):  #插入数据
        b = 0
        for i in g:
            b += 1
            a = "s_" + str(b)
            i[a].append(i["country"])
            c = tuple(i[a])
            sql = "use stu1903"
            sql1 = f"insert into polo values {c} "
            self.cur.execute(sql)
            self.cur.execute(sql1)
    def cx_select(self):  # 查询
        sql = "select * from polo"
        sql1 = "use stu1903"
        self.cur.execute(sql1)
        self.cur.execute(sql)
        # self.b= self.cur.fetchall()  #查询执行sql语句获得所有结果
        b = self.cur.fetchall()
        # d = self.cur.fetchmany(size=4)  # 查询指定条,只能一条条的查询，配合for循环可全部打印
        # print(d)
        return b
        # c = self.cur.fetchone() #只查询一条
        # print(a)
        # print(b)
    def close(self):#断开数据库
        self.connect.close()#与数据库 断开连接
    def read(self): #读写文本文档
        self.cx_select()
        y = open("a.txt", mode="a", encoding="utf-8")
        y.write(f"名字\t 性别\t 年龄\t 身高\t 国籍\n" )
        for i in self.b:
            for z in range(len(i)):
                y.write(f"{i[z]} \t")
            y.write("\n")
        y.close()


# GG = sqlserver("192.168.10.21", 3306, "root", "123456")
# GG.cx_select()




        # sql = "create table 1903(nam char(8),num  varchar(8))"
#
# cur =connect.cursor()  # 游标：类似于mysql>命令模式
#
# cur.execute(sql) # 执行语句块

import xlwt  # excel写表格
class Excel_write(sqlserver):
    def __init__(self, inm, name,hosts,ports,users,passwords):  # init 方法套用 多态套用
        sqlserver.__init__(self,hosts,ports,users,passwords)  # Excel 类init变量
        self.d = xlwt.Workbook()  # 新建一个excel文件
        self.table = self.d.add_sheet(inm)  # 新建一个excel表 add_sheet(工作表的名字)必填的
        self.name = name
    def write_a(self):
        for i in range(len(self.cx_select())):
            for g in range(len(self.cx_select()[i])):
                #   print( self.cx_select()[i][g]
                self.table.write(i, g, self.cx_select()[i][g])
        self.d.save(self.name)
# GG = Excel_write("表二","mysql.xls","192.168.10.21",3306,"root","123456")
# GG.write_a()

"""







"""
        d = {
            "data": {
                "msg":
                    [
                        {
                            "s_1": ["Jim", "男", 19, "175cm"],
                            "country": "美国"
                        },
                        {
                            "s_2": ["Kity", "女", 17, "165cm"],
                            "country": "法国"
                        },
                        {
                            "s_3": ["Tom", "男", 19, "173cm"],
                            "country": "美国"
                        },
                        {
                            "s_4": ["拖拉斯基", "男", 18, "180cm"],
                            "country": "俄罗斯"
                        },
                        {
                            "s_5": ["阿卡丽", "女", 17, "175cm"],
                            "country": "乌克兰"
                        },
                        {
                            "s_6": ["牙买稻子", "女", 18, "161cm"],
                            "country": "日本"
                        },
                        {
                            "s_7": ["龟田一郎", "男", 19, "175cm"],
                            "country": "日本"
                        },
                        {
                            "s_8": ["张三", "男", 20, "180cm"],
                            "country": "中国"
                        },
                        {
                            "s_9": ["李秀琴", "女", 19, "175cm"],
                            "country": "中国"
                        },
                        {
                            "s_10": ["宋仲基", "女", 19, "175cm"],
                            "country": "韩国"
                        },
                        {
                            "s_11": ["金正鞋", "男", 19, "168cm"],
                            "country": "朝鲜"
                        },
                        {
                            "s_12": ["卡列夫斯基", "男", 21, "190cm"],
                            "country": "俄罗斯"
                        },
                    ]
            },
        }
"""

# g = d["data"]["msg"]
# a = sqlserver("192.168.10.6",3306,"root","123456")
# a.create_database("stu1903")
# a.create_table()
# a.insert_into()
# a.cx_select()
# a.read()





"""
# python 操作excel
# python读取excel表格中的数据 --需要使用第三方包：xlrd

import xlrd
d = xlrd.open_workbook(filename="")
table = d.sheets()[0]       #获取excel表，返回的是一个包含所有excel的列表  如果存在两个或者多个 列表为[sheet1,sheet2]
x = table.row_values(0,1)       #获取表中数据 roe_values():获取整行的数据，必须指定获取的行号:(0,1)获取第一行，第一个索引值往后
y = table.row(0)[0].value       #获取某个单元格的值 先通过row() 获取某一行 返回一个列表 根据索引获取值
a = table.col_values(0)[0]       #获取一整列 第0个索引所对应的值
b = table.cell(0,0)     #获取第0行第0列（数字代表索引）
c = table.nrows     #获取行数
e = table.ncols     #获取列数
# print(d.sheet_names())      #找出文件中所有的表名字

# 通过索引获取
# 假设一个文件存在两个表sheet1，sheet2，
# sheet_by_index(0):打开就是sheet1内存位置
# table = d.sheet_by_index(0)
# print(table)
"""


"""
import xlrd  #excel读表格

# excel面向对象

class Excel(object):
    def __init__(self,nam,num):
        self.d = xlrd.open_workbook(filename=nam)     #打开一张表
        self.t = self.d.sheet_by_index(num)       #使用一张表
    def data(self):
        n = self.t.nrows
        self.a = []
        for i in range(n):
            self.a.append(self.t.row_values(i))
        return self.a
    def read(self):
        self.data()
        b = open("a.txt", mode="a", encoding="utf-8")
        for i in self.a:
            for x in i:
                b.write(f"{str(x)} \t")
            b.write("\n")
        b.close()
# GG = Excel("",0)
# GG.read()
"""


"""
import xlwt   #excel写表格
class Excel_write(Excel):
    def __init__(self,inm,name,nam,num): # init 方法套用 多态套用
        Excel.__init__(self, nam, num) # Excel 类init变量
        self.d = xlwt.Workbook()  #新建一个excel文件
        self.table = self.d.add_sheet(inm)  #新建一个excel表 add_sheet(工作表的名字)必填的
        self.name =name
        # table.write(0,0,"张三")   #写入数据到表格，一次填入一个单元格 0代表行和列
        # d.save(name)    #保存文件，save（文件名）必填


        # def __init__(self,):
        #     d = xlwt.Workbook()  #新建一个excel文件
        #     table = d.add_sheet("表一")  #新建一个excel表 add_sheet(工作表的名字)必填的
        #     table.write(0,0,"张三")   #写入数据到表格，一次填入一个单元格 0代表行和列
        #     d.save("")    #保存文件，save（文件名）必填
    def write_a(self):
        for i in range(len(self.data())):
            for g in range(len(self.data()[i])):
                self.table.write(i,g,self.data()[i][g])
        self.d.save(self.name)

# GG = Excel_write("","","",0)
# GG.write_a()



# 读写类
# class read_write(Excel):
#     def read(self):
#         b = open("a.txt", mode="a", encoding="utf-8")
#         for i in self.data():
#             for x in i:
#                 b.write(f"{str(x)} \t")
#             b.write("\n")
#         b.close()

# GG = read_write("",0)
# GG.read()



# cd = Excel("",0)
# print(cd.data())


# class A (object):
#     def fo(self,x):
#         d = []
#         for i in range(1,x):
#             c = 0
#             for g in  range(1,i+1):
#                 if i % g == 0:
#                     c += 1
#             if c == 2:
#                 d.append(i)
#         return d
# class B (A):
#     def foo(self,a):
#         d = 0
#         for y in self.fo(a):
#             d += y
#         return d
# GG = B()
# print(GG.foo(1000))
#
#
# # init
# class A (object):
#     def __init__(self,x):
#         self.x = x
#     def fo(self):
#         d = []
#         for i in range(1,self.x):
#             c = 0
#             for g in  range(1,i+1):
#                 if i % g == 0:
#                     c += 1
#             if c == 2:
#                 d.append(i)
#         return d
# class B (A):
#     def foo(self):
#         d = 0
#         for y in self.fo():
#             d += y
#         return d
# GG = B(100)
# print(GG.foo())

"""

# a = (12,34,(1,2,3),(4,5,6))
# print(len(a[2]))



import xlwt,xlrd
class w_r(object):
    def __init__(self,name,nam,names,num):  # 新表名，保存的表名，读取的表，表名索引
        self.a4 = xlrd.open_workbook(filename=names)
        self.a5 = self.a4.sheets()[num]
        self.a1 = xlwt.Workbook()
        self.a2 = self.a1.add_sheet(name)
        self.a3 = nam
    def r_r(self):
        b1 = self.a5.nrows  #表行数
        b2 = self.a5.ncols  #表列数
        for i in range(b1):
            for g in  range(b2):
                b3 = "test" + str(self.a5.row_values(i)[g])
                self.a2.write(i,g,b3)
                # print(self.a5.row_values(i)[g])
                # print(self.a5.cell(i,g))
        self.a1.save(self.a3)
    def w_w(self):
        pass


# GG = w_r("表一","data.xls","mysql.xls",0)
# GG.r_r()

# a = "tes" + str(sdufh)
# print(a)








"""
import xlwt,xlrd
class w_r(object):
    def __init__(self,name,numes):
        self.a1 = xlwt.Workbook()
        self.a2 = self.a1.add_sheet(name)
        self.a3 = numes
    def x1(self):
        b1 = open("a.txt",mode="a",encoding="utf-8")      #文本
        for i in range(1,10):
            for g in range(1,i+1):
                # self.a2.write(i - 1,g - 1,f"{g} * {i} = {i * g}")   #表格
                b1.write(f"{g} * {i} = {i * g} \t")      #文本
        # self.a1.save(self.a3)     #表格
            b1.write("\n") #表格
        b1.close() #表格


# g = w_r("表一","99.xls")
# g.x1()
"""






import xlwt,xlrd
import xlutils.copy
filename = "readline.xls"
def readline():
    wb = xlrd.open_workbook(filename,formatting_info=True) #打开excel，保留文件格式
    sheet1 = wb.sheet_by_index(0) #获取第一张表 n
    nrows = sheet1.nrows #获取总行数
    ncols = sheet1.ncols
    return nrows
def write():
    data = xlrd.open_workbook(filename)
    ws = xlutils.copy.copy(data) #复制之前表里存在的数据
    table=ws.get_sheet(0)
    nownrows = readline()
    table.write(nownrows, 0, label='test case') #最后一行追加数据
    table.write(nownrows, 1, label='expected results')
    table.write(nownrows, 2, label='actual results')
    ws.save(filename) #保存的有旧数据和新数据 write()

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
# sftp.get(a1,a2)   #执行命令  get（远程文件，本地文件）下载    get（本地文件，远程文件）上传
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



# python 与系统交互 window，mac，uninx
# python的内置模块 ，os库

import os
# print(os.getcwd()) # 获取当前目录
# os.chdir('A')#  os.chdir(目录名字) 切换到指定目录
# print(os.getcwd())
# 返回目录：os.curdir 代表一个点  os.pardir 代表两个点
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
    def any_1(self):
        a2 = 0
        a3 = 0
        for i in os.listdir(self.a1):
            print(i)
            if os.path.isdir(i):
                a2 += 1
            elif os.path.isfile(i):
                a3 += 1
        print(f"目录{a2}个，文件{a3}个")
# asd = any(r'\Users\Darcy\Desktop\文件')
# asd.any_1()




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


from datetime import *
# print(datetime.now())# 获取当前时间，日期
# print(datetime(1994,11,9,9,1,1))# 获取指定的时间，日期
# print(datetime.strptime('1994-11-09 09:01:01','%Y-%m-%d %H:%M:%S'))# 字符串时间转datetime日期
# print(datetime.now().strftime("%a %d %B %H:%M:%S")) #日期转字符串
# now = datetime.now()
# print(now + timedelta(hours=5))  #日期加减
# print(date.today()) #只获取当前日期
# print(date.today()-timedelta(days=2))  #日期加减




