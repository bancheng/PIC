#! /usr/bin/env python
#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df1 = pd.read_excel("Finaloutput_nonzero.xlsx")
df2 = pd.read_excel("Finaloutput2_nonzero.xlsx")
label1 = []
for str in df1[df1.columns[0]].values:
        li = str.split('-')
        number = int(li[0])
        label1.append(number)
label1 = np.ones(len(df1.values))
index = np.random.permutation(len(df2.values))
label2 = np.zeros(len(label1))
label = np.concatenate((label1,label2),axis=0)
data_y = label.reshape(label1.shape[0]+label2.shape[0])
Vals1 = df1[df1.columns[6:]].values
Vals2 = df2[df2.columns[6:]].values[index[:len(label1)]]
Vals3 = df2[df2.columns[6:]].values[index[len(label1):]]
dataMat = np.vstack((Vals1,Vals2))


