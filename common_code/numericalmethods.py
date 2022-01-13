# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 09:09:46 2022

@author: Mitch
"""

def latex_table(L):
    out = "\\begin{{tabular}}{{{0}}}\n".format("c"*len(L[0]))
    for row in L:
        out+="&".join([str(i) for i in row]) + "\\\\ \n"
    out += "\\end{tabular}"
    return out



def fuzzy_equal(a,b,tol=1e-6):
    if abs(a-b)<tol:
        return True
    return False