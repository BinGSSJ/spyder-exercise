#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:48:50 2018

@author: bing
"""
from bs4 import BeautifulSoup
import re
l=list()
def read_html(filename):
    with open(filename,'r',encoding='utf-8') as f:
        html=f.read()
    return html
if __name__=='__main__':
    html=read_html('test.html')
    soup=BeautifulSoup(html,'lxml')
    s=soup.find(name='ul')
    t=s.find(name='li')
    l.append(t.text.split('\n'))
    print(l)