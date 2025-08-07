from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data': [
                    {
                        'x': [1, 4, 9],
                        'y': [4, 9, 2],
                        'type': 'bar',
                        'name': 'Bar chart'
                    },
                    {
                        'x': [1, 6, 16],
                        'y': [2, 4, 9],
                        'type': 'line',  # changed to a line chart
                        'name': 'Line chart'
                    }
                ],
                'layout': {
                    'title': 'Graph title',
                    'xaxis': {'title': 'x-axis'},
                    'yaxis': {'title': 'y-axis'},
                }
            }
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)  # <-- updated for Dash v3+
