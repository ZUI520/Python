#!/usr/bin/python3
#--coding:utf-8--
import re
import numpy

countX = []
def read():
    # 打开日志文件，
    with open('access_log', 'r') as f:
        a = f.readlines()
    # 遍历日志文件里面内容，并使用关键字来查找自己需要的东西
    for i in a:
        # if 判断i里面是否有关键字包含 有就用re正则匹配处理 并写入countX列表中
        # ip = i.split(' ')[0]
        # url = i.split(' ')[6]
        # code = i.split(' ')[8]
        if "http://www.wyaq.top" in i:
            res = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", i)
            countX.append(''.join(res))
def ips():
    countSet = numpy.unique(countX)
    logfile = open("log.txt", 'w+')
    for ip in countSet:
        # print (' IP:',ip,' 出现次数:',countX.count(ip))
        print('出现次数,', countX.count(ip), ',IP,', ip, file=logfile)

def main():
    read()
    ips()

if __name__ == '__main__':
    print("日志分析开始==>>>")
    main()
    print("日志分析结束")