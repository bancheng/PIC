#! /usr/bin/env python
#-*- coding: utf-8 -*-
import os
import pandas as pd
from datetime import datetime
import numpy as np
import timeit
df = pd.read_excel("Finaloutput.xlsx")
values = df[df.columns[6:]].values
print values.shape
i = 0
while i<values.shape[0]:
    if np.any(values[i]) == 0:
        df.drop([i],axis=0)
    i = i+1
print df.values.shape

# df.drop([22,33],axis=0)##删除行；
# print df[1]