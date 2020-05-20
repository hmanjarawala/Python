# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:00:32 2020

@author: Himanshu.Manjarawala
"""

import numpy as np
import matplotlib.pyplot as plt

def d(u, v):
    diff = u-v
    return diff.dot(diff)

def cost(X, R, M):
    cost = 0
    
    for k in range(len(M)):
#        Method 1
#        for n in range(len(X)):
#            cost += R[n,k] * d(M[k], X[n])
#        
#        Method 2
        diff = X - M[k]
        sq_distances = (diff * diff).sum(axis=1)
        cost = (R[:,k]*sq_distances).sum()
    return cost

def plot_k_means(X, K, max_iter=20, beta=1.0, show_plots=False):
    N, D = X.shape
    exponents = np.empty((N,K))
    
    initialize_centers = np.random.choice(N, K, replace=False)
    M = X[initialize_centers]
       
    costs = []
    k = 0
    for i in range(max_iter):
        k += 1
        
        for k in range(K):
            for n in range(N):
                exponents[n,k] = np.exp(-beta*d(M[k], X[n]))
        R = exponents / exponents.sum(axis=1, keepdims=True)
        
        M = R.T.dot(X) / R.sum(axis=0, keepdims=True).T
        
        c = cost(X, R, M)
        costs.append(c)
        if i>0:
            if np.abs(costs[-2] - costs[-1]) < 1e-5:
                break;
            
        if len(costs) > 1:
            if costs[-1] > costs[-2]:
                pass
            
    
    if(show_plots):        
        random_colors = np.random.random((K, 3))
        colors = R.dot(random_colors)
        plt.scatter(X[:,0], X[:,1], c=colors)
        plt.show()
    
    return M, R

def create_sample_data():
    D = 2
    s = 4
    mu1 = np.array([0,0])
    mu2 = np.array([s,s])
    mu3 = np.array([0,s])
    
    N=900 # no. of samples
    X = np.zeros((N,D))
    X[:300,:] = np.random.randn(300, D) + mu1
    X[300:600,:] = np.random.randn(300, D) + mu2
    X[600:,:] = np.random.randn(300, D) + mu3
    return X
    

def main():
    X = create_sample_data()
    plt.scatter(X[:,0], X[:,1])
    plt.show()
    
    K = 3
    plot_k_means(X, K, show_plots=True)
    
    K = 3 # luckily, we already know this
    plot_k_means(X, K, beta=3.0, show_plots=True)
    
    K = 3 # luckily, we already know this
    plot_k_means(X, K, beta=10.0, show_plots=True)
    
    K = 5 # what happens if we choose a "bad" K?
    plot_k_means(X, K, max_iter=30, show_plots=True)

    K = 5 # what happens if we change beta?
    plot_k_means(X, K, max_iter=30, beta=0.3, show_plots=True)


if __name__ == '__main__':
    main()