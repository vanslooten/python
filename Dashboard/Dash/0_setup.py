# Load necessary libraries
import pandas as pd
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px

# Load data from CSV.
df = pd.read_csv('sales_data.csv')

# Setup the Dash app
app = Dash(__name__)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
