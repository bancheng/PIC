#! /usr/bin/env python
#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def _data(file1,file2):
    percent_sample = 0.7
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)
    label1 = []
    for str in df1[df1.columns[0]].values:
        li = str.split('-')
        number = int(li[0])
        label1.append(number)
    label1 = np.ones(len(df1.values))
    label11 = label1[:int(len(label1)*percent_sample)]
    label12 = label1[int(len(label1)*percent_sample):]

    index1 = np.random.permutation(len(df1.values))
    index2 = np.random.permutation(len(df2.values))

    label21 = np.zeros(int(len(label1)*percent_sample))

    label22 = np.zeros(len(df2.values)-int(len(label1)*percent_sample))

    label_train = np.concatenate((label11,label21),axis=0)
    train_y = label_train.reshape(label11.shape[0]+label21.shape[0])
    label_test = np.concatenate((label12,label22),axis=0)
    test_y = label_test.reshape(label12.shape[0]+label22.shape[0])

    Vals11 = df1[df1.columns[6:]].values[index1[:int(len(label1)*percent_sample)]]
    Vals12 = df1[df1.columns[6:]].values[index1[int(len(label1)*percent_sample):]]

    Vals21 = df2[df2.columns[6:]].values[index2[:int(len(label1)*percent_sample)]]
    Vals22 = df2[df2.columns[6:]].values[index2[int(len(label1)*percent_sample):]]

    train_x = np.vstack((Vals11,Vals21))
    test_x = np.vstack((Vals12,Vals22))
    return train_x,train_y,test_x,test_y


