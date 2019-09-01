
# 爬虫：网络蜘蛛，spider
# 根据自己制定规则，模拟浏览器批量下载网络中的资源

# 聚焦爬虫 只针对某个网站进行的资源爬取
# 搜索爬虫 针对全网络进行的资源爬取

# 模拟浏览器的模块：requests/urllib2/urllib3/httppclient
# 筛选数据：re/ bs4 / xpath
# re.S 给点加功能，让.可以匹配到包括换行符
import re,requests

class Douban(object):
    def get_html(self):
        url1 = 'https://movie.douban.com/top250?start=0&filter'
        head = {"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
        res = requests.get(url=url1,headers=head)
        html = res.content.decode('utf-8')
        return html
    def get_name(self):
        s1 = self.get_html()
        print(s1)
        s2 = re.compile('<div class="hd">(.*?)</span>',re.S)
        a2 = s2.findall(s1)
        # print(a2)
        a4 = []
        for i in a2:
            s3 = re.compile(' <span class="title">(.*)',re.S)
            a3 = s3.findall(i)
            a4.append(a3[0])
        # a9 = []
        for j in range(len(a4)):
            s4 = re.compile(f'<img width="100" alt="{a4[j]}" src="(.*?)"',re.S)
            a5 = s4.findall(s1)
            # a9.append(a5)
        # return a9,a4
    # def save(self):
    #     a8 = self.get_name()
    #     print(a8)
        # for i in a8:
            s5 = requests.get(a5[0])
            a6 = s5.content
            with open(f'E:\豆瓣\{a4[j]}.jpg','wb') as s6:
                s6.write(a6)
                print('ok')

        # print(a4)
if __name__ == '__main__':
    GG = Douban()
    GG.get_name()

