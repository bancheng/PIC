#! /usr/bin/env python
#-*- coding: utf-8 -*-import numpy
import os
import pandas as pd
from datetime import datetime
import numpy as np
import timeit


df = pd.read_csv("/home/dongge/PIC/basic_data/ChangesetsC66150-C81461.csv")
EncodedFileName = df[df.columns[3]].values


##日期格式转换
dti = df['date']
_date = []
print dti[1]
for _datetime in dti:
    _datetime = datetime.strptime(_datetime, '%Y/%m/%d')
    ppydate_array = _datetime.strftime("%Y%m%d")
    _date.append('maxwell-metrics-'+ppydate_array+'.7z')
print _date

def advance(_datetime):
    index1 = _datetime.index("s")
    index2 = _datetime.index(".")
    _datetime = _datetime[(index1+2):index2]
    _datetime = datetime.strptime(_datetime, '%Y%m%d')
    delta = datetime(2016,2,2)-datetime(2016,2,1)
    _datetime = _datetime-delta
    ppydate_array = _datetime.strftime("%Y%m%d")
    _datetime = 'maxwell-metrics-'+ppydate_array+'.7z'
    return _datetime

def retard(_datetime):
    index1 = _datetime.index("s")
    index2 = _datetime.index(".")
    _datetime = _datetime[(index1+2):index2]
    _datetime = datetime.strptime(_datetime, '%Y%m%d')
    delta = datetime(2016,2,2)-datetime(2016,2,1)
    _datetime = _datetime+delta
    ppydate_array = _datetime.strftime("%Y%m%d")
    _datetime = 'maxwell-metrics-'+ppydate_array+'.7z'
    return _datetime


##文件路径
li = os.listdir("/home/dongge/PIC/dailyMetricsUse_Sent")
_li = []
for file in li:
    index1 = file.index("s")
    index2 = file.index(".")
    number = file[(index1+2):index2]
    _li.append(number)
order = np.argsort(_li)
i = 0
while i<len(order):
    _li[i] = li[order[i]]
    i = i+1
li = _li

i = 0
start_time = timeit.default_timer()


while i<len(_date):
    if (_date[i] in li):
        index1 = li.index(_date[i])-1
        index2 = li.index(_date[i])+1
        _date1 = li[index1]
        _date2 = li[index2]
        os.chdir("/home/dongge/PIC/dailyMetricsUse_Sent/")
        path = os.getcwd()
        path1 = path + '/' + _date1
        path2 = path + '/' + _date2
        os.chdir(path1)

        path3 = os.getcwd()
        li1 = os.listdir(path3)
        if len(li1) == 0:
            supplement1 = np.zeros(25)
        else:
            if len(li1) == 2:
                df1 = pd.read_csv("sm_output_csharp_encoded.csv")
                df11 = pd.read_csv("sm_output_cpp_encoded.csv")
                if EncodedFileName[i] in list(df1[df1.columns[28]].values) or EncodedFileName[i] in list(
                        df11[df11.columns[28]].values):
                    if EncodedFileName[i] in list(df1[df1.columns[28]].values):
                        df1['Name of Most Complex Method*'] = 0
                        index1 = list(df1[df1.columns[28]].values).index(EncodedFileName[i])
                        supplement1 = df1[df1.columns[3:28]].values[index1]
                    else:
                        df11['Name of Most Complex Function*'] = 0
                        index1 = list(df11[df11.columns[28]].values).index(EncodedFileName[i])
                        supplement1 = df11[df11.columns[3:28]].values[index1]
                else:
                    supplement1 = np.zeros(25)
            else:
                df111 = pd.read_csv(li1[0])
                if EncodedFileName[i] in list(df111[df111.columns[28]].values):
                    df111['Name of Most Complex Method*'] = 0
                    df111['Name of Most Complex Function*'] = 0
                    index1 = list(df111[df111.columns[28]].values).index(EncodedFileName[i])
                    supplement1 = df111[df111.columns[3:28]].values[index1]
                else:
                    supplement1 = np.zeros(25)
        os.chdir(path2)
        path4 = os.getcwd()
        print path4
        li2 = os.listdir(path4)
        if len(li2) == 0:
            supplement2 = np.zeros(25)
        else:
            if len(li2) == 2:
                df2 = pd.read_csv("sm_output_csharp_encoded.csv")
                df22 = pd.read_csv("sm_output_cpp_encoded.csv")
                if EncodedFileName[i] in list(df2[df2.columns[28]].values) or EncodedFileName[i] in list(
                        df22[df22.columns[28]].values):
                    if EncodedFileName[i] in list(df2[df2.columns[28]].values):
                        df2['Name of Most Complex Method*'] = 0
                        index2 = list(df2[df2.columns[28]].values).index(EncodedFileName[i])
                        supplement2 = df2[df2.columns[3:28]].values[index2]
                    else:
                        df22['Name of Most Complex Function*'] = 0
                        index2 = list(df22[df22.columns[28]].values).index(EncodedFileName[i])
                        supplement2 = df22[df22.columns[3:28]].values[index2]
                else:
                    supplement2 = np.zeros(25)
            else:
                df222 = pd.read_csv(li2[0])
                if EncodedFileName[i] in list(df222[df222.columns[28]].values):
                    df222['Name of Most Complex Method*'] = 0
                    df222['Name of Most Complex Function*'] = 0
                    index2 = list(df222[df222.columns[28]].values).index(EncodedFileName[i])
                    supplement2 = df222[df222.columns[3:28]].values[index2]
                else:
                    supplement2 = np.zeros(25)
        if (supplement1.any() == 0) or (supplement2.any() == 0):
            _supplement = np.zeros(25)
        else:
            supplement1[np.where(supplement1 == '9+')] = 10
            supplement2[np.where(supplement2 == '9+')] = 10
            supplement1[np.where(supplement1 == '8')] = 8.0
            supplement2[np.where(supplement2 == '8')] = 8.0
            supplement1 = np.array(supplement1, dtype=float)
            supplement2 = np.array(supplement2, dtype=float)
            _supplement = supplement1 - supplement2
        for m in np.arange(25):
            df[df.columns[m + 6]].values[i] = _supplement[m]
    else:
        for m in np.arange(25):
            df[df.columns[m + 6]].values[i] = 0
    i = i + 1
    end_time = timeit.default_timer()
    print('ran for %.1fs' % (end_time - start_time))


print df[df.columns[6]]
os.chdir(path)
writer = pd.ExcelWriter('againFinaloutput2.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
print writer