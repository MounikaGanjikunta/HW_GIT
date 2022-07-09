import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
import pandas as pd
from dash.dependencies import Output, Input
import math
import statistics
import plotly.express as px
import numpy as np


df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
df7 = pd.read_excel("data.xlsx", sheet_name="Sheet2")
df8 = pd.read_excel("data.xlsx", sheet_name="Sheet3")



x = ()
# New_x = []* 4;
# y = []* 4;
# y = 0

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.GRID])
server = app.server

# options = ['No Pack', 'LDPE', 'PP', 'PEN', 'ML', 'SHELL']

app.layout = html.Div([
    dbc.Row(dbc.Col(html.H2("PECAN WEBSITE"), width={'offset':5})),
    dcc.Tabs(
        id="tabs-with-classes",
        value='tab-2',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Color',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Texture',
                value='tab-2', className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Lipid Oxidation - FFA',
                value='tab-3',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Lipid Oxidation - AV',
                value='tab-4',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Sensory -1',
                value='tab-5',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Sensory -2',
                value='tab-6',
                className='custom-tab',
                selected_className='custom-tab--selected'
            )
        ]),
    html.Div(id='tabs-content-classes')
])

@app.callback(Output('tabs-content-classes', 'children'),
              Input('tabs-with-classes', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        #df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
        return html.Div([
        #    dbc.Row(dbc.Col(html.H2("PECAN WEBSITE"), width={'offset':5})),
html.Br(),
html.Br(),
html.Br(),
 dbc.Row(
 [dbc.Col(children=[html.Label(['Package:'], style={'font-weight': 'bold', "text-align": "center", 'display': 'inline-block'}),
 dcc.Dropdown(options=[{'label':pac, 'value':pac} for pac in sorted (df.Package.unique())],id='package1_choice', multi=False,disabled=False, clearable=True, searchable=True, placeholder='Choose Package...', className='form-dropdown', style={'width':"100%"}#, persistence='string'#, persistence_type='memory'
 )
 ], width={'size':2, 'offset':1}),
 dbc.Col(children=[html.Label(['Condition:'],style={'font-weight': 'bold', "text-align": "center", 'display': 'inlineblock'}),
 dcc.Dropdown(id='cond_choice', options=[{'label':con, 'value':con} for con in sorted (df.Condition.unique())], multi=False, disabled=False,
 clearable=True, searchable=True, placeholder='Choose condition...'#, persistence='string'
 , style={'width':"100%"}
 #,persistence_type='memory'
 ),
 ],width={'size':2}),
 dbc.Col(children = [html.Label(('Temperature (°C)'),style={'width': '200px','margin-left': 200,'font-weight': 'bold'}),
 dcc.Input(id="input_temp", type="number",value = 20,disabled = "False", placeholder="",style={'width': '100px'}),
 
 ]),
 dbc.Col(children = [html.Label('RH (%)'),dcc.Input(id="input1_RH",value = 30, type="number",disabled = "False", placeholder="",style={'width': '100px'}),])

 ]),

 dbc.Row([
 dbc.Col(dcc.Graph(id='our_graph',config = {'scrollZoom' : True,
                                                    'doubleClick' : 'reset'
                                                         }
 ), width={'size':4}),

 dbc.Col(dcc.Graph(id='our_graph1',config = {'scrollZoom' : True,
                                                    'doubleClick' : 'reset'
                                                         }
 ), width={'size':4}),

 dbc.Col(dcc.Graph(id='our_graph2',config = {'scrollZoom' : True,
                                                    'doubleClick' : 'reset'
                                                         }
 ), width={'size':4})

 
        ]),
 
        ])

    elif tab == 'tab-2':
        
        return html.Div([
        #    dbc.Row(dbc.Col(html.H2("PECAN WEBSITE"), width={'offset':5})),
html.Br(),
html.Br(),
html.Br(),
 dbc.Row(
 [dbc.Col(children=[html.Label(['Package:'], style={'font-weight': 'bold', "text-align": "center", 'display': 'inline-block'}),
 dcc.Dropdown(options=[{'label':pac, 'value':pac} for pac in sorted (df8.Package.unique())],id='package2_choice', multi=False,disabled=False, clearable=True, searchable=True, placeholder='Choose Package...', className='form-dropdown', style={'width':"100%"}#, persistence='string'#, persistence_type='memory'
 )
 ], width={'size':2, 'offset':1}),

 dbc.Col(children = [html.Label('RH (%)'),dcc.Input(id="input2_RH",value = 60, type="number",max = 80, placeholder="",style={'width': '100px'}),])

 ]),

 dbc.Row([
 dbc.Col(dcc.Graph(id='our_graph7',config = {'scrollZoom' : True,
                                                    'doubleClick' : 'reset'
                                                         }
 ), width={'size':4}),


        ]),
        ])

    elif tab == 'tab-3':
        #df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
        return html.Div([
        #    dbc.Row(dbc.Col(html.H2("PECAN WEBSITE"), width={'offset':5})),
html.Br(),
html.Br(),
html.Br(),
 dbc.Row(
 [dbc.Col(children=[html.Label(['Package:'], style={'font-weight': 'bold', "text-align": "center", 'display': 'inline-block'}),
 dcc.Dropdown(options=[{'label':pac, 'value':pac} for pac in sorted (df.Package.unique())],id='package3_choice', multi=False,disabled=False, clearable=True, searchable=True, placeholder='Choose Package...', className='form-dropdown', style={'width':"100%"}#, persistence='string'#, persistence_type='memory'
 )
 ], width={'size':2, 'offset':1}),
 dbc.Col(children=[html.Label(['Condition:'],style={'font-weight': 'bold', "text-align": "center", 'display': 'inlineblock'}),
 dcc.Dropdown(id='cond3_choice', options=[{'label':con, 'value':con} for con in sorted (df.Condition.unique())], multi=False, disabled=False,
 clearable=True, searchable=True, placeholder='Choose condition...'#, persistence='string'
 , style={'width':"100%"}
 #,persistence_type='memory'
 ),
 ],width={'size':2}),
 dbc.Col(children = [html.Label(('Temperature (°C)'),style={'width': '200px','margin-left': 200,'font-weight': 'bold'}),
 dcc.Input(id="input_temp3", type="number",value = 20,disabled = "False", placeholder="",style={'width': '100px'}),
 
 ]),
 dbc.Col(children = [html.Label('RH (%)'),dcc.Input(id="input3_RH",value = 30, type="number",disabled = "False", placeholder="",style={'width': '100px'}),])

 ]),

 dbc.Row([
 dbc.Col(dcc.Graph(id='our_graph4',config = {'scrollZoom' : True,
                                                    'doubleClick' : 'reset'
                                                         }
 ), width={'size':4}),


        ]),
 
        ])
    
    elif tab == 'tab-4':
        #df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
        return html.Div([
        #    dbc.Row(dbc.Col(html.H2("PECAN WEBSITE"), width={'offset':5})),
html.Br(),
html.Br(),
html.Br(),
 dbc.Row(
 [dbc.Col(children=[html.Label(['Package:'], style={'font-weight': 'bold', "text-align": "center", 'display': 'inline-block'}),
 dcc.Dropdown(options=[{'label':pac, 'value':pac} for pac in sorted (df7.Package.unique())],id='package4_choice', multi=False,disabled=False, clearable=True, searchable=True, placeholder='Choose Package...', className='form-dropdown', style={'width':"100%"}#, persistence='string'#, persistence_type='memory'
 )
 ], width={'size':2, 'offset':1}),
 dbc.Col(children=[html.Label(['Condition:'],style={'font-weight': 'bold', "text-align": "center", 'display': 'inlineblock'}),
 dcc.Dropdown(id='cond4_choice', options=[{'label':con, 'value':con} for con in sorted (df.Condition.unique())], multi=False, disabled=False,
 clearable=True, searchable=True, placeholder='Choose condition...'#, persistence='string'
 , style={'width':"100%"}
 #,persistence_type='memory'
 ),
 ],width={'size':2}),
 dbc.Col(children = [html.Label(('Temperature (°C)'),style={'width': '200px','margin-left': 200,'font-weight': 'bold'}),
 dcc.Input(id="input_temp4", type="number",value = 20,disabled = "False", placeholder="",style={'width': '100px'}),
 
 ]),
 dbc.Col(children = [html.Label('RH (%)'),dcc.Input(id="input4_RH",value = 30, type="number",disabled = "False", placeholder="",style={'width': '100px'}),])

 ]),

 dbc.Row([
 dbc.Col(dcc.Graph(id='our_graph5',config = {'scrollZoom' : True,
                                                    'doubleClick' : 'reset'
                                                         }
 ), width={'size':4}),


        ]),])

    elif tab == 'tab-5':
        return  html.Div(
    [
        # html.I("Try typing in input 1 & 2, and observe how debounce is impacting the callbacks. Press Enter and/or Tab key in Input 2 to cancel the delay"),
        html.Br(),
        html.Br(),
        html.Label('2-Decenal (ppm)'),
        dcc.Input(id="input1", type="number",value = 1, placeholder="", style={'marginRight':'10px'}),
        html.Br(),
        html.Br(),
        html.Label('2-Octenal (ppm)'),
        dcc.Input(id="input2", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('3,5-Octadien-2-ol (ppm)'),
        dcc.Input(id="input3", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('D-Limonene (ppm)'),
        dcc.Input(id="input4", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('Decanal (ppm)'),
        dcc.Input(id="input5", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('Nonanoic acid, methyl ester (ppm)'),
        dcc.Input(id="input6", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('Octanoic acid (ppm)'),
        dcc.Input(id="input7", type="number",value = 1, placeholder="", debounce=True),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Label('Freshness is:'),
        html.Br(),html.Br(),
        html.Div(id="output", title = "Freshness"),
        # html.Div(id="output"),
    ]
)
    elif tab == 'tab-6':
        return  html.Div(
    [
        # html.I("Try typing in input 1 & 2, and observe how debounce is impacting the callbacks. Press Enter and/or Tab key in Input 2 to cancel the delay"),
        html.Br(),
        html.Br(),
        html.Label('1-Hexanol (ppm)'),
        dcc.Input(id="input11", type="number",value = 1, placeholder="", style={'marginRight':'10px'}),
        html.Br(),
        html.Br(),
        html.Label('1-Nonanol (ppm)'),
        dcc.Input(id="input21", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('1-Octanol (ppm)'),
        dcc.Input(id="input31", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('1-Octen-3-ol (ppm)'),
        dcc.Input(id="input41", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('1-Pentanol (ppm)'),
        dcc.Input(id="input51", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('2-Heptenal (ppm)'),
        dcc.Input(id="input61", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('2-Nonenal (ppm)'),
        dcc.Input(id="input71", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('Heptanal (ppm)'),
        dcc.Input(id="input81", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('Hexanal (ppm)'),
        dcc.Input(id="input91", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('Nonanal (ppm)'),
        dcc.Input(id="input10", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('Nonanoic acid (ppm)'),
        dcc.Input(id="input11", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('Octanal (ppm)'),
        dcc.Input(id="input12", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('γ-Ethylbutyrolactone (ppm)'),
        dcc.Input(id="input13", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('γ-Heptalactone (ppm)'),
        dcc.Input(id="input14", type="number",value = 1, placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.Label('γ-Octalactone (ppm)'),
        dcc.Input(id="input15", type="number",value = 1, placeholder="", debounce=True),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Label('Oxidized rancid is:'),
        html.Br(),html.Br(),
        html.Div(id="output1", title = "Freshness"),
        # html.Div(id="output"),
    ]
)
        
@app.callback(
    Output('output', 'children'),
    [Input('input1', 'value'),
     Input('input2', 'value'),
     Input('input3', 'value'),
     Input('input4', 'value'),
     Input('input5', 'value'),
     Input('input6', 'value'),
     Input('input7', 'value')
    ]   
     
)
def update_result(x, y,z,a,b,c,d):


    H1_1_1 = math.tanh((-0.376000041896169  -0.00121483599711933 * x  -0.00424027352264225 * y  -0.0169010946203407 * z + 0.325526842450921 * a  -0.00897247542042462 * b  -0.00815749991989946 * c  -0.000872161596031972 * d))

    H1_2_1 = math.tanh((9.84930622664092  -0.00152074301719317 * x + 0.000366305845122697 * y  -0.0322465884460055 * z  -0.312140770495709 * a  -0.00192867524284899 * b - 0.00489387953974222 * c + 0.000189481981031619 * d))

    H1_3_1 = 3.15471456978145  -0.00221384277901096 * x  -0.00112788020464943 * y  -0.0223335123621844 * z + 0.0180425112149568 * a  -0.00546841314858246 * b  -0.00690744812389907 * c  -0.000621697977842283 * d

    H1_4_1 = -7.66953150086577 + 0.0040398689509179 * x  -0.00060757972826357 * y + 0.0116099371294885 * z + 0.211562579649623 * a  -0.00833225601148325 * b + 0.0088887605977188 * c + 0.00246098562164973 * d

    x = 5.25218443112124 + 3.20164352040782 * H1_1_1  -0.975887980678915 * H1_2_1  -0.0449908554892682 * H1_3_1  -0.0978906703340289 * H1_4_1

    html.Label('Freshness')
    return (x)

@app.callback(
    Output('output1', 'children'),
    [Input('input11', 'value'),
     Input('input21', 'value'),
     Input('input31', 'value'),
     Input('input41', 'value'),
     Input('input51', 'value'),
     Input('input61', 'value'),
     Input('input71', 'value'),
     Input('input81', 'value'),
     Input('input91', 'value'),
     Input('input10', 'value'),
     Input('input11', 'value'),
     Input('input12', 'value'),
     Input('input13', 'value'),
     Input('input14', 'value'),
     Input('input15', 'value')
    ]   
     
)
def update_result(x, y,z,a,b,c,d,e,f,g,h,i,j,k,l):


    H1_1_1 = np.exp(-((0.5 * pow((-2.15054891798031 + 0.00252530082846938 * x + 0.00037907179787616 * y + 0.00015641134333561 * z + 0.00469207240285138 * a+ 0.00116071810871887 * b + -0.00401650818420952 * c + 0.00286598112486275 * d + -0.0044926109394878 * e + -0.000636887073973106 * f + 0.0000721833626853219 * g + 0.0000368991799851018 * h + 0.000570402551715885 * i + -0.00115280366978597 * j + -0.00853116002303215 * k + 0.000382946422897931 * l), 2))))

    H1_2_1 = np.exp(-((0.5 * pow((0.857964930981078 + -0.00249671426788148 * x + 0.00302213974282116 * y + -0.000465912036417836 * z + 0.000811044532222994 * a + -0.000413443379525054 * b + -0.00699777262703118 * c + -0.00235060950161139 * d + 0.00311503800210337 * e + 0.0000425017091181601 * f + -0.000114755581921628 * g + -0.0000885464446689588 * h + -0.0000827216691497593 * i + -0.000692800145125753 * j + 0.00221052655480304 * k + 0.000275590080835825 * l), 2))))

    H1_3_1 = np.exp(-((0.5 * pow((-0.30586125568954 + 0.000053287030472495 * x + 0.00244703614991901 * y + 0.000856637512176449 * z + 0.00434404473428617 * a + -0.000283695842714195 * b + -0.00122907049387424 * c + -0.00236326288381088 * d + 0.0028729732548199 * e + -0.000486419178513323 * f + -0.0000263808500402225 * g + -0.000466604049926273 * h + -0.00067753259011681 * i + -0.000239736856666679 * j + -0.00316438037523924 * k + 0.000951249174890676 * l), 2))))

    x = 14.1382036166193 + 2.99080457886999 * H1_1_1 + -1.21142492859986 * H1_2_1 + -12.8224465257989 * H1_3_1

    

    
    return (x)


# for dependant dropdowns in tab 1
@app.callback(
 Output('cond_choice','options'),
 [Input('package1_choice','value')]
)
def build_graph(chosen_pac):
 dff = df[(df.Package == chosen_pac)]
 return [{'label':p, 'value':p} for p in (dff.Condition.unique())]

 # for dependant dropdowns in tab 3
@app.callback(
 Output('cond3_choice','options'),
 [Input('package3_choice','value')]
)
def build_graph(chosen_pac):
 dff = df[(df.Package == chosen_pac)]
 return [{'label':p, 'value':p} for p in (dff.Condition.unique())]

 # for dependant dropdowns in tab 4
@app.callback(
 Output('cond4_choice','options'),
 [Input('package4_choice','value')]
)
def build_graph(chosen_pac):
 dfff = df7[(df7.Package == chosen_pac)]
 return [{'label':p, 'value':p} for p in (dfff.Condition.unique())]


### for setting min and max values for text boxes in tab 1
@app.callback(Output('input1_RH', 'min'),
              [Input('package1_choice', 'value')])
def update_slider_example_min(input):   
        dff = df[df.Package == input]
        min_value = min(dff.RH_min)
        return min_value


@app.callback(Output('input1_RH', 'max'),
              [Input('package1_choice', 'value')])
def update_slider_example_max(input):
        dff = df[df.Package == input]
        # if chosen_package == "No Pack":
        #     max_value = max(dff.RH_max) 
            
        #     return [max_value]
        # else:
        #     max_value = max(dff.RH_max)
        #     return max_value
        max_value = max(dff.RH_max)
        return max_value


@app.callback(Output('input1_RH', 'value'),
              [Input('select-keeper', 'min'),
               Input('select-keeper', 'max'),
               Input('package1_choice', 'value')])
def update_slider_example_value(min_value, max_value,input):
        dff = df[df.Package == input]
        value_package = input
        if value_package == 'No Pack':
            # print(value_package,"Value package in callback")
            return [min_value, (max_value + 10)]
        else:
            return [min_value, max_value]


### for setting min and max values for text boxes in tab 3
@app.callback(Output('input3_RH', 'min'),
              [Input('package3_choice', 'value')])
def update_slider_example_min(input):   
        dff = df[df.Package == input]
        min_value = min(dff.RH_min)
        return min_value


### for setting min and max values for text boxes in tab 3
@app.callback(Output('input3_RH', 'max'),
              [Input('package3_choice', 'value')])
def update_slider_example_max(input):
        dff = df[df.Package == input]
        max_value = max(dff.RH_max)
        return (max_value)



### for setting min and max values for text boxes in tab 3
@app.callback(Output('input3_RH', 'value'),
              [Input('select-keeper', 'min'),
               Input('select-keeper', 'max')])
def update_slider_example_value(min_value, max_value): 
        return [min_value, max_value]

### for setting min and max values for text boxes in tab 4
@app.callback(Output('input4_RH', 'min'),
              [Input('package4_choice', 'value')])
def update_slider_example_min(input):   
        dfff = df7[df7.Package == input]
        min_value = min(dfff.RH_min)
        return min_value


### for setting min and max values for text boxes in tab 4
@app.callback(Output('input4_RH', 'max'),
              [Input('package4_choice', 'value')])
def update_slider_example_max(input):
        dfff = df7[df7.Package == input]
        max_value = max(dfff.RH_max)
        return (max_value)



### for setting min and max values for text boxes in tab 4
@app.callback(Output('input4_RH', 'value'),
              [Input('select-keeper', 'min'),
               Input('select-keeper', 'max')])
def update_slider_example_value(min_value, max_value): 
        return [min_value, max_value]

# for setting min and max values for temp in tab 1

@app.callback(Output('input_temp', 'min'),
              [Input('package1_choice', 'value')])
def update_slider_example_min(input):   
        dff = df[df.Package == input]
        min_value = min(dff.Temp_min)
        return min_value

@app.callback(Output('input_temp', 'max'),
              [Input('package1_choice', 'value')])
def update_slider_example_max(input):
        dff = df[df.Package == input]
        max_value = max(dff.Temp_max)
        return max_value

@app.callback(Output('input_temp', 'value'),
              [Input('select-keeper', 'min'),
               Input('select-keeper', 'max')])
def update_slider_example_value(min_value, max_value): 

        return [min_value, max_value]


# for setting min and max values for temp in tab 3

@app.callback(Output('input_temp3', 'min'),
              [Input('package3_choice', 'value')])
def update_slider_example_min(input):   
        dff = df[df.Package == input]
        min_value = min(dff.Temp_min)
        return min_value

@app.callback(Output('input_temp3', 'max'),
              [Input('package3_choice', 'value')])
def update_slider_example_max(input):
        dff = df[df.Package == input]
        max_value = max(dff.Temp_max)
        return max_value

@app.callback(Output('input_temp3', 'value'),
              [Input('select-keeper', 'min'),
               Input('select-keeper', 'max')])
def update_slider_example_value(min_value, max_value): 
        return [min_value, max_value]

# for setting min and max values for temp in tab 4

@app.callback(Output('input_temp4', 'min'),
              [Input('package4_choice', 'value')])
def update_slider_example_min(input):   
        dfff = df7[df7.Package == input]
        min_value = min(dfff.Temp_min)
        return min_value

@app.callback(Output('input_temp4', 'max'),
              [Input('package4_choice', 'value')])
def update_slider_example_max(input):
        dfff = df7[df7.Package == input]
        max_value = max(dfff.Temp_max)
        return max_value

@app.callback(Output('input_temp4', 'value'),
              [Input('select-keeper', 'min'),
               Input('select-keeper', 'max')])
def update_slider_example_value(min_value, max_value): 
        return [min_value, max_value]

## disable temp for shell
@app.callback(
 Output('input_temp','disabled'),
 [Input('package1_choice','value')]
)
def set_textboxes(chosen_pac):
 dff = df[(df.Package == "chosen_pac")]
 chosen_package = chosen_pac
 if chosen_package == "Shell":
     return "True";

## disable RH for shell
@app.callback(
 Output('input1_RH','disabled'),
 [Input('package1_choice','value')]
)
def set_textboxes(chosen_pac):
 dff = df[(df.Package == "chosen_pac")]
 chosen_package = chosen_pac
 if chosen_package == "Shell":
     return "True";


## disable temp for shell in tab-3
@app.callback(
 Output('input_temp3','disabled'),
 [Input('package3_choice','value')]
)
def set_textboxes(chosen_pac):
 dff = df[(df.Package == "chosen_pac")]
 chosen_package = chosen_pac
 if chosen_package == "Shell":
     return "True";

## disable RH for shell in tab-3
@app.callback(
 Output('input3_RH','disabled'),
 [Input('package3_choice','value')]
)
def set_textboxes(chosen_pac):
 dff = df[(df.Package == "chosen_pac")]
 chosen_package = chosen_pac
 if chosen_package == "Shell":
     return "True";

## disable temp for shell in tab-4
@app.callback(
 Output('input_temp4','disabled'),
 [Input('package4_choice','value')]
)
def set_textboxes(chosen_pac):
 dfff = df7[(df7.Package == "chosen_pac")]
 chosen_package = chosen_pac
 if chosen_package == "Shell":
     return "True";

## disable RH for shell in tab-4
@app.callback(
 Output('input4_RH','disabled'),
 [Input('package4_choice','value')]
)
def set_textboxes(chosen_pac):
 dfff = df7[(df7.Package == "chosen_pac")]
 chosen_package = chosen_pac
 if chosen_package == "Shell":
     return "True";


# @app.callback(
#  Output('input1_RH','max'),
#  [Input('package1_choice','value')]
# )
# def set_textboxes(chosen_pac2):
#  dff = df[(df.Package == "chosen_pac2")]
#  chosen_package = chosen_pac2
#  if chosen_package == "No Pack":
#      return 90;
#  else:
#      return 80;
## tab -1
@app.callback(
 Output('cond_choice','value'),
 [Input('package1_choice','value')]
)

def set_cond(chosen_pac):
    dff = df[(df.Package == "chosen_pac")]
    chosen_package = chosen_pac
    if chosen_package == "PP" or  "AL"  or "LDPE" or "PEN":
        return 'HW'
##tab -4
@app.callback(
 Output('cond4_choice','value'),
 [Input('package4_choice','value')]
)

def set_cond(chosen_pac):
    dfff = df7[(df7.Package == "chosen_pac")]
    chosen_package = chosen_pac
    if chosen_package == "PP"  or "LDPE" or "PEN":
        return 'HW'

##tab -3
@app.callback(
 Output('cond3_choice','value'),
 [Input('package3_choice','value')]
)

def set_cond(chosen_pac):
    dff = df[(df.Package == "chosen_pac")]
    chosen_package = chosen_pac
    if chosen_package == "PP" or  "AL"  or "LDPE" or "PEN":
        return 'HW'

### for setting min and max values for text boxes in tab 2
@app.callback(Output('input2_RH', 'min'),
              [Input('package2_choice', 'value')])
def update_slider_example_min(input):   
        dfff = df8[df8.Package == input]
        min_value = min(dfff.RH_min)
        return min_value


### for setting min and max values for text boxes in tab 2
@app.callback(Output('input2_RH', 'max'),
              [Input('package2_choice', 'value')])
def update_slider_example_max(input):
        dfff = df8[df8.Package == input]
        max_value = max(dfff.RH_max)
        return (max_value)



### for setting min and max values for text boxes in tab 2
@app.callback(Output('input2_RH', 'value'),
              [Input('select-keeper', 'min'),
               Input('select-keeper', 'max')])
def update_slider_example_value(min_value, max_value): 
        return [min_value, max_value]



@app.callback(
 Output('our_graph','figure'),
 [Input('package1_choice','value'),
 Input('cond_choice','value'),
 Input('input_temp','value'),
 Input('input1_RH','value')
 ]
 
)
##Chroma
def build_plot(value_pac, value_con, value_temp, value_RH):
    #df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
    
    dff = df[(df.Package == value_pac) & (df.Condition == value_con) & (min(df.Temp_min) <= value_temp <= max(df.Temp_max)) & (min(df.RH_min) <= value_RH <= max(df.RH_max))]
        # print(dff,"dff")
        # print(np.unique(dff.Package))
    value = np.unique(dff.Package)
    con = np.unique(dff.Condition)
    
    if ((value == ['No Pack'])):

        a = [0]*5
        # Mul = 0
        if value_con == 'HW':
            Mul = 0
        elif value_con == 'Steam':
            Mul = 2
        elif value_con == 'No cond':
            Mul = 1

        
        if Mul == 0:
            a = [-17.8106078214438,-14.6701634957204,8.70848690608227,0.0213423441405451,2.5345827288334]
        elif Mul == 1:
            a = [-1.62272676590206,-7.95216867293354,-16.0969648906995,0.0522830181650153,-14.3501550063858]
        elif Mul ==2:
            a = [19.4333345873459,22.6223321686539,7.38847798461727,-0.0736253623055605,11.8155722775524]

        H1_11 = []
        H1_21 = []
        H1_31 = []
        H1_41 = []
        H1_51 = []

        print("succeeded")
        days = [0,50,100,150,200,250,300,350,400,450]
        for i in range(0,10):
            H1_1 = (1.96728717595849 + 0.00152479312331781 * days[i] -0.0203263385938567 * value_RH + 0.106772307655858 * value_temp +  0.5 * a[0])
            H1_11.append(H1_1)
            print(H1_11,"H1_1")
                
            H1_2 = (-78.3797802007158 + 0.0211103205383151 * days[i] + 1.07934346198041 * value_RH + 0.00394072223014825 * value_temp + 0.5 * a[1])
            H1_21.append(H1_2)
            print(H1_21,"H1_2")

            H1_3 = (11.44008546904 + 0.0419843878531092 * days[i]  -0.0901259481500216 * value_RH  -0.0925884217723028 * value_temp + 0.5 * a[2])
            H1_31.append(H1_3)
            print(H1_31,"H1_3")

            H1_4 = (1.38118628815114 + 0.218597609442069 * days[i]  -0.00470958095594144 * value_RH + -0.0152147161908736 * value_temp + 0.5 * a[3])
            H1_41.append(H1_4)
            print(H1_41,"H1_4")

            H1_5 = (137.965698868641 + -0.154571801983221 * days[i]  -0.349173679686559 * value_RH  -3.0549079910958 * value_temp + a[4])
            H1_51.append(H1_5)
        print(H1_51,"H1_5")
        print(H1_11[0],"list H1_11")
        # y = 0
        y = []
        for i in range(0,10):
            print("inside for loop")
            x= 64.1391132665916  -0.763858342006614 * math.tanh(H1_11[i])  -2.06132926179434 * math.tanh(H1_21[i])  -2.06714047307052 * math.tanh(H1_31[i])  -31.5569384082559 * math.tanh(H1_41[i]) + 0.109431110052649 * H1_51[i]
            
            y.append(x)
        print(y,"x")
            

        df1=pd.DataFrame({'Days':(dff.Days),'Chroma': y })
        print(dff.Days)
        fig = px.scatter(data_frame=df1,  x='Days', y='Chroma',title="Chroma")
        return fig

    
    

    elif (value == ['Shell']) :

        # dff = df[(df.Package == 'Shell') & (df.Condition == value_con)]
        H1_11 = []
        H1_21 = []
        H1_31 = []
        H1_41 = []
        H2_11 = []
        H2_21 = []
        H2_31 = []
        H2_41 = []
        
        days = [0,50,100,150,200,250,300,350,400,450]
        for i in range(0,10):
            H2_1 = ((-0.254075054860244 + -0.00196648676872312 * days[i]))
            H2_11.append(H2_1)
            
            

            H2_2 = ((0.393165928782949 + -0.0012567957093587 * days[i]))
            H2_21.append(H2_2)
            

            H2_3 = -0.739761608901521 + 0.000559824365474321 * days[i]
            H2_31.append(H2_3)
            
    
            H2_4 = -0.22744395998497 + 0.0000430042499038342 * days[i]
            H2_41.append(H2_4)
            
        print(H2_11[0:4],"H2_1")  
        print(H2_21[0:4],"H2_2") 
        print(H2_31[0:4],"H2_3")
        print(H2_41[0:4],"H2_4")

        for i in range(0,10):
            print("in the for loop")
            

            H1_1 = ((-0.0471800471246165  -0.0965024039139135 * math.tanh(H2_11[i])  -0.0253002061688209 * math.tanh(H2_21[i])  -0.0150907300801383 * H2_31[i]  -0.0174396606090334 * H2_41[i]))
            H1_11.append(H1_1)
            

            H1_2 = ((-0.257791006656331 + 0.0742310143361269 * math.tanh(H2_11[i])  -0.161699437276433 * math.tanh(H2_21[i]) + 0.364140002367755 * H2_31[i] + 0.228885950864654 * H2_41[i]))
            H1_21.append(H1_2)

            H1_3 = ((-0.0604860774478096 + 0.189535296106539 * math.tanh(H2_11[i]) + 0.354994409253068 * math.tanh(H2_21[i]) + 0.358211642897504 * H2_31[i]  -0.00475498268727404 * H2_41[i]))
            H1_31.append(H1_3)

            H1_4 = ((0.103711891319488 + 0.237617823013052 * math.tanh(H2_11[i]) + 0.20369388288555 * math.tanh(H2_21[i])  -0.238286315651181 * H2_31[i] + 0.19181528077937 * H2_41[i]))
            H1_41.append(H1_4)

        print(H1_11,"H1_1")
        print(H1_21,"H1_1")
        print(H1_31,"H1_1")
        print(H1_41,"H1_1")



        y = []
        for i in range(0,10):
            x = 3098.73589839218  -2691.17789044866 * math.tanh(H1_11[i])  -7272.93301864375 * math.tanh(H1_21[i]) + 16728.4828654953 * math.tanh(H1_31[i])  -13602.9954204387 * math.tanh(H1_41[i])
            # x = 72.619393 - 0.0472179*days[i]

            y.append(x)
        
        print(y,"y")
        df1=pd.DataFrame({'Days':(days),'Chroma': y })
        fig = px.scatter(data_frame=df1,  x='Days', y='Chroma',title="Chroma")
        return fig

    # else:
    #     fig={}
    #     return fig

    else:
        H1_11 = []
        H1_21 = []
        H1_31 = []
        H1_41 = []

        a = [0]*4
        # Mul1 = 0
        if value_pac == 'AL':
            Mul1 = 0
        elif value_pac == 'LDPE':
            Mul1 = 1
        elif value_pac == 'PEN':
            Mul1 = 2
        elif value_pac == 'PP':
            Mul1 = 3


        
        if Mul1 == 0:
            a = [4.33457681822097,-1.00795749078614,-0.488956679503936,-1.98329990985466]
        elif Mul1 == 1:
            a = [-5.32275750719597,0.165064245797621,0.346417874426599,0.141004782376049]
        elif Mul1 ==2:
            a = [5.40224223498341,0.344102790359825,0.0980226322316914,0.9611667879997]
        elif Mul1 ==3:
            a = [-4.41406154600841,0.498790454628696,0.044516172845646,0.881128339478913]

        days = [0,50,100,150,200,250,300,350,400,450,500,525]

        for i in range(0,12):
            H1_1 = ((23.9995154595376 + -0.0117515396043142 * days[i] + -0.213406873960562 * value_RH + -0.059547928414675 * value_temp + 0.5 * a[0]))
            H1_11.append(H1_1)

            H1_2 = ((-4.64108245007944 + -0.00497672636405501 * days[i] + 0.0034233723070191 * value_RH + 0.216096776264521 * value_temp + 0.5 * a[1]))
            H1_21.append(H1_2)

            H1_3 = ((0.959110859582649 + 0.0380643803415124 * days[i] + -0.00388558393096261 * value_RH + -0.0184061255559824 * value_temp + 0.5 * a[2]))
            H1_31.append(H1_3)

            H1_4 = ((-2.05631556513968 + 0.00827515299092059 * days[i] + 0.011657950514916 * value_RH + -0.00180473818309567 * value_temp + 0.5 * a[3]))
            H1_41.append(H1_4)

        y = []
        for i in range(0,12):    

            x = 43.294402361095 + 6.05094232707644 * math.tanh(H1_11[i]) + -5.29220249092087 * math.tanh(H1_21[i]) + -13.5484085947731 * math.tanh(H1_31[i]) + -8.84939643455188 * math.tanh(H1_41[i])
            y.append(x)
        print(y,"x")

        df1=pd.DataFrame({'Days':(days),'Chroma': y })
        fig = px.scatter(data_frame=df1,  x='Days', y='Chroma',title="Chroma")
        return fig


@app.callback(
 Output('our_graph1','figure'),
 [Input('package1_choice','value'),
 Input('cond_choice','value'),
 Input('input_temp','value'),
 Input('input1_RH','value')
 ])
##HUE
def build_plot1(value_pac, value_con, value_temp, value_RH):
    #df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

    dff = df[(df.Package == value_pac) & (df.Condition == value_con) & (min(df.Temp_min) <= value_temp <= max(df.Temp_max)) & (min(df.RH_min) <= value_RH <= max(df.RH_max))]
        # print(dff,"dff")
        # print(np.unique(dff.Package))
    value = np.unique(dff.Package)
    con = np.unique(dff.Condition)
    
    if ((value == ['No Pack'])):
        
        # Mul2 = 0
        # Mul3 = 0
        a = [0]*9
        if value_con == 'HW':
            Mul2 = 0
        elif value_con == 'Steam':
            Mul2 = 2
        elif value_con == 'No cond':
            Mul2 = 1

        
        if Mul2 == 0:
            # a = [-0.851747693766548,0.964131002823693,-3.85587103143504,0.143499986920091,-1.347294349006,-3.31544364967464,-2.01510143718694,-1.00247499497318,-3.87475753377902]
            a = [0.0823051616502697,0.0715315391288678]
        elif Mul2 == 1:
            # a = [-3.5259610313443,-2.20018187171061,-3.81453497976482,-4.10912640425769,4.54032915425674,-3.98687639748729,-2.03324326019117,-0.67356455233059,1.7248078049294]
            a = [0.0675032290514994,0.108513367367218]
        elif Mul2 ==2:
            # a = [4.37770872511085,1.23605086888692,7.67040601119986,3.9656264173376,-3.19303480525074,7.30232004716193,4.04834469737811,1.67603954730377,2.14994972884962]
            a = [-0.149808390701769,-0.180044906496085]

        H1_11 = []
        H1_21 = []
        # H1_31 = []
        # H1_41 = []
        # H1_51 = []
        # H1_61 = []
        # H1_71 = []
        # H1_81 = []
        # H1_91 = []
        H2_11 = []
        H2_21 = []
        # H2_31 = []
        # H2_41 = []
        # H2_51 = []
        # H2_61 = []
        # H2_71 = []
        # H2_81 = []
        # H2_91 = []

        print("succeeded")
        days = [0,50,100,150,200,250,300,350,400,450]
        for i in range(0,10):

            

            H2_1 = ((2.92449957199429 + 0.00828165645035331 * days[i] + 0.00186557442818842 * value_RH + -0.0283295676206013 * value_temp + 0.5 * a[0]))
            H2_11.append(H2_1)

            H2_2 = 11.6124502411794 + -0.00173024725643652 * days[i] + -0.00129124774859515 * value_RH + -0.0511217878472741 * value_temp + a[1]
            H2_21.append(H2_2)
    

            # H2_1 = ((-29.1480477334234 + 0.00174888729943233 * days[i] + 0.0400517748646312 * value_RH + 0.929727739510656 * value_temp + 0.5 * a[0]))
            # H2_11.append(H2_1)

            # H2_2 = ((-2.4252849006743 + -0.00456341205367015 * days[i] + 0.022787806913454 * value_RH + 0.0636569426923941 * value_temp + 0.5 * a[1]))
            # H2_21.append(H2_2)

            # H2_3 = ((18.1540273550963 + -0.0111028560678139 * days[i] + -0.0811786073108554 * value_RH + -0.348760893504854 * value_temp + 0.5 * a[2]))
            # H2_31.append(H2_3)

            # H2_4 = -4.50492616827555 + 0.019326285501989 * days[i] + 0.0732569460187587 * value_RH + -0.0855324550328632 * value_temp + a[3]
            # H2_41.append(H2_4)

            # H2_5 = -9.75368116882522 + -0.0152083592351471 * days[i] + 0.0635688038663278 * value_RH + 0.0693281376862005 * value_temp + a[4]
            # H2_51.append(H2_5)

            # H2_6 = 3.58262236778956 + 0.0467212662107457 * days[i] + -0.0364040556643711 * value_RH + 0.0316099831285567 * value_temp + a[5]
            # H2_61.append(H2_6)

            # H2_7 = np.exp(-((0.5 * pow((1.56842286492075 + -0.0049453209622135 * days[i] + -0.00135917972773531 * value_RH + 0.0337838685481198 * value_temp + a[6]), 2))))
            # H2_71.append(H2_7)

            # H2_8 = np.exp(-((0.5 * pow((9.9340574529167 + -0.0036666039860571 * days[i] + -0.0753154850507864 * value_RH + -0.101545826199081 * value_temp + a[7]), 2))))
            # H2_81.append(H2_8)

            # H2_9 = np.exp(-((0.5 * pow((2.93963314944926 + -0.00408396960607698 * days[i] + -0.0669185978548418 * value_RH + -0.0197664373031872 * value_temp + a[8]), 2))))
            # H2_91.append(H2_9)



        for i in range(0,10):

            H1_1 = -1.32401363091467 + 0.78678779823868 * math.tanh(H2_11[i]) + 0.199826194690603 * H2_21[i]
            H1_11.append(H1_1)

            H1_2 = 15.3343066388191 + -24.0247193881745 * math.tanh(H2_11[i]) + 0.830880165436906 * H2_21[i]
            H1_21.append(H1_2)

    
            # H1_1 = ((-0.986040444112381 + -1.54517276779459 * math.tanh(H2_11[i]) + 0.554156540100426 * math.tanh(H2_21[i]) + -1.46003083343992 * math.tanh(H2_31[i]) + -0.306704116605232 * H2_41[i] + 1.14541908400768 * H2_51[i] + 0.502852056846842 * H2_61[i] + -0.878416945913895 * H2_71[i] + 1.59026263081179 * H2_81[i] + -0.663139049564296 * H2_91[i]))
            # H1_11.append(H1_1)

            # H1_2 = ((-1.08780169781531 + 0.749158019468237 * math.tanh(H2_11[i]) + 0.512366615675425 * math.tanh(H2_21[i]) + -1.55769771269561 * math.tanh(H2_31[i]) + 1.53445445912392 * H2_41[i] + 2.08214263475585 * H2_51[i] + -1.66684290218844 * H2_61[i] + -1.09138938149363 * H2_71[i] + 0.09680056252272 * H2_81[i] + 0.747428213684559 * H2_91[i]))
            # H1_21.append(H1_2)

            # H1_3 = ((-1.13146217553919 + -1.80067505057626 * math.tanh(H2_11[i]) + 0.813395590456551 * math.tanh(H2_21[i]) + -1.81750085341215 * math.tanh(H2_31[i]) + -0.339821182092005 * H2_41[i] + -0.160710548938618 * H2_51[i] + -0.0471855222080077 * H2_61[i] + -1.04822320328041 * H2_71[i] + 1.71160006705835 * H2_81[i] + 2.0802318668603 * H2_91[i]))
            # H1_31.append(H1_3)

            # H1_4 = -2.48966867550589 + 0.28963852501682 * math.tanh(H2_11[i]) + -0.129212854419549 * math.tanh(H2_21[i]) + 0.930702598910342 * math.tanh(H2_31[i]) + 1.78892328113082 * H2_41[i] + -0.406404557796772 * H2_51[i] + 0.769526114410496 * H2_61[i] + 3.74304348905121 * H2_71[i] + -1.69452565296458 * H2_81[i] + -0.25194903111848 * H2_91[i]
            # H1_41.append(H1_4)

            # H1_5 = -1.87805103523098 + 0.145603632891821 * math.tanh(H2_11[i]) + 1.27327017847079 * math.tanh(H2_21[i]) + -1.170254693264 * math.tanh(H2_31[i]) + 1.22682383120559 * H2_41[i] + -0.627350524593332 * H2_51[i] + -0.675566885339333 * H2_61[i] + 2.2025407541722 * H2_71[i] + 1.76412848466477 * H2_81[i] + -0.460510473744798 * H2_91[i]
            # H1_51.append(H1_5)

            # H1_6 = 2.90263185577803 + -0.963246516985378 * math.tanh(H2_11[i]) + -0.644562888822594 * math.tanh(H2_21[i]) + -0.29902489550338 * math.tanh(H2_31[i]) + 1.68934876699711 * H2_41[i] + -0.994132228954312 * H2_51[i] + -0.154592576198289 * H2_61[i] + -3.20160667349042 * H2_71[i] + 2.48740865342625 * H2_81[i] + 2.34905970585743 * H2_91[i]
            # H1_61.append(H1_6)

            # H1_7 = np.exp(-((0.5 * pow((1.50814008763782 + 3.50797644664735 * math.tanh(H2_11[i]) + 1.86819688892339 * math.tanh(H2_21[i]) + -2.70695752054744 * math.tanh(H2_31[i]) + 1.63565695040488 * H2_41[i] + 1.94291006146455 * H2_51[i] + 2.37818708898953 * H2_61[i] + 4.64970083721064 * H2_71[i] + -5.06428053536846 * H2_81[i] + -2.76731566192687 * H2_91[i]), 2))))
            # H1_71.append(H1_7)

            # H1_8 = np.exp(-((0.5 * pow((2.09560079541348 + -0.297320487045959 * math.tanh(H2_11[i]) + -1.69081239243061 * math.tanh(H2_21[i]) + 0.411946176755453 * math.tanh(H2_31[i]) + -1.29938417003395 * H2_41[i] + -1.01851940513056 * H2_51[i] + -1.09238891914963 * H2_61[i] + 2.23745721576677 * H2_71[i] + 2.36212767008948 * H2_81[i] + 1.04680067028911 * H2_91[i]), 2))))
            # H1_81.append(H1_8)

            # H1_9 = np.exp(-((0.5 * pow((-0.367521901271898 + -2.24443538034299 * math.tanh(H2_11[i]) + -0.472536938885901 * math.tanh(H2_21[i]) + -1.27758285249741 * math.tanh(H2_31[i]) + -2.62320255267496 * H2_41[i] + 3.53944032722206 * H2_51[i] + -5.39414911317312 * H2_61[i] + -0.0385709716190692 * H2_71[i] + -0.719783258282571 * H2_81[i] + 0.98434983125282 * H2_91[i]), 2))))
            # H1_91.append(H1_9)



        y = []
        for i in range(0,10):

            x = 61.7445037115585 + 1.26091928997379 * H1_11[i] + 18.2388814150402 * H1_21[i]

    
            # x = 59.1894301688154 + -3.24255488599493 * math.tanh(H1_11[i]) + 5.77383107092709 * math.tanh(H1_21[i]) + -7.09735409848462 * math.tanh(H1_31[i]) + -3.73980263267678 * H1_41[i] + -1.2645165060809 * H1_51[i] + 4.07761358115133 * H1_61[i] + -7.84140423411436 * H1_71[i] + -3.40012527338708 * H1_81[i] + 5.03306660384992 * H1_91[i]

            y.append(x)


        df2=pd.DataFrame({'Days':(dff.Days),'Hue': y })
        print(dff.Days)
        fig = px.scatter(data_frame=df2,  x='Days', y='Hue',title="Hue")
        return fig

    
    

    elif (value == ['Shell']) :

        # dff = df[(df.Package == 'Shell') & (df.Condition == value_con)]
        # H1_11 = []
        # H1_21 = []
        # H1_31 = []
        # H1_41 = []
        # H1_51 = []
        # H1_61 = []
        # H2_11 = []
        # H2_21 = []
        # H2_31 = []
        



        days = [0,50,100,150,200,250,300,350,400,450]
        # for i in range(0,10):
        #     H2_1 = ((1.4114479494615 + -0.00443676163505974 * days[i]))
        #     H2_11.append(H2_1)

        #     H2_2 = 2.63176557757102 + -0.00538742087482835 * days[i]
        #     H2_21.append(H2_2)

        #     H2_3 = np.exp(-((0.5 * pow((-5.40334338369859 + 0.027308050944895 * days[i]), 2))))
        #     H2_31.append(H2_3)

        # for i in range(0,10):

        #     H1_1 = ((0.750981832198404 + -0.417788531894986 * math.tanh(H2_11[i]) + -0.414392933542123 * H2_21[i] + -0.433860444981626 * H2_31[i]))
        #     H1_11.append(H1_1)

        #     H1_2 = ((-0.337281501849945 + 0.321784037441422 * math.tanh(H2_11[i]) + -0.67467718489772 * H2_21[i] + 0.214438995075245 * H2_31[i]))
        #     H1_21.append(H1_2)

        #     H1_3 = 0.716865846140075 + -2.09761582428735 * math.tanh(H2_11[i]) + -0.484870741296251 * H2_21[i] + 1.39502245957306 * H2_31[i]
        #     H1_31.append(H1_3)

        #     H1_4 = -0.204603316203998 + -1.13454493165585 * math.tanh(H2_11[i]) + -0.465322402212898 * H2_21[i] + -0.133034134154835 * H2_31[i]
        #     H1_41.append(H1_4)

        #     H1_5 = np.exp(-((0.5 * pow((-0.811892537319175 + 1.72363341198156 * math.tanh(H2_11[i]) + 2.38713873948312 * H2_21[i] + 1.55755506344759 * H2_31[i]), 2))))
        #     H1_51.append(H1_5)

        #     H1_6 = np.exp(-((0.5 * pow((-0.262632803349253 + 0.22071120164023 * math.tanh(H2_11[i]) + -0.479762600945631 * H2_21[i] + 1.63778226848863 * H2_31[i]), 2))))
        #     H1_61.append(H1_6)

        y = []
        for i in range(0,10):

            # x = 60.5851802877838 + 1.4397407832255 * math.tanh(H1_11[i]) + 0.30714102695218 * math.tanh(H1_21[i]) + -3.79924447051513 * H1_31[i] + -1.50955317483906 * H1_41[i] + -6.45597792529054 * H1_51[i] + 2.45703383851654 * H1_61[i]
            x = 72.619393 - 0.0472179*days[i]
            y.append(x)
    
        
        df2=pd.DataFrame({'Days':(days),'Hue': y })
        fig = px.scatter(data_frame=df2,  x='Days', y='Hue',title="Hue")
        return fig

    # else:
    #     fig={}
    #     return fig

    else:
        H1_11 = []
        H1_21 = []
        H1_31 = []
        H1_41 = []
        H1_51 = []
        H1_61 = []
        # H2_11 = []
        # H2_21 = []
        # H2_31 = []
        # H2_41 = []
        # H2_51 = []
        # H2_61 = []

        a = [0]*6
         
        # Mul3 = 0
        if value_pac == 'AL':
            Mul3 = 0
        elif value_pac == 'LDPE':
            Mul3 = 1
        elif value_pac == 'PEN':
            Mul3 = 2
        elif value_pac == 'PP':
            Mul3 = 3


        
        if   Mul3 == 0:
            # a = [-0.121204729418545,3.00682262336466,-2.17440384886982,-0.52429580739813,-2.93425728110171,-1.44772203626297]
            a = [0.128681862247222,0.0335813274594179,-0.0117121613142338,0.00430472724743496,0.00279567328288488,0.00658783303627302]
        elif Mul3 == 1:
            # a = [-0.24681998356794,2.77515197163595,0.973727771092368,0.358402496612049,0.877699509012404,1.59348092760812]
            a = [-0.0965247679405796,-0.101569567343682,-0.0201434829490836,0.0247024909656275,0.01802740274124,0.0419783994398172]
        elif Mul3 ==2:
            # a = [-0.494337460470452,1.93140146348678,0.145333937609307,0.905089919439966,-3.70742610883452,-2.72052343257162]
            a = [0.0706339782040434,0.129935140441993,0.0064591910957662,-0.0204695400066114,-0.0147217704870022,-0.0343216697001016]
        elif Mul3 ==3:
            # a = [0.862362173456938,-7.71337605848739,1.05534214016814,-0.739196608653885,5.76398388092383,2.57476454122647]
            a = [-0.102791072510686,-0.0619469005577288,0.0253964531675512,-0.00853767820645104,-0.00610130553712266,-0.0142445627759886]

        days = [0,50,100,150,200,250,300,350,400,450,500,525]


    
        for i in range(0,12):

            

            H1_1 = ((1.80266636108719 + 0.00472300182207037 * days[i] + -0.00594175377594257 * value_RH + -0.0855601992268622 * value_temp + 0.5 * a[0]))
            H1_11.append(H1_1)

            H1_2 = ((3.82296305445259 + -0.00244390400172244 * days[i] + -0.0184036189309618 * value_RH + -0.0313207210972359 * value_temp + 0.5 * a[1]))
            H1_21.append(H1_2)

            H1_3 = ((0.289613283572206 + -0.00222855587153657 * days[i] + -0.00703751613008282 * value_RH + 0.0139512950717212 * value_temp + 0.5 * a[2]))
            H1_31.append(H1_3)

            H1_4 = -1.43626465170472 + 0.00237267161984156 * days[i] + 0.0128748812056702 * value_RH + -0.00796767216252837 * value_temp + a[3]
            H1_41.append(H1_4)

            H1_5 = -1.08077652668373 + 0.00178768932097344 * days[i] + 0.00965669319228177 * value_RH + -0.00592787138913092 * value_temp + a[4]
            H1_51.append(H1_5)

            H1_6 = -2.41443700962922 + 0.00399785929775403 * days[i] + 0.0215097368867321 * value_RH + -0.0132684545254327 * value_temp + a[5]
            H1_61.append(H1_6)

    

    
            # H2_1 = ((-2.01916937134045 + -0.0107456708609651 * days[i] + -0.00436736439934034 * value_RH + 0.0873453214785023 * value_temp + 0.5 * a[0]))
            # H2_11.append(H2_1)

            # H2_2 = ((9.81805794420904 + -0.0106851645293384 * days[i] + -0.0533680473662797 * value_RH + -0.156953898547855 * value_temp + 0.5 * a[1]))
            # H2_21.append(H2_2)

            # H2_3 = -16.4815240591322 + 0.0170056725589485 * days[i] + 0.00766659519532837 * value_RH + 0.397961682107847 * value_temp + a[2]
            # H2_31.append(H2_3)

            # H2_4 = -6.17663469910304 + 0.020780938239129 * days[i] + 0.100984566406537 * value_RH + -0.141962875785496 * value_temp + a[3]
            # H2_41.append(H2_4)

            # H2_5 = np.exp(-((0.5 * pow((-3.01440138195083 + 0.0074517683157634 * days[i] + -0.0531471798265584 * value_RH + 0.118004277822781 * value_temp + a[4]), 2))))
            # H2_51.append(H2_5)

            # H2_6 = np.exp(-((0.5 * pow((-15.7051218495497 + 0.0118743091570867 * days[i] + -0.00444537522029359 * value_RH + 0.377806879310418 * value_temp + a[5]), 2))))
            # H2_61.append(H2_6)



        # for i in range(0,12):

        #     H1_1 = ((0.120009765916417 + 0.846687943032407 * math.tanh(H2_11[i]) + -0.051718090189981 * math.tanh(H2_21[i]) + -1.81656070694803 * H2_31[i] + -0.498081151148397 * H2_41[i] + -0.590806754667144 * H2_51[i] + -0.227114943052093 * H2_61[i]))
        #     H1_11.append(H1_1)

        #     H1_2 = ((-0.439949933941113 + -0.0351322702937927 * math.tanh(H2_11[i]) + -1.31451983248882 * math.tanh(H2_21[i]) + 0.0407820824906759 * H2_31[i] + -0.131107727363917 * H2_41[i] + 0.553596985916237 * H2_51[i] + -0.714433296016195 * H2_61[i]))
        #     H1_21.append(H1_2)

        #     H1_3 = ((-0.886435819642833 + 0.88677642642917 * math.tanh(H2_11[i]) + -1.17529487916714 * math.tanh(H2_21[i]) + -0.205100301301496 * H2_31[i] + -0.014634666676522 * H2_41[i] + -0.156743480999565 * H2_51[i] + 0.222024285272595 * H2_61[i]))
        #     H1_31.append(H1_3)

        #     H1_4 = np.exp(-((0.5 * pow((-1.2366114156489 + 3.11506685023901 * math.tanh(H2_11[i]) + -2.35692135938022 * math.tanh(H2_21[i]) + -0.37889537898238 * H2_31[i] + -2.21360425040421 * H2_41[i] + -0.948365478624135 * H2_51[i] + -2.27130684521379 * H2_61[i]), 2))))
        #     H1_41.append(H1_4)

        #     H1_5 = np.exp(-((0.5 * pow((1.97639876368231 + 3.27687295348808 * math.tanh(H2_11[i]) + 1.04377409286322 * math.tanh(H2_21[i]) + 0.398185507652745 * H2_31[i] + -0.0451220885857183 * H2_41[i] + -0.873259869783226 * H2_51[i] + 0.64288177079819 * H2_61[i]), 2))))
        #     H1_51.append(H1_5)

        #     H1_6 = np.exp(-((0.5 * pow((3.304313758512 + -2.72516472131556 * math.tanh(H2_11[i]) + 0.210719895709789 * math.tanh(H2_21[i]) + -1.3761944219602 * H2_31[i] + -2.51419512687945 * H2_41[i] + -1.18067250138614 * H2_51[i] + 1.26997457685453 * H2_61[i]), 2))))
        #     H1_61.append(H1_6)

        y = []
        for i in range(0,12):

            # x = 63.8296914497334 + 3.10742649233829 * math.tanh(H1_11[i])   + -9.04878308820476 * math.tanh(H1_21[i]) + 9.40532208408668 * math.tanh(H1_31[i]) + 6.76855577352509 * H1_41[i] + -14.5548712399872 * H1_51[i] + -9.85849582756989 * H1_61[i]
            x = 36.1884675494859 + 28.1600272618452 * math.tanh(H1_11[i]) + 132.502969891986 * math.tanh(H1_21[i]) + 205.556339146359 * math.tanh(H1_31[i]) + 33.0209803994752 * H1_41[i] + 24.815229931858 * H1_51[i] + 55.6992010312312 * H1_61[i]
            y.append(x)

    

        df2=pd.DataFrame({'Days':(days),'Hue': y })
        fig = px.scatter(data_frame=df2,  x='Days', y='Hue',title="Hue")
        return fig

@app.callback(
 Output('our_graph2','figure'),
 [Input('package1_choice','value'),
 Input('cond_choice','value'),
 Input('input_temp','value'),
 Input('input1_RH','value')
 ])

##color - Lightness
def build_plot2(value_pac, value_con, value_temp, value_RH):
    #df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

    dff = df[(df.Package == value_pac) & (df.Condition == value_con) & (min(df.Temp_min) <= value_temp <= max(df.Temp_max)) & (min(df.RH_min) <= value_RH <= max(df.RH_max))]
    # print(dff,"dff")
    # print(np.unique(dff.Package))
    value = np.unique(dff.Package)
    con = np.unique(dff.Condition)

    if ((value == ['No Pack'])):

        H1_11 = []
        H1_21 = []
        H1_31 = []
        H1_41 = []
        H1_51 = []
        H1_61 = []
        H1_71 = []
        a = [0]*7
        
        # Mul4 = 0
        if value_con == 'HW':
            Mul4 = 0
        elif value_con == 'Steam':
            Mul4 = 2
        elif value_con == 'No cond':
            Mul4 = 1

        
        if Mul4 == 0:
            a = [12.3020021698333,-0.790650738517611,-0.0171897050774622,-0.370864594148457,73.4728200241082,-6.39045721109864,-16.3136045335026]
        elif Mul4 == 1:
            a = [12.0204662648316,0.286327031172647,-0.0879596326241215,0.123318991095999,-22.6097136482707,-6.40857710913303,-16.339801263754]
        elif Mul4 ==2:
            a = [-24.3224684346649,0.504323707344964,0.105149337701584,0.247545603052458,-50.8631063758375,12.7990343202317,32.6534057972571]


        days = [0,50,100,150,200,250,300,350,400,450]
        for i in range(0,10):
            
            H1_1 = ((-114.536168827394 + 0.0587141664230977 * days[i] + 0.258722812573826 * value_RH + 2.16317893972791 * value_temp + 0.5 * a[0]))
            H1_11.append(H1_1)

            H1_2 = ((-5.48181667858477 + -0.0133635990813712 * days[i] + 0.0221202565515742 * value_RH + 0.141426771054458 * value_temp + 0.5 * a[1]))
            H1_21.append(H1_2)

            H1_3 = ((0.703686056943713 + 0.299339115843674 * days[i] + -0.00145381697326315 * value_RH + -0.00788932600113627 * value_temp + 0.5 * a[2]))
            H1_31.append(H1_3)

            H1_4 = ((-2.61287085305161 + 0.00377280636134614 * days[i] + 0.0105889487408807 * value_RH + 0.0741308952466916 * value_temp + 0.5 * a[3]))
            H1_41.append(H1_4)

            H1_5 = np.exp(-((0.5 * pow((-133.343419982568 + 0.22013666595131 * days[i] + 1.77385967104484 * value_RH + 0.282674152056853 * value_temp + a[4]), 2))))
            H1_51.append(H1_5)

            H1_6 = np.exp(-((0.5 * pow((7.06618596925601 + 0.569495662959788 * days[i] + 0.0122977147842836 * value_RH + -0.100546287400845 * value_temp + a[5]), 2))))
            H1_61.append(H1_6)

            H1_7 = np.exp(-((0.5 * pow((291.883836843065 + -0.31078307407321 * days[i] + -1.66522373125123 * value_RH + -3.69291372953298 * value_temp + a[6]), 2))))
            H1_71.append(H1_7)

        y = []
        for i in range(0,10):
            x = 71.0182639688873 + -13.9308939280801 * math.tanh(H1_11[i]) + 5.20671351307816 * math.tanh(H1_21[i]) + -31.2106962057316 * math.tanh(H1_31[i]) + -12.1878270310853 * math.tanh(H1_41[i]) + -4.38995332263299 * H1_51[i] + -2.27610208214436 * H1_61[i] + 8.88432185022385 * H1_71[i]

            y.append(x)
        
        df3=pd.DataFrame({'Days':(days),'Lightness': y })
        fig = px.scatter(data_frame=df3,  x='Days', y='Lightness',title="Lightness")
        return fig

    elif (value == ['Shell']) :

        days = [0,50,100,150,200,250,300,350,400,450]
        H1_11 = []
        H1_21 = []
        H1_31 = []
        H2_11 = []
        H2_21 = []
        H2_31 = []
        

        for i in range(0,10):

            H2_1 = ((-0.551327730696755 + 0.00137831956571801 * days[i]))
            H2_11.append(H2_1)

            H2_2 = -2.95320969709069 + 0.00862368588306539 * days[i]
            H2_21.append(H2_2)

            H2_3 = np.exp(-((0.5 * pow((0.598915325580838 + -0.00594871221234246 * days[i]), 2))))
            H2_31.append(H2_3)


        for i in range(0,10):

            H1_1 = ((-0.469725079228966 + 0.32953988480411 * math.tanh(H2_11[i]) + 0.249775587304739 * H2_21[i] + 0.566092311862786 * H2_31[i]))
            H1_11.append(H1_1)

            H1_2 = 0.339028510555748 + -0.433968717102769 * math.tanh(H2_11[i]) + -1.18622080387525 * H2_21[i] + 1.3248068658515 * H2_31[i]
            H1_21.append(H1_2)

            H1_3 = np.exp(-((0.5 * pow((0.0378866643662934 + -0.34624770863061 * math.tanh(H2_11[i]) + 0.28856435306671 * H2_21[i] + 0.580661631818298 * H2_31[i]),2))))
            H1_31.append(H1_3)

        y = []
        for i in range(0,10):
            x = 444.090934630841 + -104.110105265241 * math.tanh(H1_11[i]) + -1.64428427717083 * H1_21[i] + -442.036958392417 * H1_31[i]

            y.append(x)
   

        df3=pd.DataFrame({'Days':(days),'Lightness': y })
        fig = px.scatter(data_frame=df3,  x='Days', y='Lightness',title="Lightness")
        return fig

    else:

        if value_pac == 'AL':
            Mul4 = 0
        elif value_pac == 'LDPE':
            Mul4 = 1
        elif value_pac == 'PEN':
            Mul4 = 2
        elif value_pac == 'PP':
            Mul4 = 3


        
        if   Mul4 == 0:
            a = [-0.893331762793084,-10.64755911049,-181.449789936768,1.00804069804724]
        elif Mul4 == 1:
            a = [0.481301408918591,-26.1603635190232,-79.0754954532044,-0.445414783059274]
        elif Mul4 ==2:
            a = [0.4750263616172,17.9568565589869,-90.8579892225782,-0.500659863066393]
        elif Mul4 ==3:
            a = [-0.0629960077427074,18.8510660705263,351.38327461255,-0.061966051921574]

        days = [0,50,100,150,200,250,300,350,400,450,500,525]
        H1_11 = []
        H1_21 = []
        H1_31 = []
        H1_41 = []

        for i in range(0,12):
            H1_1 = ((1.163384195557 + -0.00063998687849314 * days[i] + -0.00236229463253681 * value_RH + -0.0152496899966601 * value_temp + 0.5 * a[0]))
            H1_11.append(H1_1)

            H1_2 = ((162.652336458493 + 0.0000344595718234055 * days[i] + 0.0219668830103746 * value_RH + -5.77439659574531 * value_temp + 0.5 * a[1]))
            H1_21.append(H1_2)

            H1_3 = ((203.365946700649 + -0.511516979415802 * days[i] + -2.34045331859455 * value_RH + 1.56065309805235 * value_temp + 0.5 * a[2]))
            H1_31.append(H1_3)

            H1_4 = ((-1.38583211410668 + -0.0285486115601688 * days[i] + 0.0017130418279907 * value_RH + 0.0185502647744596 * value_temp + 0.5 * a[3]))
            H1_41.append(H1_4)

        y = []
        for i in range(0,12):

            x = 90.4068018435208 + 47.7437071568827 * math.tanh(H1_11[i]) + 2.33268622973395 * math.tanh(H1_21[i]) + 3.94670654598295 * math.tanh(H1_31[i]) + 73.9042250743099 * math.tanh(H1_41[i])
            y.append(x)

        df3=pd.DataFrame({'Days':(days),'Lightness': y })
        fig = px.scatter(data_frame=df3,  x='Days', y='Lightness',title="Lightness")
        return fig
   
@app.callback(
 Output('our_graph4','figure'),
 [Input('package3_choice','value'),
 Input('cond3_choice','value'),
 Input('input_temp3','value'),
 Input('input3_RH','value')
 ]
 
)
##FFA
def build_plot(value_pac, value_con, value_temp, value_RH):
    #df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
    
    dff = df[(df.Package == value_pac) & (df.Condition == value_con) & (min(df.Temp_min) <= value_temp <= max(df.Temp_max)) & (min(df.RH_min) <= value_RH <= max(df.RH_max))]
        # print(dff,"dff")
        # print(np.unique(dff.Package))
    value = np.unique(dff.Package)
    con = np.unique(dff.Condition)
    
    if ((value == ['No Pack'])):

        a = [0]*5
        # Mul = 0
        if value_con == 'HW':
            Mul = 0
        elif value_con == 'Steam':
            Mul = 2
        elif value_con == 'No cond':
            Mul = 1

        
        if Mul == 0:
            a = [0.206313811623389,0.140783693145118,0.587971020768325]
        elif Mul == 1:
            a = [-0.222712672563747,-0.0353925901223843,-1.07316761370568]
        elif Mul ==2:
            a = [0.0163988609403584,-0.105391103022734,0.485196592937357]

        H1_11 = []
        H1_21 = []
        H1_31 = []
        H2_11 = []
        H2_21 = []
        H2_31 = []
        

        print("succeeded")
        days = [0,50,100,150,200,250,300,350,400,450]
        for i in range(0,10):
            

            H2_1 = ((-0.82801466886175 + 0.0079596947625985 * days[i] + -0.00194396645112909 * value_RH + -0.0134289011513696 * value_temp + 0.5 * a[0]))
            H2_11.append(H2_1)
            H2_2 = ((1.46191794592187 + -0.00161693758326164 * days[i] + -0.00217438056065772 * value_RH + -0.0278598874059186 * value_temp + 0.5 * a[1]))
            H2_21.append(H2_2)

            H2_3 = ((6.42382748313862 + 0.00391555130768852 * days[i] + -0.0812337653001466 * value_RH + -0.0597109293571702 * value_temp + 0.5 * a[2]))
            H2_31.append(H2_3)

        for i in range(0,10):

            H1_1 = ((-0.508002771186089 + 0.49902351216057 * math.tanh(H2_11[i]) + -0.235230201682704 * math.tanh(H2_21[i]) + -0.371272830775528 * math.tanh(H2_31[i])))
            H1_11.append(H1_1)
            H1_2 = ((0.508874626465208 + -0.511396729325896 * math.tanh(H2_11[i]) + -0.0692674365262307 * math.tanh(H2_21[i]) + -0.283055525996724 * math.tanh(H2_31[i])))
            H1_21.append(H1_2)

            H1_3 = ((-0.310292651804248 + -0.483541472989825 * math.tanh(H2_11[i]) + -0.022500938114622 * math.tanh(H2_21[i]) + -0.299751061510614 * math.tanh(H2_31[i])))
            H1_31.append(H1_3)

    
        y = []
        for i in range(0,10):
            print("inside for loop")
            x = 0.28526781755532 + 3.58682497028558 * math.tanh(H1_11[i]) + 4.19485552274019 * math.tanh(H1_21[i]) + -3.61691902647478 * math.tanh(H1_31[i])
            
            y.append(x)
        print(y,"x")
            

        df1=pd.DataFrame({'Days':(dff.Days),'FFA': y })
        print(dff.Days)
        fig = px.scatter(data_frame=df1,  x='Days', y='FFA',title="NEUTRAL")
        return fig

    
    

    elif (value == ['Shell']) :

        # dff = df[(df.Package == 'Shell') & (df.Condition == value_con)]
        H1_11 = []
        H1_21 = []
        H2_11 = []
        H2_21 = []
        
        
        days = [0,50,100,150,200,250,300,350,400,450]
        for i in range(0,10):

            H2_1 = -1.00410516334414 + 0.00140110441915073 * days[i]
            H2_11.append(H2_1)

            H2_2 = np.exp(-((0.5 * pow((-2.02748326912914 + 0.00663494860910701 * days[i]), 2))))
            H2_21.append(H2_2)

        for i in range(0,10):

            H1_1 = ((-0.254501550721886 + 0.44365351390902 * H2_11[i] + -0.275374552638649 * H2_21[i]))
            H1_11.append(H1_1)

            H1_2 = 0.0365754285075347 + 0.195692970312028 * H2_11[i] + -0.187499222133813 * H2_21[i]
            H1_21.append(H1_2)

        

        y = []
        for i in range(0,10):
            x = 2.27952450272188 + 3.1271576465429 * math.tanh(H1_11[i]) + 0.134110499107072 * (H1_21[i])
            y.append(x)
        
        print(y,"y")
        df1=pd.DataFrame({'Days':(days),'FFA': y })
        fig = px.scatter(data_frame=df1,  x='Days', y='FFA',title="NEUTRAL")
        return fig

    # else:
    #     fig={}
    #     return fig

    else:
        H1_11 = []
        H1_21 = []
        H1_31 = []
        H1_41 = []

        a = [0]*4
        # Mul1 = 0
        if value_pac == 'AL':
            Mul1 = 0
        elif value_pac == 'LDPE':
            Mul1 = 1
        elif value_pac == 'PEN':
            Mul1 = 2
        elif value_pac == 'PP':
            Mul1 = 3


        
        if Mul1 == 0:
            a = [-0.230052884111455,0.322882357388249,0.345651706871531,-0.133052329137043]
        elif Mul1 == 1:
            a = [-0.273745534453369,0.607641944813567,0.126372341764002,-0.296174672258081]
        elif Mul1 ==2:
            a = [0.429977226809868,-0.304150541479981,-0.226958438329832,0.220341885153352]
        elif Mul1 ==3:
            a = [0.0738211917549548,-0.626373760721835,-0.245065610305701,0.208885116241772]

        days = [0,50,100,150,200,250,300,350,400,450,500,525]

        for i in range(0,12):
            
            H1_1 = ((-2.26139088353829 + -0.00512707750159664 * days[i] + 0.047911151586842 * value_RH + 0.0192555626784469 * value_temp + 0.5 * a[0]))
            H1_11.append(H1_1)

            H1_2 = ((-1.78736275703663 + -0.00174522899243888 * days[i]  + -0.00721944934302697 * value_RH + 0.0693360587543322 * value_temp + 0.5 * a[1]))
            H1_21.append(H1_2)

            H1_3 = 1.21749891674453 + 0.00133466112060344 * days[i]  + -0.0176297856127001 * value_RH + -0.00838004194821216 * value_temp + a[2]
            H1_31.append(H1_3)

            H1_4 = 1.55330805897667 + -0.00462575313892442 * days[i]  + 0.0163219018440638 * value_RH + -0.0586835413037316 * value_temp + a[3]
            H1_41.append(H1_4)

        y = []
        for i in range(0,12):

            x = -0.236308618536409 + 1.5948715754361 * math.tanh(H1_11[i]) + -1.44900079015266 * math.tanh(H1_21[i]) + 0.108510790266813 * H1_31[i] + -1.32537284859601 * H1_41[i]
            y.append(x)
   

        df1=pd.DataFrame({'Days':(days),'FFA': y })
        fig = px.scatter(data_frame=df1,  x='Days', y='FFA',title="NEUTRAL")
        return fig    


@app.callback(
 Output('our_graph5','figure'),
 [Input('package4_choice','value'),
 Input('cond4_choice','value'),
 Input('input_temp4','value'),
 Input('input4_RH','value')
 ]
 
)
### Lipid oxidation -AV
def build_plot(value_pac, value_con, value_temp, value_RH):
    #df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
    

    # df = pd.read_excel("data.xlsx", sheet_name="Sheet2")
    dfff = df7[(df.Package == value_pac) & (df.Condition == value_con) & (min(df.Temp_min) <= value_temp <= max(df.Temp_max)) & (min(df.RH_min) <= value_RH <= max(df.RH_max))]
    # print(df7)
    print(dfff)
        # print(dff,"dff")
        # print(np.unique(dff.Package))
    value = np.unique(dfff.Package)
    print(value)
    con = np.unique(dfff.Condition)
    
    if ((value == ['No Pack'])):

        a = [0]*5
        # Mul = 0
        if value_con == 'HW':
            Mul = 0
        elif value_con == 'Steam':
            Mul = 2
        elif value_con == 'No cond':
            Mul = 1

        
        if Mul == 0:
            a = [-0.0582830831344857,1.51767881672466,-0.13222083829778,0.121068666137303,5.6314694814815,-0.592084844782328]
        elif Mul == 1:
            a = [-0.102549065113804,-0.305015230621686,0.0371737648771988,-3.53409779063701,0.429856946837202,-2.99801793078166]
        elif Mul ==2:
            a = [0.16083214824829,-1.21266358610298,0.0950470734205816,3.4130291244997,-6.0613264283187,3.59010277556399]

        H1_11 = []
        H1_21 = []
        H1_31 = []
        H1_41 = []
        H1_51 = []
        H1_61 = []
        

        print("succeeded")
        days = [0,50,100,150,200,250,300,350,400,450]
        for i in range(0,10):
            
            H1_1 = ((1.23178008060393 + 0.00279600361370856 * days[i] + -0.0291221005916624 * value_RH + 0.011088838401852 * value_temp + 0.5 * a[0]))
            H1_11.append(H1_1)

            H1_2 = ((1.54376482985967 + 0.00299681375402645 * days[i] + -0.00196453290094959 * value_RH + -0.0836629219610647 * value_temp + 0.5 * a[1]))
            H1_21.append(H1_2)

            H1_3 = ((-3.14436688665228 + 0.00362682069336294 * days[i] + 0.00311072217802555 * value_RH + 0.0563563431785924 * value_temp + 0.5 * a[2]))
            H1_31.append(H1_3)

            H1_4 = 2.29257475374975 + -0.00465374589724901 * days[i] + 0.0217100256689014 * value_RH + -0.0547858583673591 * value_temp + a[3]
            H1_41.append(H1_4)

            H1_5 = -2.26263284546719 + -0.00297319769959735 * days[i] + 0.013305063286233 * value_RH + -0.0827834734898814 * value_temp + a[4]
            H1_51.append(H1_5)

            H1_6 = -0.175393728651044 + 0.00520954783221067 * days[i] + -0.0567575241222745 * value_RH + 0.174455269922439 * value_temp + a[4]
            H1_61.append(H1_6)

    
        y = []
        for i in range(0,10):
            print("inside for loop")
            x = 2.72696877475224 + 1.67255257590084 * math.tanh(H1_11[i]) + -1.05922854242596 * math.tanh(H1_21[i]) + 3.10377108040633 * math.tanh(H1_31[i]) + 0.408052346977725 * H1_41[i] + 0.0836998922920763 * H1_51[i] + -0.46402877054102 * H1_61[i]
            y.append(x)
        print(y,"x")
            

        df1=pd.DataFrame({'Days':(dfff.Days),'AV': y })
        print(dfff.Days)
        fig = px.scatter(data_frame=df1,  x='Days', y='AV',title="NEUTRAL")
        return fig

    
    

    elif (value == ['Shell']) :

        # dff = df[(df.Package == 'Shell') & (df.Condition == value_con)]
        H1_11 = []
        H1_21 = []
        
        
        
        days = [0,50,100,150,200,250,300,350,400,450]
        for i in range(0,10):

            H1_1 = ((0.854527697743417  -0.00175570933319872 * days[i]))
            H1_11.append(H1_1)

            H1_2 = ((-0.805959087358981 + 0.00253925225607468 * days[i]))
            H1_21.append(H1_2)

            

        y = []
        for i in range(0,10):
            x = 18.8095096370112  -64.0643637518625 * math.tanh(H1_11[i])  -38.8205405399208 * math.tanh(H1_21[i])
            y.append(x)
        
        print(y,"y")
        df1=pd.DataFrame({'Days':(days),'AV': y })
        fig = px.scatter(data_frame=df1,  x='Days', y='AV',title="NEUTRAL")
        return fig

    

    else:
        H1_11 = []
        H1_21 = []
        H1_31 = []
        H1_41 = []
        H1_51 = []

        a = [0]*4
        # Mul1 = 0
        
        if value_pac == 'LDPE':
            Mul1 = 0
        elif value_pac == 'PEN':
            Mul1 = 1
        elif value_pac == 'PP':
            Mul1 = 2


        
        if Mul1 == 0:
            a = [4.38330423299747,1.9429754434401,3.5652404973706,-0.387363477044715,-0.122625077217793]
        elif Mul1 == 1:
            a = [1.44999633462306,-0.605898194879269,0.954474134351496,1.01361961267985,-1.57831668460869]
        elif Mul1 ==2:
            a = [-5.83330056762053,-1.33707724856083,-4.5197146317221,-0.626256135635137,1.70094176182648]
       

        days = [0,50,100,150,200,250,300,350,400,450,500,525]

        for i in range(0,12):

            H1_1 = ((-0.708280087315602 + -0.00230742455300583 * days[i] + 0.0282697592236388 * value_RH + -0.0255472418394408 * value_temp + 0.5 * a[0]))
            H1_11.append(H1_1)

            H1_2 = ((3.78655859383922 + 0.00069845084061436 * days[i] + -0.0170566413656545 * value_RH + -0.104660537738883 * value_temp + 0.5 * a[1]))
            H1_21.append(H1_2)

            H1_3 = ((1.87557144225351 + -0.0035634932498831 * days[i] + 0.023207006361319 * value_RH + -0.115631012786087 * value_temp + 0.5 * a[2]))
            H1_31.append(H1_3)

            H1_4 = ((-4.96950065335479 + -0.00198117680197071 * days[i] + 0.00807502456978327 * value_RH + 0.11511649909585 * value_temp + 0.5 * a[3]))
            H1_41.append(H1_4)

            H1_5 = ((-15.2908940407555 + 0.00888441147395293 * days[i] + 0.067727481836647 * value_RH + 0.240908172050656 * value_temp + 0.5 * a[4]))
            H1_51.append(H1_5)

    

        y = []
        for i in range(0,12):

            x = 4.01843111988337 + 2.69450790068321 * math.tanh(H1_11[i]) + -0.0532904812280805 * math.tanh(H1_21[i]) + -2.81606452017431 * math.tanh(H1_31[i]) + -2.77841774066095 * math.tanh(H1_41[i]) + 6.19784540897458 * math.tanh(H1_51[i])
            y.append(x)
   

        df1=pd.DataFrame({'Days':(days),'AV': y })
        fig = px.scatter(data_frame=df1,  x='Days', y='AV',title="NEUTRAL")
        return fig  

@app.callback(
 Output('our_graph7','figure'),
 [Input('package2_choice','value'),
 Input('input2_RH','value')
 ]
 
)
## Texture
def build_plot(value_pac, value_RH):

    dff = df8[(df8.Package == value_pac) & (min(df8.RH_min) <= value_RH <= max(df8.RH_max))]
    print(dff)
     # & (min(df.RH_min) <= value_RH <= max(df.RH_max))
    value = np.unique(dff.Package)
    print(value)
    days = [0,50,100,150,200,250,300,350,400,450,500,525]

    y = []
    x = []
    if value == 'LDPE':

        for i in range(0,12):

            x = ( -1.291+0.02864 * value_RH) / (1 + np.exp((-1 * (294.7-3.356*value_RH) * -1* ( -0.1615+0.00282*value_RH) + days[i] * -1*( -0.1615+0.00282*value_RH))))
            y.append(x)
            print(y,"y")

    if value == 'PEN':

        for i in range(0,12):       

            x = ( -1.418+0.03023*value_RH) / (1 + np.exp((-1 * (161.5-1.044*value_RH) * -1*( -0.0544+.00096*value_RH) + days[i] * -1*( -0.0544+.00096*value_RH))))
            y.append(x)

    if value == 'PP':

        for i in range(0,12): 

            x = ( -1.829+0.03536*value_RH) / (1 + np.exp((-1 * (216.7 - 1.995*value_RH) * -1*( -0.0282+0.000727*value_RH) + days[i] * -1*( -0.0282+0.000727*value_RH))))
            y.append(x)

    if value == 'No Pack':

        for i in range(0,12): 

            x = ( -0.2703+0.01531*value_RH) / (1 + np.exp((-1 * (158.3-1.908*value_RH) * -1*(0.000000000000001023* np.exp(0.426862117407512*value_RH)) + days[i] * -1*(0.000000000000001023* np.exp(0.426862117407512*value_RH)))))
            y.append(x)
    

    df1=pd.DataFrame({'Days':(days),'F/H (Rift Ratio)': y })
    fig = px.scatter(data_frame=df1,  x='Days', y='F/H (Rift Ratio)',title="TEXTURE")
    return fig
    # return "yes"
    


if __name__ == '__main__':
 app.run_server(debug=False)
