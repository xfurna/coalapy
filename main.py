"""modalities here"""
import src
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

# READ MODALITIES
path_list = ["",""] # add absolute path to data files here

lap= []

try:
    for path in path_list:
        X= src.modalities.modality(path, mat_type="gaussian")
        print("made X onto making laplacian")
        lap.append(X.laplacian)
        print("laplacian appended successfully!")
except: 
    print("NO PATH PROVIDED")

# expected number of clusters 
k = 2
rank = 4

Ls = src.modalities.lap_list(lap = lap, rank = rank)

V = Ls.joint_eig_vectors
V = V.real

kmeans = KMeans(n_clusters=k, random_state=0).fit(V[:,:1])
k_mean_affinity = kmeans.predict(V[:,:1])

k_mean_affinity = np.array(k_mean_affinity) 

CoALa = src.tests.wrap_test(k_mean_affinity, "columns")
np.savetxt(".data/CoALa.csv" , CoALa , delimiter = ',')

print("Computed data-point belonging info stored in CoALa.csv")
# X1 = pd.read_csv(path_list[0])
# x1 = X1.to_numpy()

# import matplotlib.pyplot as plt
# plt.scatter(x1[0],x1[1], c=k_mean_affinity, s=50,cmap="viridis")
# plt.show()