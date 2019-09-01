


# #字典
# def k(**kwargs):
#     print(kwargs)
# #写法一
# k(c=1,b=2,a=3)
# #写法二
# n = {"33":231,"22":234,"11":12}
# k(**n)



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




