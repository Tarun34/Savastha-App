import streamlit as st
import os
def app():
    path="C:/Users/Tarun/PycharmProjects/minor/test"
    os.chdir(path)
    st.markdown("<h1 style='text-align:center; color:blue; font-family:archia;'>Test Result </h1>",
            unsafe_allow_html=True)
    st.file_uploader("Please upload your Test File")
    os.chdir("C:/Users/Tarun/PycharmProjects/minor")