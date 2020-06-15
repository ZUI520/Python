import requests
from bs4 import BeautifulSoup
import lxml
import re

class Baidu():
    def __init__(self,keyword,page=1):
        self.keyword = keyword
        self.page = page
    

    def href(self):
        for i in range(self.page):
            url = "https://www.baidu.com/s?ie=UTF-8&wd=%s&pn=%d"%(self.keyword,i*10)
        
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

            r = requests.get(url,headers=headers).text
            soup = BeautifulSoup(r, 'lxml')
            tagh3 = soup.find_all('h3')
            for h3 in tagh3:
                href = h3.find('a').get('href')
                try:
                    baiurl = requests.get(url=href,headers=headers).url
                    if 'id=' in baiurl:
                        
                        yield baiurl
                except Exception as e:
                    pass
                                                                            

if __name__=='__main__':
    a = Baidu("inurl:php?id=")
    a.href()