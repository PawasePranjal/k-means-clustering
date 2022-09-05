import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plot_graph(data, cluster_label, new_centroid):
    list_of_colours = []
    for cluster in cluster_label:
        if cluster == 1:
            list_of_colours.append("blue")
        else:
            list_of_colours.append("red")
    # print(list_of_colours)
    plt.clf()                             ## here .clf is used for clear figure in each loop.
    plt.scatter(data[:, 0], data[:, 1], c=list_of_colours)
    colours = ["yellow", "black"]
    plt.scatter(new_centroid[:, 0], new_centroid[:, 1], c=colours, s=100, marker="X")
    return plt
