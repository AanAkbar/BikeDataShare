import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

 
uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)




