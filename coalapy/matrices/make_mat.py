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


def make_orthonorm_basis(lap_list, r):
    n = len(lap_list[0])
    Ur0 = hf.utils.sorted_u(lap_list[0])
    U = np.zeros((n, r))
    U = Ur0[:, 1:r+1].copy()
    print("\nUr0 is\n", Ur0[1:,0,:9],"\n",Ur0[1:1,:9])

    for i in lap_list[1:]:
        Ui = hf.utils.sorted_u(i)
        Uri = Ui[:, 1:r+1].copy()

        Ut = U.transpose()

        S = Ut.dot(Uri)
        P = U.dot(S)
        Q = Uri - P
        print("\nUi is\n", Ui[1:,:9],"\n",Ui[1:,1,:9])
        G = hf.utils.orthogonalize(Q)

        U = np.append(U, G, axis=1)
        print("Made Orthonormal basis successfully...")
    return U


def make_H(orthonorm_basis, lr_list, alpha, r):
    M = len(lr_list)
    H = np.zeros((M * r, M * r))
    for i in range(M):
        Lr = lr_list[i]
        gamma = orthonorm_basis[:, :].copy()
        gamma[:, i + 1 :] = 0
        gamma_T = np.transpose(gamma)
        P = gamma_T.dot(Lr)
        H = H + alpha[i] * P.dot(gamma)
    print("Made H matrix successfully...")
    return H
