from os import name
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import seaborn as sns
df = sns.load_dataset('tips')

app = dash.Dash()

day_options = []
for day in df['day'].unique():
    day_options.append({'label':str(day),'value':str(day)})


app.layout = html.Div([
    dcc.Graph(id ='graphwithslider'),
    dcc.Dropdown(id ='daypicker', options=day_options, value = 'Sun')
])

@app.callback(Output('graphwithslider', 'figure'),
             [Input('daypicker', 'value')])  
def update_figure(selected_day):
    df1 = df[df['day']==selected_day]
    data = [go.Scatter(x =df1['total_bill']
                        , y =df1['tip']
                        , text=df.time.astype("string") + "," + df.sex.astype("string")
                        , mode ='markers'
                        , marker=dict(size=df['total_bill'], color = df['size'], showscale=True))]
    return {'data':data
            ,'layout': go.Layout(title='Tips -versus- Total Bill'
	        ,xaxis = {'title':'TOTAL_BILL'}
            ,yaxis ={"title":"TIP"})    
    }

if __name__ == '__main__':
    app.run_server()