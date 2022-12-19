#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
import os
import re
import matplotlib.pyplot as plt

filt=["(","=","http","<","::"]

if not os.path.isfile("data.txt"):
	# 模拟浏览器的身份验证信息
	headers = {'User-Agent':'Chrome/78.0.3904.108'}  
	
	url="https://www.winehq.org/announce/8.0-rc1"
	
	response=requests.get(url=url,headers=headers,timeout=20).text.encode()
	
	with open('data.txt','wb') as fp:
		fp.write(response)
fd=open("data.txt")
soup=BeautifulSoup(fd,'lxml')

words=soup.decode().split()
word_table={}
for word in words:
	if ":" in word:
		if not any(f in word for f in filt):
			if (word.find(":")+1) == len(word):
				   word=word[:-1]	   
			if word.lower() in word_table:
				word_table[word.lower()]=word_table[word.lower()]+1
			else:
				word_table[word]=1
result=sorted(word_table.items(),key=lambda d:d[1],reverse=True)[:20]

x=[]
y=[]
for r in result:
	x.append(r[0])
	y.append(r[1])
fig,ax=plt.subplots(figsize=(12,7),dpi=100)
ax.set_title("The hot words that wine-8.0 updated")
for a,b in zip(x, y):
    ax.text(b,a,b,ha='left', va='center')

#ax.set_xlabel("word",fontproperties='SimHei',fontsize=12)
ax.set_xlabel("nums",fontsize=12)
ax.set_ylabel("word",fontsize=12)
plt.barh(x,y)
plt.show()
#plt.savefig("barChart.jpg")

