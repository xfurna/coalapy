"""
all commands to dedicated files goes through this file of helper fnctions.
for example, 
"""

from . import matrices as sm
import numpy as np
import cmath

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


def dist_sq(i, j, df): #pandas df
    result_vector = df[list(df.columns)[i]] - df[list(df.columns)[j]]
    result_vector= result_vector * result_vector
    result = result_vector.sum()
    return result



# Cleans the matrix by removing imaginary part from each element
def clean(mat):
    return mat.real

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

def get_lra(SVD=None, A=None, r=1):
    if not SVD:
        SVD = np.linalg.svd(A, full_matrices=False)
    u, s, v = SVD
    Ar = np.zeros((len(u), len(v)))
    for i in range(r):
        Ar += s[i] * np.outer(u.T[i], v[i])
    return Ar

def get_weights(lap):
    M = len(lap)
    return np.full((1, M), 1/M, dtype=float)


def sorted_u(M): # write code to avoid passing repeatetive eigenvectors
    s,u = np.linalg.eig(M)
    for i in range(len(s)-1, -1, -1):
        ind = np.where(s == np.partition(s, i)[i])[0][0]
        t = len(s) - i - 1
        temp=s[ind]
        s[ind]=s[t]
        s[t]=temp
        u[:,[ind,t]] = u[:,[t,ind]]
    return u


def orthogonalize(U, eps=1e-15):
    n = len(U[0])
    V = U.T
    for i in range(n):
        prev_basis = V[0:i]     # orthonormal basis before V[i]
        coeff_vec = np.dot(prev_basis, V[i].T)  # each entry is np.dot(V[j], V[i]) for all j < i
        # subtract projections of V[i] onto already determined basis V[0:i]
        V[i] -= np.dot(coeff_vec, prev_basis).T
        if np.linalg.norm(V[i]) < eps:
            V[i][V[i] < eps] = 0.   # set the small entries to 0
        else:
            V[i] /= np.linalg.norm(V[i])
    return V.T


def get_orthonorm_basis(lr_list = None , rank = 3):
    if lr_list is not None:
        return sm.make_orthonorm_basis(lr_list, rank)
    else:
        print("provide list of lra laplacian matrices")


def get_H_matrix(orthonorm_basis = None , lr_list = None , rank = 3):
    if lr_list is not None and orthonorm_basis is not None:
        return sm.make_H(orthonorm_basis , lr_list, rank)
    else:
        print("provide list of lra laplacian matrices and orthonormal basis matrix")