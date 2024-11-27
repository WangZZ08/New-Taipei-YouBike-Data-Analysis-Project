# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:56:09 2022

@author: Zhi就是我啦><
"""
import urllib.request
import re

url = 'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv?page=0&size=1000'

url_request = urllib.request.urlopen(url)
data_read = url_request.read()
data = data_read.decode(encoding = 'utf-8', errors = 'ignore')

datalist = re.split(r'","|"\n"' , data) #原始檔中遇到，和\N分割為一個元素
#print(datalist)
area = [] # Set area is a empty list
number = [] # Set number is a empty list

#由第16個元素(第一個區的Ubike總數)開始，每間隔14換下一個所需元素
for r in range(16, len(datalist), 14):
    #print(datalist[r],datalist[r+2])
    
    #給定位置
    try:
        area.index(datalist[r+2])
        #print(datalist[r+2])
        #print(area)
    except:
        area.append(datalist[r+2])
    
#print(area)
 
for a in area:
    total = 0
    
    for d in range(16, len(datalist), 14):
        #print(a, datalist[d+2])
        if a == datalist[d+2]:
            total = total + int(datalist[d])
            
   # print(total, a) 
    number.append(total)

null = number.copy() 
null.sort() #由小至大排列

#print(area)
#print(number)
#print(null)

t = 0

# 將使用過的值歸0
for n in null:
    pr = number.index(n)
    print(area[pr], n)
    number[pr] = 0
    t = t + n
    #print(number)
print('新北Ubike各區總量:',t) 
