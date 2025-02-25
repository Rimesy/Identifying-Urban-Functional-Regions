import numpy as np
from math import radians
import sklearn as skl

def haversine_distance(acoords, bcoords):
    acoords_in_radians = [radians(_) for _ in acoords]
    bcoords_in_radians = [radians(_) for _ in bcoords]

    distance = skl.metrics.pairwise.haversine_distances([acoords_in_radians, bcoords_in_radians])
    distance = distance * 6371000/1000

    return distance

def euclidean_distance(acoords, bcoords):
    distance = skl.metrics.pairwise.euclidean_distances(acoords, bcoords)

    return distance

# Function cluster takes in an array of lat lon pairs and clusters them based on euclidean distance
def DBSCAN(data):
    X = np.array(data)
    clustering = skl.cluster.DBSCAN(eps=0.5, min_samples=10).fit(X)
    cluster_array = clustering.labels_

    return cluster_array