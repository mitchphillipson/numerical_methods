# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:47:26 2022

@author: Mitch
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle



def make_data(N = 1000,file = "data.pickle"):
    X = np.random.rand(2,N)*10-5
    
    y = np.zeros(N)

    y[X[0,:]<= X[1,:]] = 1
    
    pickle.dump([X,y], open(file,'wb'))

def load_data(file = "data.pickle"):
    
    X,y = pickle.load(open(file,"rb"))
    
    return X,y


def sigmoid(x):
    return 1/(1+np.exp(-x))



def initalize_weights(t):
    
    W = np.random.randn(t)*.01
    b = np.random.randn(1)*.01
    
    return W,b



def logistic_regression(X,y,alpha = .1):
    
    t,m = X.shape
    
    W,b = initalize_weights(t)
    #print(W)
    #print(W.shape)
    
    for i in range(10000):
        
        Z = np.dot(W.T,X)+b
        A = sigmoid(Z)
        
        dZ = A - y
        
        #print("dZ - ",dZ.shape)
        
        dW = 1/m*np.dot(dZ,X.T)#np.sum(X,axis=1))
        
        #print(dW.shape)
        
        db = np.sum(dZ)/m
        
        W = W - alpha*dW
        b = b - alpha*db
        
        #print(W)
        
    return W,b


def predict(x,W,b):
    
    y = sigmoid(np.dot(W.T,x)+b)
    
    return y



def problem_03():
    
    X,y = pickle.load(open("hw_28-data_01.pickle","rb"))
    
    W,b = logistic_regression(X, y)

    Xhat = pickle.load(open("hw_28-predict_01.pickle",'rb'))

    yhat = predict(Xhat,W,b)

    
    fig,ax = plt.subplots(2,figsize=(10,20))
    
    ax[0].plot(X[0,y>.5],X[1,y>.5],'o',color='red')
    ax[0].plot(X[0,y<=.5],X[1,y<=.5],'o',color='blue')
    
    ax[0].plot([-5,5],[-W[0]/W[1]*(-5)-b[0]/W[1],-W[0]/W[1]*(5)-b[0]/W[1]],color='black')
    #ax[0].plot([-5,5],[-W[0]/W[1]*(-5)+2/3,-W[0]/W[1]*(5)+2/3],color='black')
    
    ax[1].plot(Xhat[0,yhat>.5],Xhat[1,yhat>.5],'o',color='red')
    ax[1].plot(Xhat[0,yhat<=.5],Xhat[1,yhat<=.5],'o',color='blue')
    ax[1].plot([-5,5],[-W[0]/W[1]*(-5)-b[0]/W[1],-W[0]/W[1]*(5)-b[0]/W[1]],color='black')
    
    return W,b
    
    #return yhat_raw
                            

def problem_04():
    
    X,y = pickle.load(open("hw_28-data_02.pickle","rb"))
    
    W,b = logistic_regression(X, y)

    Xhat = pickle.load(open("hw_28-predict_02.pickle",'rb'))

    yhat = predict(Xhat,W,b)

    
    fig,ax = plt.subplots(2,figsize=(10,20))
    
    ax[0].plot(X[0,y>.5],X[1,y>.5],'o',color='red')
    ax[0].plot(X[0,y<=.5],X[1,y<=.5],'o',color='blue')
    
    ax[0].plot([-5,5],[-W[0]/W[1]*(-5)-b[0]/W[1],-W[0]/W[1]*(5)-b[0]/W[1]],color='black')
    #ax[0].plot([-5,5],[-W[0]/W[1]*(-5)+2/3,-W[0]/W[1]*(5)+2/3],color='black')
    
    ax[1].plot(Xhat[0,yhat>.5],Xhat[1,yhat>.5],'o',color='red')
    ax[1].plot(Xhat[0,yhat<=.5],Xhat[1,yhat<=.5],'o',color='blue')
    ax[1].plot([-5,5],[-W[0]/W[1]*(-5)-b[0]/W[1],-W[0]/W[1]*(5)-b[0]/W[1]],color='black')
    
    return W,b






if __name__ == "__main__":
    

    
    W,b = problem_04()















