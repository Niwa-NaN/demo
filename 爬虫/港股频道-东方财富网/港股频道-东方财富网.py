# coding = utf-8
import requests
import re

def get_firstpage(url):
    response = requests.get(url)
    html = response.text
    print(html)
    # get_href(html)

def get_href(html):
    hrefs = re.findall('<li.*?<a href="(.*?)" target="_blank">港股通\((.*?)\)</a>.*?/li>',html,re.S)
    # print(hrefs)
    for href in hrefs:
        print(href)

if __name__ == '__main__':
    get_firstpage('http://hk.eastmoney.com/')