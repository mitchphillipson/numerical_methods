# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 09:36:36 2022

@author: Mitch
"""

import matplotlib.pyplot as plt
import numpy as np



def classification():
    X = np.random.rand(100,2)*10-5
    
    fig,ax = plt.subplots(figsize=(10,10))
    
    red = X[X[:,0]>X[:,1]]
    
    blue = X[X[:,0]<= X[:,1]]
    
    ax.plot(red[:,0],red[:,1],'o',color='red')
    ax.plot(blue[:,0],blue[:,1],'o',color='blue')
    
    ax.plot([-5,5],[-5,5],'--',color='grey')
    
    
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_graph():
    
    X = np.linspace(-5,5,1000)
    fig,ax = plt.subplots(figsize=(10,10))
    
    ax.plot(X,sigmoid(X))
    
    ax.plot([-5,5],[.5,.5],'--',color='grey')
    
    
    
