from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px

register_page(__name__, icon="fluent-mdl2:education")

layout = html.Div(
    [
        # dmc.Select(
        #     id="dropdown",
        #     data=[{"label": x, "value": x} for x in days],
        #     value=days[0],
        #     clearable=False,
        # ),
        # dcc.Graph(id="bar-chart"),
    ]
)

