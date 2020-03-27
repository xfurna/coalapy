from . import dfhandler

def data_gen_test():
    try:
        mat = dfhandler.data_generator()
        if mat == 0:
            print("PASS")
    except:
        print("Return something")