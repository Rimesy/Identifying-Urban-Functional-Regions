# INFO: UPDATE DOCUMENTATION
from dash import Dash, html, dcc, callback, Input, Output, State
import pandas as pd
import data_utilities
import map_handling
import poi_handling
import se_handling

app = Dash(__name__, suppress_callback_exceptions=True)

layers = ['None']

app.layout = [
    html.H1(children='Interactive Functional Region Map'),
    html.Div([
        html.Div([
        dcc.Upload(id='poi_file_input', children=html.Button('Choose POI file / Drag & drop', className='upload-button'))# Opens pop-up for upload when clicked
        ], className='upload-button-div'),

        html.Div([
        dcc.Upload(id='se_file_input', children=html.Button('Choose Socio-Economic file / Drag & drop', className='upload-button'))# Opens pop-up for upload when clicked
        ], className='upload-button-div'),
        ], className='upload-div'),

    # TODO: Change minimum POIs for clusters
    # TODO: Add dropdown for se layers (multi=False)
    html.Div([
        html.Div([
            dcc.Checklist(id = 'checklist', options = [
            {'label': 'Hide clusters', 'value': 'clusters'},],
            value = [], # Default checklist has Hide clusters unticked
            inline = True),
        ], className='checklist-div'),

        html.Div([
            html.Label(children='Select which clusters are visible:', id='cluster_dropdown_label', style={'textAlign':'centre', 'margin-bottom':'5px'}),
            dcc.Dropdown(['All', 'Accommodation, eating and drinking', 'Commercial services', 'Attractions', 'Sport and entertainment', 'Education and health', 'Public Infrastructure', 'Manufacturing and production', 'Retail', 'Transport'], 'All', multi=True, id='cluster_dropdown'),
        ], className='dropdown-div'),
        
        html.Div([
            html.Label(children='Size of clusters:', id='slider_label', style={'textAlign':'centre', 'margin-bottom':'5px'}),
            dcc.Slider(0.0005, 0.005, 0.0005, value=0.001, marks=None, id='slider', className='slider',
                       tooltip={'placement': 'bottom', 'always_visible': True}),
        ], className='slider-div'),

        html.Div([
            html.Label(children='Select socio-economic layer:', id='layer_dropdown_label', style={'textAlign':'centre', 'margin-bottom':'5px'}),
            dcc.Dropdown(options=['None'], value='None', multi=False, id='layer_dropdown')
        ], className='dropdown-div'),
    ], className='toolbar-div'),

    html.Div(id='data_output', className='data-div'), # Displays the data table
    html.Div(id='which_layer'),
    html.H2(children='Made by Josh Rimes    2025'),
]

@callback(
    Output('data_output', 'children'),
    Output('layer_dropdown', 'options'),
    Input('poi_file_input', 'contents'),
    Input('se_file_input', 'contents'),
    Input('checklist', 'value'),
    Input('cluster_dropdown', 'value'),
    Input('layer_dropdown', 'value'), 
    Input('slider', 'value'),
    State('poi_file_input', 'filename'),
)
    

def update_output(poi_file_input, se_file_input, checklist, cluster_dropdown, layer_dropdown, slider, filename):
    data_output = None
    options = ['None']
    se_df = pd.DataFrame({'A' : []}) # TODO: Do the sme for poi_df?
    print('\n\nUpdating output:')
    if poi_file_input is not None:
        poi_df = data_utilities.parse_contents(poi_file_input, filename) # Parse the POI data
        poi_df = poi_handling.clean_POI_data(poi_df) # Clean the POI data
        poi_df, cluster_data = poi_handling.add_cluster_ids(poi_df, 1, slider) # Cluster POIs
    
        if se_file_input is not None:
            se_df = data_utilities.parse_contents(se_file_input, 'file.csv')
            se_df = se_handling.clean_se_data(se_df)
            options = se_handling.get_layers(se_df)

        data_output = [map_handling.create_map(poi_df, cluster_data, checklist, cluster_dropdown, se_df, layer_dropdown, filename), data_utilities.data_display(poi_df, filename)]
        
    
    return data_output, options
    
    

if __name__ == '__main__':
    app.run(debug=True)
