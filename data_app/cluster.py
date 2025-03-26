import numpy as np
from scipy.spatial import ConvexHull
from math import radians
import sklearn as skl
import data_utilities
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
    clustering = skl.cluster.DBSCAN(eps = size, min_samples = 5).fit(X) # There is noway to make a maximum cluster size
    cluster_array = clustering.labels_

    return cluster_array


# Function create_cluster_data finds the coordintes of the four corners of each cluster in an array of clusters, as well as the color associated with the group of the cluster
def create_cluster_data(df, array_of_clusters, index_bin):

    shape_lon_coords = [] # This 2D list will hold all of the latitude coordinates for clusters
    shape_lat_coords = [] # This 2D list will hold all of the longitude coordinates for clusters
    shape_colors = [] # This list will hold the colours for every cluster

    error_count = 0 # For counting caught errors

    for cluster_id in array_of_clusters:
        cluster_id = cluster_id.astype('int32')

        poi_id_array = [] # List to hold all of the POIs within the cluster # INFO: This is crap coding... sort it out you idiot
        poi_coords_array = [] # List to hold the coords of POIs in the cluster
        for i in range(0, len(df.index)):
            # This if statement is true if the POI is in the cluster
            if (i not in index_bin) and (df.at[i, 'cluster id'] == cluster_id):
                poi_id_array.append(i)
                poi_coords_array.append([df.at[i, 'lon'], df.at[i, 'lat']])

        # The rest of the code within the for loop doesn't work if the id_array is empty
        if poi_id_array == []:
            continue

        # Old rectangular cluster shapes
        """
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
        
        north, west ----- north, east
             |                 |
             |                 |
             |                 |
             |                 |
        south, west ----- south, east
        """

        try:
            points = np.array(poi_coords_array)
            hull = ConvexHull(points) # Computes a convex hull from the POIs in the cluster - to find out more about convex hulls visit https://www.geeksforgeeks.org/convex-hull-algorithm/
            boundary_points = points[hull.vertices].tolist() # This assigns the coordinates of the hull points to a new list
        
            boundary_lats = []
            boundary_lons = []
            # This loop creates a set of coordinates for the cluster that can then be used later to create a shape in plotly
            for point in boundary_points:
                boundary_lats.append(point[1])
                boundary_lons.append(point[0])
            boundary_lats.extend([boundary_lats[0], None])
            boundary_lons.extend([boundary_lons[0], None])

            shape_lat_coords.append(boundary_lats)
            shape_lon_coords.append(boundary_lons)

            # Assign a color from the color map
            group = data_utilities.classify_data(1, df.at[poi_id_array[0], 'pointX classification code'])
            shape_colors.append(color_map[group])

        except Exception as e:
            error_count += 1
            print(error_count, ' QH6154 Qhull precision errors caught', end='\r')
    print(error_count, 'QH6154 Qhull precision errors caught', end='\n')
        
    return shape_lon_coords, shape_lat_coords, shape_colors