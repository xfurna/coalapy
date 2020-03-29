# """modalities here"""
import src
import numpy as np

# READ MODALITIES

path = '/hdd/Ztudy/BTP/code/CoALa/algo/toy_data.csv'

try:
    x1= src.modalities.modality(path, mat_type="gaussian")
    print("made x1")
except: 
    print("NO PATH PROVIDED")

# EIGEN DECOMPOSITION



