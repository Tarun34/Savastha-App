import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
def app():
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center; color:grey; font-family:archia;  font-size :50px;'> Government Scheme  </h1>",unsafe_allow_html=True)
    local_css("style2.html")
    scheme_df = pd.read_excel("scheme.xlsx")
    scheme_df=scheme_df.drop(["Sr. No."],axis=1)
    scheme_df = scheme_df.drop(["Unnamed: 5"], axis=1)
    opt=scheme_df.copy("Scheme Name")
    select = st.selectbox("Select the Scheme name",opt)
    scheme = scheme_df[scheme_df["Scheme Name"]==select]
    st.table(scheme)
    if st.button("Click more Infomation"):
        webbrowser.open_new_tab("https://www.india.gov.in/my-government/schemes/")
    img = Image.open(("Capture.png"))
    buff, col, buff = st.beta_columns([4.5, 3, 4.5])
    col.image(img)
    buff, col4, buff = st.beta_columns(3)
    col.markdown(
        "<h5 <p style ='font-family:archia; text-align: center; color: grey;'>We stand with everyone fighting on the frontlines</p></h5>",
        unsafe_allow_html=True)

