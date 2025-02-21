from dash import Dash, html, dcc, callback, Input, Output, State
import plotly.express as px
import pandas as pd
import data_handling

app = Dash()

app.layout = [
    html.H1(children='Interactive Functional Region Map', style={'textAlign':'center'}),
    html.Label(children='Upload POI data:', id='POI_upload_label', style={'textAlign':'centre'}),
    dcc.Upload(id='POI_file_input', children=html.Button('Upload')),
    html.Hr(),
    html.Label(children='Upload Map (.tif):', id='map_upload_label', style={'textAlign':'centre'}),
    dcc.Upload(id='map_file_input', children=html.Button('Upload')),
    html.Hr(),
    html.Div(id='data_output'),
]

@callback(
    Output('data_output', 'children'),
    [Input('POI_file_input', 'contents'),
     Input('map_file_input', 'contents')],
    State('POI_file_input', 'filename'),
    
)

def update_output(contents, filename):
    if contents is not None:
        df = data_handling.parse_contents(contents, filename)
        df = data_handling.clean_POI_data(df)
        children = [data_handling.data_table(df, filename)]
        return children

if __name__ == '__main__':
    app.run(debug=True)
