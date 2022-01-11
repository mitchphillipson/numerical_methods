# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:01:53 2021

@author: mitch
"""

import numpy as np
import hw_04 as hw
import pickle
import random

functions = {"my_sum":hw.my_sum,
             "my_prod":hw.my_prod,
             "my_all":hw.my_all,
             "my_any":hw.my_any}

def p_04(n,file):
    out = []
    for i in range(n):
        f = random.choice(list(functions))
        if f in ['my_sum','my_prod']:
            L = [np.random.randint(-50,50) for i in range(np.random.randint(10,30))]
        else:
            L = [np.random.randint(0,2)==0 for i in range(np.random.randint(10,30))]
        out.append((f,L,hw.combine(functions[f],L)))

 
    with open(file,"wb") as d:
        pickle.dump(out,d)
        
        
        
        
p_04(100,"hw04_problem_04.pickle")
p_04(1000,"hw04_problem_04-sol.pickle")


def p_05(n,file):
    
    out = []
    
    for i in range(n):
        m = np.random.randint(4,500)
        n = np.random.randint(4,500)
        out.append((m,n,hw.gcd(m,n)))
    
    with open(file,"wb") as d:
        pickle.dump(out,d)
     
p_05(100,"hw04_problem_05.pickle")
p_05(1000,"hw04_problem_05-sol.pickle")    