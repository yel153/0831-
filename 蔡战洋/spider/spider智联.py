# -*- coding: utf-8 -*-
import re,requests,json,xlutils,xlrd,xlwt
from xlutils.copy import *

# class excel_1(object):
#     def __init__(self,name,inm):
#         self.d = xlwt.Workbook()  #新建一个excel文件
#         self.table = self.d.add_sheet(inm) #新建一个excel表 add_sheet(工作表的名字)必填的
#         self.inm = inm
#         self.name =name
#         self.d.save(self.name)
class zhilian_data(object):
    def __init__(self,inm,name): # init 方法套用 多态套用
        # Excel.__init__(self, nam, num) # Excel 类init变量
        s1 = xlrd.open_workbook(name)
        self.s2 = copy(s1)
        self.s3 = self.s2.add_sheet(inm)
        # self.d = xlwt.Workbook()  #新建一个excel文件
        # self.table = self.d.add_sheet(inm) #新建一个excel表 add_sheet(工作表的名字)必填的
        # self.inm = inm
        self.name =name
        # self.d.save(self.name)
    def get_html(self,a1,a2):
        header = {
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        # url = 'https://sou.zhaopin.com/?jl=653&kw=%E6%B5%8B%E8%AF%95&kt=3'
        # url = 'https://sou.zhaopin.com/?jl=653&kw=测试&kt=3&sf=0&st=0'
        url1 = f'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId={a2}&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={a1}&kt=3&_v=0.50977908&x-zp-page-request-id=e05b20c9e977471285258f06cf24ee9f-1562659591323-87269&x-zp-client-id=7eeac520-5b26-44ef-90f9-f96f87ec26c4'
        # a2 = urllib.parse.quote(a1)
        # url1 = url+f'{a2}'
        # ky = {'kw':a1}
        s1 = requests.get(url=url1,headers=header)
        html = s1.content.decode('utf-8')
        print(html)
        data = json.loads(html)  #字符串转想转的内容    json.dumps  将python类型装换成json字符串
        news = data['data']['results']
        return news
    def read_write(self,a6,a5):
        a1 = self.get_html(a1=a6,a2=a5)
        # s1 = xlrd.open_workbook(self.name)
        # self.s2 = copy(s1)
        # self.s3 = self.s2.add_sheet(a4)
        a3 = ['公司',['职位'],['薪资'],['年限'],['位置'],['学历']]
        for j in range(6):
            self.s3.write(0,j,a3[j])
        a2 = 0
        for i in a1:
            a2 += 1
            self.s3.write(a2, 0, i['company']['name'])
            self.s3.write(a2, 1, i['jobName'])
            self.s3.write(a2, 2, i['salary'])
            self.s3.write(a2, 3, i['workingExp']['name'])
            self.s3.write(a2, 4, i['city']['display'])
            self.s3.write(a2, 5, i['eduLevel']['name'])
        self.s2.save(self.name)



if __name__ =='__main__':
    gg = zhilian_data('测试深圳','新智联.xls')
    gg.read_write('测试','深圳')
