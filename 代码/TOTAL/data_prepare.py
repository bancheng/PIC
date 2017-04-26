#! /usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def _data(file):
    df = pd.read_excel(file)
    label = []
    # for str in df[df.columns[1]]:
    #     li = str.split('-')
    #     number = int(li[0])
    #     label.append(number)
    data_y = df[df.columns[1]]
    Vals = df[df.columns[3:]]
    dataMat = Vals
    return dataMat,data_y




