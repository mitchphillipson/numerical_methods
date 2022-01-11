# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 12:19:15 2022

@author: Mitch
"""

import numpy as np

import pickle

def data_01(N,M):
    X = np.random.rand(2,N)*10-5
    
    y = np.zeros(N)

    y[X[0,:]<= 3*X[1,:]-2] = 1
    
    pickle.dump([X,y], open('hw_28-data_01.pickle','wb'))
    
    X = np.random.rand(2,M)*10-5
    y = np.zeros(M)

    y[X[0,:]<= 3*X[1,:]-2] = 1   
    pickle.dump([X,y], open('hw_28-predict_01.pickle','wb'))
    
    
    
def data_02(N,M):
    X = np.random.rand(2,N)*10-5
    
    y = np.zeros(N)

    y[X[1,:]<=X[0,:]**2-4] = 1
    
    pickle.dump([X,y], open('hw_28-data_02.pickle','wb'))
    
    X = np.random.rand(2,M)*10-5
    
    y = np.zeros(M)

    y[X[1,:]<=X[0,:]**2-4] = 1
    
    pickle.dump([X,y], open('hw_28-predict_02.pickle','wb'))