import streamlit as st
import pandas as pd
 
uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)



values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)
