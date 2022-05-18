import requests
from bs4 import BeautifulSoup
req=requests.get('https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt')
#print(req.text.find('美國2022中期選舉懶人包：你需要了解的基本問題答案在這裏'))
soup=BeautifulSoup(req.text,'lxml')
title=soup.findAll('span',{'class':"lx-stream-post__header-text gs-u-align-middle" })
alist=[]
for i in title:
    alist.append(i.getText())
print(alist)

