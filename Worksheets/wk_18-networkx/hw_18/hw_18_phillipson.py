# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:51:15 2021

@author: Mitch
"""

import networkx as nx


G = nx.barbell_graph(5,4)


print(nx.average_clustering(G))


H = nx.Graph({0:[3,4],1:[3,4,2],2:[4],4:[5]})


def prob_4():
    
    n = 50
    
    out = []
    
    for m in range(250,801,50):
        G = nx.gnm_random_graph(n,m)
        out.append([m,nx.average_clustering(G),nx.diameter(G),nx.radius(G)])
    
    return out