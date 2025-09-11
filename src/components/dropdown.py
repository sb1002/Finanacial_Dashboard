from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids

def render(app: Dash) -> html.Div:
    all_categories = ["Housing", "Transportation", "Food", "Utilities", "Clothing", "Health", "Insurance", "Household items", "Loans", "Investing", "Entertainment", "Other"]

    @app.callback(
        Output(ids.CATEGORY_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_CATEGORIES_BUTTON, "n_clicks")
    )

    def select_all_categories(_: int) -> list[str]:
        return all_categories

    return html.Div(
        children=[
            html.H6("Category"),
            dcc.Dropdown(
                id=ids.CATEGORY_DROPDOWN,
                options=[{"label": category, "value":category} for category in all_categories],
                value=all_categories,
                multi=True
            ),
            html.Button(
                id=ids.SELECT_ALL_CATEGORIES_BUTTON,
                className="dropdown-button",
                children=["Select All"]
            )
        ]
    )