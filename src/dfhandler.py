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
    
def data_generator(multiplier = 1, filename = "toy.csv"):
    oc, circles_clusters = skl_data.make_circles(n_samples=400, noise=.01, random_state=0, factor = 0.5)
    oc = multiplier * oc
    circles = np.transpose(oc)
    circles = helperFunc.wrapx(circles)

    np.savetxt(filename, circles, delimiter = ',')
    print("Saving toy data csv w/d", len(circles[:,0]))#, oc[0,:10])
    d = len(oc[0]) - len(circles[0])
    # print(d)
    return d

# generate_data()

# df = pd.read_csv("toy_data.csv"    df = pd.read_csv("toy_data.csv")
# print(df.shape)