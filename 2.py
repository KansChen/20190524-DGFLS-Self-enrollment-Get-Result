#微信请求：Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI
import time
import csv
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import re
import json
import os
def htmlcatch(pcode,pname):

        s2='https://wx.tigerlu.com/app/index.php?keyword='+pname+'%23'+pcode+'&c=entry&do=index&i=3&m=tigerlu_search&id=145'
        wechathead={'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI'}

        browser2=requests.get(s2,headers=wechathead)
        time.sleep(0.5)

        input=browser2.text
        #print(input)
        soup = BeautifulSoup(input, "html.parser")
        score =soup.find_all('p')
        pattern = re.compile(r'\d+\.?\d*')
        tmp=pattern.findall(str(score))
        if len(tmp):
                print(tmp[-1],file=ans)
        else:
                print('No data',file=ans)
        time.sleep(1)

csvfile=open('data.CSV','r',encoding='utf-8')
ans=open('score2.txt','w',encoding='utf-8')
reader=csv.DictReader(csvfile)
a=0
for row in reader:
        print(row['number'],row['name'],file=ans)
        htmlcatch(row['number'],row['name'])
        a=a+1
        print(a)
exit(0)