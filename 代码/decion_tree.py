#! /usr/bin/env python
#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import data_prepare2
import data_prepare4
from sklearn.externals import joblib
reg1 = DecisionTreeClassifier(max_depth=10)
reg2 = DecisionTreeClassifier(max_depth=10)
reg3 = DecisionTreeClassifier(max_depth=10)
reg4 = DecisionTreeClassifier(max_depth=10)
reg5 = DecisionTreeClassifier(max_depth=10)
reg6 = DecisionTreeClassifier(max_depth=10)



train_x,train_y,test_x,test_y = data_prepare4._data("Finaloutput_nonzero.xlsx","Finaloutput2_nonzero.xlsx")
reg1.fit(train_x,train_y)
joblib.dump(reg1, "decision_model.m")
predict_y = reg1.predict(test_x)
i = 0
k = 0
while i<len(test_y):
        if test_y[i] == predict_y[i]:
                k = k+1
        i = i+1
print (k+0.0)/i
i = 0
k = 0
j = 0
while i<len(test_y):
        if test_y[i] == 1:
                j = j+1
                if test_y[i] == predict_y[i]:
                        k = k+1
        i = i+1
print k,j,(k+0.0)/j
i = 0
k = 0
j = 0
while i<len(test_y):
        if predict_y[i] == 1:
                j = j+1
                if test_y[i] == predict_y[i]:
                        k = k+1
        i = i+1
print k,j,(k+0.0)/j


