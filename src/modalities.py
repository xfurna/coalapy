from . import dfhandler
from . import helperFunc



class modality:
    def __init__(self, path=None , mat_type="gaussian"):
        self.W = helperFunc.get_similarity(dfhandler.dframe_csv(path, mat_type=mat_type))
        self.degree = helperFunc.matrix(W = self.W, get="degree")
        self.laplacian = self.__get_laplacian(get = "shifted_laplacian")

    def __get_laplacian(self, get = "shifted_laplacian"): #private function
        return helperFunc.matrix(W = self.W, D = self.degree, get=get)
        
class lap_list:
    def __init__(self , lap=None , rank=None):
        self.rank = rank
        self.M = len(lap)
        self.lap = lap
        self.lra = self.__compute_lra()# define _compute_lra() within this class
        self.weights = helperFunc.get_weights(self.lap)# alphas from helperfunc
        self.orthonorm_basis = helperFunc.get_orthonorm_basis(lr_list = self.lra, rank = rank) # define make_orthonorm_basis() within this class
        self.H = helperFunc.get_H_matrix(orthonorm_basis = self.orthonorm_basis , lr_list = self.lra, rank = rank)  # define make_H() within the calss
        self.rotation = self.__compute_rotation_matrix()  #define get_rotation()
        self.joint_eig_vectors = self.__compute_eig_vectors() # multiply U and R
    
    def __compute_lra(self):
        lap_r = []
        for i in range(self.M):
            lap_r.append(helperFunc.get_lra(A=self.lap[i] , r=self.rank))
        return lap_r
    
    def __compute_rotation_matrix(self):
        R = helperFunc.sorted_u(self.H)
        return R

    def __compute_eig_vectors(self):
        U = self.orthonorm_basis
        R = self.rotation
        V = U.dot(R)
        return V