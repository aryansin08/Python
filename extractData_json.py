#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
from urllib.request import urlopen
import ssl

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Location: ")
data = urlopen(url, context = ctx).read().decode()

info = json.loads(data)
s = 0
print(info)
for item in info['comments']:
    s+=int(item['count'])
print(s)

# Url http://py4e-data.dr-chuck.net/comments_42.json Sum =2553


# In[ ]:




