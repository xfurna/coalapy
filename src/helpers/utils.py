"""
helpers.utils: module that contains methods that are used here and there as an utility.

helpers.utils.low_rank_mat:
    params: 
        SVD: the single value decomposition of the matrix
        A: the matrix itsef
        r: rank to which the matrix A is needed to be approximated
    return: 
        Ar: a matrix

helpers.utils.get_weights:
    params: 
        lap: a square symmetric matrix
    returns: a numoy array with all values 1/(number of rows in lap)

helpers.utils.sorted_u:
    params: 
        M: a square matrix
    return: 
        u: a matrix with columns being the eigenvectors of M sorted on the basis of their corresponding eigenvalues 

helpers.utils.orthogonalize:
    params:
        U: the matrix to be orthogonalized
        eps: threshold to set extremely small values to 0
    return: a matrix

helpers.utils.get_orthonorm_basis:
    params: 
        lr_list: List of low rank approximated laplacian matrices of each modality
        rank: the low rank of the laplacian matrices
    return: orthonormal basis of U

helpers.utils.get_H_matrix:
    params:
        orthonorm_basis: an orthonormal matrix (just as returned by helpers.utils.get_orthonorm_basis)
        lr_list: List of low rank approximated laplacian matrices of each modality
        rank: the low rank of the laplacian matrices
    return: a matrix (M*rank x Mrank)
"""
from .. import matrices as Matrix
import numpy as np


def low_rank_mat(SVD=None, A=None, r=1):
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
        return Matrix.make_mat.make_orthonorm_basis(lr_list, rank)
    else:
        print("Provide list of lra laplacian matrices")


def get_H_matrix(orthonorm_basis = None , lr_list = None , rank = 3):
    if lr_list is not None and orthonorm_basis is not None:
        return Matrix.make_mat.make_H(orthonorm_basis , lr_list, rank)
    else:
        print("Provide list of lra laplacian matrices and orthonormal basis matrix")