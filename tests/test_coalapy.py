from . import meta
import coalapy
import pandas as pd
import numpy as np


def test_accuracy():
    gr_truth = pd.read_csv(meta.GR_TRUTH).to_numpy()[:, 1]
    assert coalapy.analyse.gr_accuracy(GR_TRUTH=meta.GR_TRUTH, labels=gr_truth) == 100


def test_coala():
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score

    # READ MODALITIES

    print("Making modalities.")

    try:
        for path in meta.PATH_LIST:
            X = coalapy.modalities.modality(path, mat_type="gaussian", clean=True)
            meta.LAP.append(X.laplacian)
    except:
        print("NO PATH PROVIDED")

    print("All modalities made successfully!")
    print("Laplacian appended successfully!")

    Ls = coalapy.modalities.lap_list(lap_full=meta.LAP, rank=meta.rank)

    V = Ls.joint_eig_vectors
    V = V.real
    metadata = {"n_cluster": 2, "data": V[:, :1]}

    print("Silhoutte score: ", coalapy.analyse.silhouette_score(metadata=metadata))
    accuracy = coalapy.analyse.gr_accuracy(
        GR_TRUTH=meta.GR_TRUTH, metadata={"n_cluster": 2, "data": V[:, :1]}
    )

    assert accuracy > 49
