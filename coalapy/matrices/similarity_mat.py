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
    A = np.zeros((ncol, ncol))

    sigma_sq = 0

    for x in range(0, ncol):
        for y in range(x, ncol):
            A[x][y] = hf.house_keeper.dist_sq(x, y, df)
            A[y][x] = A[x][y]
            if sigma_sq < A[x][y]:
                sigma_sq = A[x][y]

    for x in range(0, ncol):
        for y in range(x, ncol):
            A[y][x] = A[y][x] / ((-2) * sigma_sq)
            A[x][y] = A[x][y] / ((-2) * sigma_sq)

    for x in range(0, ncol):
        A[x] = np.exp(A[x])

    return A
