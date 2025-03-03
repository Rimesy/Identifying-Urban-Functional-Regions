from dash import html, dash_table
import io
import base64
import pyproj
import pandas as pd
import cluster

# Function parse_contents reads a file and strips it to leave the data we want to use
def parse_POI_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string) # Decodes the data with base64 

    # Allow three file types to be uploaded
    try:
        if 'csv' in filename: # .csv format
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename: # .xls format
            df = pd.read_excel(io.BytesIO(decoded))
        elif 'json' in filename: # .json format
            df = pd.read_json(io.StringIO(decoded.decode('utf-8')))
    except Exception as e:
        print(e)
        return html.Div(['There was an error processing this file.'])
    
    return df # df is DataFrame https://pandas.pydata.org/docs/reference/frame.html

# Function parse_map_contents converts a .tif file into a DataFrame
"""
def parse_map_contents(contents, filename):
    content_type, content_string = contents.split(',')

    dtm_pre_arr = rxr.open_rasterio(content_string, masked=True).squeeze().rio.reproject('EPSG:3857')
    converted_df = dtm_pre_arr.to_dataframe(name='map').reset_index()
    df = converted_df.dropna().reset_index(drop=True)

    return df
"""

# Function data_table creates a visual data table to be displayed in the dash app
def data_display(df, filename):
    # Return a html <div> with the dash table nested
    return html.Div([
        html.H5(filename),

        # Display DataFrame as a table of i columns
        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line
    ])

# Function clean_POI_data takes the the data we need from the DataFrame
def clean_POI_data(df):
    df.rename(columns={'A': 'unique reference number', 'B': 'name', 'C': 'pointX classification code', 'D': 'lon', 'E': 'lat'}, inplace=True)
    df['positional accuracy code'] = None # Add sixth column needed

    global index_bin
    index_bin = [] # Bin for indexes that hold incomplete data, and therefore need to be removed
    transformer = pyproj.Transformer.from_crs('EPSG:27700', 'EPSG:4326') # The transformer allows for BNG(27700) coordinates to be converted to Lat/Long(4326) coordinates

    for i in range(0, len(df.index)):
        line = df.at[i, 'unique reference number'] # Create a String variable of the data in row i of the DataFrame
        data_list = line.split('|') # Splits the row data into sections that we can store individually
        
        # This statement checks that all the necessary columns are present 
        if len(data_list) < 6:
            index_bin.append(i)
            df.drop([i], axis=0, inplace=True) # Removes row with incomplete data
            continue

        df.at[i, 'unique reference number'] = data_list[0]
        df.at[i, 'name'] = data_list[1]
        df.at[i, 'pointX classification code'] = data_list[2]

        lat, lon = transformer.transform(data_list[3], data_list[4])
        print('Uploaded ' + str(i) + '/' + str(len(df.index)) + ' rows', end='\r') # Sends a message to th terminal to show how quickly the rows are being cleaned

        df.at[i, 'lon'] = lon
        df.at[i, 'lat'] = lat
        df.at[i, 'positional accuracy code'] = data_list[5]

    print('Uploaded ' + str(i + 1) + '/' + str(len(df.index)) + ' rows', end='\n')

    return df

# Function classify_data returns the classification of a POI using its pointX code and a chosen levelof classification
def classify_data(level, pointX_code):
    from classification import groups, categories, classes

    try:
        if level == 1:
            return groups[pointX_code[:2]]
        elif level == 2:
            return categories[pointX_code[2:4]]
        elif level == 3:
            return classes[pointX_code[4:]]
    except Exception as e:
        print(e)

def add_cluster_ids(df, level):
    from classification import groups, categories, classes

    df['cluster id'] = None
    num_clusters = 0

    try:
        if level == 1:
            for group in groups:
                coord_array = []
                index_array = []

                for i in range(0, len(df.index)):
                    if (i not in index_bin) and (groups[group] == classify_data(1, df.at[i, 'pointX classification code'][:2])):
                        coord_array.append([float(df.at[i, 'lat']), float(df.at[i, 'lon'])])
                        index_array.append(i)

                cluster_ids = cluster.DBSCAN(coord_array)
                if -1 in cluster_ids: num_clusters += len(set(cluster_ids)) - 1
                elif -1 not in cluster_ids: num_clusters += len(set(cluster_ids))

                for i in range(0, len(index_array) - 1):
                    df.at[index_array[i], 'cluster id'] = cluster_ids[i] + num_clusters

            return df

        elif level == 2:

            pass
        elif level == 3:
            pass
    except Exception as e:
        print(e)

        return df

# Function add_cluster_ids makes an array of POI coordinates, passes them through the DBSCAN algorithm, and adds the rsulting cluster ids to the data table
"""
def add_cluster_ids(df, level):
    coord_array = []
    for i in range(0, len(df.index)):
        if i not in index_bin:
            coord_array.append([float(df.at[i, 'lat']), float(df.at[i, 'lon'])])
            print('Clustered ' + str(i) + '/' + str(len(df.index)) + ' rows', end='\r') # Sends a message to th terminal to show how quickly the rows are being clustered

    print('Clustered ' + str(i + 1) + '/' + str(len(df.index)) + ' rows', end='\r')
    
    cluster_ids = cluster.DBSCAN(coord_array)

    df['cluster id'] = None
    for i in range(0, len(df.index) - len(index_bin)):
        df.at[i, 'cluster id'] = cluster_ids[i]

    return df
"""