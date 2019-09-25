#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:46:14 2018

@author: si_han
"""

from interpolateCurve import*
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('path.txt', header=None, delimiter="\s+")
ary = np.asarray(data)

data_interp = interpolateCurve(ary)

plt.figure()
plt.plot(data_interp[:,0], data_interp[:,1],'-')
plt.plot(ary[:,1], ary[:,2], 'o', markersize=4, color='r')