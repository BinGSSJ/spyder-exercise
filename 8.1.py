#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:24:37 2018

@author: bing
"""

import tesserocr
from PIL import Image

image=Image.open('CheckCode.jpg')
result=tesserocr.image_to_text(image)
print(result)