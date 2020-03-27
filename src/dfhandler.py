"""
Reads the csv and returns dataframe/Similarity
"""

# from . import matrices 
import pandas as pd
import sklearn.cluster as skl_cluster
import sklearn.datasets as skl_data
import numpy as np


class dframe_csv:
    def __init__(self, path, mat_type):
        self.df = pd.read_csv(path)
        self.path = path
        self.mat_type = mat_type
        self.nrow = self.df.shape[0]
        self.ncol = self.df.shape[1]
    
def data_generator():
    circles, circles_clusters = skl_data.make_circles(n_samples=400, noise=.01, random_state=0)

    wrapy = [0]
    wrapy[0]=[i for i in range(len(circles[0]))]
    circles = np.vstack((wrapy, circles))
    circles = np.transpose(circles)

    wrapx = []
    wrapx=[i for i in range(len(circles[0]))]
    circles = np.vstack((wrapx, circles))

    np.savetxt("toy_data.csv", circles, delimiter = ',')

# generate_data()

# df = pd.read_csv("toy_data.csv"    df = pd.read_csv("toy_data.csv")
# print(df.shape)