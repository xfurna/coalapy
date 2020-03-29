"""
all commands to dedicated files goes through this file of helper fnctions.
for example, 
"""

from . import matrices as sm
import numpy as np

def get_similarity(df_csv): #dfraem_csv obj
    if df_csv.path:
        print("recieved dframe_csv object with path-", df_csv.path)
        print("calling matrix with df_csv args", df_csv.path)
        mat = matrix(df_csv = df_csv) #dframe_csv obj
        print("similarity matrix: ", df_csv.ncol, "x", df_csv.ncol)
        return mat
    else:
        print("no paths. good ", df_csv.path)
    
        
def matrix(df_csv = None, W = None, D = None, get = None): #df_csv is dfraem_csv obj; W is the subject matrix; get is the matrix to be returned 
    if df_csv:
        if df_csv.mat_type == 'gaussian':
            return sm.Gaussian(df_csv.df, df_csv.df.shape[1])
    elif W is not None:
        if get == "degree":
            return sm.get_degree(W)
        elif get == "shifted_laplacian":
            return sm.get_shifted_laplacian(W, D)
        elif get == "laplacian":
            return sm.get_laplacian(W, D)
        # elif get == 'random_walk':
            # return sm.get_RandomWalk(D, )

def dist(i, j, df): #pandas df
    result_vector = df[list(df.columns)[i]] - df[list(df.columns)[j]]
    result_vector= result_vector * result_vector
    result = result_vector.sum()
    return result


# wrapper function for dfhandler.data_generator()
def wrapx(mat):
    wrapx = [0]
    wrapx[0] = [i for i in range(len(mat[0]))]
    mat = np.vstack((wrapx, mat))
    return mat

def wrapy(mat):
    mat = np.transpose(mat)
    wrapy = [0]
    wrapy[0] = [i for i in range(len(mat[0]))]
    mat = np.vstack((wrapy, mat))
    mat = np.transpose(mat)
    return mat

def wrap(mat):
    mat = wrapy(mat)
    wrap = [0]
    wrap[0] = [i for i in range(len(mat[0]))]
    mat = np.vstack((wrap, mat))
    return mat