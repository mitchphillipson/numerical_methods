#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:22:14 2020

@author: mitch
"""

import numpy as np


def backsub(A,b):
    """
        Assume A is upper triangular. Solve Ax=b.
        
        Safe to assume non-zero entries on diagonal.
    """
    system = np.concatenate((A,b),axis=1)
    N = A.shape[0]
    
    for i in range(N-1,-1,-1):
        system[i] = system[i]/system[i,i]
        for j in range(i+1,N):
            system[i] = system[i] - system[i,j]*system[j]
            
    return system[:,N].reshape((N,1))


def forwardsub(A,b):
    """
        Assume A is lower triangular. Solve Ax=b.
        
        Safe to assume non-zero entries on diagonal.
    """
    system = np.concatenate((A,b),axis=1)
    N = A.shape[0]
    
    for i in range(N):
        system[i] = system[i]/system[i,i]
        for j in range(i):
            system[i] = system[i] - system[i,j]*system[j]
            
    return system[:,N].reshape((N,1))   
    

def gaussian_elim(A,b):
    """
        Assumes A is non-singular and doesn't require pivots
    """
    system = np.concatenate((A,b),axis=1)
    N = A.shape[0]
    
    for i in range(N):
        system[i] = system[i]/system[i,i]
        for j in range(i+1,N):
            system[j] = system[j] - system[j,i]*system[i]
    return backsub(system[:,:N],system[:,N].reshape((N,1)))
    

def lu_decomp(A):    
    N = A.shape[0]
    
    U = A.copy()
    L = np.identity(N)
    
    for i in range(N):
        T = np.identity(N)    
        Li = np.identity(N)
        
        Li[i:,i] = U[i:,i]        
        T[i+1:,i] = -U[i+1:,i]        
        T[i:,i] = 1/(U[i,i]) * T[i:,i]
        
        U = np.matmul(T,U)
        L = np.matmul(L,Li)
        
    #y = forwardsub(L,b)
    #x = backsub(U,y)
    
    return (L,U)


def LU_solve(L,U,b):
    y = forwardsub(L,b)
    x = backsub(U,y)
    return x

def hilbert(n):
    
    A = 1/(np.arange(1,n+1)+np.arange(n).reshape((n,1)))
    
    b =  np.sum(A,axis=0).reshape(n,1)
    
    return (gaussian_elim(A,b),A,b)
    
    


if __name__ == "__main__":
    
    A = np.array([[3.0,5,-1],[2,3,-2],[4,2,3]])
    
    b = np.array([1,1,1]).reshape((3,1))

    #print(gaussian_elim(A,b) - lu_decomp(A,b))
    
    N = 50
    
    sol,A,b = hilbert(N)
    
    lu_sol,_,_ = lu_decomp(A,b)
    
    my_sol = np.ones((N,1))
    
    print(sol)
    
    new_b = np.linalg.solve(A,b)
    
    print(sol-lu_sol)
    
    
    
    
    
    
    
    
    
    
    