"""
Module to handle all dataframe related affairs. 
"""


from . import helpers
import pandas as pd
import sklearn.cluster as skl_cluster
import sklearn.datasets as skl_data
import numpy as np


"""
dfhandler.dframe_csv.__init__:
    params:
        path: absolute path to the datafile to be read (modality)
        mat_type: type of similarity matrix you want for the the modality
"""


class dframe_csv:
    def __init__(self, path, mat_type):
        self.df = pd.read_csv(path)
        self.path = path
        self.mat_type = mat_type
        self.nrow = self.df.shape[0]
        self.ncol = self.df.shape[1]


"""
dfhandler.data_generator: generates data which when plotted depicts two circular clusters 
    params: 
        multiplier: usefull in case multiple datafiles are requierd to be generated for experimentation
        filename: file name of the generated datafile
    return: a csv file gets stored
"""


def data_generator(multiplier=1):
    filename = None
    oc, circles_clusters = skl_data.make_circles(
        n_samples=400, noise=0.01, random_state=0, factor=0.5
    )
    oc = multiplier * oc
    circles = np.transpose(oc)
    circles = helpers.house_keeper.wrapx(circles)

    if filename == None:
        filename = "file" + str(multiplier) + ".csv"

    np.savetxt(filename, circles, delimiter=",")
    print("Saving toy data csv w/d", len(circles[:, 0]))
    d = len(oc[0]) - len(circles[0])


if __name__ == "__main__":
    import sys

    multipliers = sys.argv[1:]
    map(data_generator, multipliers)
