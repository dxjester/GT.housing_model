import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go

raw = pd.read_csv('geo_df_export.csv')

raw.head(10)
raw.columns

splice = raw[['room_type', 'price']]
room_df = splice.groupby(['room_type']).mean().reset_index()
room_df.head(10)


splice2 = raw[['neighbourhood', 'price']]
neighbor_df = splice2.groupby(['neighbourhood']).mean().reset_index()
neighbor_df.head(10)

# create the dash object
app = dash.Dash()

app.layout = html.Div([
    
    # the container div    
    html.Div([
        
        # first  chart (top)
        html.Div([
            html.H3('AVG Price by Room Type'),
            dcc.Graph(id='g1', figure={'data': [go.Bar(
                            x = room_df['room_type'],
                            y = room_df['price'],
                            )
                    ],
                    'layout': go.Layout(
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )})
        ], className="six columns"),

        # second chart (bottom)
        html.Div([
            html.H3('AVG Price by Neighborhood'),
            dcc.Graph(id='g2', figure={'data': [go.Bar(
                            x = neighbor_df['neighbourhood'],
                            y = neighbor_df['price'],
                            )
                    ],
                    'layout': go.Layout(
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )})
        ], className="six columns"),
    ], 
    className="row")
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)