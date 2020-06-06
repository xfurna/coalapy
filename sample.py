"""modalities here"""
import coalapy
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

# READ MODALITIES
# add absolute path to data files here

path_list = []
lap = []

# expected number of clusters
k = 2
rank = 8

try:
    for path in path_list:
        X = coalapy.modalities.modality(path, mat_type="gaussian")
        print("Made a modality.")
        lap.append(X.laplacian)
        print("Laplacian appended successfully!")
except:
    print("NO PATH PROVIDED")

Ls = coalapy.modalities.lap_list(lap=lap, rank=rank)

V = Ls.joint_eig_vectors
V = V.real

kmeans = KMeans(n_clusters=k, random_state=0).fit(V[:, :1])
k_mean_affinity = kmeans.predict(V[:, :1])

k_mean_affinity = np.array(k_mean_affinity)
k_mean_affinity = k_mean_affinity + 1

CoALa = coalapy.helpers.helper.csv_wrapper(mat=k_mean_affinity, arg="columns")
np.savetxt(".inventory/results.csv", CoALa, delimiter=",")

print("Computed cluster info stored in .inventory/results.csv")
