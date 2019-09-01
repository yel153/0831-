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
        a = self.cur.execute(sql)
        self.b = self.cur.fetchall() ##查询执行sql语句获得所有结果  ，返回的结果是一个元组
        d = self.cur.fetchmany(size=4)  # 查询指定条
        d = self.cur.fetchmany()#一条条的查询，配合for循环
        c = self.cur.fetchone() #只查询一条
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
# sql = "create table 1903(nam char(8),num  varchar(8))"
#
# cur =connect.cursor()  # 游标：类似于mysql>命令模式
#
# cur.execute(sql) # 执行语句块

# g = d["data"]["msg"]
# a = sqlserver("192.168.10.6",3306,"root","123456")
# a.create_database("stu1903")
# a.create_table()
# a.insert_into()
# a.cx_select()
# a.read()