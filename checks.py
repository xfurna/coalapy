"""
For testing, import tests module and experiment with the modules here
"""

import numpy as np
import pandas as pd
import src


def junk(): #uncomment to plot the comaprision b/w k mean and spectral clustering
    import sklearn.cluster as skl_cluster
    import sklearn.datasets as skl_data
    import matplotlib.pylab as plt 
    # cluster with kmeans
    circles, circles_clusters = skl_data.make_circles(n_samples=400, noise=.01, random_state=0)

    Kmean = skl_cluster.KMeans(n_clusters=2)
    Kmean.fit(circles)
    clusters = Kmean.predict(circles)

    # plot the data, colouring it by cluster
    plt.scatter(circles[:, 0], circles[:, 1], s=15, linewidth=0.1, c=clusters,cmap='flag')
    plt.show()

    # cluster with spectral clustering
    model = skl_cluster.SpectralClustering(n_clusters=2, affinity='nearest_neighbors', assign_labels='kmeans')
    labels = model.fit_predict(circles)
    plt.scatter(circles[:, 0], circles[:, 1], s=15, linewidth=0, c=labels, cmap='flag')
    plt.show()

def make_laplacian():
    path_lap = 'mi_lap.csv'

    try:
        x1= src.modalities.modality(path, mat_type="gaussian")
        print("made x1")
        np.savetxt("mi_lap.csv", x1.laplacian, delimiter = ',')

    except: 
        print("NO PATH PROVIDED. wrapping laplacian")
        mi_lap = pd.read_csv(path_lap)
        lap = mi_lap.to_numpy()
        lap = src.tests.wrapx_test(lap, arg = "columns")
    return lap


# data generation
def generate_data(multiplier, filename):
    src.tests.data_gen_test(multiplier, filename)


def RawToLap(): #function generates(optional) and saves two modalities followed by their laplacians 
    # generate_data(multiplier=1, filename="X1.csv")
    # generate_data(multiplier=1.6, filename="X2.csv")
    path_x1 = "/hdd/Ztudy/BTP/code/CoALa/algo/.data/X1.csv"
    path_x2 = "/hdd/Ztudy/BTP/code/CoALa/algo/.data/X2.csv"

    print("Read X1 X2. Making laplacian")

    x1 = src.modalities.modality(path_x1, mat_type="gaussian")
    x2 = src.modalities.modality(path_x2, mat_type="gaussian")


    l1 = src.tests.wrap_test(x1.laplacian, "columns")
    l2 = src.tests.wrap_test(x2.laplacian, "columns")

    np.savetxt(".data/L1.csv", l1, delimiter = ',')
    np.savetxt(".data/L2.csv", l2, delimiter = ',')
RawToLap()
