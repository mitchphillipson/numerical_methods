# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:42:46 2021

@author: mitch
"""

import numpy as np
import matplotlib.pyplot as plt

def diff(f,x,h):
    
    return (f(x+h)-f(x-h))/(2*h)


def gradient_descent(f,a,alpha,tol=1e-9,max_iter = 500):
    
    out = [a]
    error = 1
    iters = 0
    while iters<max_iter and abs(error)>tol:
        iters+=1
        
        x = out[-1]
        out.append( x - alpha*diff(f,x,1e-9))
        error = x-out[-1]
    
    return (out[-1],out)

def f(x):
    return x**2

fig,ax = plt.subplots(figsize = (10,10))

x,L = gradient_descent(f,2,.1)

X = np.linspace(-2,2,100)

ax.plot(X,f(X))
ax.plot(np.array(L),f(np.array(L)),"o")

