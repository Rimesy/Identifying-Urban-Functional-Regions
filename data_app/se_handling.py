import pyproj
import cluster
import data_utilities

def clean_se_data(df):
    transformer = pyproj.Transformer.from_crs('EPSG:27700', 'EPSG:4326') # The transformer allows for BNG(27700) coordinates to be converted to Lat/Long(4326) coordinates

    df.rename(columns={'centroid_x': 'latitude', 'centroid_y': 'longitude'}, inplace=True)
    for i in range(0, len(df.index)):
        if df.at[i, 'census_geography'] != 'lsoa':
            df.drop([i])
            continue

        lat, lon = transformer.transform(df.at[i, 'latitude'], df.at[i, 'longitude'])
        df.at[i, 'longitude'] = lon
        df.at[i, 'latitude'] = lat      

        print('Uploaded ' + str(i) + '/' + str(len(df.index)) + ' rows', end='\r') # Sends a message to th terminal to show how quickly the rows are being cleaned

    print('Uploaded ' + str(i + 1) + '/' + str(len(df.index)) + ' rows', end='\n')

    return df

def get_layers(df):
    layers = list(df.columns.values)
    non_layers = ['area_code', 'area_name', 'census_geography', 'latitude', 'longitude']

    for val in non_layers:
        while val in layers:
            layers.remove(val)
    
    return layers