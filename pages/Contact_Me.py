import streamlit as st

st.header("Contact Me")

with st.form(key="emailForm"):
    userEmail = st.text_input("Your Email Address")
    rawMessage = st.text_area("Your Message")
    submitBtn = st.form_submit_button("Submit")