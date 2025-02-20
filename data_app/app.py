from dash import Dash, html, dcc, callback, Input, Output, State
import plotly.express as px
import pandas as pd
import data_handling

app = Dash()

app.layout = [
    html.H1(children='Interactive Functional Region Map', style={'textAlign':'center'}),
    html.Label(children='Upload POI data:', id='file_upload_label', style={'textAlign':'centre'}),
    dcc.Upload(id='file_input', children=html.Button('Upload')),
    html.Div(id='data_output')
]

@callback(
    Output('data_output', 'children'),
    Input('file_input', 'contents'),
    State('file_input', 'filename')
)

def update_output(contents, filename):
    if contents is not None:
        df = data_handling.parse_contents(contents, filename)
        children = [data_handling.data_table(df, filename)]
        return children

if __name__ == '__main__':
    app.run(debug=True)
