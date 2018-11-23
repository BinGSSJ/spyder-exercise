#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:08:53 2018

@author: bing
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import csv
browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
keyword='iPad'

with open('data.csv','w') as f:
    fieldnames=['image','price','deal','title','shop','location']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    
def save_to_text(product):
    with open('data.csv','a',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=fieldnames)
            writer.writerow(product)
def get_products():
    html=browser.page_source
    doc=pq(html)
    items=doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product={
                'image':item.find('.pic .img').attr('data-src'),
                'price':item.find('.price').text(),
                'deal':item.find('.deal-cnt').text(),
                'title':item.find('.title').text(),
                'shop':item.find('.shop').text(),
                'location':item.find('.location').text()
                }
        print(product)
        #save_to_text(product)
def index_page(page):
    """
    抓取索引页
    """
    print('正在爬取第'+str(page)+'页')
    try:
        url='https://s.taobao.com/search?q='+quote(keyword)
        browser.get(url)
        if page>1:
            inp=wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form >input')))
            submit=wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
            inp.clear()
            inp.send_keys(page)
            submit.click()
        wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active >span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)
              
if __name__=='__main__':
    browser.get('https://www.taobao.com')
    for i in range(1,3):
        index_page(i)