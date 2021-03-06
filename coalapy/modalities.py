"""
Contains classes modality and lap_list 
"""


from . import dfhandler
from . import helpers
import numpy as np

class modality:
    def __init__(self, path=None, mat_type="gaussian", clean=True):
        self.W = helpers.helper.matrix(
            dfhandler.dframe_csv(path, mat_type=mat_type, clean=clean)
        )
        self.degree = helpers.helper.matrix(W=self.W, get="degree")
        self.laplacian = self.__get_laplacian(get="shifted_laplacian")
        print(
            "Set modality parameters: similarity-matrix degree-matrix laplacian-matrix"
        )

    def __get_laplacian(self, get="shifted_laplacian"):  # private function
        print("Returning laplacian...")
        return np.around(helpers.helper.matrix(W=self.W, D=self.degree, get=get), decimals=9)

class lap_list:
    def __init__(self, lap_full=None, rank=None, n_clusters=3):
        self.lap_full = lap_full
        self.rank = rank
        self.M = len(lap_full)
        self.lra = self.__compute_lra(lap_full)
        self.chi_list = helpers.utils.compute_chi(lap_full)
        self.lap = helpers.utils.sort_lr(self.chi_list, self.lra)
        self.orthonorm_basis, self.Gamma = helpers.utils.get_orthonorm_basis(
            lap_list=self.lap_full, chi_list=self.chi_list, rank=rank
        )
        self.H = helpers.utils.get_H_matrix(
            orthonorm_basis=self.Gamma,
            lr_list=self.lap,
            chi_list=helpers.utils.get_alpha(chi_list=self.chi_list),
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
