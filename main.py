"""modalities here"""
import src
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

# READ MODALITIES
# add absolute path to data files here

path_list = ["/hdd/Ztudy/BTP/code/CoALa/algo/.data/cleaned_mi.csv", "/hdd/Ztudy/BTP/code/CoALa/algo/.data/cleaned_mr.csv"] 

lap= []

try:
    for path in path_list:
        X= src.modalities.modality(path, mat_type="gaussian")
        print("Made a modality.")
        lap.append(X.laplacian)
        print("Laplacian appended successfully!")
except: 
    print("NO PATH PROVIDED")

# expected number of clusters 
k = 2
rank = 8

Ls = src.modalities.lap_list(lap = lap, rank = rank)

V = Ls.joint_eig_vectors
V = V.real

kmeans = KMeans(n_clusters=k, random_state=0).fit(V[:,:1])
k_mean_affinity = kmeans.predict(V[:,:1])

# X1 = pd.read_csv(path_list[0])
# x1 = X1.to_numpy()

# import matplotlib.pyplot as plt
# plt.scatter(x1[0,0:],x1[1,0:], c=k_mean_affinity, s=50,cmap="viridis")
# plt.show()


k_mean_affinity = np.array(k_mean_affinity) 
k_mean_affinity = k_mean_affinity + 1

CoALa = src.helpers.helper.csv_wrapper(mat = k_mean_affinity, arg = "columns")
np.savetxt(".data/mi_mr_CoALa.csv" , CoALa , delimiter = ',')

print("Computed cluster info stored in .data/CoALa_mi_mr.csv")