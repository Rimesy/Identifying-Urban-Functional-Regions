from dash import html, dash_table
import io
import base64
import pandas as pd

# Function parse_contents reads a file and strips it to leave the data we want to use
def parse_contents(contents, filename):
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

# Function data_table creates a visual data table to be displayed in the dash app
def data_table(df, filename):
    # Return a html <div> with the dash table nested
    return html.Div([
        html.H5(filename),

        # Display DataFrame as a table of i columns
        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        """ 
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        }) 
        """
    ])

# Function clean_POI_data takes the the data we need from the DataFrame and 
def clean_POI_data(df):
    # df.drop(columns=['B', 'C', 'D', 'E']) # Removes columns holding incomplete information
    df.rename(columns={'A': 'Unique Reference Number', 'B': 'Name', 'C': 'PointX Classification Code', 'D': 'Easting', 'E': 'Northing'}, inplace=True)
    df['Positional Accuracy code'] = None

    index_bin = [] # Bin for indexes that hold incomplete data, and therefore need to be removed
    for i in range(0, len(df.index)):
        line = df.at[i, 'Unique Reference Number'] # Create a String variable of the data in row i of the DataFrame
        data_list = line.split('|')
        if len(data_list) < 6:
            index_bin.append(i)
            continue
        # TODO: find way to iterate or condense the following crap
        df.at[i,'Unique Reference Number'] = data_list[0]
        df.at[i,'Name'] = data_list[1]
        df.at[i,'PointX Classification Code'] = data_list[2]
        df.at[i,'Easting'] = data_list[3]
        df.at[i,'Northing'] = data_list[4]
        df.at[i,'Positional Accuracy code'] = data_list[5]
    

    df.drop(index_bin) # Removes all rows with incomplete data

    return df
