# Run in Interactive Window for VSCode, can save output as j#Jupyter notebook
# Import required libraries
import pandas as pd
import plotly.graph_objects as px
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Read the airline data into pandas dataframe
spacex_df =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv')

# Create a dash application
app = dash.Dash(__name__)

app.layout = html.Div([dcc.Dropdown(id='site-dropdown',
                                    options=[
                                        {'label': 'All Sites', 'value': 'ALL'},
                                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                        {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
                                        ],value='ALL',
                placeholder="Launch Site selection",
                searchable='True'),
                html.Div(id='dd-output-container')
                ,
                dcc.RangeSlider(id='payload-slider',
                                    min=0, max=10000, step=1000,
                                    marks={0: '0',100: '100'},
                                    value=[min, max]),
                html.Div(id='dd-output-container')
                ]
                )

# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))

def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(data=filtered_df, values='class', 
        names='pie chart names', 
        title='title')
        return fig
    else:
        # return the outcomes pie-chart for a selected site

#@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
    #    [Input(component_id='site-dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value")])

# def get_scatter_chart(entered_site):
#     filtered_df = spacex_df
#     if entered_site == 'ALL':
#         fig = px.scatter(data=filtered_df, x='Payload Mass (kg)', y='class', 
#         names='scatter chart names', 
#         color = 'Booster Version Category',
#         title='title')
#         return fig
#     else:
#         fig = px.scatter(data=filtered_df[entered_site], x='Payload Mass (kg)', y='class', 
#         names='scatter chart names', 
#         color = 'Booster Version Category',
#         title='title')
#         return fig
        # return the outcomes piechart for a selected site

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)