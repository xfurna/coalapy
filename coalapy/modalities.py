"""
Contains classes modality and lap_list 
"""


from . import dfhandler
from . import helpers


class modality:
    def __init__(self, path=None, mat_type="gaussian", clean=True):
        self.W = helpers.helper.matrix(dfhandler.dframe_csv(path, mat_type=mat_type, clean=clean))
        self.degree = helpers.helper.matrix(W=self.W, get="degree")
        self.laplacian = self.__get_laplacian(get="shifted_laplacian")
        print(
            "Set modality parameters: similarity-matrix degree-matrix laplacian-matrix"
        )

    def __get_laplacian(self, get="shifted_laplacian"):  # private function
        print("Returning laplacian...")
        return helpers.helper.matrix(W=self.W, D=self.degree, get=get)


class lap_list:
    def __init__(self, lap=None, rank=None):
        self.rank = rank
        self.M = len(lap)
        self.lra = self.__compute_lra(lap)
        self.chi_list = helpers.utils.compute_chi(lap)
        self.lap = helpers.utils.sort_lr(self.chi_list, self.lra)
        self.orthonorm_basis = helpers.utils.get_orthonorm_basis(
            lr_list=self.lra, rank=rank
        )
        self.H = helpers.utils.get_H_matrix(
            orthonorm_basis=self.orthonorm_basis,
            lr_list=self.lap,
            chi_list=self.chi_list,
            rank=rank,
        )
        self.rotation = self.__compute_rotation_matrix()
        self.joint_eig_vectors = self.__compute_eig_vectors()
        print(
            "Set laplacian-list parameters: rank M low-rank-approximations relevance sorted-laplacian orthonormal-basis-matrix H-matrix rotation-matrix joint-eigenvector-matrix"
        )

    def __compute_lra(self, lap):
        lap_r = []
        for i in range(self.M):
            lap_r.append(helpers.utils.low_rank_mat(A=lap[i], r=self.rank))
        print("Computed lra...")
        return lap_r

    def __compute_rotation_matrix(self):
        R = helpers.utils.sorted_u(self.H)
        print("Computed rotation-matrix")
        return R

    def __compute_eig_vectors(self):
        U = self.orthonorm_basis
        R = self.rotation
        V = U.dot(R)
        print("computed joint-eigenvector-matrix")
        return V

    def plan_b(self, beta=1.25):
        import numpy as np
        alpha_list=self.chi_list
        for i, chi in enumerate(alpha_list):
            alpha_list[i]=chi/((beta)**(i+1))
        alpha_list = [chi/np.sum(chi_list) for chi in alpha_list]        
        L = np.zeros(self.lap[0].shape)
        for i,lr in enumerate(self.lap):
            L+=lr*alpha_list[i]
        return L



