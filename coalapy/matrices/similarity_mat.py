"""
matrices.similarity_mat: conatines methods to make different types of similarity matrices


matrices.similarity_mat.Gaussian: computes Guassian similarity matrix
    params:
        df: pandas dataframe object
        ncol: number of columns in the dataframe
    return: 
"""


import numpy as np
from .. import helpers as hf


def Gaussian(df, ncol):
    from scipy.spatial.distance import pdist

    A = np.zeros((ncol, ncol))
    sigma_sq = max(pdist(df.T)) * 0.5
    for x in range(0, ncol):
        for y in range(x, ncol):
            A[x][y] = A[y][x] = hf.house_keeper.dist_sq(x, y, df)
    factor = -2 * sigma_sq * sigma_sq
    A = np.exp(A / factor)
    return A
