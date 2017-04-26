#! /usr/bin/env python
#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd

def _data(file1,file2):
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)
    label1 = []
    for str in df1[df1.columns[0]].values:
        li = str.split('-')
        number = int(li[0])
        label1.append(number)
    label1 = np.ones(len(df1.values))
    label2 = np.zeros(len(df2.values))
    label = np.concatenate((label1,label2),axis=0)
    data_y = label.reshape(label1.shape[0]+label2.shape[0])
    Vals1 = df1[df1.columns[6:]].values
    Vals2 = df2[df2.columns[6:]].values
    dataMat = np.vstack((Vals1,Vals2))
    return dataMat,data_y


