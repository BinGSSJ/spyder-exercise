#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:48:06 2018

@author: bing
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import requests
import os
import re
browser=webdriver.Chrome()
wait=WebDriverWait(browser,100)


def get_one(url):
    print('正在爬取...')
    try:
        browser.get(url)
        lists=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'commentlist')))
        html=lists.get_attribute('innerHTML')
    except Exception as e:
        print(e)
        return None
    print(html)
    return html
        
def write_html(html):
    with open('da.html','w',encoding='utf-8') as f:
        f.write(html)

def parse_one(html,page):
    if html!=None:
        try:
            soup=BeautifulSoup(html,'lxml')
            count=0
            imgs=soup.find_all(name='p')
            print(imgs)
            for img in imgs:
                img_url=re.findall('src="(.*?)"',str(img))
                for i in img_url:
                    print('正在下载:%s 第%s张 ' %(i,count))
                    count=count+1
                    #print(i)
                    write_to_file(i,'%s'%(str(page)),count)
        except Exception  as e:
            print(e)
def write_to_file(url,num,count):
    dirname=u'{}/{}'.format('jiandan',num)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    filename='%s/%s/%s.' %(os.path.abspath('.'),dirname,count)
    #print(filename)
    try:
        p=requests.get(url,timeout=10).content
        if url[-3:]=='jpg':
            filename=filename+'jpg'
        elif url[-3:]=='png':
            filename=filename+'png'
        elif url[-3:]=='gif':
            filename=filename+'gif'
        with open(filename,'wb+') as pic:
            pic.write(p)
    except Exception as e:
        print('图片%s下载失败'%(url))
        print(e)

def main():
    url='http://www.jandan.net/ooxx/page-35#comments'
    page=1
    while page!=20:
        html=get_one(url)
        parse_one(html,page)
        page+=1
        url='http://www.jandan.net/ooxx/page-'+str(36-page)+'#comments'
        
    
if __name__=='__main__':
    main()