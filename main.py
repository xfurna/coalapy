# """modalities here"""
import src
import numpy as np

# READ MODALITIES

path = '/hdd/Ztudy/BTP/code/CoALa/algo/toy_data.csv'

try:
    x1= src.modalities.modality(path, mat_type="gaussian")
    print("made x1. onto wrapping laplacian")
    lap = src.tests.wrap_test(x1.laplacian, "columns")
    np.savetxt("mi_lap.csv", lap, delimiter = ',')
except: 
    print("NO PATH PROVIDED")

# EIGEN DECOMPOSITION