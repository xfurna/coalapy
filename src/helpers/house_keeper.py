
"""
helpers.house_keeper: module that contains methods that are used here and there for maintenence.


helpers.house_keeper.dist_sq(i , j , df): computes square of the difference between i'th and j'th column vector of the matrix
    params:
        i, j: indices of the columns of a matrix
        df: pandas dataframe object
    return: a vector


helpers.house_keeper.clean(mat): duplicates the matrix just with all values real
    params: 
        mat: a matrix
    return: 
        mat: mat


helpers.house_keeper.wrapx(mat): enumerates first row of the matrix from the first column to the las
    params: 
        mat: a square matrix
    return: 
        mat: a matrix


helpers.house_keeper.wrapy(mat): enumerates first columns of the mmtrix from the first first to the last
    params: 
        mat: a square matrix
    return: 
        mat: a matrix


helpers.house_keeper.wrap(mat): enumerates top rows and columns of the matrix from first to the last
    params: 
        mat: a square matrix
    return: 
        mat: a matrix
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
