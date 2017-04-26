#! /usr/bin/env python
#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import data_prepare2
import data_prepare4
from sklearn.externals import joblib



train_x,train_y,test_x,test_y = data_prepare4._data("Finaloutput_nonzero.xlsx","Finaloutput2_nonzero.xlsx")
clf = joblib.load("svm_model.m")
predict_y = clf.predict(test_x)
i = 0
k = 0
while i<len(test_y):
        if test_y[i] == predict_y[i]:
                k = k+1
        i = i+1
print (k+0.0)/i
