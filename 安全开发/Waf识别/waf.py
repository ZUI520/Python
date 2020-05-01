#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests,re,sys



headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
}

def waf():
    url = 'https://www.yunsuo.com.cn/%20and%201=1'
    r= requests.get(url=url,headers=headers)
    if re.search('eventID: ',str(r.content)):
        print("waf：奇安信")
    elif re.search('wzws-waf-cgi ',str(r.content)):
        print("waf：360防火墙")
    elif re.search('errors.aliyun.com ',str(r.content)):
        print("waf：云盾")
    elif re.search('.*__jsluid ',str(r.headers.values())):
        print("waf：知道创宇家")
    elif re.search('Safedog ',str(r.content)):
        print("waf：安全狗")
    elif re.search('405 method not allow ',str(r.content)):
        print("waf：腾讯云")
    elif re.search('Yunjiasu-ngnix ',str(r.headers.values())):
        print("waf：百度云")
    else:
        print("暂时没有记录waf指纹")


if __name__ == "__main__":
    waf()