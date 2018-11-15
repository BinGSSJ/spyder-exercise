#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:31:33 2018

@author: bing
"""
import csv
with open('data.csv','w') as f:
    fieldnames=['id','name','age']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'1234','name':'Bob','age':'18'})
    writer.writerow({'id':'1234','name':'Bob','age':'18'})
    writer.writerow({'id':'1234','name':'Bob','age':'18'})