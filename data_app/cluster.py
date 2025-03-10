import numpy as np
from math import radians
import sklearn as skl


# Function haversine_distance measures the haversine distance between 2 sets of lat/long coordinates
def haversine_distance(acoords, bcoords):
    acoords_in_radians = [radians(_) for _ in acoords]
    bcoords_in_radians = [radians(_) for _ in bcoords]

    distance = skl.metrics.pairwise.haversine_distances([acoords_in_radians, bcoords_in_radians])
    distance = distance * 6371000/1000

    return distance


# Function euclidean_distance measures the euclidean distance between 2 sets of lat/long coordinates
def euclidean_distance(acoords, bcoords):
    distance = skl.metrics.pairwise.euclidean_distances(acoords, bcoords)

    return distance


# Function cluster takes in an array of lat lon pairs and clusters them based on euclidean distance
def DBSCAN(data):
    X = np.array(data)

    # DBSCAN info https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html 
    clustering = skl.cluster.DBSCAN(eps = 0.005, min_samples = 7).fit(X)
    cluster_array = clustering.labels_

    return cluster_array


def get_cluster_shape(df, cluster_id):
    import random

    id_array = []
    for i in range(0, len(df.index)):
        if df.at[i, 'cluster id'] == cluster_id:
            id_array.append(i)

    north, south = df.at[random.choice(id_array), 'lat']
    east, west = df.at[random.choice(id_array), 'lon']
    for id in id_array:
        if df.at[id, 'lat'] > north: north = df.at[id, 'lat']
        if df.at[id, 'lat'] < south: south = df.at[id, 'lat']
        if df.at[id, 'lon'] > west: west = df.at[id, 'lon']
        if df.at[id, 'lon'] < east: east = df.at[id, 'lon']

    return north, south, east, west