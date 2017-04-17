#! /usr/bin/env python
#-*- coding: utf-8 -*-import numpy
import os
import pandas as pd
from datetime import datetime
import numpy as np
import timeit


df = pd.read_excel("Finaloutput_test.xlsx")
i = 0
j = 0
value = df.values[:,6:]
print value[:,0]
while i< len(value):
       if value[i].any() == 0:
              j = j+1
              df = df.drop(i)
       i = i+1
writer = pd.ExcelWriter('Finaloutput_nonzero.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()