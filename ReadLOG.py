# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:35:08 2017

@author: surface
"""
import re
from datetime import datetime as dt
from pandas import DataFrame as df

with open('C:/Users/surface/Desktop/test.txt', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
    

def HRL(findkey):
    HRL=[]
    for line in lines:
        if line.find(findkey) != -1:
            HRL.append(line)
    return HRL

def FindMH(HRL):
    result = []
    for line in HRL:
        k = [float(h) for h in re.findall('\d+\.\d+',line)]
        k.insert(0,dt.strptime(re.search('\d+\:\d+\:\d+\:\d+',line)[0],'%H:%M:%S:%f'))
               
        result.append(k)
    return result


HRLE = HRL('ETH: GPU')
HRLS = HRL('SC: GPU')
MHE = FindMH(HRLE)
MHS = FindMH(HRLS)
dfe = df(MHE)
dfs = df(MHS)
print(dfe.mean())
print(sum(dfe.mean())) 
print(sum(dfs.mean()))



        