
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
# Student().name("蔡战洋")

"""

"""
# class Su(object):
#     a = int(input("请输入你的成绩"))
#     b = int(input("请输入你的成绩"))
#     def lo(self,h,g):
#         d = f"{h}#Ahce#"
#         e = f"{g}#鸡蛋#"
#         if self.a  > self.b :
#             return d
#         else:
#             return e
# print(Su().lo("sanmu","sherli"))

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
# a = Su("宏",20)# 这是创造对象的过程
# a.show() # 对象使用类的方法，类的方法只有类的对象才能用
"""

# print(Su.nianji)  # 类的公有属性可以直接使用类名.属性名
# 类的私有属性不能在类的外面通过类名.属性名的方式使用
# 对象公有属性，通过对象名.属性名的方式使用
# 对象私有属性，不能再类外部通过对象名.属性名的方式使用
# 类名.对象的属性是不可以使用



#  类的属性 ： 私有 共有
#  实例属性 ： 私有 共有
#  区分类的属性和对象属性
#  类的属性：定义在类的内部，方法的外部
#  对象属性：定义在init方法内部

# 公有和私有：
# 私有是以双下划线开头：__sex = "1"
# 私有属性在定义之后，不希望被修改，可以通过：self.__变量名/self._类名__变量名的方式使用它



"""
class ning(object):
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
    def li(self):
        self.__siyou()
        #在类的方法中使用其他方法的方式 self.方法名


# Ning().__siyou()
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
        print(res)
    # 多态，重写方法
    def say(self):
        print("c的方法")


# c = C("zz",30)
# c.gg()
# c.say()

# 多态 继承类对被继承的方法的重写【方法名一样，语句块不一样】
# 使用super（）.被继承类的方法


