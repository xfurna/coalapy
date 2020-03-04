"""
Reads the csv and returns dataframe/Similarity
"""

from . import similarity_mat
import pandas as pd

class dframe_csv:
    def __init__(self, path, mat_type):
        self.df = pd.read_csv(path)

    def get_nrow(self):
        self.nrow = self.df.shape[0]
        
    def get_ncol(self)
        self.ncol = self.df.shape[1]
