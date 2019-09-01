import re
import urllib.request
import os
import time
from urllib.parse import quote

search_input = input("请输入搜索的书名或作者:")
search_Book = "https://www.qidian.com/search?kw=" + quote(search_input)
page = urllib.request.urlopen(search_Book).read()
txt = page.decode('utf-8')


def bookname():
    filter_bookname = r'<h4><a href=".+?" target="_blank" data-eid=".+?" data-bid=".+?" data-algrid="0.0.0">(.+?)</h4>'
    book_name_nosub = re.findall(filter_bookname, txt, re.S)
    book_name_sub = re.sub(r'<cite class="red-kw">|</a>|</cite>', '', " ".join(book_name_nosub))
    book_name = book_name_sub.split(' ')  # 书名
    return book_name


def bookChapter():
    filter_Chapter = r'<p class="update"><a href=".+?>(.+?)</a>'
    state_Chapter = re.findall(filter_Chapter, txt, re.S)
    return state_Chapter


def state():
    filter_time = r'<em>·</em><span>(.+?)</span>'
    state_time = re.findall(filter_time, txt, re.S)
    return state_time


def booklist():
    list1 = ["   "] * 10
    list2 = ["   "] * 10
    number = ["&#9450;", "&#9461;", "&#9462;", "&#9463;", "&#9464;", "&#9465;", "&#9466;", "&#9467;", "&#9468;",
              "&#9469;"]
    a = list(
        map(lambda c, x, a, y, b, z,: c + x + a + y + b + z, number, bookname(), list1, bookChapter(), list2, state()))
    b = "\n".join(a)
    return b


print(booklist())

i = int(input("输入你要下载书的号数:"))


def book_link(i):
    filter_book_id = r'<a class="red-btn" href="(.+?)"'
    book_id = re.findall(filter_book_id, txt, re.S)
    book_id_add = " http:".join(book_id)
    book_id_list = ("http:" + book_id_add).split(' ')
    book_id_love = book_id_list[i]
    return book_id_love


def book_First():
    page = urllib.request.urlopen(book_link(i=i)).read()
    txt = page.decode('utf-8')
    filter_book_id = r'data-firstchapterjumpurl="(.+?)">'
    book_first = "http:" + re.findall(filter_book_id, txt, re.S)[0]
    return book_first


######################################################################################################
def mkdir(path):  # 创建文件夹
    floder = os.path.exists(path)
    if not floder:
        os.makedirs(path)
        print("创建成功")
    else:
        print("文件已存在")


img_path = "E:/txt/txt/"
mkdir(img_path)

z = 0
url = []
link = book_First()  # url为第几页就从第几页开始获取
print("VIP章节暂不支持，不可以超过本书免费章节数")
x = int(input("请输入要下载的章节:"))
for read in (range(0, x)):  # 下载几章，这里默认5章
    url.append(link)  # append() 方法用于在列表末尾添加新的对象。
    page = urllib.request.urlopen(url[z]).read().decode('UTF-8')
    filter_page = r'p>\u3000\u3000(.+?)<'  # 小说的文本  <p>　****<p>　\u3000 代表空格
    html = re.findall(filter_page, page, re.S)
    filter_bookname = r'60c;</em>(.+?)</a>'
    bookname = re.findall(filter_bookname, page, re.S)

    filter_chaptername = r'<h3 class="j_chapterName">(.+?)</h3>'  # <h3 class="j_chapterName">第4章 继任者</h3>
    chaptername = re.findall(filter_chaptername, page, re.S)  # 获取章节和章节名字
    i = 0
    for txt in html:
        line = html[i]
        f = open(img_path + chaptername[0] + ".txt", "a")  # a代表追加模式，不覆盖
        f.write(line + "\n")
        f.close()
        i = i + 1
    print(chaptername[0] + "  下载完成")

    next = r'<a id="j_chapterNext".+?href="//(.+?)"'  # <a id="j_chapterNext" href="//read.qidian.com/chapter/HZe9IzSe3h3iUReBXKVubw2/mvMfZ61JMBHM5j8_3RRvhw2" data-eid="qd_R109" >下一章</a>
    nextread = re.findall(next, page, re.S)
    b = ''
    link = "https://" + b.join(nextread)  # 本页的下一章链接
    z = z + 1
img_path2 = "E:/txt/" + bookname[0]

c = 0
if not os.path.exists(img_path2):  # 如果文件不存在，则重命名文件
    os.rename(img_path, img_path2)  # 文件夹重命名
    print("下载完成")
else:
    path = "E:/txt/txt/"
    downloadtime = time.strftime("%Y%m%d%I%M%S", time.localtime())
    os.rename(img_path, img_path2 + downloadtime)
    print("文件名:" + bookname[0] + " 已存在,重命名为:" + bookname[0] + downloadtime + "\n" + "请勿重复操作")