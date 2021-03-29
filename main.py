import numpy as np
import pandas as pd
import plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

Read Data from the downloaded file
df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
print(df.head())
print(df.tail())

#clean data
df = df.drop("AverageTemperatureUncertainty", axis=1)

#rename columns
rename columns
df = df.rename(columns={'dt':'Date'})
df = df.rename(columns={'AverageTemperature':'AvTemp'})

#Handlng null values
df = df.dropna()

#Data Preprocessing
df_countries = df.groupby( ['Country','Date']).sum().reset_index().sort_values('Date', ascending=False)
print(df_countries)

start_date = '2000-01-01'
end_date = '2002-01-01'
mask = (df_countries['Date'] > start_date) & (df_countries['Date'] <= end_date)
df_countries = df_countries.loc[mask]
df_countries.head(10)

#Creating the visualization
fig = go.Figure(data=go.Choropleth( locations = df_countries['Country'], locationmode = 'country names', z = df_countries['AvTemp'], colorscale = 'Reds', marker_line_color = 'black', marker_line_width = 0.5, ))
fig.update_layout( title_text = 'Climate Change', title_x = 0.5, geo=dict( showframe = False, showcoastlines = False, projection_type = 'equirectangular' ) ) 
#fig.show()

df_countrydate = df_countries.groupby(['Date','Country']). sum().reset_index()
fig = px.choropleth(df_countrydate, locations="Country", locationmode = "country names", color="AvTemp", hover_name="Country", animation_frame="Date" )

fig.update_layout( title_text = 'Average Temperature Change', title_x = 0.5, geo=dict( showframe = False, showcoastlines = False, ))
fig.show()
