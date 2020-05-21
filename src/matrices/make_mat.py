"""
Module curating methods that makes matrices as directed in the algorithm


matrices.make_mat.make_orthonorm_basis(lr_list, r): computes orthonormal basis as guided in the CoALa algorithm
    params: 
        lr_list: List of low rank approximated laplacian matrices of each modality
        r: the low rank of the laplacian matrices
    return: orthonormal basis U


matrices.make_mat.make_H(rthonorm_basis, lr_list, r)): computes H matrix from the algorithm
    params:
        orthonorm_basis: an orthonormal matrix (just as returned by helpers.utils.get_orthonorm_basis)
        lr_list: List of low rank approximated laplacian matrices of each modality
        r: the low rank of the laplacian matrices
    return: a matrix H of dim(M*rank x M*rank)
"""


import numpy as np
from .. import helpers as hf


def make_orthonorm_basis(lr_list, r):
    n = len(lr_list[0]) 
    Ur0 = hf.utils.sorted_u(lr_list[0])
    U = np.zeros((n, r))
    U = Ur0[:,:r].copy()

    for i in lr_list[1:]:
        Ui = hf.utils.sorted_u(i)
        Uri = Ui[:,:r].copy()
    
        Ut=U.transpose()

        S = Ut.dot(Uri)
        P = U.dot(S)
        Q = Uri - P
        G = hf.utils.orthogonalize(Q)
    
        U = np.append(U, G, axis=1)
    return U


def make_H(orthonorm_basis, lr_list, r):
    M = len(lr_list)
    H = np.zeros((M*r, M*r))
    alpha = hf.utils.get_weights(lr_list)
    for i in range(M):
        Lr=lr_list[i]
        gamma = orthonorm_basis[:,:].copy()
        gamma[:,i+1:] = 0
        gamma_T = np.transpose(gamma)
        P = gamma_T.dot(Lr)
        H = H + alpha[0][i]*P.dot(gamma)
    return H
