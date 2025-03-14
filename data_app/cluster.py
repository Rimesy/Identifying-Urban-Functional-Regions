import numpy as np
from math import radians
import sklearn as skl
import data_handling
from classification import color_map


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
    clustering = skl.cluster.DBSCAN(eps = 0.003, min_samples = 7).fit(X)
    cluster_array = clustering.labels_

    return cluster_array


def create_cluster_coords(df, array, index_bin):
    # print("Array: " + str(array)) # TODO: check why array isn't parsing properly

    lon_coords = []
    lat_coords = []
    colors = []

    for cluster_id in array:
        cluster_id = cluster_id.astype('int32')
        # print("Cluster id: " + str(cluster_id))

        id_array = []
        for i in range(0, len(df.index)):
            if (i not in index_bin) and (df.at[i, 'cluster id'] == cluster_id):
                id_array.append(i)

        if id_array == []:
            continue

        north = df.at[id_array[0], 'lat']
        south = df.at[id_array[0], 'lat']
        east = df.at[id_array[0], 'lon']
        west = df.at[id_array[0], 'lon']
        for _id in id_array:
            if df.at[_id, 'lat'] > north: north = df.at[_id, 'lat']
            if df.at[_id, 'lat'] < south: south = df.at[_id, 'lat']
            if df.at[_id, 'lon'] > west: west = df.at[_id, 'lon']
            if df.at[_id, 'lon'] < east: east = df.at[_id, 'lon']

        lat_coords.append([north, south, south, north, north, None])
        lon_coords.append([west, west, east, east, west, None])

        """
        north, west ----- north, east
             |                 |
             |                 |
             |                 |
             |                 |
        south, west ----- south, east
        """

        group = data_handling.classify_data(1, df.at[id_array[0], 'pointX classification code'])
        colors.append(color_map[group])

    return lon_coords, lat_coords, colors

