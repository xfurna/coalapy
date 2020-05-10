# """modalities here"""
import src
import numpy as np


import pandas as pd

# READ MODALITIES
def na():
    try:
        x1= src.modalities.modality(path, mat_type="gaussian")
        print("made x1. onto wrapping laplacian")
        lap = src.tests.wrap_test(x1.laplacian, "columns")
        np.savetxt("mi_lap.csv", lap, delimiter = ',')
    except: 
        print("NO PATH PROVIDED")

# list laplacians

L1 = pd.read_csv("/hdd/Ztudy/BTP/code/CoALa/algo/.data/L1.csv")
L2 = pd.read_csv("/hdd/Ztudy/BTP/code/CoALa/algo/.data/L2.csv")

l1=L1.to_numpy()
l2=L2.to_numpy()

lap = [l1, l2]

# Find alphas

l1=0.5*l1
l2=0.5*l2
 
# make orthonormal basis



# make H matrix

# get rotation matrix

# multiply it with ortho basis

# perform kmean affinity on k largest eigenvecors.