#!/usr/bin/python3
#--coding:utf-8--
import requests,re,json,base64





def fofaserach(keyword):
    FOFA_EMAIL= ''
    FOFA_KEY = ''
    page = 2
    size= 5000
    keyword = base64.b64encode(keyword.encode('utf-8')).decode('utf-8')
    #print(keyword)

    url = "https://fofa.so/api/v1/search/all?email="+str(FOFA_EMAIL)+"&key="+str(FOFA_KEY)+"&qbase64="+str(keyword)+"&page="+str(page)+"&size="+str(size)
    res = requests.get(url).text

    txt = json.loads(res)
    #print(txt)
    for i in txt['results']:
        print(i[0])
        f=open('qqW.txt','a+')
        f.write('\n')
        f.write(i[0])
        f.close()
        



if __name__ == "__main__":
    fofaserach('app="thinkcmf" && country="US"')

