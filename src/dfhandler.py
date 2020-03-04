"""
Reads the csv and returns dataframe/Similarity
"""

from . import similarity_mat
import pandas as pd

class dframe_csv:
    def __init__(self, path, mat_type):
        self.df = pd.read_csv(path)
        self.W = similarity_mat.matrix(mat_type)

