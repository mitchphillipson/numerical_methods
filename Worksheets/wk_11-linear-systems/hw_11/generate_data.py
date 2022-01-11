#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:34:59 2019

@author: mitch
"""

import pickle
import numpy as np

#import warnings

import phillipson_hw11 as ph


import time

class Timer:
    
    def __init__(self):
        self.start = time.time()
        
    def reset(self):
        self.start = time.time()
        
    def stop(self):
        out = time.time() - self.start
        self.reset()
        return out
    

#warnings.filterwarnings('error')

np.random.seed(10)

# Matrix - Students



num_points = 5

num_solutions = np.random.randint(50,100,size = num_points)

array_sizes = np.random.randint(50,60,size = num_points)



data = [(1.0*np.random.randint(-5,5,size = (array_sizes[i],array_sizes[i])),
         [1.0*np.random.randint(-5,5,size = (array_sizes[i],1)) for j in range(num_solutions[i])])
            for i in range(num_points)
        ]





def make_table():

    out = []
    
    for A,solutions in data:
        out.append([len(solutions),A.shape[0]])
        T = Timer()
        for b in solutions:
            ph.gaussian_elim(A, b)
        t = T.stop()
        out[-1].append(t)
        T.reset()
        L,U = ph.lu_decomp(A)
        for b in solutions:
            ph.LU_solve(L, U, b)
        t = T.stop()
        out[-1].append(t)
        print(out[-1])
    return out

















