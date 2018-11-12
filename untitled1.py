#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:14:19 2018

@author: bing
"""

from urllib import request,parse
url='http://httpbin.org/post'
headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MISE 5.5; WindowsNT)',
    'Host': 'httpbin.org'
    }
dict={
      'name':'Bob'
      }
data=bytes(parse.urlencode(dict),encoding='utf-8')
req=request.Request(url=url,data=data,headers=headers,method='POST')
response=request.urlopen(req)
print(response.read())