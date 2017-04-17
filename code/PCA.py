#! /usr/bin/env python
#-*- coding: utf-8 -*-import numpy

import numpy as np

def pca(dataMat, topNfeat):
    meanVals = np.mean(dataMat,axis=0)
    meanRemoved = dataMat-meanVals
    covMat = np.cov(meanRemoved,rowvar=False)
    print covMat
    eigVal,eigVect = np.linalg.eig(np.mat(covMat))
    eigValInd = np.argsort(eigVal)
    eigValInd = eigValInd[:-(topNfeat+1):-1]
    redEigVects = eigVect[:,eigValInd]
    lowDDataMat = np.dot(meanRemoved,redEigVects)
    reconMat = np.dot(lowDDataMat,redEigVects.T) + np.mat(meanVals)  #对原矩阵进行重构reconMat近似于dataMat
    return lowDDataMat,reconMat
