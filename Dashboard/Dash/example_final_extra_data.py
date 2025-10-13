# Dash Example: 5 Steps to Build a Simple Interactive Dashboard
# 2nd version, updates:
# - with external CSS
# .css files will automatically be included from the assets directory (in alphanumerical order).

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
# This step loads the dataset at the start of the script, as a global variable.
# This ensures the data is loaded only once when the app starts,
# rather than on every user interaction.
# ---------------------------------------------------------------------------------
df = pd.read_csv('sales_data2.csv')

# ---------------------------------------------------------------------------------
# 0. Setup the Dash app
# ---------------------------------------------------------------------------------

app = Dash(__name__)

# ---------------------------------------------------------------------------------
# 1. The Dash Layout (Frontend Structure) & 3. Styling
# Defines the visual structure and uses external styling.
# ---------------------------------------------------------------------------------
app.layout = html.Div(className='main-container', children=[
    html.H1(
        children='Interactive Sales Dashboard',
        className='main-title'
    ),
    html.Div([
        html.Div([
            html.Label("Select Year:", className='dropdown-label'),
            dcc.Dropdown(
                id='year-selector',
                options=[{'label': str(y), 'value': y} for y in df['Year'].unique()],
                value=2021,
                className='year-dropdown'
            ),
        ], className='dropdown-container'),
        html.Div([
            html.Label("Select Period:", className='dropdown-label'),
            dcc.Dropdown(
                id='period-selector',
                options=[
                    {'label': 'Full Year', 'value': 'full'},
                    {'label': 'Q1 (Jan-Mar)', 'value': 'q1'},
                    {'label': 'Q2 (Apr-Jun)', 'value': 'q2'},
                    {'label': 'Q3 (Jul-Sep)', 'value': 'q3'},
                    {'label': 'Q4 (Oct-Dec)', 'value': 'q4'},
                ],
                value='full',
                className='year-dropdown'
            ),
        ], className='dropdown-container'),
        html.Div([
            html.Label("View:", className='dropdown-label'),
            dcc.RadioItems(
                id='view-selector',
                options=[
                    {'label': 'Single Year', 'value': 'single'},
                    {'label': 'Combined (All Years)', 'value': 'combined'}
                ],
                value='single',
                labelStyle={'display': 'inline-block', 'margin-right': '10px'},
                className='view-radio'
            ),
        ], className='radio-container'),
    ], className='dropdown-row'),
    dcc.Graph(id='main-data-graph')
])

# ---------------------------------------------------------------------------------
# 2. Interactivity: The Callback Mechanism (Backend Logic)
# Links the Dropdown (Input) to the Graph (Output).
# ---------------------------------------------------------------------------------
@callback(
    Output(component_id='main-data-graph', component_property='figure'),
    Input(component_id='year-selector', component_property='value'),
    Input(component_id='period-selector', component_property='value'),
    Input(component_id='view-selector', component_property='value')
)
def update_graph(selected_year, selected_period, selected_view):
    period_months = {
        'full': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'q1': ['Jan', 'Feb', 'Mar'],
        'q2': ['Apr', 'May', 'Jun'],
        'q3': ['Jul', 'Aug', 'Sep'],
        'q4': ['Oct', 'Nov', 'Dec'],
    }
    period_label = {
        'full': 'Full Year',
        'q1': 'Q1 (Jan-Mar)',
        'q2': 'Q2 (Apr-Jun)',
        'q3': 'Q3 (Jul-Sep)',
        'q4': 'Q4 (Oct-Dec)',
    }

    if selected_view == 'single':
        filtered_df = df[(df['Year'] == selected_year) & (df['Month'].isin(period_months[selected_period]))]
        fig = px.bar(
            filtered_df,
            x='Month',
            y='Sales',
            title=f"Sales for {selected_year} ({period_label[selected_period]})",
            color_discrete_sequence=['#007bff']
        )
    else:
        filtered_df = df[df['Month'].isin(period_months[selected_period])]
        fig = px.bar(
            filtered_df,
            x='Month',
            y='Sales',
            color='Year',
            barmode='group',
            title=f"Combined Sales for All Years ({period_label[selected_period]})"
        )
    return fig

# ---------------------------------------------------------------------------------
# 0. Run the app
# ---------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
