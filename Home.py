import streamlit as st
import pandas as pd
import math

st.set_page_config(layout="wide")

st.title("My Profile")
col1, col2 = st.columns(2)

with col1:
    st.images("images/photos.png")
    
with col2:
    st.title("Sara Bella Gauci")
    content = """
    Hello, I am Sara! I am a beginner in coding and welcome to my first website using Python. I still am learning and want improve my coding skills and make it my career. 
    """
    st.info(content)
    
st.write("Below you can find some of the apps I have built. Feel free to contact me.")

col3, col4 = st.columns(2)

df = pandas.read_csv("AppList.csv", sep=";") # sep argument is by default ","

len_list = len(df)
div_list = math.ceil(len_list/2)

with col3:
    for index, row in df[:div_list].iterrows():
        st.header(row["Title"])
        st.write(row["Description"])

with col4:
    for index, row in df[div_list:].iterrows():
        st.header(row["Title"])
        st.write(row["Description"])
