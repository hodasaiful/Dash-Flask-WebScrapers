'''
This a plotly Dash web app; that extracts the close px through yahoo api and publishes line chart .
The date range can be selected from the drop down and one or more tickers listed on the HK Ex, ASX and NSE can be passsed as a parameter.
'''

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

server = app.server

nsdq = pd.read_csv('https://docs.google.com/spreadsheets/d/' + '1-caZGmeKiiynXYf8FRUB6_VXw3dBAHRPCzc1csFtmug' + '/export?gid=120896742&format=csv')
nsdq.set_index('Symbol',inplace=True)
options =[]

for tic in nsdq.index:
    options.append({'label':'{} {}'.format(tic,nsdq.loc[tic]['Name']), 'value':tic})

colors = {
    'background': 'lightcyan',
    'text': 'black',
    'text1': 'blue'
}


app.layout = html.Div([
                    html.H1('CLOSE PRICE LINE CHART', style={'backgroundColor':colors['background'], 'color':colors['text']}),
                    html.Div([html.H3('ENTER THE RIC (TICKER)',style ={'paddingRight':'30px'}),
                    dcc.Dropdown(
                            id='my_stock_picker',
                            options = options,
                            value =['00001.HK'],
                            multi=True
                            #style={'fontsize':24,'width':75}
                    )], style={'display':'inline-block','verticalAlign':'top','color':colors['text1']}),
                    html.Div([html.H3('ENTER START AND END DATES'),
                            dcc.DatePickerRange(id='my_date_picker',
                                                min_date_allowed=datetime(2015,1,1),
                                                max_date_allowed=datetime.today(),
                                                start_date=datetime(2018,1,1),
                                                end_date=datetime.today()
                            )
                    ],style={'display':'inline-block','width':'30%', 'color':colors['text1']}),
                    html.Div([
                            html.Button(id='sumbit-button',
                                        n_clicks=0,
                                        children='Submit',
                                        style={'fontSize':24,'marginLeft':'30px','color':colors['text']}
                            )
                    ],style={'display':'inline-block'}),

                    dcc.Graph(id='my_graph',
                                figure={'data':[
                                        {'x':[1,2],'y':[3,1]}
                                ],'layout':{'title':'Close Price'}}
                    )
], style={'backgroundColor': colors['background']})
@app.callback(
            Output('my_graph','figure'),
            [Input('sumbit-button','n_clicks')],
            [State('my_stock_picker','value'),
                State('my_date_picker','start_date'),
                State('my_date_picker','end_date')
            ])
def update_graph(n_clicks,stock_ticker,start_date,end_date):
    start =datetime.strptime(start_date[:10],'%Y-%m-%d')
    end =datetime.strptime(end_date[:10],'%Y-%m-%d')

    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic,'yahoo',start,end)
        traces.append({'x':df.index,'y':df['Adj Close'],'name':tic})
    fig = {'data':traces,
            'layout':{'title':stock_ticker}
    }
    return fig


if __name__ == '__main__':
    app.run_server()