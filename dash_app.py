from dash import Dash, dcc, html, Input, Output
import os
import plotly.express as px
from dash import dcc, html, Input, Output, no_update
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data/macros_dataset_images.csv")

color_sequence = [
    "#0077C9", # Fish
    "#8B4513", # Nuts
    "#F5E042", # Grains
    "#4EB265", # Vegetables
    "#FF0066", # Fruits
    "#9E005D", # Beans
    "#FFCF48", # Cheese
    "#6F6F6F", # Seeds
    "#EC7357", # Meat
    "#009E49", # Legumes
    "#00B6CB", # Shellfish & Mollusks
    "#F7E5D5", # Milk
    "#F8E9A1", # Eggs
    "#A5A052", # Soy Products
    "#FFC0CB", # Yogurts
    "#B2B2B2"  # Vegan Meat Substitute
]

# let's make a scatter plot of the fat_100g and the proteins_100g grouped by category_name
fig = px.scatter(df, 
    x = "fat_100g", 
    y = "proteins_100g", 
    color = "category_name", 
    hover_name = "food_name",
    size = "energy_100g", 
    title = "Fat vs Proteins (100g)", 
    labels =  {
        "fat_100g":"Fat (g)", 
        "proteins_100g":"Proteins (g)", 
        "energy_100g":"Energy (kcal)"},
    width = 1200, 
    height = 600, 
    color_discrete_sequence = color_sequence,
    custom_data = ["energy_100g", "image_url", "fat_100g", "proteins_100g", "energy_100g", "carbohydrates_100g", "category_name"],
    hover_data = {"image_url":True, "energy_100g":True})
# let's make the dots bigger
fig.update_traces(marker=dict(size=10))

fig.update_traces(hoverinfo="none", hovertemplate=None)

fig.update_layout(modebar_remove=['select', 'autoScale', 'lasso2d', "lasso"])
# change the default behavior to pan
fig.update_layout(dragmode="pan")

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Visualização de Informação"),
    html.H2("Por: Lucas Treuke"),
    dcc.Graph(id="graph", figure=fig, clear_on_unhover=True),
    dcc.Tooltip(id="graph-tooltip"),
], style={
    "font-family": "Helvetica, sans-serif",
    "margin": "10px",
})


@app.callback(
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "bbox"),
    Output("graph-tooltip", "children"),
    Input("graph", "hoverData"),
)
def display_hover(hoverData):
    if hoverData is None:
        return False, no_update, no_update

    pt = hoverData["points"][0]
    bbox = pt["bbox"]

    img_src = pt["customdata"][1]
    fat_100g = pt["customdata"][2]
    proteins_100g = pt["customdata"][3]
    energy_100g = pt["customdata"][4]
    carbohydrates_100g = pt["customdata"][5]
    category_name = pt["customdata"][6]
    name = pt["hovertext"]

    children = [
        html.Div(children=[
            html.H2(f"{name}", style={"color": "black", "font-family": "Arial"}),
            html.Img(src=img_src, style={"width": "100%"}),
            html.P(children=[
                html.Span("⬤  ", style={"color": color_sequence[pt["curveNumber"]]}),
                html.Span(f"{category_name}")
                ], style={"color":"#111", "font-family": "Arial", "margin-top":"3px", "border-top": "1px solid #888", "font-weight": "bold"}),
            html.P(f"Quantity: 100g",style={"color":"#333", "font-family": "Arial"}),
            html.P(f"Fat: {fat_100g}g",style={"color":"#333", "font-family": "Arial"}),
            html.P(f"Proteins: {proteins_100g}g",style={"color":"#333", "font-family": "Arial"}),
            html.P(f"Energy: {energy_100g}kcal",style={"color":"#333", "font-family": "Arial"}),
            html.P(f"Carbohydrates: {carbohydrates_100g}g",style={"color":"#333", "font-family": "Arial"})
        ],
        style={'width': '200px', 'white-space': 'normal'})
    ]

    return True, bbox, children



if __name__ == '__main__':
    app.run_server(port=8050, debug=False, dev_tools_ui=False, dev_tools_props_check=False)