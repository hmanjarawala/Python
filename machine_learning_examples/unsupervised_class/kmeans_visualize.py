# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:47:11 2020

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
        for n in range(len(X)):
            cost += R[n,k] * d(M[k], X[n])
    return cost

def plot_k_means(X, K, max_iter=20, beta=1.0):
    N, D = X.shape
    M = np.zeros((K, D))
    R = np.ones((N, K)) / K
    
    #initialize M to random
    for k in range(K):
        M[k] = X[np.random.choice(N)]
    
    grid_width = 5
    grid_height = int(max_iter/grid_width)
    random_colors = np.random.random((K, 3))
    plt.figure()
    
    costs = np.zeros(max_iter)
    for i in range(max_iter):
        colors = R.dot(random_colors)
        plt.subplot(grid_width, grid_height, i+1)
        plt.scatter(X[:,0], X[:,1], c=colors)
        
        # step 1: determine assignment / responsibilities
        for k in range(K):
            for n in range(N):
                exponent_iterable = (np.exp(-beta * d(M[j], X[n])) for j in range(K))
                R[n,k] = np.exp(-beta * d(M[k], X[n])) / np.sum(np.fromiter(exponent_iterable, float))
        
        # step 2: recalculate means
        for k in range(K):
            M[k] = R[:,k].dot(X) / R[:,k].sum()
        
        costs[i] = cost(X, R, M)
        if i>0:
            if np.abs(costs[i] - costs[i-1]) < 1e-5:
                break
    plt.show()

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
    
#    K = 3 # luckily, we already know this
#    plot_k_means(X, K)
    
    K = 5 # what happens if we choose a "bad" K?
    plot_k_means(X, K, max_iter=30)

    # K = 5 # what happens if we change beta?
    # plot_k_means(X, K, max_iter=30, beta=0.3)
    

if __name__ == '__main__':
    main()