import os,sys
import argparse
from lib.baidu import Baidu
from lib.bing import Bing
from lib.google import Google
from lib.yahoo import Yahoo
from src.scan import Scan



def menu():
    parse = argparse.ArgumentParser()
    parse.add_argument('-k',dest='keyword',metavar='inurl:example',help="sql injection 关键字")
    parse.add_argument('-p',dest='page',metavar='page 20',help="搜索翻页数")
    parse.add_argument('-e',dest='engine',metavar='search engine',help="搜索引擎")
    args = parse.parse_args()
    return args

def main():
    args = menu()
    if (sys.argv) == 1:
        print("Please add -h to get help ")
        sys.exit()
    keyword = str(args.keyword)
    page = int(args.page)
    engine = str(args.engine)
    if engine == 'baidu':
        url = Baidu(keyword,page)
        link = (url.href())
    elif engine == 'bing':
        url = Bing(keyword,page)
        link = (url.href())
    elif engine == 'google':
        url = Google(keyword,page)
        link = (url.href())
    elif engine == 'yahoo':
        url = Yahoo(keyword,page)
        link = (url.href())

    scan = Scan(link)
    scan.main()


if __name__ == "__main__":
    main()

