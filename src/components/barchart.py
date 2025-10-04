from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

from . import ids
from ..data.loader import DataSchema

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_GRAPH, "children"),
        Input(ids.YEAR_DROPDOWN, "value")
    )

    def update_bar_graph(years: list[str]) -> html.Div:
        FILTERED_DATA = data.query("year in @years")

        if FILTERED_DATA.shape[0] == 0:
            return html.Div("No data selected.",id=ids.BAR_GRAPH)

        def create_pivot_table() -> pd.DataFrame:
            pt = FILTERED_DATA.pivot_table(
                values=DataSchema.AMOUNT,
                index=[DataSchema.CATEGORY],
                aggfunc="sum",
                fill_value=0
            )
            return pt.reset_index().sort_values(DataSchema.AMOUNT, ascending=False)

        fig = px.bar(
            create_pivot_table(),
            x=DataSchema.CATEGORY,
            y=DataSchema.AMOUNT,
            color=DataSchema.CATEGORY
        )

        return html.Div(
            dcc.Graph(figure=fig), id=ids.BAR_GRAPH
        )
    return html.Div(id=ids.BAR_GRAPH)