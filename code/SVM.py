#! /usr/bin/env python
#-*- coding: utf-8 -*-import numpy

import numpy as np
import sklearn
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib as plt

def _svm(data_x,data_y):
    train_x,test_x,train_y,test_y = train_test_split(data_x,data_y,test_size=0.25, random_state=42)
    clf = svm.SVC(kernel='rbf')
    clf.fit(train_x,train_y)
    train_predict = clf.predict(train_x)
    test_predict = clf.predict(test_x)
    target_names = ['class 0', 'class 1', 'class 2','class3','class4']
    print ('train_predict',metrics. accuracy_score(train_y,train_predict))
    print ('test_predict',metrics. accuracy_score(test_y,test_predict))
    print ('report',metrics.classification_report(test_y,test_predict,target_names=target_names))
    #print clf.predict(test_x)


