from dash import Dash, html
from . import dropdown, year_dropdown, barchart, month_dropdown
import pandas as pd

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(), # divider line
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, data),
                    month_dropdown.render(app,data)
                ]
            ),
            barchart.render(app, data)
        ]
    )

