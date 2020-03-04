from . import similarity_mat as sm


def get_matrix(path=None, mat_type):
    if path:
        print("don't give path yet")
    else:
        print("no paths. good")
        sm.matrix("gaussian")
        
