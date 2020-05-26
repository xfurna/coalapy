"""modalities here"""
import src
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

def CoALa():
    from sklearn.metrics import silhouette_score 
    # READ MODALITIES
    # add absolute path to data files here


    lap_mi = pd.read_csv("/hdd/Ztudy/BTP/code/CoALa/.data/cancer/laplacian/lap_mi.csv")
    lap_mr = pd.read_csv("/hdd/Ztudy/BTP/code/CoALa/.data/cancer/laplacian/lap_mr.csv")

    lap = [lap_mi.to_numpy(), lap_mr.to_numpy()]
    # try:
    #     for path in path_list:
    #         X= src.modalities.modality(path, mat_type="gaussian")
    #         print("Made a modality.")
    #         lap.append(X.laplacian)
    #         print("Laplacian appended successfully!")
    # except: 
    #     print("NO PATH PROVIDED")

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

    s_score = silhouette_score(V[:,:1], k_mean_affinity)

    k_mean_affinity = k_mean_affinity + 1

    # CoALa = src.helpers.helper.csv_wrapper(mat = k_mean_affinity, arg = "columns")
    # np.savetxt("/hdd/Ztudy/BTP/code/CoALa/.data/cancer/v_mi_mr.csv" , V , delimiter = ',')

    truth = pd.read_csv("/hdd/Ztudy/BTP/code/CoALa/.data/cancer/laplacian/origal_classinformation.csv")
    truth = truth.to_numpy()
    tr = truth[:,1]
    diff = tr - k_mean_affinity
    print("label diff 0: ", len(np.where(diff==0)[0]))
    print("label diff 1: ", len(np.where(diff==1)[0]))
    print("label diff -1: ", len(np.where(diff==-1)[0]))
    print("\nAccuracy on comparision with ground truth: ", max(100*len(np.where(diff==0)[0])/304, 100*len(np.where(diff==1)[0])/304, 100*len(np.where(diff==-1)[0])/304))
    print("Silhoutte score for [miRNA, mrRNA]: ", s_score)

def spectral():
    from sklearn.metrics import silhouette_score 
    from sklearn.cluster import SpectralClustering 
    x = pd.read_csv("/hdd/Ztudy/BTP/code/CoALa/CoALa/.data/cleaned_mi.csv")
    x = x.to_numpy().transpose()
    # Building the clustering model 
    spectral_model_nn = SpectralClustering(n_clusters = 2, affinity ='nearest_neighbors') 
    
    # Training the model and Storing the predicted cluster labels 
    labels_nn = spectral_model_nn.fit_predict(x) 
    
    truth = pd.read_csv("/hdd/Ztudy/BTP/code/CoALa/.data/cancer/laplacian/origal_classinformation.csv")
    truth = truth.to_numpy()
    tr = truth[:,1]

    s_score = silhouette_score(x, labels_nn)
#     print(len(labels_nn), len(tr))
    diff = tr-labels_nn
    print("label diff 0: ", len(np.where(diff==0)[0]))
    print("label diff 1: ", len(np.where(diff==1)[0]))
    print("label diff -1: ", len(np.where(diff==-1)[0]))
    print("\nAccuracy on comparision with ground truth: ", max(100*len(np.where(diff==0)[0])/304, 100*len(np.where(diff==1)[0])/304, 100*len(np.where(diff==-1)[0])/304))
    print("Silhoutte when sklearn.cluster.SpectralClustering on miRNA data : ", s_score)


CoALa()


