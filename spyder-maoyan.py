#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 19:44:55 2018

@author: bing
"""
#spyder maoyan
import requests
import re
import json
import time
headers={
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
        }
def get_page(url):
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    print(response.status_code)
    return None
def write_to_file(content):
    with open('resuly.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
def parse_page(html):
    pattern=re.compile(
            '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
            re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield{
                'index':item[0],
                'image-url':item[1],
                'title':item[2].strip(),
                'actor':item[3].strip()[3:] if(len(item[3])>3) else'',
                'time':item[4].strip()[5:] if(len(item[4])>5) else '',
                'score':item[5].strip()+item[6].strip()
                }
     
        
def main(offset):
    url='http://www.maoyan.com/board/4?offset='+str(offset)
    html=get_page(url)
    for item in parse_page(html):
        print(item)
        write_to_file(item)
        
if __name__=='__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)