#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 22:07:03 2018

@author: copu
"""
import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean
from scipy.interpolate import interp1d


def interpolateCurve(rawdata, pts=200, kind='cubic'):
    data = rawdata[:,1:3]

    pairlist = []
    for i in range(len(data)-1):
        pairlist.append([data[i], data[i+1]])
        
    cum_euc_dist = [0]
    dist = 0
    for i in range(len(pairlist)):
        dist += euclidean(pairlist[i][0],pairlist[i][1])
        cum_euc_dist.append(dist)
    cum_euc_dist = np.array(cum_euc_dist) 
    
    func1 = interp1d(cum_euc_dist, data[:,0], kind=kind)
    func2 = interp1d(cum_euc_dist, data[:,1], kind=kind)
    
    xnew = np.linspace(0, cum_euc_dist[-1], num=pts, endpoint=True)
    
    return np.column_stack((func1(xnew), func2(xnew)))

if __name__ == "__main__":
    import sys
    data = pd.read_csv(sys.argv[1], header=None, delimiter="\s+")
    ary = np.asarray(data)
    data_interp = interpolateCurve(ary)
    np.savetxt(sys.argv[2], data_interp, delimiter='\t')
