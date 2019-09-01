# -*- coding: utf-8 -*-
import re,requests,json,xlutils,xlrd,xlwt,urllib
from xlutils.copy import *

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

header1={'Cookie':'yfx_c_g_u_id_10000042=_ck18012900250116338392357618947; VISITED_MENU=%5B%228528%22%5D; yfx_f_l_v_t_10000042=f_t_1517156701630__r_t_1517314287296__v_t_1517320502571__r_c_2',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
'Referer':'https://www.51job.com/'
}


# abs()
# a=[8,9,1,3]
# a.sort()
# url = 'https://search.51job.com/list/010000%252C00,000000,0000,00,9,99,%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# area_url='https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js?20190610'
# s1 = requests.get(url=url,headers=header1)
# html = s1.content.decode('utf-8')
# print(html)


class job_51(object):

    def city_code(self):
        area_url = 'https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js?20190610'
        s1 = requests.get(url=area_url,headers=header1)
        s2 = s1.content.decode('gbk')
        a1 = re.compile('var area=(.*?);',re.S)
        a3 = a1.findall(s2)
        a4 = json.loads(a3[0])
        new_city_code = {}
        for ky,vl in dict.items(a4):
            new_city_code[vl] = ky
        return new_city_code

    def get_html(self):
        html_url = 'https://search.51job.com/list/{}%252C00,000000,0000,00,9,99,{},2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(self.city_code()[self.city_search],self.job_search)
        # html_url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,Java%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        s1 = requests.get(url=html_url,headers=header1)
        s2 = s1.content.decode('gbk')
        # print(s2)
        # a1 = re.compile('<div class="el">.*?title="(.*?)".*?href="(.*?)".*?title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S)
        a1 = re.compile('<div class="el">.*?title="(.*?)".*?href="(.*?)".*?title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>',re.S)
        a2 = a1.findall(s2)
        return a2

    def write_read(self):
        try:
            s6 = self.get_html()
            s1 = xlrd.open_workbook(self.write_xls)
            s2 = copy(s1)
            s3 = s2.add_sheet(self.new_xls)
            s4 = ['职位', '公司链接', '公司名称', '工作地点', '薪资']
            for s in range(5):
                s3.write(0, s, s4[s])
            for i in range(1,len(s6)+1):
                for j in range(5):
                    s3.write(i,j,s6[i-1][j])
            s2.save(self.write_xls)
            print('ok')
        except:
            a5 = self.get_html()
            a1 = xlwt.Workbook(self.write_xls)
            a2 = a1.add_sheet(self.new_xls)
            a3 = ['职位','公司链接','公司名称','工作地点','薪资']
            for a in range(5):
                a2.write(0,a,a3[a])
            for i in range(1, len(a5) + 1):
                for j in range(5):
                    a2.write(i, j, a5[i-1][j])
            a1.save(self.write_xls)
            print('ok')

class main_main(job_51):
    def job_city(self):
        while True:
            self.job_search = input("请输入你要选择的职位，输入'N'退出爬虫：")
            if self.job_search != 'N':
                self.city_search = input("请选择你要选择的城市：")
                self.write_xls = input("大表名字：")
                self.new_xls = input("大表里的sheet表名：")
                self.write_read()
            else:
                break


if __name__=='__main__':
    gg = main_main()
    gg.job_city()
# a = re.compile('<em id="work_position_click_center_right_list_category_000000_.*" data-value="(.*？)" data-navigation=".*" class="">(.*?)</em>')



"""
# class str_1(object):
#     def __init__(self,a1):
#         self.a1 = a1
def int_1(self):
    s1 = self.a1[::-1]
    num = 0
    for s2,s3 in enumerate(s1):
        for i in range(10):
            if str(i) == s3:
                # break
                num += i * 10 ** s2
    return num
print(eval('12434'))   #不用int转数值类型



# def k(**gg):
    # print(gg)/
# k({1,2,34})
    # x,y,z = gg
    # print()
# if __name__ == '__main__':
    # print(type('891234'))
    # gg = str_1('891234')
    # print(gg.int_1())
    # print(type(gg.int_1()))

"""
