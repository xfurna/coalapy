"""
helpers.utils: module that contains methods that are used here and there as an utility.


helpers.utils.low_rank_mat(SVD=None, A=None, r=1): computes low rank approximation by SVD method
    params: 
        SVD: the single value decomposition of the matrix
        A: the matrix itsef
        r: rank to which the matrix A is needed to be approximated
    return: 
        Ar: a matrix


helpers.utils.get_weights(lap): a simple assignment of equal weights to the modalities toill alpha thing is ready
    params: 
        lap: a square symmetric matrix
    returns: a numoy array with all values 1/(number of rows in lap)


helpers.utils.sorted_u(M): computes and returns eigenvectors sorted according to the order of their corresponding eigenvalues 
    params: 
        M: a square matrix
    return: 
        u: a matrix with columns being the eigenvectors of M sorted on the basis of their corresponding eigenvalues 


helpers.utils.orthogonalize(U, eps=1e-15): performs Gram-Schmidt orthogonalisation on U
    params:
        U: the matrix to be orthogonalized
        eps: threshold to set extremely small values to 0
    return: a matrix


helpers.utils.get_orthonorm_basis(lr_list = None , rank = 3): computes orthonormal basis as guided in the CoALa algorithm
    params: 
        lr_list: List of low rank approximated laplacian matrices of each modality
        rank: the low rank of the laplacian matrices
    return: orthonormal basis U


helpers.utils.get_H_matrix(orthonorm_basis = None , lr_list = None , rank = 3): computes H matrix from the algorithm
    params:
        orthonorm_basis: an orthonormal matrix (just as returned by helpers.utils.get_orthonorm_basis)
        lr_list: List of low rank approximated laplacian matrices of each modality
        rank: the low rank of the laplacian matrices
    return: a matrix (M*rank x M*rank)
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


def get_weights(lap=None, Num=None):
    if lap is not None:
        M = len(lap)
    else:
        M = Num
    return np.full((1, M), 1 / M, dtype=float)[0]


# ToDo: write code to avoid passing repeatetive eigenvectors
def sorted_u(M):
    s, u = np.linalg.eig(M)
    for i in range(len(s) - 1, -1, -1):
        ind = np.where(s == np.partition(s, i)[i])[0][0]
        t = len(s) - i - 1
        temp = s[ind]
        s[ind] = s[t]
        s[t] = temp
        u[:, [ind, t]] = u[:, [t, ind]]
    return u


def orthogonalize(U, eps=1e-15):
    n = len(U[0])
    V = U.T
    for i in range(n):
        prev_basis = V[0:i]
        coeff_vec = np.dot(prev_basis, V[i].T)
        V[i] -= np.dot(coeff_vec, prev_basis).T
        if np.linalg.norm(V[i]) < eps:
            V[i][V[i] < eps] = 0.0
        else:
            V[i] /= np.linalg.norm(V[i])
    return V.T


def get_orthonorm_basis(lr_list=None, rank=3):
    if lr_list is not None:
        return Matrix.make_mat.make_orthonorm_basis(lr_list, rank)
    else:
        print("Provide list of lra laplacian matrices")


def get_H_matrix(orthonorm_basis=None, lr_list=None, chi_list=None, rank=3, beta=1.25):
    if lr_list is not None and orthonorm_basis is not None:
        if chi_list is not None:
            for i, chi in enumerate(chi_list):
                chi_list[i]=chi/((beta)**(i+1))
            return Matrix.make_mat.make_H(orthonorm_basis, lr_list, chi_list, rank)
        else:
            return Matrix.make_mat.make_H(
                orthonorm_basis, lr_list, get_weights(len(lr_list)), rank
            )
    else:
        print("Provide list of lra laplacian matrices and orthonormal basis matrix")


def compute_chi(lr_list):
    from sklearn.metrics import silhouette_score
    from sklearn.cluster import KMeans

    chi_list = []
    for lr in lr_list:
        s, u = np.linalg.eig(lr)

        ind = np.where(s == np.partition(s, 1)[1])[0][0]

        Y = s[ind].real
        u = sorted_u(lr).real

        cluster = KMeans(n_clusters=2, random_state=None).fit(u[:, :1])
        cluster_labels = cluster.predict(u[:, :1])
        s_score = silhouette_score(u[:, :1], cluster_labels)

        chi = 0.25 * (s_score * Y + 1)
        chi_list.append(chi)
    return chi_list


def sort_lr(chi_list, lr_list):
    len_chi = len(chi_list)
    for i in range(1, len_chi):

        key_chi = chi_list[i]
        key_lr = lr_list[i]

        j = i - 1
        while j >= 0 and key_chi > chi_list[j]:
            chi_list[j + 1] = chi_list[j]
            lr_list[j + 1] = lr_list[j]
            j -= 1
        chi_list[j + 1] = key_chi
        lr_list[j + 1] = key_lr
    return lr_list
