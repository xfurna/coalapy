import numpy as np
from . import helperFunc as hf

def Gaussian(df, ncol): #pandas data frame
    A = np.zeros((ncol - 1,ncol - 1))

    sigma_sq = 0

    for x in range(0, ncol - 1):
        for y in range(x, ncol - 1):
            A[x][y]=hf.dist(x+1,y+1, df)
            A[y][x]=A[x][y]
            if sigma_sq < A[x][y]:
                sigma_sq = A[x][y]
    
    for x in range(0, ncol - 1):
        for y in range(x, ncol - 1):
            A[y][x]=A[y][x]/((-0.5)*sigma_sq)
            A[x][y]=A[x][y]/((-0.5)*sigma_sq)

    for x in range(0, ncol - 1):
        A[x]=np.exp(A[x])
    
    return A