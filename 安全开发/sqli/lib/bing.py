import requests,re


class Bing():
    def __init__(self,keyword,page=1):
        self.keyword = keyword
        self.page = page


    def href(self):
        for first in range(self.page):
            try:
                url = 'https://www.bing.com/search?q=%s&first=%d'%(self.keyword,first*10)
                headers = {'User-Agent':'"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)"'}
                content = (requests.get(url,headers=headers).content.decode())
                regex = '<h2>.*?href="(http.*?)".*?</h2>'
                items = (re.findall(regex,content))
                for item in items:
                    if 'id=' in item:
                        if '&amp;' in item:
                            item = item.replace('&amp;','&')
                    #links.append(item)
                        yield item
            except Exception as e:
                pass
if __name__ == '__main__':
    a= Bing("inurl:php?id=")
    a.href()