from dash import Dash, html
from . import dropdown

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(), # divider line
            html.Div(
                className="dropdown-container",
                children=[
                    dropdown.render(app)
                ]
            )
        ]
    )

