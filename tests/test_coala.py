from . import meta


def test_coalapy():
    import coalapy
    import numpy as np
    from sklearn.cluster import KMeans
    import pandas as pd
    from sklearn.metrics import silhouette_score

    # READ MODALITIES

    try:
        for path in meta.PATH_LIST:
            X = coalapy.modalities.modality(path, mat_type="gaussian")
            print("Made a modality.")
            meta.LAP.append(X.laplacian)
            print("Laplacian appended successfully!")
    except:
        print("NO PATH PROVIDED", meta.PATH_LIST)

    Ls = coalapy.modalities.lap_list(lap=meta.LAP, rank=meta.rank)

    V = Ls.joint_eig_vectors
    V = V.real

    kmeans = KMeans(n_clusters=meta.k, random_state=0).fit(V[:, :1])
    k_mean_affinity = kmeans.predict(V[:, :1])

    k_mean_affinity = np.array(k_mean_affinity)

    truth = pd.read_csv(meta.GR_TRUTH)
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

    assert accuracy > 60
