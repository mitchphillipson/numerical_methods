# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:43:56 2021

@author: mitch
"""

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(N):
    real_values = np.linspace(-2,2,N)
    imaginary_values = np.linspace(-2,2,N).reshape((-1,1))
    
    C = real_values+1.0j*imaginary_values
    
    z = np.zeros(C.shape)
    
    for i in range(100):
        
        z = z**2 + C
        z[np.abs(z)>2] = 2
    
    
    return np.abs(z)

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


if __name__ == "__main__":
    
    from PIL import Image
    
    #fig,ax = plt.subplots(figsize=(10,10))
    
    z = mandelbrot(10000)
    
    z[z<2] = 0
    
    image = Image.fromarray(z*128)
    
    image = image.convert("RGB")
    
    image.save("mandelbrot.png")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    