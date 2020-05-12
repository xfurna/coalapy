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


Ls = src.modalities.lap_list(lap = lap, rank = 4)

V = Ls.joint_eig_vectors
V = V.real
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, random_state=0).fit(V[:,:1])
y_mean = kmeans.predict(V[:,:1])
X1 = pd.read_csv("/hdd/Ztudy/BTP/code/CoALa/algo/.data/X1.csv")
x1 = X1.to_numpy()
import matplotlib.pyplot as plt
plt.scatter(x1[0],x1[1], c=y_mean, s=50,cmap="viridis")
plt.show()
# Find alphas

 
# make orthonormal basis



# make H matrix

# get rotation matrix

# multiply it with ortho basis

# perform kmean affinity on k largest eigenvecors.