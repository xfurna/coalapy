from . import dfhandler
from . import helpers

def data_gen_test(multiplier, filename):
    # mat = dfhandler.data_generator(multiplier = multiplier, filename = filename)

    try:
        mat = dfhandler.data_generator(multiplier = multiplier, filename = filename)
        if mat == 0:
            print("PASS")
    except:
        print("Return something")


# following function is taken from main.py just in case in future it is considered
"""
def na():
    try:
        x1= coalapy.modalities.modality(path, mat_type="gaussian")
        print("made x1. onto wrapping laplacian")
        lap = coalapy.tests.wrap_test(x1.laplacian, "columns")
        np.savetxt("mi_lap.csv", lap, delimiter = ',')
    except: 
        print("NO PATH PROVIDED")
"""
