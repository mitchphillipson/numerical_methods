#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:09:40 2020

@author: mitch
"""

import numpy as np

import matplotlib.pyplot as plt

import time

def riemann(f,a,b,N):
    
    return sum(f(np.linspace(a,b,N+1)[:N])*(b-a)/N)


def trapezoidal(f,a,b,N):
    
    stp = np.empty((N+1,),int)
    stp[0],stp[-1] = 1,1
    stp[1:N]=2
    
    return np.dot(f(np.linspace(a,b,N+1)),stp)*(b-a)/(2*N)

def trapezoidal_new(f,a,b,N):
    dx = (b-a)/N
    out = f(a)
    for i in range(1,N):
        out += 2*f(a+i*dx)
    out+= f(b)
    out*= dx/2
    return out


def simpsons(f,a,b,N):
    stp = np.empty((N+1,),int)
    stp[0],stp[1] = 1,1
    
    stp[1:N:2] = 4
    stp[2:N:2] = 2
    
    return np.dot(f(np.linspace(a,b,N+1)),stp)*(b-a)/(3*N)


def f(x):
    return np.exp(-x**2)


def custom_trap(a,b,N):
     
    stp = np.empty((N+1,),int)
    stp[0],stp[-1] = 1,1
    stp[1:N]=2
    
    return np.dot(np.exp(-(np.linspace(a,b,N+1))**2),stp)*(b-a)/(2*N)   



class Timer(object):
    def __init__(self):
        self.start = time.time()
        
    def stop(self):
        out = time.time() -self.start
        self.restart()
        return out
    
    def restart(self):
        self.start = time.time()

if __name__ == "__main__":
    
    times = {N:[0,0] for N in [10**i for i in range(1,7)]}
    
    
    timer = Timer()
    
    for N in times:
        timer.restart()
        trapezoidal(f,-2,2,N)
        times[N][0] = timer.stop()
        
        custom_trap(-2,2,N)
        times[N][1] = timer.stop()
    
    
    for N in times:
        print("N: {0:7d} -- {1:4f}  {2:4f}".format(N,times[N][0],times[N][1]))
    
    
    
    
    