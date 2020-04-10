import numpy as np
from scipy import linalg
from . import helperFunc as hf

def Gaussian(df, ncol): #pandas data frame
    A = np.zeros((ncol,ncol))

    sigma_sq = 0

    for x in range(0, ncol):
        for y in range(x, ncol):
            A[x][y]=hf.dist_sq(x,y, df)
            A[y][x]=A[x][y]
            if sigma_sq < A[x][y]:
                sigma_sq = A[x][y]
    
    for x in range(0, ncol):
        for y in range(x, ncol):
            A[y][x]=A[y][x]/((-2)*sigma_sq)
            A[x][y]=A[x][y]/((-2)*sigma_sq)

    for x in range(0, ncol):
        A[x]=np.exp(A[x])
    
    return A

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

# def low_rank_approx(M, r): # r is the rank
#     val, vect = linalg.eig(M)
#     val = 


# def get_RandomWalk(D, L):
#     D_inv = linalg.inv(D)
#     R = D_inv.dot(L)
#     return R