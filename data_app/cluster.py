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