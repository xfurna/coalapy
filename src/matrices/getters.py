import numpy as np
from . import similarity_mat


def get_similarity(df_csv): 
    if df_csv.path:
        print("Recieved dframe_csv object with path-", df_csv.path)
        print("Calling matrix with df_csv args", df_csv.path)
        mat = similarity_mat.Gaussian(df_csv = df_csv) #dframe_csv obj
        print("Constructed similarity matrix: ", df_csv.ncol, "x", df_csv.ncol)
    else:
        print("no paths!!", df_csv.path)

    return mat

def get_degree(W):
    D = np.zeros((len(W[0]), len(W[0])))
    for x in range(0, len(D[0])):
        D[x][x] = np.sum(W[x])
    return D

def get_shifted_laplacian(W, D):
    D_diag = D.diagonal()
    D_diag = 1/D_diag**1/2
    Dd = np.zeros((len(D),len(D)))
    np.fill_diagonal(Dd, D_diag)
    prod = Dd.dot(W)
    L = np.identity(len(D[0]), dtype=float) + prod.dot(Dd)        
    return L

def get_laplacian(W, D):
    return (D - W)    
