import main
import news
import vacine
import additional
import null
import last
import beds
import insurance
import style2
import streamlit as st
st.set_page_config(layout='wide',
                    initial_sidebar_state='collapsed',
                    page_icon="Capture.png",
                    page_title="Savastha App")
pages = {
      "Home" : main,
       "News":news,
       "Vaccine":vacine,
       "Self Assement Test":null,
        "Check Beds Availibilty/Helpline no" : beds,
        "Insurance" :insurance,
        "Govt Schemes" :style2,
        "Test Result":last,
       "Additional Information" : additional
}

st.sidebar.image("Capture.png")
selection = st.sidebar.radio("Welcome", list(pages.keys()))
page = pages[selection]
page.app()