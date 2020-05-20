# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:53:38 2020

@author: Himanshu.Manjarawala
"""

import numpy as np
import matplotlib.pyplot as plt
from kmeans import create_sample_data, plot_k_means
import pandas as pd

def get_data(limit=None):
    print("Reading in and transforming data...")
    df = pd.read_csv('../large_files/train.csv')
    data = df.values
    np.random.shuffle(data)
    X = data[:,1:] / 255.0
    Y = data[:,0]
    
    if limit is not None:
        X, Y = X[:limit], Y[:limit]
    return X, Y

def purity(Y, R):
    # maximum purity is 1, higher is better
    N, K = R.shape
    p = 0
    
    for k in range(K):
#        best_target = -1
        max_intersection = 0
        for j in range(K):
            intersection = R[Y==j,k].sum()
            if intersection > max_intersection:
                max_intersection = intersection
#                best_target = j
        p += max_intersection
    return p / N

def purity2(Y, R):
    # maximum purity is 1, higher is better
    C = np.argmax(R, axis=1) # cluster assignments
    
    N = len(Y) # number of data points
    K = len(set(Y)) # number of labels
    
    total = 0.0
    for k in range(K):
        max_intersection = 0
        for j in range(K):
            intersection = ((C==k) & (Y==j)).sum()
            if intersection > max_intersection:
                max_intersection = intersection
        total += max_intersection
    return total / N

def main():
    X, Y = get_data(1000)
    
#    # sample data
#    X = create_sample_data()
#    Y = np.array([0]*300 + [1]*300 + [2]*300)
    
    print("Number of data points:", len(Y))
    M, R = plot_k_means(X, len(set(Y)))
    
    print("Purity:", purity(Y, R))
    print("Purity 2:", purity2(Y, R))
    
    # plot the mean images
    # they should look like digits
    for k in range(len(M)):
        im = M[k].reshape(28, 28)
        plt.imshow(im, cmap='gray')
        plt.show()
    
    

if __name__ == '__main__':
    main()