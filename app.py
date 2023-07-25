import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

model = pickle.load(open('model.sav', 'rb'))

st.title('Prediction of Hourly Productivity')
st.sidebar.header('Input Parameters')
image = Image.open('img.jpg')
st.image(image,'')

def user_report():
  T_water = st.sidebar.slider('Water Temperature',20.0,70.0,1.0)
  T_inside_glass = st.sidebar.slider('Inside Glass Temperature',30.0,70.0,0.01)
  Ambient_Temperature = st.sidebar.slider('Ambient Temperature',20.0,40.0,0.01)
  Irradiance = st.sidebar.slider('Irradiance',0.0,1000.0,0.01)
  mirror_dimensions = ['No Mirror', '25cm X 50cm','50cm X 50cm','75cm X 50cm']
  result = st.sidebar.selectbox('Mirror', mirror_dimensions)
  if result=='No Mirror':
      Mirror = 0
  elif result=='25cm X 25cm':
      Mirror = 1
  elif result=='25cm X 50cm':
      Mirror = 2
  else:
      Mirror = 3

  user_report_data = {
    'T_water': T_water,
    'T_inside_glass': T_inside_glass,
    'Ambient_Temperature': Ambient_Temperature,
    'Irradiance': Irradiance,
    'Mirror': Mirror  
  }

  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('Input Parameters')
st.write(user_data)

hourly_productivity = model.predict(user_data)
st.subheader('Hourly Productivity')
st.subheader(str(np.round(hourly_productivity[0], 4)) + ' Kg/m2')
