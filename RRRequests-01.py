#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:33:46 2018

@author: bing
"""
#requests
import requests
import re
headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36'
        }
r=requests.get("http://www.zhihu.com/explore",headers=headers)
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles=re.findall(pattern,r.text)
print(titles)