#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:19:43 2018

@author: bing
"""

#抓取二进制数据
import requests
headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36'
        }
r=requests.get("http://jianshu.com",headers=headers)
print(r.status_code) if not r.status_code==requests.codes.forbidden else print("No")