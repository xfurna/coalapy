from . import dfhandler
from . import helperFunc

def data_gen_test():
    try:
        mat = dfhandler.data_generator()
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