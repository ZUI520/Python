#!/usr/bin/env python
# -*- conding:utf-8 -*- 
import urllib.request

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Connection': 'close',
'Upgrade-Insecure-Requests': '1'
}
url = "url.txt"
webdir = []
with open(url) as infile:
    while True:
        dirdir = infile.readline().strip()
        if(len(dirdir)==0):break
        webdir.append(dirdir)

for line in webdir:
    f = open('成功.txt', 'a+')
    # url="http://www.lszyxy.edu.cn"
    dir ='/data/backupdata/dede_a~'
    for i in range(1,6):

        urls = 'http://'+ line + dir + str(i) + '.txt'

        try:
            head = urllib.request.Request(urls, headers=headers)
            data = urllib.request.urlopen(head, timeout=3).getcode()
            print(urls)
            if data == 200:
                print('成功啦----》' + urls)

                f.write("%s \n"%str(urls))

            else:
                print('错误：' + urls)
        except Exception as e:
            print("访问失败！")
            print(e)
            continue
