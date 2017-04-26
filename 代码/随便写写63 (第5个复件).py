#! /usr/bin/env python
#-*- coding: utf-8 -*-import numpy
import os
import pandas as pd
import time
import numpy as np
from collections import OrderedDict
from datetime import datetime


df = pd.read_excel("/home/dongge/PIC/dailyMetricsUse_Sent/BugsAndChangesetsC66150-C81461.xlsx")
dti = df['date']

_date1 = []
for _datetime in dti:
    delta = datetime(2016,2,2)-datetime(2016,2,1)
    _datetime = _datetime-delta
    ppydate_array = _datetime.strftime("%Y%m%d")
    _date1.append('maxwell-metrics-'+ppydate_array+'.7z')
print len(_date1)

_date2 = []
for _datetime in dti:
    delta = datetime(2016,2,2)-datetime(2016,2,1)
    _datetime = _datetime+delta
    ppydate_array = _datetime.strftime("%Y%m%d")
    _date2.append('maxwell-metrics-'+ppydate_array+'.7z')
print _date2

li = os.listdir("/home/dongge/PIC/dailyMetricsUse_Sent")
EncodedFileName = df[df.columns[3]].values

i = 0

if (_date1[i] in li)and(_date2[i] in li):
    os.chdir("/home/dongge/PIC/dailyMetricsUse_Sent/")
    path = os.getcwd()
    path1 = path +'/'+ _date1[i]
    path2 = path +'/'+_date2[i]
    os.chdir(path1)
    print os.getcwd()
    df1 = pd.read_csv("sm_output_csharp_encoded.csv")
    if EncodedFileName[i] in list(df1[df1.columns[28]].values):
        print 999999
