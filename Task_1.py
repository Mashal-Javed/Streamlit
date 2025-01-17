import streamlit as st
import pandas as pd
st.title ("Top Universities")
st.header('Single File Upload')
#uploaded_file = st.file_uploader('Upload a file', type=['csv'])
df=pd.read_csv("top universities.csv")
st.write(df)