"""
Call it the heart of the black-box. All kind of instructions are carried out by the helper functions defined herein.
"""

from src import matrices as Matrix
from . import house_keeper

"""
helper.matrix(df_csv = None, W = None, D = None, get = None): Directs the instructions meant for the matrices. 

params:
    df_csv: object of dfhandler.dframe_csv class
    W, D: Matrices on which the operations are intended. 
    get: takes three values- 
        degree: returns degree matrix
        shifted_laplacia: returns shifted laplacian
        laplacian: returns simple laplacian

return: A matrix
"""
def matrix(df_csv = None, W = None, D = None, get = None): #df_csv is dfraem_csv obj; W is the subject matrix; get is the matrix to be returned 
    if df_csv:
        if df_csv.mat_type == 'gaussian':
            return Matrix.similarity_mat.Gaussian(df_csv.df, df_csv.df.shape[1])
    elif W is not None:
        if get == "degree":
            return Matrix.getters.get_degree(W)
        elif get == "shifted_laplacian":
            return Matrix.getters.get_shifted_laplacian(W, D)
        elif get == "laplacian":
            return Matrix.getters.get_laplacian(W, D)
    else:
        return None

def csv_wrapper(mat, arg = None):
    try:
        if arg == "columns":
            return house_keeper.wrapx(mat)
        elif arg == "rows":
            return house_keeper.wrapy(mat)
        elif arg == "around":
            return house_keeper.wrap(mat)
    except:
        print("NO arg PROVIDED!\nReturning a wrap around...")
        return house_keeper.wrap(mat)


