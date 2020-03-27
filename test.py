import sklearn.cluster as skl_cluster
import sklearn.datasets as skl_data
# import matplotlib.pylab as plt 
import numpy as np
import pandas as pd


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

def generate_data():
    circles, circles_clusters = skl_data.make_circles(n_samples=400, noise=.01, random_state=0)
    # t_circles = np.transpose(circles)
    # print(x1.degree, '\n', x1.W, '\n', x1.laplacian)
    # result = circles[:,0]
    wrapy = [0]
    # a = [[11,21,31,14,15],[61,71,81,91,110]]
    wrapy[0]=[i for i in range(len(circles[0]))]
    circles = np.vstack((wrapy, circles))
    circles = np.transpose(circles)

    # print(a)
    wrapx = []
    wrapx=[i for i in range(len(circles[0]))]
    circles = np.vstack((wrapx, circles))
    # a = wrap2 + a 
    
    # wrap = np.arange(1, len(a[0])+1, 1)
    # a = np.append(wrap, a, axis=1)
    # a = np.append(wrap, a, axis=0)
    # result = np.transpose(a)

    # wrap = np.arange(1, len(a[0]), 1)
    # a = np.append(wrap, a, axis=0)
    np.savetxt("toy_data.csv", circles, delimiter = ',')

# generate_data()

df = pd.read_csv("toy_data.csv")
print(df.shape)