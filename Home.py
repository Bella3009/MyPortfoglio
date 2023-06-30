import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")
projects = 13

st.title("My Profile")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")
    
with col2:
    st.title("Sara Bella Gauci")
    content = f"""
    Hello, I am Sara! I am a beginner in coding and welcome to my first website using Python. 
    I still am learning and want to improve my coding skills and make it my career. 
    At the moment the moment I only have {projects} projects ready but I will slowly add more and of different coding languages.
    """
    st.info(content)
    
st.write("Below you can find some of the apps I have built. Feel free to contact me.")

# The list represent the ratio for how the columns have to be wide.
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# sep argument is by default ","
df = pd.read_csv("AppList.csv")

with col3:
    for index, row in df[:projects].iterrows():
        if index % 2 == 0:
            lan = row['language']
            if "," in lan:
                lang = "Languages"
            else:
                lang = "Language"
            st.header(row["title"])
            st.write(row["description"])
            st.write(f"{lang} used: {row['language']}")
            st.image("images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")
            # This is the special syntax for a website url.
            # "[Source Code](url)" Source code is the text displayed in the website

with col4:
    for index, row in df[:projects].iterrows():
        if index % 2 != 0:
            lan = row['language']
            if "," in lan:
                lang = "Languages"
            else:
                lang = "Language"
            st.header(row["title"])
            st.write(row["description"])
            st.write(f"{lang} used: {row['language']}")
            st.image("images/"+row["image"])
            st.write(f"[Source Code]({row['url']})")
