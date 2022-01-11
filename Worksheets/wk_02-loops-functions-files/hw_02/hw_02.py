# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:06:14 2021

@author: mitch
"""

import numpy as np


def quadratic(a,b,c):
    
    disc = b**2 - 4*a*c
    
    if disc >= 0:
        out = [((-b/(2*a)-np.sqrt(disc))/(2*a),0),((-b/(2*a)+np.sqrt(disc))/(2*a),0)]
    else:
        out = [(-b/(2*a), -np.sqrt(-disc)/(2*a)) , (-b/(2*a), np.sqrt(-disc)/(2*a))]
    return out



def my_min(L):
    m = L[0]
    for l in L:
        if l<m:
            m = l
    return m



def f(x):
    if x<= -1:
        return x**2
    elif -1<x<1:
        return x/4-2*x
    else:
        return 2**(x-1)