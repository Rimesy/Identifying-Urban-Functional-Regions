# INFO: UPDATE DOCUMENTATION
from dash import Dash, html, dcc, callback, Input, Output, State
import data_utilities
import map_handling
import poi_handling

app = Dash()

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
            html.Label(children='Select which clusters are visible:', id='dropdown_label', style={'textAlign':'centre', 'margin-bottom':'5px'}),
            dcc.Dropdown(['All', 'Accommodation, eating and drinking', 'Commercial services', 'Attractions', 'Sport and entertainment', 'Education and health', 'Public Infrastructure', 'Manufacturing and production', 'Retail', 'Transport'], 'All', multi=True, id='dropdown'),
        ], className='dropdown-div'),
        
        html.Div([
            html.Label(children='Size of clusters:', id='slider_label', style={'textAlign':'centre', 'margin-bottom':'5px'}),
            dcc.Slider(0.0005, 0.005, 0.0005, value=0.001, marks=None, id='slider', className='slider',
                       tooltip={'placement': 'bottom', 'always_visible': True}),
        ], className='slider-div'),
    ], className='toolbar-div'),

    html.Div(id='data_output', className='data-div'), # Displays the data table

    html.H2(children='Made by Josh Rimes    2025'),
]

@callback(
    Output('data_output', 'children'),
    Input('poi_file_input', 'contents'),
    Input('se_file_input', 'contents'),
    Input('checklist', 'value'),
    Input('dropdown', 'value'),
    Input('slider', 'value'),
    State('poi_file_input', 'filename'),
)

def update_output(poi_file_input, se_file_input, checklist, dropdown, slider, filename):
    if poi_file_input is not None:
        df = data_utilities.parse_contents(poi_file_input, filename) # Parse the POI data
        df = poi_handling.clean_POI_data(df) # Clean the POI data
        df, cluster_data = poi_handling.add_cluster_ids(df, 1, slider) # Cluster POIs
        
        children = [map_handling.create_map(df, cluster_data, checklist, dropdown, filename), data_utilities.data_display(df, filename)]
        
        return children

if __name__ == '__main__':
    app.run(debug=True)
