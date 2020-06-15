"""
Author : d4m1ts
Version : 0.0.1
"""

import requests
import threading
import sys
import os
from src import color

vulnerables = []

class Scan:
    def __init__(self,link):
        '''
        type errors  : list
        param errors : sqli error that may exist

        type links  : generate
        param links : all links want wo test
        '''
        #a= r'E:\Python项目\pc\安全开发\sqli\src\sql_error.ini'
        a= r'sql_error.ini'
        sql_error = open(a,'r')
        errors = sql_error.readlines()
        sql_error.close()
        self.errors = errors
        self.link = link

    def create_link(self,url):
        '''
        Create a link with symbol '

        type url  : str
        param url : which url to add '

        return type : str
        '''
        domain = url.split("?")[0]
        params = {}
        param = url.split("?")[1]
        for pm in param.split('&'):
            key,value = pm.split('=')
            try:
                int(value)  # if the param can int(),illustrate it was a number
                value += "'"
            except:
                pass
            params[key] = value
        website = domain+'?'
        for param in params:
            pm = param + '=' + params[param] + '&'
            website += pm
        return (website.strip('&'))

    def check_sqli(self,url):
        '''
        check SQL injection vulnerability

        type url  : str
        param url : URL that needs to be detected
        '''
        try:
            headers = {'User-Agent':'"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)"'}
            content = requests.get(url,headers=headers,timeout=5).content.decode('utf-8','ignore')
            for sql_error in self.errors:
                if sql_error.strip('\n') in content:
                    vulnerables.append(url.replace("'",''))
                    
                    color.printRed("[存在注入漏洞]" + url.replace("'",''))
                    
                    #break
                    sys.exit(0)
                else:
                    pass
        except:
            pass

    def main(self):
        '''
        type links : list
        param links : all links need to test
        '''
        for links in self.link:
            try:
                url = (self.create_link(links.strip('\n')))
                thread = threading.Thread(target=self.check_sqli,args=(url,))
                thread.start()
                #thread.join()
            except Exception as e:
                print (e)
                pass
