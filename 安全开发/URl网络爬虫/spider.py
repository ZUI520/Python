#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests,re,sys
from urllib.parse import urljoin

urls = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
}

def spider():
    try:
        url = sys.argv[1]
        res = requests.get(url=url,headers=headers).text
        a = re.findall(r'href="(.*?)"',res,re.S)
        
        for url_s in a:
            if url_s not in urls:
                if 'css' not in url_s:
                    urls.append(urljoin(url,url_s))
        
        while True:
            for url_i in urls:
                if 'http:' not in url_i:
                    url = 'http://'+ url_i
                print(url_i)
                with open("url_suecc.txt","a+") as f:
                    f.write(url_i)
                    f.write("\n")
                    f.close()
            if len(urls) == len(urls):
                break
    except:
        pass


if __name__ == "__main__":
    spider()
    