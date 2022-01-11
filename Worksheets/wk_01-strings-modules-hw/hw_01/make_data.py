# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:18:00 2021

@author: mitch
"""

import pickle,random


### Problem 3 data ###
data = []
sol = []
for i in range(100):
    new_list = [random.randint(-50,50) for i in range(random.randint(10,50))]
    data.append(new_list)
    sol.append((sum(new_list),min(new_list),max(new_list)))
    
with open("hw_01-problem_03.pickle","wb") as d:
    pickle.dump(data,d)
    
with open("hw_01-problem_03-sol.pickle","wb") as d:
    pickle.dump(sol,d)