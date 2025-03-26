from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
from classification import color_map

# Function create_map creates a map figure with the POI data overlaid 
def create_map(poi_data, cluster_data, checklist_value, dropdown_value, filename):
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

    # Checks if the hide clusters checkbox is ticked
    if 'clusters' not in checklist_value:
        lons, lats, colors = cluster_data # Expands and assigns values from the cluster data
        for longitude, latitude, color in zip(lons, lats, colors):
            group = list(color_map.keys())[list(color_map.values()).index(color)]
            if ('All' in dropdown_value) or (group in dropdown_value):
                # Using add_trace allows multiple layers on the map
                fig.add_trace(
                    # go.scattermap is different from px.scatter_map, don't ask how, but go has the capability to draw and fill lines
                    go.Scattermap(mode = 'lines', fill = 'toself', line = {'color': color}, lon = longitude, lat = latitude, showlegend = False)) # Show legend is set to false so that the hover data for clusters is at a minimum
    # TODO: Show chosen layer of se data using Choropleth Map with go.Choropleth
    # Throughput html elements that display the map
    return html.Div([
        dcc.Graph(figure=fig),
        html.Hr(),  # Horizontal line
    ])