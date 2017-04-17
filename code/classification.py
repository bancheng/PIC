#! /usr/bin/env python
#-*- coding: utf-8 -*-import numpy
import numpy as np
import PCA
import SVM
import data_prepare

dataMat,data_y = data_prepare._data('/home/dongge/PIC/代码/filename-avg-max-metrics.xlsx')
lowDDataMat,reconMat = PCA.pca(dataMat,15)
SVM._svm(dataMat,data_y)
