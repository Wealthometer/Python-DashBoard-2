from dash import Dash, dcc, html, dash_table, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# ---------- SAMPLE DATA ----------
df = px.data.gapminder()  # built-in Plotly dataset
years = df['year'].unique()

# ---------- APP SETUP ----------
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Advanced Sample Dashboard"

# ---------- LAYOUT ----------
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("🌍 Global Data Dashboard", className="text-center text-primary mb-4"), width=12)
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("Select a Year:"),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(y), 'value': y} for y in years],
                value=2007,
                clearable=False
            )
        ], width=4)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-chart')
        ], width=6),
        dbc.Col([
            dcc.Graph(id='line-chart')
        ], width=6),
    ]),

    dbc.Row([
        dbc.Col([
            html.H5("Country Data Table", className="mt-4"),
            dash_table.DataTable(
                id='data-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=[],
                page_size=8,
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left'},
            )
        ], width=12)
    ])
], fluid=True)

# ---------- CALLBACKS ----------
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('line-chart', 'figure'),
     Output('data-table', 'data')],
    [Input('year-dropdown', 'value')]
)
def update_dashboard(selected_year):
    filtered_df = df[df['year'] == selected_year]

    bar_fig = px.bar(
        filtered_df,
        x='country',
        y='gdpPercap',
        color='continent',
        title=f"GDP per Capita by Country ({selected_year})"
    )

    line_fig = px.line(
        filtered_df,
        x='lifeExp',
        y='gdpPercap',
        color='continent',
        title=f"Life Expectancy vs GDP per Capita ({selected_year})",
        markers=True
    )

    return bar_fig, line_fig, filtered_df.to_dict('records')

# ---------- RUN APP ----------
if __name__ == '__main__':
    app.run(debug=True)
