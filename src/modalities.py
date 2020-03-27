# import numpy as np
# from scipy import linalg
from . import dfhandler

from . import helperFunc



class modality:
    def __init__(self, path=None , mat_type="gaussian"):
        self.W = helperFunc.get_similarity(dfhandler.dframe_csv(path, mat_type=mat_type))
        self.degree = helperFunc.matrix(W = self.W, get="degree")
        self.laplacian = self.__get_laplacian(get = "shifted_laplacian")

    def __get_laplacian(self, get = "shifted_laplacian"): #private function
        return helperFunc.matrix(W = self.W, D = self.degree, get=get)
        

 