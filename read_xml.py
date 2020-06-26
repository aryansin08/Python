#!/usr/bin/env python
# coding: utf-8

# In[2]:


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
commentinfo = ET.fromstring(data)
    
results = commentinfo.findall('comments/comment')
    
s=0
for item in results:
    s+=int(item.find('count').text)
print(s)
   


# In[ ]:




