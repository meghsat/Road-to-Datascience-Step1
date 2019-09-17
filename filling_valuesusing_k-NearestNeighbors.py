'''  Basic idea & GOAL: Impute array with a basic mean impute and then use the resulting complete array to construct a KDTree. Use this KDTree to compute nearest neighbours.
    After finding `k` nearest neighbours, take the weighted average of them. Basically,
    find the nearest row in terms of distance
'''
import pandas as pd
import numpy as np
import random
import sys
from impyute.imputation.cs import fast_knn
diab = np.genfromtxt('NaN_k-nn_filling.csv', delimiter=",") #taking the CSV dataset containing NaN values  and converting it into numpy.ndarray
# start the KNN training
imputed_training=fast_knn(diab, k=5)  # fast_knn assigns the lowest weight to the nearest neighbor instead of assigning the highest weight to the nearest neighbor.
pd.DataFrame(imputed_training).to_csv("file.csv")  # writing the replaced NAN values into a new csv file
