#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:21:16 2018

@author: bing
"""
#4.1 Xpath练习
import requests
from lxml import etree
url='http://www.a-hospital.com/w/北京市医院列表'
headers={
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
        }
def get_html(url):
    response=requests.get(url,headers=headers)
    return response.text
def write_file(html):
    with open('test.html','a',encoding='utf-8') as f:
        f.write(html)
        
if __name__=='__main__':
    html=etree.parse('./test.html',etree.HTMLParser())
    result=html.xpath('//ul//li//b/a/text()')
    print(result)