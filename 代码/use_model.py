#! /usr/bin/env python
#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import data_prepare2
import data_prepare4
from sklearn.externals import joblib



df1 = pd.read_excel("All_Main_C86153_to_C87956_output_nonzero.xlsx")
ID1 = df1["ChangesetId"].values

clf = joblib.load("svm_model.m")
i = 0
j = 0
k = 0
m = 0

print type(df1["Work Item Type"].values[13])
while i<len(ID1):
        changeid = []
        changeid.append(i)
        while i<len(ID1):
                if (i+1 == len(ID1)):
                        i = i + 1
                        test_x = df1[df1.columns[6:]].values[changeid]
                        predict_y = clf.predict(test_x)
                        label = np.average(predict_y)
                        j = j + 1
                        if label > 0.5:
                                k = k + 1
                        break

                else:
                        if (ID1[i+1] == ID1[i]):
                                changeid.append(i+1)
                                i = i+1
                        else:
                                i = i+1
                                reallabel = df1["Work Item Type"].values[changeid]
                                if np.where(reallabel == 1):
                                        y_label = 1
                                else:
                                        y_label = 0
                                test_x = df1[df1.columns[6:]].values[changeid]
                                predict_y = clf.predict(test_x)
                                label = np.average(predict_y)
                                j =j+1
                                if label > 0.5:
                                        label = 1
                                else:
                                        label = 0
                                if label == y_label:
                                        k = k+1
                                break
print k,j,float(k/(j+0.0))
