
"""
helpers.house_keeper: module that contains methods that are used here and there for maintenence.

helpers.house_keeper.dist_sq(i , j , df):
    params:
        i, j: indices of the columns of a matrix
        df: pandas dataframe object
    return: square of the difference between i'th and j'th column vector of the matrix

helpers.house_keeper.clean(mat):
    params: 
        mat: a matrix
    return: 
        mat: a matrix with all real values

helpers.house_keeper.wrapx(mat):
    params: 
        mat: a square matrix
    return: 
        mat: a matrix with top rows enumerated from the first column to the last

helpers.house_keeper.wrapy(mat):
    params: 
        mat: a square matrix
    return: 
        mat: a matrix with first columns enumerated from the first first to the last

helpers.house_keeper.wrap(mat):
    params: 
        mat: a square matrix
    return: 
        mat: a matrix with top rows and columns enumerated from first to the last
"""

import numpy as np
import cmath

def dist_sq(i , j , df): #pandas df
    result_vector = df[list(df.columns)[i]] - df[list(df.columns)[j]]
    result_vector= result_vector * result_vector
    result = result_vector.sum()
    return result

def clean(mat):
    return mat.real

def wrapx(mat):
    wrapx = [0]
    n = len(mat[0])
    wrapx[0] = np.arange(0, n, 1)
    mat = np.vstack((wrapx, mat))
    return mat

def wrapy(mat):
    mat = np.transpose(mat)
    wrapy = [0]
    n = len(mat)
    wrapy[0] = np.arange(0, n, 1)
    mat = np.vstack((wrapy, mat))
    mat = np.transpose(mat)
    return mat

def wrap(mat):
    mat = wrapy(mat)
    wrap = [0]
    wrap[0] = [i for i in range(len(mat[0]))]
    mat = np.vstack((wrap, mat))
    return mat
