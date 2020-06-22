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
    s[np.where(s < 1e-10)] = 0
    s = np.around(s, decimals=10)
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
    s[np.where(s < 1e-10)] = 0
    s = np.around(s, decimals=10)
    for i in range(len(s) - 1, -1, -1):
        ind = np.where(s == np.partition(s, i)[i])[0][0]
        t = len(s) - i - 1
        temp = s[ind]
        s[ind] = s[t]
        s[t] = temp
        u[:, [ind, t]] = u[:, [t, ind]]
    return u


def orthogonalize(x):
    n = x.shape[1]
    m = x.shape[0]
    q = np.zeros((m, n))
    r = np.zeros((n, n))

    for j in range(n):
        v = x[:, j]
        if j > 1:
            for i in range(j - 1):
                # tq = q[:, i].T
                r[i, j] = np.dot(q[:,i].T, x[:, j])
                v = v - r[i, j] * q[:, i]
        r[j, j] = sum(v ** 2) ** 0.5
        q[:, j] = v / r[j, j]
    return q

    
def get_orthonorm_basis(lap_list=None, chi_list=None, rank=3):
    if lap_list is not None:
        lap = sort_lr(chi_list=chi_list, lr_list=lap_list)
        return Matrix.make_mat.make_orthonorm_basis(lap, rank)
    else:
        print("Provide list of lra laplacian matrices")


def get_H_matrix(orthonorm_basis=None, lr_list=None, chi_list=None, rank=3, beta=1.25):
    if lr_list is not None and orthonorm_basis is not None:
        if chi_list is not None:
            alpha = []
            for i, chi in enumerate(chi_list):
                alpha.append(chi / ((beta) ** (i + 1)))
            alpha = [chi_f / np.sum(alpha) for chi_f in alpha]
            return Matrix.make_mat.make_H(orthonorm_basis, lr_list, alpha, rank)
        else:
            return Matrix.make_mat.make_H(
                orthonorm_basis, lr_list, get_weights(len(lr_list)), rank
            )
    else:
        print("Provide list of lra laplacian matrices and orthonormal basis matrix")


def compute_chi(lap_list):
    from sklearn.metrics import silhouette_score
    from sklearn.cluster import KMeans

    chi_list = []
    for lr in lap_list:
        s, u = np.linalg.eig(lr)
        s[np.where(s < 1e-10)] = 0
        s = np.around(s, decimals=10)

        ind = np.where(s == np.partition(s, -2)[-2])[0][0]

        Y = s[ind].real
        u = sorted_u(lr).real
        u_ = u[:, 1].reshape(-1, 1)
        cluster = KMeans(n_clusters=2, random_state=None).fit(u_)
        cluster_labels = cluster.predict(u_)
        s_score = silhouette_score(u_, cluster_labels)

        chi = s_score * np.absolute(Y)
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


def scale(df, center=True, scale=True):
    ncol = df.shape[0]
    if center:
        for i in range(ncol):
            df.iloc[i] -= df.iloc[i].mean()
    if scale and center:
        for i in range(ncol):
            df.iloc[i] /= df.iloc[i].std()
    elif scale:
        for i in range(ncol):
            df.iloc[i] /= np.sqrt(df.iloc[i].pow(2).sum().div(df.iloc[i].count() - 1))
    return df


def get_alpha(chi_list):
    chi_ls = chi_list.copy()
    for i, chi in enumerate(chi_ls):
        chi_ls[i] = chi / ((1.25) ** (i + 1))
    return chi_ls / sum(chi_ls)
