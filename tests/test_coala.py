def test_coalapy():

    import coalapy
    import numpy as np
    from sklearn.cluster import KMeans
    import pandas as pd
    from sklearn.metrics import silhouette_score

    # lists

    path_list = [".inventory/X2.csv", ".inventory/X1.csv"]
    lap = []

    # expected number of clusters

    k = 2
    rank = 8

    # READ MODALITIES

    try:
        for path in path_list:
            X = coalapy.modalities.modality(path, mat_type="gaussian")
            print("Made a modality.")
            lap.append(X.laplacian)
            print("Laplacian appended successfully!")
    except:
        print("NO PATH PROVIDED", path_list)

    Ls = coalapy.modalities.lap_list(lap=lap, rank=rank)

    V = Ls.joint_eig_vectors
    V = V.real

    kmeans = KMeans(n_clusters=k, random_state=0).fit(V[:, :1])
    k_mean_affinity = kmeans.predict(V[:, :1])

    k_mean_affinity = np.array(k_mean_affinity)

    # Comparing the calculations with the ground truth

    truth = pd.read_csv(".inventory/gr_truth.csv")
    truth = truth.to_numpy()
    labels = truth[:, 1]

    n = len(labels)
    diff = labels - k_mean_affinity

    s_score = silhouette_score(V[:, :1], k_mean_affinity)

    accuracy = max(
        100 * len(np.where(diff == 0)[0]) / n,
        100 * len(np.where(diff == 1)[0]) / n,
        100 * len(np.where(diff == -1)[0]) / n,
    )

    print("label diff 0: ", len(np.where(diff == 0)[0]))
    print("label diff 1: ", len(np.where(diff == 1)[0]))
    print("label diff -1: ", len(np.where(diff == -1)[0]))
    print("\n % Accuracy on comparision with ground truth: ", accuracy)
    print("Silhoutte score for: ", s_score)

    assert accuracy > 55
