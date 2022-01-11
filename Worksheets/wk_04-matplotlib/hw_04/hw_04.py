# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:43:56 2021

@author: mitch
"""

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(N):
    pass

def factorial(n):
    
    out = 1
    for i in range(2,n+1):
        out *= i
    return out 


def combine(f,L):
    
    out = L[0]
    
    for i in range(1,len(L)):
        out = f(out,L[i])
        
    return out

def my_sum(a,b):
    return a+b

def my_prod(a,b):
    return a*b

def my_all(a,b):
    return a and b

def my_any(a,b):
    return a or b


def gcd(m,n):
    if n== 0:
        return m
    return gcd(n,m%n)