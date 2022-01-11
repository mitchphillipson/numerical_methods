# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:04:46 2021

@author: mitch
"""

import pickle
import numpy as np

import itertools as it

import hw_02 as hw

## Problem 2 - Quadratic Formula
## [(a,b,c,sol1,sol2)]


def p_02(N,file):
    A = [np.random.randint(-10,10) for i in range(N)]
    B = [np.random.randint(-10,10) for i in range(N)]
    C = [np.random.randint(-10,10) for i in range(N)]
    
    out = []
    for a,b,c in zip(A,B,C):
        if a == 0:
            a+=1
        out.append(hw.quadratic(a, b, c))
        
    #test_file = "problem_02.pickle"
    with open(file,"wb") as d:
        pickle.dump(out,d)
        
p_02(100,"problem_02.pickle")
p_02(1000,"problem_02-sol.pickle")



def p_03(N,file):
    
    out = []
    
    for i in range(N):
        L = [np.random.randint(-100,100) for i in range(np.random.randint(10,100))]
        out.append((L,hw.my_min(L)))
        
    with open(file,"wb") as d:
        pickle.dump(out,d)  
        
p_03(100,"problem_03.pickle")
p_03(1000,"problem_03-sol.pickle")


def p_04(N,file):
    
    out = []
    
    for x in 6*np.random.random(N)-3:
        out.append((x,hw.f(x)))
    
    with open(file,"wb") as d:
        pickle.dump(out,d)     



p_04(100,"problem_04.pickle")
p_04(1000,"problem_04-sol.pickle")

























                           