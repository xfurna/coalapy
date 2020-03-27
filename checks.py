import sklearn.cluster as skl_cluster
import sklearn.datasets as skl_data
import matplotlib.pylab as plt 
import numpy as np
import pandas as pd
import src



src.tests.task()
def junk(): #uncomment to plot the comaprision b/w k mean and spectral clustering
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
