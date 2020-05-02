#!/usr/bin/python3
#-*- coding:utf-8 -*-

#导入模块
import requests
import hashlib
import json
import threading

#定义一个数组
Cms = []

#定义一个read()方法 用来处理cms的指纹
def read():
    f = open(r"E:\\Python项目\\pc\\安全开发\\Cms\\data.json","r",encoding='utf-8')
    #将已编码的 JSON 字符串解码为 Python 对象
    cms = json.load(f)
    #然后讲cms遍历并写入到数组中 list
    for i in cms:
        Cms.append(i)

def Cms_url(url):
    for i in Cms:
        urls = url + i['url']
        #加个异常处理
        try:
            #现在开始用到requests模块
            res = requests.get(url=urls,timeout=2)
            print(urls)
            #使用hashlib来获取网站MD5 并判断cms版本
            md5 = hashlib.md5(res.content).hexdigest()
            if md5 == i["md5"]:
                #打印urls
                
                #打印结果
                print("CMS版本:%s"%i['name'])
                #使用break来结束
                break
        except:
            pass


if __name__ == "__main__":
    read()
    Cms_url("http://www.wyaq.top")
    
    