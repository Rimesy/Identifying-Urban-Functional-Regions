# INFO: UPDATE DOCUMENTATION
from dash import Dash, html, dcc, callback, Input, Output, State
import data_handling
import map_handling

app = Dash()

app.layout = [
    html.H1(children='Interactive Functional Region Map'),
    html.Div([
        dcc.Upload(id='POI_file_input', children=html.Button('Choose file / Drag & drop', className='download-button'))# Opens pop-up for upload when clicked
    ], className='download-button-div'),

    # TODO: Change minimum POIs for clusters
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
    Input('POI_file_input', 'contents'),
    Input('checklist', 'value'),
    Input('dropdown', 'value'),
    Input('slider', 'value'),
    State('POI_file_input', 'filename'),
)

def update_output(contents, checklist, dropdown, slider, filename):
    if contents is not None:
        df = data_handling.parse_POI_contents(contents, filename) # Parse the POI data
        df = data_handling.clean_POI_data(df) # Clean the POI data
        df, cluster_data = data_handling.add_cluster_ids(df, 1, slider) # Cluster POIs
        
        children = [map_handling.create_map(df, cluster_data, checklist, dropdown, filename), data_handling.data_display(df, filename)]
        
        return children

if __name__ == '__main__':
    app.run(debug=True)
