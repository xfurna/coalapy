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