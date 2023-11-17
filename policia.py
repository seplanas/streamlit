import streamlit as st
import pandas as pd
import numpy as np
import plotly as px
import plotly.figure_factory as ff
from bokeh.plotting import figure
import matplotlib.pyplot as plt

st.title("Police incidents report")

df = pd.read_csv("Policia.csv")

st.markdown('The data shown...')

mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Incident Subcategory'] = df['Incident Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()
