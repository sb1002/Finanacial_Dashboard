from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout
from src.data.loader import load_transaction_data

DATA_PATH = "Finanacial_Dashboard/src/data/sample_data.csv"

def main() -> None:
    data = load_transaction_data(DATA_PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Financial Dashboard"
    app.layout = create_layout(app, data)
    app.run()

if __name__ == "__main__":
    main()