# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:36:54 2022

@author: admin
"""
import requests 
from bs4 import BeautifulSoup
import html5lib

url="https://www.drishtiias.com/"
req=requests.get(url)
#print(req.content)
bp=BeautifulSoup(req.content, 'html5lib')
#print(bp.prettify())


tal=bp.findAll('div',{'class':'col-6 col-6 menu-list'})
for t in tal:
    for i in t.find('a'):
        print(i.text)
    