from dash import Dash, html, dcc
from . import ids

def render(app: Dash) -> html.Div:
    all_categories = ["Housing", "Transportation", "Food", "Utilities", "Clothing", "Health", "Insurance", "Household items", "Loans", "Investing", "Entertainment", "Other"]
    return html.Div(
        children=[
            html.H6("Category"),
            dcc.Dropdown(
                id=ids.CATEGORY_DROPDOWN,
                options=[{"label": category, "value":category} for category in all_categories],
                value=all_categories,
                multi=True
            )
        ]
    )