import requests
import re
from bs4 import BeautifulSoup

headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",

}


def get_html(url):
    r = requests.get(url,headers=headers).content.decode('gb2312')
    ips = re.findall("<td>(\d+.\d+.\d+.\d+)</td><td>(\d+)</td><td>",r,re.S)
    ipss= str(ips).replace(", ",":").replace("'):(","\n").replace("[('","").replace("'","").replace(")]","")
    print(ipss)
    f= open('./ips.txt','a+')
    f.write(ipss)
    f.close()







if __name__ == "__main__":
    for i in range(1,79):
        url = 'http://www.66ip.cn/areaindex_3/%d.html'%i
        get_html(url)

