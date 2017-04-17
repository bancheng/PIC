#! /usr/bin/env python
#-*- coding: utf-8 -*-import numpy
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras import optimizers
import data_prepare
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
model = Sequential()
model.add(Dense(32, input_shape=(25,),init='uniform',activation='tanh'))
model.add(Dense(32,activation='tanh'))
model.add(Dense(4,activation='softmax'))

sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

_dataMat,data_y = data_prepare._data('/home/dongge/PIC/代码/Finaloutput_nonzero.xlsx')
data_y = data_y -1
print _dataMat.values[0,0]
dataMat = np.zeros((_dataMat.shape[0],_dataMat.shape[1]))
print dataMat.shape
print type(dataMat)
i = 0
j = 0
while i<_dataMat.shape[0]:
    while j<_dataMat.shape[1]:
        dataMat[i,j] = _dataMat.values[i,j]
        j = j+1
    i = i+1
print dataMat.shape

data_y = to_categorical(data_y,nb_classes=4)
print data_y.shape
train_x,test_x,train_y,test_y = train_test_split(dataMat,data_y,test_size=0.3, random_state=42)
print type(train_x)
print type(train_y)
print train_x.shape
model.fit(train_x, train_y)#batch_size=16, nb_epoch=5, validation_split=0.2)
score = model.evaluate(test_x,test_y,batch_size=32)
print('\t')
print score



