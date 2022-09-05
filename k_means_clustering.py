from utils import get_K_initial_centroids, get_clusters_assign, get_data, get_updated_centroids, get_status
from plotting import plot_graph
import pandas as pd
import matplotlib.pyplot as plt



no_of_cluster = 2
input_file_path = "C:/Users/admin/Downloads/Iris.csv"
data = get_data(input_file_path)
# print(data)
initial_centroids = get_K_initial_centroids(data, no_of_cluster)
print(initial_centroids)
tolerance = 0.05
plt.scatter(data[:, 0], data[:, 1])
plt.savefig(r"D:\code\k_means_clustering\test0")

for loop in range(1, 500):

    cluster_label = get_clusters_assign(initial_centroids, data)
    # print(cluster_label)
    new_centroids = get_updated_centroids(data, cluster_label)
    print(new_centroids)
    status = get_status(initial_centroids, new_centroids, tolerance)
    plot = plot_graph(data, cluster_label, new_centroids)
    # plt.show()
    plt.savefig(r"D:\code\k_means_clustering\test" + str(loop) + ".png")
    if status:              ## here if status means in our status function output of return is true then our loop is break
        break
    initial_centroids = new_centroids


