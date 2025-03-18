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
    distance = distance * 6371000/1000 # Pretty sure this just converts to kilometers

    return distance


# Function euclidean_distance measures the euclidean distance between 2 sets of lat/long coordinates
def euclidean_distance(acoords, bcoords):
    distance = skl.metrics.pairwise.euclidean_distances(acoords, bcoords)

    return distance


# Function cluster takes in an array of lat lon pairs and clusters them based on euclidean distance
def DBSCAN(data, size):
    X = np.array(data)

    # DBSCAN info https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html
    clustering = skl.cluster.DBSCAN(eps = size, min_samples = 5).fit(X) # TODO: Maximum cluster size??
    cluster_array = clustering.labels_

    return cluster_array


# Function create_cluster_data finds the coordintes of the four corners of each cluster in an array of clusters, as well as the color associated with the group of the cluster
def create_cluster_data(df, array, index_bin):

    lon_coords = []
    lat_coords = []
    colors = []

    for cluster_id in array:
        cluster_id = cluster_id.astype('int32')

        id_array = [] # List to hold all of the POIs within the cluster
        for i in range(0, len(df.index)):
            # This if statement is true if the POI is in the cluster
            if (i not in index_bin) and (df.at[i, 'cluster id'] == cluster_id):
                id_array.append(i)

        # The rest of the code within the for loop doesn't work if the id_array is empty
        if id_array == []:
            continue

        # TODO: Change shape from rectangle to polygon
        # Set the corner coordinates
        north = df.at[id_array[0], 'lat']
        south = df.at[id_array[0], 'lat']
        east = df.at[id_array[0], 'lon']
        west = df.at[id_array[0], 'lon']
        # This for loop checks if the coordinates of each POI extend the bounds of the cluster
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

        # Assign a color from the color map
        group = data_handling.classify_data(1, df.at[id_array[0], 'pointX classification code'])
        colors.append(color_map[group])

    return lon_coords, lat_coords, colors