import numpy as np
import pandas as pd

def gr_accuracy(GR_TRUTH = None, labels = None, metadata = None):        
    if labels is None:
        from sklearn.cluster import KMeans
        from sklearn.metrics import silhouette_score

        labels = KMeans(n_clusters=metadata['n_cluster'], random_state=0).fit(metadata['data']).predict(metadata['data'])

        labels = np.array(labels)

    if GR_TRUTH is not None:
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

def silhouette_score(labels=None, data=None, metadata = None):
    from sklearn.metrics import silhouette_score
    if metadata is not None:
        from sklearn.cluster import KMeans

        labels_pred = KMeans(n_clusters=metadata['n_cluster'], random_state=0).fit(metadata['data']).predict(metadata['data'])

        labels_pred = np.array(labels_pred)
        s_score = silhouette_score(metadata['data'], labels_pred)
    else:
        s_score = silhouette_score(data, labels)

    return s_score

def f_measure(metadata = None):
    from sklearn.metrics import f1_score
    from sklearn.cluster import KMeans
    labels_pred = KMeans(n_clusters=metadata['n_cluster'], random_state=0).fit(metadata['data']).predict(metadata['data'])

    labels_pred = np.array(labels_pred)
    f_measure = f1_score(metadata['gr_truth'], labels_pred, )

    return f_measure

def jaccard(metadata = None):
    from sklearn.cluster import KMeans
    from sklearn.metrics import jaccard_score

    labels_pred = KMeans(n_clusters=metadata['n_cluster'], random_state=0).fit(metadata['data']).predict(metadata['data'])

    labels_pred = np.array(labels_pred)
    j_score = jaccard_score(metadata['gr_truth'], labels_pred)

    return j_score

def purity():
    pass

def dice():
    pass

def rand():
    pass

