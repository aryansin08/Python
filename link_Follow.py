#!/usr/bin/env python
# coding: utf-8

# In[4]:


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input("Enter count: "))
position = int(input("Enter position: "))
# Retrieve all of the anchor tags
tags = soup('a')
lst = list()
for tag in tags:
    lst.append(tag.get('href', None))
for _ in range(count):
    html = urllib.request.urlopen(lst[position-1], context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print("Retrieving", lst[position-1])
    lst = []
    for tag in tags:
        lst.append(tag.get('href', None))


# In[ ]:




