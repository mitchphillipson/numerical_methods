#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:33:47 2020

@author: mitch
"""
import pickle,random

import phillipson_hw05 as ph
from my_functions import *



    


functions = [f1,f2,f3,f4,f5,f6]
    
#Combine - Students

num_points = 100

data = []

for i in range(num_points):
    function = random.choice(functions)
    
    a = random.randint(-10,10)+random.random()
    
    b = random.randint(-10,10)+random.random()
    
    N = random.randint(10,1000)


    r = ph.riemann(function,a,b,N)
    t = ph.trapezoidal(function,a,b,N)
    
    
    if N%2 == 0:
        s = ph.simpsons(function,a,b,N)
    else:
        s = None
    
    data.append([function,a,b,N,r,t,s])
    #t = tuple([random.randint(-100,100) for j in range(random.randint(5,50))])
    #f = random.choice(functions)
    #data[t] = (f,ph.combine(f,list(t)))

with open("hw06_problem_01.pickle","wb") as d:
    pickle.dump(data,d)

#Combine - Solutions
num_points = 1000

data = []

for i in range(num_points):
    function = random.choice(functions)
    
    a = random.randint(-10,10)+random.random()
    
    b = random.randint(-10,10)+random.random()
    
    N = random.randint(10,1000)


    r = ph.riemann(function,a,b,N)
    t = ph.trapezoidal(function,a,b,N)
    
    
    if N%2 == 0:
        s = ph.simpsons(function,a,b,N)
    else:
        s = None
    
    data.append([function,a,b,N,r,t,s])
    #t = tuple([random.randint(-100,100) for j in range(random.randint(5,50))])
    #f = random.choice(functions)
    #data[t] = (f,ph.combine(f,list(t)))
    
with open("hw06_problem_01-sol.pickle","wb") as d:
    pickle.dump(data,d)    
