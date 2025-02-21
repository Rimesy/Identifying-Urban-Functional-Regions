from dash import Dash, html, dcc, callback, Input, Output, State
import data_handling

app = Dash()

app.layout = [
    html.H1(children='Interactive Functional Region Map', style={'textAlign':'center'}),
    html.Label(children='Upload POI data:', id='POI_upload_label', style={'textAlign':'centre'}),
    dcc.Upload(id='POI_file_input', children=html.Button('Upload')), # Opens pop-up for upload when clicked
    html.Hr(), # Horizontal line
    html.Div(id='data_output'), # Displays the data table
]

@callback(
    Output('data_output', 'children'),
    Input('POI_file_input', 'contents'),
    State('POI_file_input', 'filename'),    
)

def update_output(contents, filename):
    if contents is not None:
        df = data_handling.parse_POI_contents(contents, filename) # Parse the POI data
        df = data_handling.clean_POI_data(df) # Clean the POI data
        children = [data_handling.data_display(df, filename)] 
        return children

if __name__ == '__main__':
    app.run(debug=True)
