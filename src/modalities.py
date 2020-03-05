# import numpy as np
# from scipy import linalg
from . import dfhandler

from . import helperFunc



class modality:
    def __init__(self, path=None , mat_type="gaussian"):
        self.W = helperFunc.get_similarity(dfhandler.dframe_csv(path, mat_type=mat_type))
        self.degree = helperFunc.matrix(W = self.W)
        self.laplacian = self.__get_laplacian()

    def __get_laplacian(self):
        D_sqrt = scipy.linalg.sqrtm(D)
        D_nsqrt = scipy.linalg.inv(D_sqrt)
        L = np.identity(mi.shape[1]-1, dtype=float) + D_nsqrt.dot(A).dot(D_nsqrt)
        return L

 