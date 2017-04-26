#! /usr/bin/env python
#-*- coding: utf-8 -*-import numpy

import numpy as np
import sklearn
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib as plt
from sklearn.externals import joblib

def _svm(train_x,train_y,test_x,test_y):
    # train_x,test_x1,train_y,test_y1 = train_test_split(data_x,data_y,test_size=0, random_state=42)
    clf = svm.SVC(kernel='rbf')
    clf.fit(train_x,train_y)
    joblib.dump(clf, "svm_model.m")
    train_predict = clf.predict(train_x)
    test_predict = clf.predict(test_x)
    target_names = ['class 0', 'class 1']
    print ('train_predict',metrics. accuracy_score(train_y,train_predict))
    print ('test_predict',metrics. accuracy_score(test_y,test_predict))
    print ('report',metrics.classification_report(test_y,test_predict,target_names=target_names))
    #print clf.predict(test_x)
    i = 0
    j = 0
    k = 0
    while i<len(test_y):
        if test_y[i] == 1:
            j = j+1
            if test_y[i] == test_predict[i]:
                k = k+1
        i = i+1
    print k,j,float(k/(j+0.0))
    i = 0
    j = 0
    k = 0
    while i<len(test_y):
        if test_y[i] == 0:
            j = j+1
            if test_y[i] == test_predict[i]:
                k = k+1
        i = i+1
    print k,j,float(k/(j+0.0))



