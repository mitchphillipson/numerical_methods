# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:56:46 2021

@author: Mitch
"""

import numpy as np

def partial(f,x,i,h=1e-8):
    
    h_vec = np.zeros(x.shape)
    h_vec[i] = h
    
    return (f(x+h_vec)-f(x-h_vec))/(2*h)




def gradient(f,x,h=1e-8):
    
    out = np.zeros(x.shape)
    
    for i in range(x.shape[0]):
        out[i] = partial(f,x,i,h)
    return out


def gradient_descent(f,x,alpha=.1,max_iter = 50, h=1e-8):
    for i in range(max_iter):
        x = x - alpha*gradient(f,x,h)
        
    return x
    



def problem_4(x):
    
    
    return np.sum(x*x+2*x) + x[0]+x[0]*x[1]







if __name__ == "__main__":
    
    a = gradient_descent(problem_4,np.array([2,3]))