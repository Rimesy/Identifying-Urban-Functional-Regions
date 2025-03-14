from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import cluster
from classification import color_map

def create_shaded_regions(df, cluster_ids):
    cluster_shapes = []
    for id in set(cluster_ids):
        cluster_shapes.append([id, cluster.get_cluster_shape(df, id)])
    
    df_shapes = pd.DataFrame(data=cluster_shapes, columns=['id', 'north', 'south', 'east', 'west'])

# Function create_map creates a map figure with the POI data overlaid 
def create_map(poi_data, cluster_data, checklist_value, filename):
    # Use of scatter_map takes in data, column headings, as well as other styling, formatting parameters
    fig = px.scatter_map(poi_data, 
                         lat = 'lat', 
                         lon = 'lon', 
                         color = 'group', 
                         hover_name = 'name', 
                         hover_data = 'pointX classification code', 
                         color_discrete_map = color_map, 
                         zoom = 13, 
                         height = 600)
    fig.update_layout(map_style = "open-street-map") # The map figure uses the open street map base style
    fig.update_layout(margin = {"r":0,"t":0,"l":0,"b":0})

    if 'clusters' not in checklist_value:
        # TODO: Look at implementing geojson functionality
        lons, lats, colors = cluster_data
        for longitude, latitude, color in zip(lons, lats, colors):
            fig.add_trace(
                go.Scattermap(
            mode = 'lines', fill = 'toself', line = {'color': color},
            lon = longitude,
            lat = latitude,
            showlegend = False))

    # Throughput html elements that display the map
    return html.Div([
        dcc.Graph(figure=fig),
        html.Hr(),  # Horizontal line
    ])