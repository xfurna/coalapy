from . import dfhandler
from . import helperFunc

def data_gen_test(multiplier, filename):
    # mat = dfhandler.data_generator(multiplier = multiplier, filename = filename)

    try:
        mat = dfhandler.data_generator(multiplier = multiplier, filename = filename)
        if mat == 0:
            print("PASS")
    except:
        print("Return something")

def wrap_test(mat, arg = None):
    try:
        if arg == "columns":
            return helperFunc.wrapx(mat)
        elif arg == "rows":
            return helperFunc.wrapy(mat)
        elif arg == "around":
            return helperFunc.wrap(mat)
    except:
        print("NO arg PROVIDED!\nReturning a wrap around...")
        return helperFunc.wrap(mat)


# following function is taken from main.py just in case in future it is considered
def na():
    try:
        x1= src.modalities.modality(path, mat_type="gaussian")
        print("made x1. onto wrapping laplacian")
        lap = src.tests.wrap_test(x1.laplacian, "columns")
        np.savetxt("mi_lap.csv", lap, delimiter = ',')
    except: 
        print("NO PATH PROVIDED")