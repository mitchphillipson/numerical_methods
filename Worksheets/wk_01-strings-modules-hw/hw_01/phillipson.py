# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 18:43:52 2021

@author: mitch
"""

import pickle

def fizzbuzz(n):
    
    out = ""
    
    for i in range(n):
        new_line = ""
        if i % 3 == 0:
            new_line += "fizz"
        if i % 5 == 0:
            new_line += "buzz"
        if new_line != "":
            out += new_line + "\n"
    print(out)
    
    
def latex_table(L):
    out = "\\begin{{tabular}}{{{0}}}\n".format("c"*len(L[0]))
    for row in L:
        out+="&".join([str(i) for i in row]) + "\\\\ \n"
    out += "\\end{tabular}"
    return out


def list_stats(data):    
    out = []
    for row in data:
        out.append((sum(row),min(row),max(row)))
    return out



if __name__ == "__main__":
    
    with open("hw_01-problem_03.pickle","rb") as d:
        data = pickle.load(d)
        
    with open("hw_01-problem_03-sol.pickle","rb") as d:
        sol = pickle.load(d)
        
    test_sol = list_stats(data)
    
    for a,b in zip(test_sol,sol):
        if a!=b:
            print("Error: {0} {1}".format(a,b))