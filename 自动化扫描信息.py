# -*- encoding:utf-8 -*-
#/usr/bin/python3
#端口，端口服务，指纹，子域名，备案查询，ip历史解析
import nmap,sys,re,json,requests
from bs4 import BeautifulSoup

def callback_result(host,scan_result):
    Port_range = re.findall("services\".*\"}}, \"scanstats\"",json.dumps(scan_result))
    
    for x in Port_range:
        print("Scan port range:"+x.strip("}}, \"scanstats\"").strip("ervices\":\""))
    Port_statere = re.findall("user-set\"},.*",json.dumps(scan_result))

    for State_filtering in Port_statere:
        port = re.findall(".{9}.state.{8}",State_filtering)
        Open_port = re.findall("\d+",str(port).replace("\":{\"state\":\"open\'","").replace("[\' {\"",""))
        print("开放的端口：","\n",Open_port)
        print("--"*30)

    #端口开放的服务
    for Open_service in Port_statere:
        server = re.findall("name.{10}",Open_service)
        x= str(server).replace("\'name\": \"","")
        print("端口开放的服务：","\n",x)
        print("--"*30)

    #域名解析历史
    try:
        history = "https://site.ip138.com/" +sys.argv[1]
        domain_history = requests.get(url=history,headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Mobile Safari/537.36'} ).text
        print("域名历史解析结果：")
        html = BeautifulSoup(domain_history,'html.parser')
        soup = html.find('div',id='J_ip_history')
        p = soup.find_all('p')
        ip = soup.find_all('a')
        rs = re.findall(r'<a href=".*?" target="_blank">(.*?)</a>',str(ip),re.S)
        print(rs,'\n')
        print("--"*30)


    #指纹识别
        header = {
             'Host': 'whatweb.bugscaner.com',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
             'X-Requested-With': 'XMLHttpRequest',
        }
        data = {'url':sys.argv[1],'location_capcha': 'no'}
        cms = requests.post(url='http://whatweb.bugscaner.com/what.go',data=data,headers=header).text
        ner = str(cms).replace(", ","\n").replace("{","").replace("}","").replace("\"status\": 99", " -"*30)
        print("指纹识别结果：")
        print(ner.encode('utf-8').decode('unicode_escape'))
        print("--"*30)
    #子域名搜索
     
    except Exception as e:
        pass

#异步Scanner
nm = nmap.PortScannerAsync()


try:
    nm.scan(sys.argv[1],ports=sys.argv[2],arguments='-Pn',callback=callback_result)
    if 'gov' in sys.argv[1]:
        print('警告！！gov属于政府类，禁止扫描！！')
    else:
        while nm.still_scanning():
            nm.wait(2)
except:
    info = '''
 * 　　　　　　　 ┏┓　　　┏┓
 * 　　　　　　　┏┛┻━━━━━┛┻┓
 * 　　　　　　　┃　　　　　　┃ 　
 * 　　　　　　　┃　　　━　　 ┃
 * 　　　　　　　┃　＞　　＜　 ┃
 * 　　　　　　　┃　　　　　　 ┃
 * 　　　　　　　┃... ⌒ ... ┃
 * 　　　　　　　┃　　　　　　┃
 * 　　　　　　　┗━┓　　　┏━┛
 * 　　　　　　　　 ┃　　　┃　Code is far away from bug with the animal protecting　　　　　　　　　　
 * 　　　　　　　　 ┃　　　┃   神兽保佑,代码无bug
 * 　　　　　　　　 ┃　　　┃　　　　　　　　　　　
 * 　　　　　　　　 ┃　　　┃  　　　　　　
 * 　　　　　　　　 ┃　　　┃
 * 　　　　　　　　 ┃　　　┃　　　　　　　　　　　
 * 　　　　　　　　 ┃　　　┗━━━┓
 * 　　　　　　　　 ┃　　　　　　　┣┓
 * 　　　　　　　　 ┃　　　　　　　┏┛
 * 　　　　　　　　 ┗┓┓┏━┳┓┏┛
 * 　　　　　　　　　┃┫┫　┃┫┫
 * 　　　　　　　　　┗┻┛　┗┻┛
 *
 '''
    print(info)
    print("--"*30)
    print("Use:python test.py domain/IP Port-range")
    print("--"*30)
    print("Example:python test.py www.baidu.com 1-1000")
    print("--"*30)
