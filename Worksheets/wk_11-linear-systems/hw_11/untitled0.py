#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:21:30 2020

@author: mitch
"""

def sequence(tol=10**-8):
    x1 = 2
    xn = (1/2)*(x1)+(1/x1)
    error = 10
    while abs(error) > tol:
        xp = xn
        xn = (1/2)*xp+(1/xp)
        error = xn-xp
    return xn
    
print(sequence())