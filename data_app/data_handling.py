from dash import html, dash_table
import io
import base64
import pyproj
import pandas as pd

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
    
    return df # df is DataFrame (https://pandas.pydata.org/docs/reference/frame.html)

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

    index_bin = [] # Bin for indexes that hold incomplete data, and therefore need to be removed
    transformer = pyproj.Transformer.from_crs('EPSG:27700', 'EPSG:4326') # The transformer allows for BNG(27700) coordinates to be converted to Lat/Long(4326) coordinates

    for i in range(0, len(df.index)):
        line = df.at[i, 'unique reference number'] # Create a String variable of the data in row i of the DataFrame
        data_list = line.split('|') # Splits the row data into sections that we can store individually
        
        # This statement checks that all the necessary columns are present 
        if len(data_list) < 6:
            index_bin.append(i)
            continue

        df.at[i,'unique reference number'] = data_list[0]
        df.at[i,'name'] = data_list[1]
        df.at[i,'pointX classification code'] = data_list[2]

        lat, lon = transformer.transform(data_list[3], data_list[4])
        print('Uploaded ' + str(i) + '/' + str(len(df.index)) + ' rows', end='\r') # Sends a message to th terminal to show how quickly the rows are being cleaned

        df.at[i,'lon'] = lon
        df.at[i,'lat'] = lat
        df.at[i,'positional accuracy code'] = data_list[5]

    print('Uploaded ' + str(i + 1) + '/' + str(len(df.index)) + ' rows', end='\r')

    df.drop(index_bin) # Removes all rows with incomplete data

    return df
