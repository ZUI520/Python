
import requests
from bs4 import BeautifulSoup
import threading
import Pymysql_DBUtils
from Pymysql_DBUtils import MyPymysqlPool
import importlib,sys
importlib.reload(sys)


# 给请求指定一个请求头来模拟chrome浏览器
global headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
server = 'http://www.biquge.tv/'
# 星辰变地址
book = 'http://www.biquge.tv/41_41485/'

# 定义DB
mysql = MyPymysqlPool("dbMysql")


#解析内容
def get_content(chapter):
    req = requests.get(chapter,headers=headers).content
    soup = BeautifulSoup(req,'html.parser')
    texts = soup.find_all('div',id='content')
    contents = texts[0].text
    return contents
    #print(content)

# 写入数据库
def write_db(chapter, content):
    sql = "INSERT INTO novel (title, content) VALUES(%(title)s, %(content)s);"
    param = {"title": chapter, "content": content}
    mysql.insert(sql, param)


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
            chapter = i.string 
            print('正在爬取：%s'%chapter)
            write_db(chapter,content)
        except Exception as e:
            print(e)
    mysql.dispose()

    

if __name__ == "__main__":
    main()
    
