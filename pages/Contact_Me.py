import streamlit as st
from sendEmail import send_email


st.header("Contact Me")
# The contact me form set up
with st.form(key="emailForm"):
    userEmail = st.text_input("Your Email Address")
    rawMessage = st.text_area("Your Message")
    message = f"""\
Subject: New email from {userEmail}

From: {userEmail}
{rawMessage}
"""
    submitBtn = st.form_submit_button("Submit")
    # When submitBtn is pressed comes True and the email will be send
    if submitBtn:
        send_email(message)
        st.info("Email send successfully. Your email will be answer as soon as possible.")