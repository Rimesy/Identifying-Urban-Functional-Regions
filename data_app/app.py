from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash()

app.layout = [
    html.H1(children='Title', style={'textAlign':'center'}),
    html.Label(children='Select a file:', id='file_upload_label', style={'textAlign':'centre'}),
    dcc.Upload(id='file_input', children=html.Button('Upload'))
]

@callback(
    # Output('graph-content', 'figure'),
    Input('file_input', 'contents')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)
