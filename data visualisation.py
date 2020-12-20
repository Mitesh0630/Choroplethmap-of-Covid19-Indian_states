# Note: """ is used for comment that particular function so if u want to use  variety of function u can use..by removing """
import json
import numpy as np
import pandas as pd
import plotly.express as px
india_states = json.load(open("states_india.geojson", "r")) #
state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

df = pd.read_csv("covid19.csv")
df["id"] = df["state_ut"].apply(lambda x: state_id_map[x])


fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color="active_cases",
    hover_name="state_ut",
    hover_data=["confirmed_cases", "active_cases" , "recovered_cases", "death_cases"],
    title="Indian_covid cases",
    color_continuous_scale="Viridis",
    color_continuous_midpoint=0,
    labels={"confirmed_cases","active_cases" , "recovered_cases", "death_cases"}
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(fitbounds="locations", visible=False)
fig.show()

                                                 #OR
 
"""fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color="recovered_cases",
    hover_name="state_ut",
    hover_data=["confirmed_cases", "active_cases" , "recovered_cases", "death_cases"],
    title="Indian_covid cases",
    color_continuous_scale=px.colors.sequential.Plasma,
    color_continuous_midpoint=0,
    labels={"confirmed_cases","active_cases" , "recovered_cases", "death_cases"}
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(fitbounds="locations", visible=False)
fig.show()"""

                                                      #OR
    

"""fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color="confirmed_cases",
    hover_name="state_ut",
    hover_data=["confirmed_cases", "active_cases" , "recovered_cases", "death_cases"],
    title="Indian_covid cases",
    color_continuous_scale=px.colors.diverging.BrBG,
    color_continuous_midpoint=0,
    labels={"confirmed_cases","active_cases" , "recovered_cases", "death_cases"}
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(fitbounds="locations", visible=False)
fig.show()"""
 
    
                                        #OR
    
    
"""fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color="death_cases",
    hover_name="state_ut",
    hover_data=["confirmed_cases", "active_cases" , "recovered_cases", "death_cases"],
    title="Indian_covid cases",
    color_continuous_scale=px.colors.diverging.BrBG,
    color_continuous_midpoint=0,
    labels={"confirmed_cases","active_cases" , "recovered_cases", "death_cases"}
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(fitbounds="locations", visible=False)
fig.show()"""




#USING MAPBOX FOR Customization

"""fig = px.choropleth_mapbox(
    df,
    locations="id",
    geojson=india_states,
    color="confirmed_cases",
    hover_name="state_ut",
    hover_data=["confirmed_cases","active_cases" , "recovered_cases", "death_cases"],
    title="Indian statewise covid cases",
    mapbox_style="carto-positron",
    color_continuous_scale=px.colors.diverging.BrBG,
    color_continuous_midpoint=0,
    center={"lat": 24, "lon": 78},
    zoom=4,
    opacity=1,
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()"""


