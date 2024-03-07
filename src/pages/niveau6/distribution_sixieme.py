from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px

register_page(__name__, icon="fluent-emoji-high-contrast:world-map")
df = px.data.tips()
days = df.day.unique()

layout = html.Div(
    [

    ]
)

