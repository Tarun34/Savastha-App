import datetime
import json
import numpy as np
import requests
import pandas as pd
from copy import deepcopy
from fake_useragent import UserAgent
import streamlit as st
import webbrowser
from PIL import Image
def app():
    st.markdown("<h1 style='text-align:justify; color:red; font-family:archia;'>Why Vaccine Is Important </h1>",unsafe_allow_html=True)
    st.video("impvaccine.mp4")
    st.subheader("Please tap on the Vaccine button to Book the slot")
    url ="https://selfregistration.cowin.gov.in/"
    if st.button("Book your Slot"):
        webbrowser.open_new_tab(url)
    st.subheader("Covaxin")
    col2,col1=st.beta_columns([1,3])
    with col2:
        size=(200,300)
        image = Image.open("bharat.jpg")
        image=image.resize(size)
        st.image(image)
    with col1:
        st.write("COVAXIN®, India's indigenous COVID-19 vaccine by Bharat Biotech is developed in collaboration with the Indian Council of Medical Research (ICMR) - National Institute of Virology (NIV).")
        st.write("The indigenous, inactivated vaccine is developed and manufactured in Bharat Biotech's BSL-3 (Bio-Safety Level 3) high containment facility.")
        st.write("The vaccine is developed using Whole-Virion Inactivated Vero Cell derived platform technology. Inactivated vaccines do not replicate and are therefore unlikely to revert and cause pathological effects. They contain dead virus, incapable of infecting people but still able to instruct the immune system to mount a defensive reaction against an infection.")
    st.subheader("Covishiled")
    col3, col4 = st.beta_columns([1,3])
    with col3:
        size=(200,300)
        image1 = Image.open("product_covishield.jpg")
        image1=image1.resize(size)
        st.image(image1)
    with col4:
        st.write("Covishield has been prepared using the viral vector platform which is a totally different technology.")
        st.write("A chimpanzee adenovirus – ChAdOx1 – has been modified to enable it to carry the COVID-19 spike protein into the cells of humans. Well, this cold virus is basically incapable of infecting the receiver but can very well teach the immune system to prepare a mechanism against such viruses.")
        st.write("The exact technology was used to prepare vaccines for viruses like Ebola.")

    @st.cache(allow_output_mutation=True, suppress_st_warning=True)
    def load_mapping():
        df = pd.read_csv("district_mapping.csv")
        return df

    def filter_column(df, col, value):
        df_temp = deepcopy(df.loc[df[col] == value, :])
        return df_temp

    def filter_capacity(df, col, value):
        df_temp = deepcopy(df.loc[df[col] > value, :])
        return df_temp

    @st.cache(allow_output_mutation=True)
    def Pageviews():
        return []

    mapping_df = load_mapping()

    rename_mapping = {
        'date': 'Date',
        'min_age_limit': 'Minimum Age Limit',
        'available_capacity': 'Available Capacity',
        'vaccine': 'Vaccine',
        'pincode': 'Pincode',
        'name': 'Hospital Name',
        'state_name': 'State',
        'district_name': 'District',
        'block_name': 'Block Name',
        'fee_type': 'Fees'
    }

    st.title('CoWIN Vaccination Slot Availability')
    st.info('The CoWIN APIs are geo-fenced so sometimes you may not see an output! Please try after sometime ')

    valid_states = list(np.unique(mapping_df["state_name"].values))

    left_column_1, center_column_1, right_column_1 = st.beta_columns(3)
    with left_column_1:
        numdays = st.slider('Select Date Range', 0, 100, 3)

    with center_column_1:
        state_inp = st.selectbox('Select State', [""] + valid_states)
        if state_inp != "":
            mapping_df = filter_column(mapping_df, "state_name", state_inp)

    mapping_dict = pd.Series(mapping_df["district id"].values,
                             index=mapping_df["district name"].values).to_dict()

    unique_districts = list(mapping_df["district name"].unique())
    unique_districts.sort()
    with right_column_1:
        dist_inp = st.selectbox('Select District', unique_districts)

    DIST_ID = mapping_dict[dist_inp]

    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]

    temp_user_agent = UserAgent()
    browser_header = {'User-Agent': temp_user_agent.random}

    final_df = None
    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(
            DIST_ID, INP_DATE)
        response = requests.get(URL, headers=browser_header)
        if (response.ok) and ('centers' in json.loads(response.text)):
            resp_json = json.loads(response.text)['centers']
            if resp_json is not None:
                df = pd.DataFrame(resp_json)
                if len(df):
                    df = df.explode("sessions")
                    df['min_age_limit'] = df.sessions.apply(lambda x: x['min_age_limit'])
                    df['vaccine'] = df.sessions.apply(lambda x: x['vaccine'])
                    df['available_capacity'] = df.sessions.apply(lambda x: x['available_capacity'])
                    df['date'] = df.sessions.apply(lambda x: x['date'])
                    df = df[["date", "available_capacity", "vaccine", "min_age_limit", "pincode", "name", "state_name",
                             "district_name", "block_name", "fee_type"]]
                    if final_df is not None:
                        final_df = pd.concat([final_df, df])
                    else:
                        final_df = deepcopy(df)
            else:
                st.error("No rows in the data Extracted from the API")
    #     else:
    #         st.error("Invalid response")

    if (final_df is not None) and (len(final_df)):
        final_df.drop_duplicates(inplace=True)
        final_df.rename(columns=rename_mapping, inplace=True)

        left_column_2, center_column_2, right_column_2, right_column_2a, right_column_2b = st.beta_columns(5)
        with left_column_2:
            valid_pincodes = list(np.unique(final_df["Pincode"].values))
            pincode_inp = st.selectbox('Select Pincode', [""] + valid_pincodes)
            if pincode_inp != "":
                final_df = filter_column(final_df, "Pincode", pincode_inp)

        with center_column_2:
            valid_age = [18, 45]
            age_inp = st.selectbox('Select Minimum Age', [""] + valid_age)
            if age_inp != "":
                final_df = filter_column(final_df, "Minimum Age Limit", age_inp)

        with right_column_2:
            valid_payments = ["Free", "Paid"]
            pay_inp = st.selectbox('Select Free or Paid', [""] + valid_payments)
            if pay_inp != "":
                final_df = filter_column(final_df, "Fees", pay_inp)

        with right_column_2a:
            valid_capacity = ["Available"]
            cap_inp = st.selectbox('Select Availablilty', [""] + valid_capacity)
            if cap_inp != "":
                final_df = filter_capacity(final_df, "Available Capacity", 0)

        with right_column_2b:
            valid_vaccines = ["COVISHIELD", "COVAXIN"]
            vaccine_inp = st.selectbox('Select Vaccine', [""] + valid_vaccines)
            if vaccine_inp != "":
                final_df = filter_column(final_df, "Vaccine", vaccine_inp)

        table = deepcopy(final_df)
        table.reset_index(inplace=True, drop=True)
        st.table(table)
    else:
        st.error("Unable to fetch data currently, please try after sometime")

    pageviews = Pageviews()
    pageviews.append('dummy')

    img = Image.open(("Capture.png"))
    buff, col, buff = st.beta_columns([4.5, 3, 4.5])
    col.image(img)
    buff, col4, buff = st.beta_columns(3)
    col.markdown( "<h5 <p style ='font-family:archia; text-align: center; color: grey;'>We stand with everyone fighting on the frontlines</p></h5>",unsafe_allow_html=True)