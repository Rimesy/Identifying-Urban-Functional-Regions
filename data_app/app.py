from dash import Dash, html, dcc, callback, Input, Output, State
import data_handling
import map_handling

app = Dash()

app.layout = [
    html.H1(children='Interactive Functional Region Map', style={'textAlign':'center'}),
    html.Label(children='Upload POI data:', id='POI_upload_label', style={'textAlign':'centre'}),
    dcc.Upload(id='POI_file_input', children=html.Button('Upload')), # Opens pop-up for upload when clicked
    html.Hr(), # Horizontal line
    dcc.Checklist(id = 'checklist', options = [
        {'label': 'Hide clusters', 'value': 'clusters'},
    ],
    value = ['clusters'],
    inline = True),
    html.Hr(),
    html.Div(id='data_output'), # Displays the data table
]

@callback(
    Output('data_output', 'children'),
    Input('POI_file_input', 'contents'),
    Input('checklist', 'value'),
    State('POI_file_input', 'filename'),
)

def update_output(contents, value, filename):
    if contents is not None:
        df = data_handling.parse_POI_contents(contents, filename) # Parse the POI data
        df = data_handling.clean_POI_data(df) # Clean the POI data
        df, cluster_data = data_handling.add_cluster_ids(df, 1) # Cluster POIs
        children = [map_handling.create_map(df, cluster_data, value, filename), data_handling.data_display(df, filename)]
        return children

if __name__ == '__main__':
    app.run(debug=True)
