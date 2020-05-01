#!/usr/bin/python3
#-*- coding:utf-8 -*-
#导入模块
import requests,re
from bs4 import BeautifulSoup



url_ok = []
url_b =  []
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
}

class UrlSpider():
   
    def get_html(self,root_url):
        res = requests.get(url=root_url,headers=headers,timeout=3).text
        html = BeautifulSoup(res,'html.parser')
        div = html.find('div',id="search")
        lis = div.find_all("div",class_="g")
        href = re.findall('<a href="(http.*?\..*?\..*?)".*?ping="',str(lis),re.S)
        #re正则匹配
        url = str(href).replace(", ","\n").replace("['","").replace("']","").replace("'","")
        urlr = r'(http[s]?://.*?)/'
        r =re.findall(urlr,url,re.S)
        url_ok.append(r[0])

     #去重处理   
    def qc(self):
        for i in url_ok:
            if i not in url_b:
                url_b.append(i)

        print(str(url_b).replace("['","").replace("]","").replace(", ","\n").replace("'",""))
        with open("res_url.txt","a+") as f:
            f.write(str(url_b).replace("['","").replace("]","").replace(", ","\n").replace("'",""))
            f.write("\n")
            f.close()
    
    


if __name__ == "__main__":
    #翻页：&start=20
    for i in range(0,10):
        root_url = 'https://www.google.com/search?&q=肖战&start=%d'%i
        a = UrlSpider()    
        a.get_html(root_url)
        a.qc()
       
        

