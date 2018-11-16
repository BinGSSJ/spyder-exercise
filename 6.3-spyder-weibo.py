#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:21:59 2018

@author: bing
"""

import requests
import csv
from urllib.parse import urlencode
from pyquery import PyQuery as pq
base_url='https://m.weibo.cn/api/container/getIndex?'
headers={
        'Host':'m.weibo.cn',
        'Referer':'https://m.weibo.cn/u/2830618474',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'X-Requested-With':'XMLHttpRequest'
        }

def get_page(page):
    params={
            'type':'uid',
            'value':'2830678474',
            'containerid':'1076032830678474',
            'page':page
            }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
            print('Error',e.args)
            
def parse_page(json):
    if json:
        items=json.get('data').get('cards')
        for item in items:
            item=item.get('mblog')
            weibo={}
            weibo['id']=item.get('id')
            weibo['text']=pq(item.get('text')).text()
            weibo['attitudes']=item.get('attitudes_count')
            weibo['comments']=item.get('comments_count')
            print(weibo)
            
def write_to_csv(dicts):
    with open('weibo.csv','a',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writerow(dicts)
        
if __name__=='__main__':
    fieldnames=['id','text','attitudes','comments']
    with open('weibo.csv','w',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        json=get_page(2)
        parse_page(json)
            