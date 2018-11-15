#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:09:32 2018

@author: bing
"""

import json
str='''
[{
  "name":"冰",
  "gender":"male",
  "birthday":"1998-12-05"
  },{
        "name":"john",
        "gender":"male",
        "birthday":"1998-12-05"
        }]'''
data=json.loads(str)
with open('data.json','w',encoding='utf-8') as f:
    f.write(json.dumps(data,indent=2,ensure_ascii=False))