from dash import html
import plotly.express as px

# Function create_map creates a map figure with the POI data overlaid 
def create_map(poi_data, filename):
    # Use of scatter_map takes in data, column headings, as well as other styling, formatting parameters
    fig = px.scatter_map(poi_data, lat = 'lat', lon = 'lon', hover_name = 'name', hover_data = ['unique reference number', 'pointX classification code'], color_discrete_sequence = ['blue'], zoom = 12, height = 600)
    fig.update_layout(map_style = "open-street-map") # The map figure uses the open street map base style
    fig.update_layout(margin = {"r":0,"t":0,"l":0,"b":0})

    # Throughput html elements that display the map
    return html.Div([
        html.H5(filename),

        fig.show(),

        html.Hr(),  # Horizontal line
    ])