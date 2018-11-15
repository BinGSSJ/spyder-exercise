#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:25:35 2018

@author: bing
"""

import requests
from pyquery import PyQuery as pq

headers={
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
        }
url='https://www.zhihu.com/explore'
html=requests.get(url,headers=headers).text
doc=pq(html)
items=doc('.explore-tab .feed-item').items()
for item in items:
    question=item.find('h2').text()
    author=item.find('.author-link-line').text()
    level=item.find('.bio').text()
    answer=pq(item.find('.content').html()).text()
    file=open('explore.txt','a',encoding='utf-8')
    file.write('\n'.join([question,author,level,answer]))
    file.write('\n'+'='*50+'\n')
    file.close()