import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)

with col1 :
    st.image("images/photo.png")

with col2 :
    st.title("Dhanushka Madhushan")
    content = """
    My name is Dhanushka , I am Mechatronic Engineering , I am a Dhanushka
    """

    st.info(content)

content2 = """
    My name is Dhanushka , I am Mechatronic Engineering , I am a Dhanushka
    """

st.info(content2)

col3 , col4 = st.columns(2)
df = pd.read_csv("data.csv",sep=";")
with col3 :
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']}]")

with col4 :
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']}]")