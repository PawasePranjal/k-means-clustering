import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics


def get_data(input_file_path):
    data_df = pd.read_csv(input_file_path, skiprows=[0])
    # print(data_df)
    data_df.drop(data_df.columns[[0, 1, 2, 5]], axis=1, inplace=True)
    # print(data_df)
    array = data_df.to_numpy()
    return array


def get_K_initial_centroids(data, no_of_cluster):
    no_of_rows = data.shape[0]
    # print(no_of_rows)
    numbers = data[np.random.choice(no_of_rows, size=no_of_cluster)]
    return numbers


def get_clusters_assign(initial_centroids, data):
    Dist = metrics.pairwise_distances(data, initial_centroids, metric='euclidean')
    df = pd.DataFrame(Dist, columns=["1st_centroid", "2nd_centroid"])
    # print(df)
    df["minimum_dist"] = ''
    # print(df)
    for i in range(len(df)):
        if df.loc[i, "1st_centroid"] < df.loc[i, "2nd_centroid"]:
            df.loc[i, "minimum_dist"] = 1
        else:
            df.loc[i, "minimum_dist"] = 2
    # print(df["minimum_dist"])
    # print(df["minimum_dist"].to_numpy())
    return df["minimum_dist"].to_numpy()


def get_updated_centroids(data, cluster_label):
    df = pd.DataFrame(data, columns=["feature_1", "feature_2"])
    df["cluster_label"] = cluster_label
    print(df)
    new_centroid = df.groupby(["cluster_label"]).mean()
    print(new_centroid)
    new_centroid = new_centroid.to_numpy()
    return new_centroid


def get_status(initial_centroids, new_centroids, tolerance):
    difference = np.subtract(new_centroids, initial_centroids)
    difference = np.absolute(difference)
    # print(difference)
    return np.all(difference < tolerance)   #here .all is for checking the condition is true for each element in dataframe




