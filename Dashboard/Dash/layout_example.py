# Tutorial:
# https://medium.com/plotly/how-to-create-a-beautiful-interactive-dashboard-layout-in-python-with-plotly-dash-a45c57bb2f3c
# Tutorial focuses purely on the first step in dashboard creation: the layout design
#
# Code on Github: https://github.com/plotly/datasets/tree/master/dash-layout-tutorial
#
# Learn more about Dash HTML components here:
# https://dash.plotly.com/dash-html-components
#
# Another Dash tutorial "Getting Started With Dash: Easy Data Visualization In Python"
# https://www.youtube.com/watch?v=XOFrvzWFM7Y
#
# Dash documentation: https://dash.plotly.com/

# Import Dash core components and Bootstrap for styling
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Import Plotly for graphing, numpy for data, random for color selection
import plotly.graph_objects as go
import numpy as np
import random

# Initialize the Dash app and apply a Bootstrap theme for styling
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# Create a random scatter plot using Plotly
fig = go.Figure(
    go.Scattergl(
        x = np.random.randn(1000),
        y = np.random.randn(1000),
        mode='markers',
        marker=dict(color=random.sample(['#ecf0f1']*500 + ["#3498db"]*500, 1000), line_width=1)
    )
)
fig.update_layout(
    plot_bgcolor='#010103', width=790, height=730,
    xaxis_visible=False, yaxis_visible=False, showlegend=False,
    margin=dict(l=0,r=0,t=0,b=0)
)

"""
Define the layout of the dashboard using Dash HTML and Bootstrap components.
The layout consists of:
- A sidebar with title, description, radio buttons, buttons, dropdowns, and an image
- A main area with a graph and output sections
"""
app.layout = dbc.Container([
    # Sidebar section
    html.Div([
    # Title and description
    html.Div([
            html.H1([
                html.Span("Welcome"),
                html.Br(),
                html.Span("to my beautiful dashboard!")
            ]),
            html.
            P("This dashboard prototype shows how to create an effective layout."
              )
        ],
                 style={"vertical-alignment": "top", "height": 260}),
    # Controls: radio buttons and About button
    html.Div([
            html.Div(
                dbc.RadioItems(
                    className='btn-group',
                    inputClassName='btn-check',
                    labelClassName="btn btn-outline-light",
                    labelCheckedClassName="btn btn-light",
                    options=[
                        {"label": "Graph", "value": 1},
                        {"label": "Table", "value": 2}
                    ],
                    value=1,
                    style={'width': '100%'}
                ), style={'width': 206}
            ),
            html.Div(
                dbc.Button(
                    "About",
                    className="btn btn-info",
                    n_clicks=0
                ), style={'width': 104})
        ], style={'margin-left': 15, 'margin-right': 15, 'display': 'flex'}),
    # Dropdowns section
    html.Div([
            html.Div([
                html.H2('Unclearable Dropdown:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Option A', 'value': 1},
                        {'label': 'Option B', 'value': 2},
                        {'label': 'Option C', 'value': 3}
                    ],
                    value=1,
                    clearable=False,
                    optionHeight=40,
                    className='customDropdown'
                )
            ]),
            html.Div([
                html.H2('Unclearable Dropdown:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Option A', 'value': 1},
                        {'label': 'Option B', 'value': 2},
                        {'label': 'Option C', 'value': 3}
                    ],
                    value=2,
                    clearable=False,
                    optionHeight=40,
                    className='customDropdown'
                )
            ]),
            html.Div([
                html.H2('Clearable Dropdown:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Option A', 'value': 1},
                        {'label': 'Option B', 'value': 2},
                        {'label': 'Option C', 'value': 3}
                    ],
                    clearable=True,
                    optionHeight=40,
                    className='customDropdown'
                )
            ])
        ], style={'margin-left': 15, 'margin-right': 15, 'margin-top': 30}),
        # Sidebar image
        html.Div(
            html.Img(src='assets/image.svg',
                     style={'margin-left': 15, 'margin-right': 15, 'margin-top': 30, 'width': 310})
        )
    ], style={
        'width': 340,
        'margin-left': 35,
        'margin-top': 35,
        'margin-bottom': 35
    }),
    # Main content area: graph and outputs
    html.Div(
        [
            html.Div(
                dcc.Graph(
                    figure=fig
                ),
                     style={'width': 790}),
            html.Div([
                html.H2('Output 1:'),
                html.Div(className='Output'),
                html.H2('Output 2:'),
                html.Div(html.H3("Selected Value"), className='Output')
            ], style={'width': 198})
        ],
        style={
            'width': 990,
            'margin-top': 35,
            'margin-right': 35,
            'margin-bottom': 35,
            'display': 'flex'
        })
],
                           fluid=True,
                           style={'display': 'flex'},
                           className='dashboard-container')

# Run the Dash app in debug mode when this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
