# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:44:52 2020

@author: Himanshu.Manjarawala
"""
import numpy as np
import matplotlib.pyplot as plt
from kmeans import create_sample_data, cost, plot_k_means

def main():
    X = create_sample_data()
    
    plt.scatter(X[:,0], X[:,1])
    plt.show()
    
    costs = np.empty(10)
    costs[0] = None
    for k in range(1, 10):
        M, R = plot_k_means(X, k, show_plots=False)
        costs[k] = cost(X, R, M)
    
    plt.plot(costs)
    plt.title("Cost vs K")
    plt.show()

if __name__ == '__main__':
    main()