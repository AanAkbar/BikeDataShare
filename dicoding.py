import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.header('Dicoding Analisis Data :sparkles:')

st.subheader('Bike sharing Dataset')

path = "day.csv"
data = pd.read_csv(path)
data

st.subheader("Count of Rentals Per Month")

path = "day.csv"
data = pd.read_csv(path)

df = pd.DataFrame(data[1:13], columns = ["mnth","cnt"])
st.bar_chart(df)

st.caption('Dapat kita lihat pada diagram batang diatas bahwa puncak penyewaan sepeda terjadi pada bulan 6-9 dengan puncaknya terjadi dibulan 6. Pada bulan 6 sepeda yang disewa diketahui sekitar 6000 lebih sepeda. Dengan begitu dapat disimpulkan bahwa puncak penyewaaan sepeda terjadi di bulan 6.')

st.subheader("Bar Chart of Bike Rentals by Season")

df = pd.DataFrame(data[:4], columns = ["season","cnt"])
st.bar_chart(df)

st.caption('Pada musim gugur orang orang cendenrung merental sepeda. Dibandingkan dengan musim lainnya yaitu musim panas, dingin dan semi. Pada musim semi total orang merental sepeda diketahui lebih dari 5000, sedangkan pada musim semi hanya ada lebih dari 2000 sepeda yang dirental. musim semi di tampilkan dengan angka 3 pada grafik tersebut.')

st.subheader("Scatter Plot of Temperature vs. Bike Rentals with Trendline")

df = pd.DataFrame(data[1:90], columns = ["temp","cnt"])
st.scatter_chart(df)

st.caption('Dari grafik scater plot diatas dapat diketahui bahwa semakin tinggi suhuh udara semakin banyak juga penyewa/orang yang merental sepeda. Dari suhu udara 1°C-9°C grafik menunjukan adanya kenaikan, hingga terjadi puncaknya pada suhu udara 9°C.')