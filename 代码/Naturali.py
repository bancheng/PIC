#! /usr/bin/env python
#-*- coding: utf-8 -*-import numpy
import os
import pandas as pd
import time
import numpy as np
from collections import OrderedDict
from datetime import datetime
import string

def ReverseWords(str):
    _len = len(str)
    if _len<2:
        return str
    else:
        i = 0
        j = _len-1
        while i<j:
            temp = str[j]
            str[j] = str[i]
            str[i] = temp
            i = i+1
            j = j-1
        return str

b = ReverseWords("hello")
print b
