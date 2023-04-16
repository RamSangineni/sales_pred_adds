import streamlit as st
import numpy as np
import pandas as pd
import joblib

loaded_model = joblib.load(open('C:/Users/ramsa/Downloads/Linear Regression(SALES DATA)/model.joblib','rb'))
st.title('Sales Prediction by Advertisement')
TV=st.number_input('Enter amount spent on TV Adds :')
Radio=st.number_input('Enter amount spent on Radio Adds :')
Newspaper=st.number_input('Enter amount spent on Newspaper Adds :')

if st.button('predict sales'):
    prediction=loaded_model.predict([[TV,Radio,Newspaper]])[0][0]
    st.success(prediction)