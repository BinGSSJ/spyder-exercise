#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:34:40 2018

@author: bing
"""

from requests import Request,Session
headers={
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
        }
data={
      'name':'germy'
      }
url='http://httpbin.org/post'
s=Session()
req=Request('POST',url,data=data,headers=headers)
prepped=s.prepare_request(req)
r=s.send(prepped)
print(r.text)