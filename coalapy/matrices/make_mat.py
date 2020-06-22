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
    U = Ur0[:, 1 : r + 1].copy()
    Gamma = []
    Gamma.append(U)
    for i in lap_list[1:]:
        Ui = hf.utils.sorted_u(i)
        Uri = Ui[:, 1 : r + 1].copy()

        S = np.dot(U.T, Uri)
        P = U.dot(S)
        Q = Uri - P
        G = hf.utils.orthogonalize(Q)
        Gamma.append(G)
        U = np.append(U, G, axis=1)
    print("Made Orthonormal basis successfully...")
    print("Basis: ", U.shape, " Gamma shape: ", Gamma[1].shape)
    return U, Gamma

def make_H(Gamma, lr_list, alpha, r):
    M = len(Gamma)
    HmList=[]
    H=np.zeros((M*r, M*r))
    for m in range(M):
        Lr=lr_list[m]
        HmTemp = np.zeros((M*r, M*r))
        for p in range(M):
            for q in range(M):
                Blockpq=(np.array(Gamma[p]).T).dot(Lr).dot(np.array(Gamma[q]))
                Blockpq[np.where(Blockpq < 1e-10)] = 0
                rs=(p)*r
                rl=(p)*r+r
                cs=(q)*r
                cl=(q)*r+r
                HmTemp[rs:rl,cs:cl]=Blockpq.copy()
        HmList.append(HmTemp)
    for i in range(M):
        H=H+alpha[i]* HmList[i]
    return H
    