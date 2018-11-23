#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 15:38:46 2018

@author: bing
"""

#今日头条街拍 待完善
import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from bs4 import BeautifulSoup
import json
from multiprocessing.pool import Pool

count=0
def get_page(offset):
    params={
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'3',
        }
    url='https://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError:
        return None

def parse_page(html):
    if html.get('data'):
        for item in html.get('data'):
            title=item.get('title')
            if title is None:
                title=str(count)
                count=count+1
            images=item.get('image_list')
            for image in images:
                yield{
                        'image':'http:'+image.get('url').replace('list','large') if image.get('url') else' ',
                        'title':title
                        } 


def save_image(item):
    print(item.get('title'))
    title=item.get('title')
    if not os.path.exists(item.get('title')):
            os.mkdir(item.get('title'))
    try:
        response=requests.get(item.get('image'))
        if response.status_code==200:
            file_path='{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
    except requests.ConnectionError:
        print('Failed to save images')
    
def main(offset):
    json=get_page(offset)
    for item in parse_page(json):
        print(item)
        save_image(item)
        
if __name__=='__main__':
    pool=Pool()
    groups=([x*20 for x in range(1,21)])
    pool.map(main,groups)
    pool.close()
    pool.join()
        