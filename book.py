
import requests
from bs4 import BeautifulSoup
import re
import codecs
import threading

# 给请求指定一个请求头来模拟chrome浏览器
global headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
server = 'http://www.biquge.tv/'
# 星辰变地址
book = 'http://www.biquge.tv/0_377/'
# 定义存储位置
global save_path
save_path = 'E:/xiaos'



#解析内容
def get_content(chapter):
    req = requests.get(chapter,headers=headers).content
    soup = BeautifulSoup(req,'html.parser')
    texts = soup.find_all('div',id='content')
    contents = texts[0].text
    return contents
    #print(content)
#文件保存函数
def wite_txt(chapter,content,code):
    with codecs.open(chapter,'a',encoding=code) as f:
        f.write(content)


#主函数
def main():
    res = requests.get(url=book,headers=headers).content
    soup = BeautifulSoup(res,'html.parser')
    a= soup.find('div',id='list').find_all('a')
    print('总章节数: %d ' % len(a))
    for i in a:
        try:
            chapter = server + i.get('href')
            content = get_content(chapter)
            chapter = save_path +'/'+i.string + ".txt"
            print('正在爬取：%s'%chapter)
            wite_txt(chapter,content,'utf-8')
        except Exception as e:
            print(e)
def thread():
    th = []
    th_num = 10
    for x in range(th_num):
        t = threading.Thread(target=main)
        th.append(t)
    for x in range(th_num):
        th[x].start()
    for x in range(th_num):
        th[x].join
   

if __name__ == "__main__":
    thread()
    
