import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

data = pd.read_excel (r'C:\Users\shagh\Documents\Python Scripts\employment-and-wages-annual-data.xlsx')
df = pd.DataFrame(data)

x = df['Year']
y = df[['Average Employment', 'Total Wage', 'Annual Average Salary', 'Establishments']] 

figl = make_subplots(rows=len(y), cols=1, shared_xaxes=True, vertical_spacing=0.03)

for i in range(len(y)):
    figl.add_trace(go.Line(x = df[x], y = df[y[i]],name=y[i]),row=len(y)-i, col=1)
plotly_chart(figl).show()