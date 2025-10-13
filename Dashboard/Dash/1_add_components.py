# Load necessary libraries
import pandas as pd
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px

# Load data from CSV.
df = pd.read_csv('sales_data.csv')

# Setup the Dash app
app = Dash(__name__)

# Add a layout with a first component
app.layout = html.Div(style={'backgroundColor': '#f0f0f0', 'padding': '20px'}, children=[
    html.H1(
        children='Interactive Sales Dashboard', 
        # Inline styling applied to the H1
        style={
            'textAlign': 'center', 
            'color': '#333333',
            'fontFamily': 'Arial',
            'borderBottom': '2px solid #007bff',
            'paddingBottom': '10px'
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
