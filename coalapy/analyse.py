import numpy as np
import pandas as pd

def gr_accuracy(GR_TRUTH = None, labels = None, metadata = None):        
    if labels is None:
        from sklearn.cluster import KMeans
        from sklearn.metrics import silhouette_score

        labels = KMeans(n_clusters=metadata['n_cluster'], random_state=0).fit(metadata['data']).predict(metadata['data'])

        labels = np.array(labels)

    if GR_TRUTH:
        n = len(labels)
        gr_truth = pd.read_csv(GR_TRUTH).to_numpy()[:,1]

        diff = gr_truth - labels
        accuracy = max(
            100 * len(np.where(diff == 0)[0]) / n,
            100 * len(np.where(diff == 1)[0]) / n,
            100 * len(np.where(diff == -1)[0]) / n,
        )

        print("label diff 0: ", len(np.where(diff==0)[0]))
        print("label diff 1: ", len(np.where(diff==1)[0]))
        print("label diff -1: ", len(np.where(diff==-1)[0]))
        print("\n % Accuracy on comparision with ground truth: ", accuracy)
    
    else:
        raise Exception("No ground truth provided!") 
    
    return  accuracy

def silhouette_score(metadata = None):
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score

    labels = KMeans(n_clusters=metadata['n_cluster'], random_state=0).fit(metadata['data']).predict(metadata['data'])

    labels = np.array(labels)
    s_score = silhouette_score(metadata['data'], labels)

    return s_score

