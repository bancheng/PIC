#! /usr/bin/env python
#-*- coding: utf-8 -*-
import os
import pandas as pd
from datetime import datetime
import numpy as np
import timeit
df = pd.read_excel("Finaloutput2.xlsx")
print df.columns[6]
values = df[df.columns[6:]].values
i = 0
while i<values.shape[0]:
    if np.any(values[i]) == 0:
        df = df.drop(i)
    i = i+1
writer = pd.ExcelWriter('againFinaloutput2_nonzero.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()
print writer
