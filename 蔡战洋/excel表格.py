# -*- coding: utf-8 -*-
# python 操作excel
# python读取excel表格中的数据 --需要使用第三方包：xlrd
# 写入表格数据 xlwt

import xlrd
# d = xlrd.open_workbook(filename="ab.xlsx")
# table = d.sheets()[0]       #获取excel表，返回的是一个包含所有excel的列表  如果存在两个或者多个 列表为[sheet1,sheet2]
# x = table.row_values(0,1)       #获取表中数据 roe_values():获取整行的数据，必须指定获取的行号:(0,1)获取第一行，第一个索引值往后
# y = table.row(0)[0].value       #获取某个单元格的值 先通过row() 获取某一行 返回一个列表 根据索引获取值
# a = table.col_values(0)[0]       #获取一整列 第0个索引所对应的值
# b = table.cell(0,0)     #获取第0行第0列（数字代表索引）
# c = table.nrows     #获取行数
# e = table.ncols     #获取列数
# print(d.sheet_names())      #找出文件中所有的表名字

# 通过索引获取
# 假设一个文件存在两个表sheet1，sheet2，
# sheet_by_index(0):打开就是sheet1内存位置
# table = d.sheet_by_index(0)
# print(table)


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
# GG = Excel("mysql.xls",0)
# print(GG.data())


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
        #     d.save("mysql.xls")    #保存文件，save（文件名）必填
    def write_a(self):
        for i in range(len(self.data())):
            for g in range(len(self.data()[i])):
                self.table.write(i,g,self.data()[i][g])
        self.d.save(self.name)

# GG = Excel_write("表一","mysql.xls","ab.xlsx",0)
# GG.write_a()


with xlrd.open_workbook(r'C:\Users\Darcy\Desktop\蔡战洋\xlstext\mysql.xls') as  f:
    tab=f.sheet_by_index(0)
    ow=tab.nrows
    for _ in range(ow):
        print(tab.row_values(_))
    # with f.sheet_by_index(0) as bs:
        # print(bs.row_values(0))




