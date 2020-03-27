"""
Reads the csv and returns dataframe/Similarity
"""

from . import helperFunc 
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
    oc, circles_clusters = skl_data.make_circles(n_samples=400, noise=.01, random_state=0)
    circles = np.transpose(oc)
    cirlces = helperFunc.wrapx(circles)

    np.savetxt("toy_data.csv", circles, delimiter = ',')
    print("Saving toy data csv")
    d = len(oc[0]) - len(circles[0])
    return d

# generate_data()

# df = pd.read_csv("toy_data.csv"    df = pd.read_csv("toy_data.csv")
# print(df.shape)