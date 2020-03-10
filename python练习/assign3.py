#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lesson 3 Week 2
file = open('C:/Users/Koe.Shu/Desktop/Coursera/Python_for_Everyone/practice/regex_sum_42.txt')
import re
numstrg = file.read()
num = re.findall('[0-9]+',numstrg)
numlist = list()
for n in num:
    x = int(n)
    numlist.append(x)
print (sum(numlist))


# In[5]:


#Lesson 3 Week 2
file = open('C:/Users/Koe.Shu/Desktop/Coursera/Python_for_Everyone/practice/regex_sum_366525.txt')
import re
numstrg = file.read()
num = re.findall('[0-9]+',numstrg)
numlist = list()
for n in num:
    x = int(n)
    numlist.append(x)
print (sum(numlist))


# In[ ]:


#Lesson 3 Week 3 
#This code is not perfect.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()


# In[12]:


#Lesson3 Week3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

numbers = soup.find_all('span')
numlist = list()
for num in numbers:
    num = int(num.text)
    numlist.append(num)
print('SUM:', sum(numlist))


# In[24]:


#Lesson3Week4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter the website: ')
position = int(input('Enter position:'))-1
count = int(input('Enter count:'))

while True:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    links = soup('a')
    link = links[position].get('href', None)
    if count > 1:
        count = count - 1
        url = link
    else:
        ans = links[position].get_text()
        break
print(ans)


# In[ ]:


#Lesson3Week5
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#正式开始代码运作
url = input('Enter Location: ')
xml2 = urllib.request.urlopen(url, context=ctx).read()
xxml = ET.fromstring(xml2)
counts = xxml.findall('.//count')
total = 0
for count in counts:
    total += int(count.text)

print ("Sum:" + str(total))


# In[23]:


#Lesson3Week6
import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter Location: ')
info = urllib.request.urlopen(url).read()

data = json.loads(info)
data = data['comments']
total = 0
for item in data:
    total += int(item['count'])
print("Sum: "+str(total))


# In[10]:


#Lesson3Week6
import urllib.request,urllib.parse,urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = input("Enter location:")


url = serviceurl + urllib.parse.urlencode({'address':address,'key':42})
data = urllib.request.urlopen(url).read()
js = json.loads(data)
place_id = js['results'][0]['place_id']
print('PLACE ID: ', place_id)


# In[ ]:




