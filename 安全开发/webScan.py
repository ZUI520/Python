#
#目录扫描  简单实现 python dir.py http://127.0.0.1/   扫描结果打印出来
import sys
import requests
import threading

s=sys.argv[1]
def dir():
    with open('dic.txt','r') as f:
        for line in f.readlines():  #readlines() 从dic.txt文件中读取所有行
            lines=line.strip()  #strip()移除字符串头尾指定的字符 如空格 回车\n
            #print(lines)
            r=requests.get(url=s+lines,)
            print("扫描结果为：",r.url,r.status_code)
def thread():
    th = []
    th_num = sys.argv[2]
    for x in range(th_num):
        t = threading.Thread(target=dir)
        th.append(t)
    for x in range(th_num):
        th[x].start()
    for x in range(th_num):
        th[x].join()

if __name__ == '__main__':
    thread()
