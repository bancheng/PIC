#! /usr/bin/env python
#-*- coding: utf-8 -*-import numpy
import numpy as np
import PCA
import SVM
import data_prepare4
import data_prepare2

train_x,train_y,test_x,test_y = data_prepare4._data("Finaloutput_nonzero.xlsx","Finaloutput2_nonzero.xlsx")
# test_x,test_y = data_prepare2._data("Finaloutput_nonzero.xlsx","Finaloutput2_nonzero.xlsx")
# lowDDataMat,reconMat = PCA.pca(dataMat,15)
SVM._svm(train_x,train_y,test_x,test_y)
