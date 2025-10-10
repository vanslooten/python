# Dash Example: 5 Steps to Build a Simple Interactive Dashboard

# 5 steps:
# 0. Load necessary libraries, setup the app, and run the app
# 1. The Dash Layout (Frontend Structure)
# 2. Interactivity: The Callback Mechanism (Backend Logic)
# 3. Styling 
# 4. Data Flow (Load Data Once)

# ---------------------------------------------------------------------------------
# 0. Load necessary libraries
# ---------------------------------------------------------------------------------

import pandas as pd
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px

# ---------------------------------------------------------------------------------
# 4. Data Flow (Load Data Once)
# This step loads the dataset at the start of the script, as a gloval variable.
# This ensures the data is loaded only once when the app starts,
# rather than on every user interaction.
# ---------------------------------------------------------------------------------
df = pd.DataFrame({
    'Year': [2020, 2020, 2020, 2021, 2021, 2021],
    'Month': ['Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
    'Sales': [100, 150, 120, 200, 220, 250]
})

# ---------------------------------------------------------------------------------
# 0. Setup the Dash app
# ---------------------------------------------------------------------------------

app = Dash(__name__)

# ---------------------------------------------------------------------------------
# 1. The Dash Layout (Frontend Structure) & 3. Styling
# Defines the visual structure and uses inline styling.
# ---------------------------------------------------------------------------------
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
    ),
    
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='year-selector',
            # Dynamically populate options from the DataFrame for best practice
            options=[{'label': str(y), 'value': y} for y in df['Year'].unique()],
            value=2021,  # Set an initial value
            style={'width': '200px', 'marginTop': '5px'}
        ),
    ], style={'marginBottom': '20px'}),
    
    # dcc.Graph is the container for the visualization (Output)
    dcc.Graph(id='main-data-graph')
])

# ---------------------------------------------------------------------------------
# 2. Interactivity: The Callback Mechanism (Backend Logic)
# Links the Dropdown (Input) to the Graph (Output).
# ---------------------------------------------------------------------------------
@callback(
    # OUTPUT: The 'figure' property of the component with id='main-data-graph'
    Output(component_id='main-data-graph', component_property='figure'),
    # INPUT: The 'value' property of the component with id='year-selector'
    Input(component_id='year-selector', component_property='value')
)
def update_graph(selected_year):
    # The selected_year variable holds the 'value' from the dropdown
    
    # 1. Process Data (filter the global DataFrame 'df')
    filtered_df = df[df['Year'] == selected_year]
    
    # 2. Generate a Plotly figure
    fig = px.bar(
        filtered_df, 
        x='Month', 
        y='Sales', 
        title=f'Monthly Sales for {selected_year}',
        color_discrete_sequence=['#007bff']
    )
    
    # 3. Return the figure to the dcc.Graph component
    return fig

# ---------------------------------------------------------------------------------
# 0. Run the app
# ---------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
