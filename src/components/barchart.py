from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from . import ids

SAMPLE_DATA = pd.read_csv('Finanacial_Dashboard/src/components/data/sample_data.csv')

def render(app: Dash) -> html.Div:
    fig = px.bar(SAMPLE_DATA, x="Housing", y="Transportation", color="Month", text="Month")
    return html.Div(
        dcc.Graph(figure=fig), id=ids.BAR_GRAPH
    )