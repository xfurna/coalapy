# import numpy as np
# from scipy import linalg
from .dfhandler import dframe_csv

from . import helperFunc



class modality:
    def __init__(self, path=None , mat_type="gaussian"):
        
        self.W = helperFunc.get_matrix(dframe_csv(path, mat_type=mat_type))
    #     self.dim=len(W) - 1
    #     self.similarity=W
    #     # self.degree=D
    #     if type:
            
    #     self.laplacian=np.identity(self.dim, dtype=self.type)