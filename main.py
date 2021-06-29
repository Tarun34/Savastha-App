import streamlit as st
import pandas as pd
import plotly.express as px
import time
from  PIL import Image
from datetime import datetime
def app():

    st.markdown("<h4 style='text-align: center; color: grey; font-family:archia;'>Search your state</h4>", unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    def remote_css(url):
        st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

    def icon(icon_name):
        st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

    local_css("style.css.html")
    #remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
    #icon("search")
    buff,col,buff1 = st.beta_columns([2,3,2])
    selected = col.text_input("", "Search...")
    f,g,p =st.beta_columns([5,1.5,5])
    now = datetime.now()
    g.write("%s:%s:%s  (%s/%s/%s)" % (now.hour, now.minute,now.second,now.day, now.month, now.year))
    time.sleep(1)
    st.image("new.png")
    col3,col4=st.beta_columns(2)
    col3.markdown("<h1 <p style ='font-family:archia;'text-align: center; color: black;'>India</p></h1>", unsafe_allow_html=True)
    col4.markdown("<h1 <p style ='font-family:archia;'text-align: center; color: black;'>Spread Trend</p></h1>", unsafe_allow_html=True)
    #st.video("Preventing.mp4")
    world_df = pd.read_csv("world.csv")
    vaccine_df = pd.read_csv("vaccine.csv")
    cases_df = pd.read_csv("cases.csv")
    vaccine = vaccine_df[vaccine_df.State =="India"]
    india_df = world_df[world_df.location == "India"]
    test_df = pd.read_csv("testing.csv")
    #st.header("Cases In Last 24 Hours")
    #st.dataframe(india_df.tail(1))

    col1,col2=st.beta_columns(2)
    with col1:
        st.image("Capture1.png")
        pop = 1380004385
        total_cases=india_df.loc[37939]["total_cases"]
        st.plotly_chart(px.pie(names=["Total Population ", "Infected People"], values=[pop, total_cases],title="Percentage of people Infected in India", width=700, height=300))
        male = vaccine.loc[122]["Male(Individuals Vaccinated)"]
        female = vaccine.loc[122]["Female(Individuals Vaccinated)"]
        trans = vaccine.loc[122]["Transgender(Individuals Vaccinated)"]
        st.plotly_chart(px.pie(names=["Male Vaccinated", "Female Vaccinated", "Transgender Vaccinated", "Population"],
                               values=[male, female, trans, pop], title="Male Female Vaccinated ratio in India",
                               width=700, height=300))
    with col2:
        st.plotly_chart(px.line(india_df,x="date",y="new_cases" , title ="Confirmed",width=700, height=300,template="ggplot2"))
        st.plotly_chart(px.line(india_df , x = "date" , y = "new_deaths" , title = " Deaths",width=700, height=300,template="ggplot2"))
        st.plotly_chart(px.line(india_df, x="date", y="total_tests",title = "Test" ,template = "plotly",width=700,height=300))
        st.plotly_chart(px.line(vaccine,x="Updated On" , y="Total Individuals Vaccinated",title = "Vaccination",width=700, height=300,template ="plotly"))

    test_df = pd.read_csv("testing.csv")
    #positivity_rate = (test_df["Positive"].sum() / test_df["TotalSamples"].sum()) *100
    #st.header("The Positivity Rate in India {}".format(positivity_rate*100))

    if selected == "Andhra Pradesh":
            Andhra_df_test = test_df[test_df["State"]=="Andhra Pradesh"]
            Andhra_df_vaccine = vaccine_df[vaccine_df["State"]=="Andhra Pradesh"]
            Andhra_df = cases_df[cases_df["State/UnionTerritory"]=="Andhra Pradesh"]
            col1,col2=st.beta_columns(2)
            with col2:
                st.markdown("<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                         unsafe_allow_html=True)
                st.plotly_chart(px.line(Andhra_df, x= "Date",y="Confirmed",title = "Cases in Andhra Pradesh",width=700, height=300,template="ggplot2"))
                st.plotly_chart(px.line(Andhra_df_test , x = "Date" , y = "TotalSamples" , title = "Testing in Andhra Pradesh" ,width=700, height=300,template="plotly"))
                st.plotly_chart(px.line(Andhra_df , x="Date", y= "Deaths",title = "Deaths In Andhra Pradesh",width=700, height=300,template="ggplot2"))
                st.plotly_chart(px.line(Andhra_df_vaccine , x="Updated On" , y = "Total Individuals Vaccinated",title ="Vaccination In Andhra Pradesh",width=700, height=300,template="plotly"))
            andhra_pop =49634314
            cases = Andhra_df.loc[14619]["Confirmed"]

            male = Andhra_df_vaccine.loc[333]["Male(Individuals Vaccinated)"]
            female = Andhra_df_vaccine.loc[333]["Female(Individuals Vaccinated)"]
            trans = Andhra_df_vaccine.loc[333]["Transgender(Individuals Vaccinated)"]
            with col1:
                st.markdown("<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Andhra Pradesh</p></h1>", unsafe_allow_html=True)
                st.image("AndhraPradesh.png")
                st.plotly_chart(px.pie(names=["Total Population of Andhra Pradesh", "Infected people in Andhra Pradesh"],
                                   values=[andhra_pop, cases], title="Percentage of people infected in Andhra Pradesh",width=700, height=300))
                st.plotly_chart(px.pie(names = ["Male(Individuals Vaccinated)" , "Female(Individuals Vaccinated)" ,"Transgender(Individuals Vaccinated)","andhra_pop"],values=[male,female,trans,andhra_pop],title= "Male Female Vaccinated Ratio in Andhra Pradesh",width=700, height=300))
    if selected == "Maharashtra":
            m_df = cases_df[cases_df["State/UnionTerritory"] == "Maharashtra"]
            mv_df = vaccine_df[vaccine_df["State"]=="Maharashtra"]
            mt_df = test_df[test_df["State"]=="Maharashtra"]
            col1,col2 = st.beta_columns(2)
            with col2:
                st.markdown(
                    "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                    unsafe_allow_html=True)
                st.plotly_chart(px.line(m_df , x = "Date" , y="Confirmed" , title = "Cases In Maharashta",width=700, height=300,template = "ggplot2"))
                st.plotly_chart(px.line(m_df , x = "Date" , y= "Deaths" , title = "Deaths in Maharashtra",width=700, height=300,template = "ggplot2"))
                st.plotly_chart(px.line(mt_df , x = "Date" , y="TotalSamples"  , title ="Tests in Maharashtra",width=700, height=300,template = "plotly"))
                st.plotly_chart(px.line(mv_df , x = "Updated On" , y="Total Individuals Vaccinated" , title = "Vaccination in Maharshtra",width=700, height=300,template = "plotly"))
            m_pop = 20668000
            total_cases = m_df.loc[14638]["Confirmed"]
            with col1:
                st.markdown(
                    "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Maharashtra</p></h1>",
                    unsafe_allow_html=True)
                st.image("Maharashtra.png")
                st.plotly_chart(px.pie(names =["Total Population" , "Cases"] ,values = [m_pop , total_cases] , title = "Infected people Percentage",width=700, height=300))
                male  = mv_df.loc[2726]["Male(Individuals Vaccinated)"]
                female =mv_df.loc[2726]["Female(Individuals Vaccinated)"]
                trans = mv_df.loc[2726]["Transgender(Individuals Vaccinated)"]
                st.plotly_chart(px.pie(names = ["Male (Individual Vaccinated)" , "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)","Population"] , values =[male,female,trans,m_pop],title = "Male female Vaccinated Ration In Maharashtra",width=700, height=300))
    if selected == "Karnatka":
        k_df = cases_df[cases_df["State/UnionTerritory"] == "Karnataka"]
        kv_df = vaccine_df[vaccine_df["State"]=="Karnataka"]
        kt_df = test_df[test_df["State"]=="Karnataka"]
        col1,col2 = st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            st.plotly_chart(px.line(k_df , x = "Date" , y="Confirmed" , title = "Cases In Karnataka",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(k_df , x = "Date" , y= "Deaths" , title = "Deaths in Karnataka",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(kt_df , x = "Date" , y="TotalSamples"  , title ="Tests in Karnataka",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(kv_df , x = "Updated On" , y="Total Individuals Vaccinated" , title = "Vaccination in Karnataka",width=700,height=300,template="seaborn"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Karnatka </p></h1>",
                unsafe_allow_html=True)
            k_pop = 61095297
            st.image("Karnatka.jpg")
            total_cases = k_df.loc[14633]["Confirmed"]
            st.plotly_chart(px.pie(names =["Total Population" , "Cases"] , values =[k_pop,total_cases],width=700,height=300))
            male = kv_df.loc[2106]["Male(Individuals Vaccinated)"]
            female =kv_df.loc[2106]["Female(Individuals Vaccinated)"]
            trans = kv_df.loc[2106]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names = ["Male (Individual Vaccinated)" , "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)","Population"] , values =[male,female,trans,k_pop],title = "Male female Vaccinated Ration In Karnataka",width=700,height=300))
    if selected == "Kerala":
        ke_df = cases_df[cases_df["State/UnionTerritory"] == "Kerala"]
        kev_df = vaccine_df[vaccine_df["State"]=="Kerala"]
        ket_df = test_df[test_df["State"]=="Kerala"]
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            st.plotly_chart(px.line(ke_df , x = "Date" , y="Confirmed" , title = "Cases In Kerala",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(ke_df , x = "Date" , y= "Deaths" , title = "Deaths in Kerala",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(ket_df , x = "Date" , y="TotalSamples"  , title ="Tests in Kerala",width=700,height=300,template="seaborn"))
            st.plotly_chart(px.line(kev_df , x = "Updated On" , y="Total Individuals Vaccinated" , title = "Vaccination in kerala",width=700,height=300,template ="plotly"))
        with col1:
            ke_pop = 33406061
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Kerala </p></h1>",
                unsafe_allow_html=True)
            st.image("kerala.jpg")
            total_cases = ke_df.loc[14634]["Confirmed"]
            st.plotly_chart(px.pie(names =["Total Population" , "Cases"] , values =[ke_pop,total_cases],title = "Infected people in Kerala"))
            male  = kev_df.loc[2230]["Male(Individuals Vaccinated)"]
            female =kev_df.loc[2230]["Female(Individuals Vaccinated)"]
            trans = kev_df.loc[2230]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names = ["Male (Individual Vaccinated)" , "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)","Population"] , values =[male,female,trans,ke_pop],title = "Male female Vaccinated Ration In Kerala"))
    if selected == "Uttar Pradesh":
        up_df = cases_df[cases_df["State/UnionTerritory"] == "Uttar Pradesh"]
        upv_df = vaccine_df[vaccine_df["State"]=="Uttar Pradesh"]
        upt_df = test_df[test_df["State"]=="Uttar Pradesh"]
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            st.plotly_chart(px.line(up_df , x = "Date" , y="Confirmed" , title = "Cases In Uttar Pradesh",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(up_df , x = "Date" , y= "Deaths" , title = "Deaths in Uttar Pradesh",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(upt_df , x = "Date" , y="TotalSamples"  , title ="Tests in Uttar Pradesh",width=700,height=300,template="plolty"))
            st.plotly_chart(px.line(upv_df , x = "Updated On" , y="Total Individuals Vaccinated" , title = "Vaccination in Uttar Pradesh",width=700,height=300,template="seaborn"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Uttar Pradesh </p></h1>",
                unsafe_allow_html=True)
            up_pop = 199812341
            st.image("Uttar.jpg")
            total_cases = up_df.loc[14652]["Confirmed"]
            st.plotly_chart(px.pie(names =["Total Population" , "Cases"] , values =[up_pop,total_cases],title = "Infected people in Uttar pradesh",width=700,height=300,template="ggplot2"))
            male  = upv_df.loc[4339]["Male(Individuals Vaccinated)"]
            female =upv_df.loc[4339]["Female(Individuals Vaccinated)"]
            trans = upv_df.loc[4339]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names = ["Male (Individual Vaccinated)" , "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)","Population"] , values =[male,female,trans,up_pop],title = "Male female Vaccinated Ratio In Uttar pradesh",width=700,height=300,template="ggplot2"))
    if selected == "Tamil Nadu":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown("<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",unsafe_allow_html=True)
            tn_df = cases_df[cases_df["State/UnionTerritory"] == "Tamil Nadu"]
            tnv_df = vaccine_df[vaccine_df["State"]=="Tamil Nadu"]
            tnt_df = test_df[test_df["State"]=="Tamil Nadu"]
            st.plotly_chart(px.line(tn_df , x = "Date" , y="Confirmed" , title = "Cases In Tamil Nadu",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(tn_df , x = "Date" , y= "Deaths" , title = "Deaths in Tamil Nadu",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(tnt_df , x = "Date" , y="TotalSamples"  , title ="Tests in Tamil Nadu",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(tnv_df , x = "Updated On" , y="Total Individuals Vaccinated" , title = "Vaccination in Tamil Nadu",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Tamil Nadu </p></h1>",
                unsafe_allow_html=True)
            tn_pop = 77841267
            st.image("Tamil.png")
            total_cases = tn_df.loc[14648]["Confirmed"]
            st.plotly_chart(px.pie(names =["Total Population" , "Cases"] , values =[tn_pop,total_cases],title = "Infected in Tamil Nadu"))
            male  = tnv_df.loc[3967]["Male(Individuals Vaccinated)"]
            female =tnv_df.loc[3967]["Female(Individuals Vaccinated)"]
            trans = tnv_df.loc[3967]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names = ["Male (Individual Vaccinated)" , "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)","Population"] , values =[male,female,trans,tn_pop],title = "Male female Vaccinated Ratio In Tamil Nadu"))
    if selected == "Delhi":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown("<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",unsafe_allow_html=True)
            de_df = cases_df[cases_df["State/UnionTerritory"] == "Delhi"]
            dev_df = vaccine_df[vaccine_df["State"]=="Delhi"]
            det_df = test_df[test_df["State"]=="Delhi"]
            st.plotly_chart(px.line(de_df , x = "Date" , y="Confirmed" , title = "Cases In Delhi",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(de_df , x = "Date" , y= "Deaths" , title = "Deaths in Delhi",width=700,height=300,template="ggplot2"))
            st.plotly_chart( px.line(det_df , x = "Date" , y="TotalSamples"  , title ="Tests in Delhi",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(dev_df , x = "Updated On" , y="Total Individuals Vaccinated" , title = "Vaccination in Delhi",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Delhi </p></h1>",
                unsafe_allow_html=True)
            de_pop = 31181000
            st.image("delhi.jpg")
            total_cases = de_df.loc[14626]["Confirmed"]
            st.plotly_chart(px.pie(names =["Total Population" , "Cases"] , values =[de_pop,total_cases],title ="Infected people in Delhi",width=700,height=300))
            male  = dev_df.loc[1238]["Male(Individuals Vaccinated)"]
            female =dev_df.loc[1238]["Female(Individuals Vaccinated)"]
            trans = dev_df.loc[1238]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names = ["Male (Individual Vaccinated)" , "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)","Population"] , values =[male,female,trans,de_pop],title = "Male female Vaccinated Ratio In Delhi",width=700,height=300))
    if selected == "West Bengal":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            wb_df = cases_df[cases_df["State/UnionTerritory"] == "West Bengal"]
            wbv_df = vaccine_df[vaccine_df["State"]=="West Bengal"]
            wbt_df = test_df[test_df["State"]=="West Bengal"]
            st.dataframe(wbv_df.tail(10))
            st.plotly_chart(px.line(wb_df , x = "Date" , y="Confirmed" , title = "Cases In West Bengal",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(wb_df , x = "Date" , y= "Deaths" , title = "Deaths in West Bengal",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(wbt_df , x = "Date" , y="TotalSamples"  , title ="Tests in West Bengal",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(wbv_df , x = "Updated On" , y="Total Individuals Vaccinated" , title = "Vaccination in West Bengal",width=700,height=300,template="plotly"))
        with col1:
            wb_pop = 99609303
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>West Bengal </p></h1>",
                unsafe_allow_html=True)
            st.image("west.jpg")
            total_cases = wb_df.loc[14653]["Confirmed"]
            st.plotly_chart(px.pie(names =["Total Population" , "Cases"] , values =[wb_pop,total_cases],title ="Infected people in West Bengal",width=700,height=300))
            male  = wbv_df.loc[4587]["Male(Individuals Vaccinated)"]
            female =wbv_df.loc[4587]["Female(Individuals Vaccinated)"]
            trans = wbv_df.loc[4587]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names = ["Male (Individual Vaccinated)" , "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)","Population"] , values =[male,female,trans,wb_pop],title = "Male female Vaccinated Ratio In West Bengal",width=700,height=300))
    if selected == "Chhatisgarh":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            c_df = cases_df[cases_df["State/UnionTerritory"] == "Chhattisgarh"]
            cv_df = vaccine_df[vaccine_df["State"]=="Chhattisgarh"]
            ct_df = test_df[test_df["State"]=="Chhattisgarh"]
            st.plotly_chart(px.line(c_df , x = "Date" , y="Confirmed" , title = "Cases In Chhattisgarh",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(c_df , x = "Date" , y= "Deaths" , title = "Deaths in Chhattisgarh",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(ct_df , x = "Date" , y="TotalSamples"  , title ="Tests in Chhattisgarh",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(cv_df , x = "Updated On" , y="Total Individuals Vaccinated" , title = "Vaccination in Chhattisgarh",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Chhatisgarh </p></h1>",
                unsafe_allow_html=True)
            st.image("chattisgarh.jpg")
            c_pop = 25545198
            total_cases = c_df.loc[14624]["Confirmed"]
            st.plotly_chart(px.pie(names =["Total Population" , "Cases"] , values =[c_pop,total_cases],title ="Infected people in Chhattisgarh",width=700,height=300))
            male  = cv_df.loc[990]["Male(Individuals Vaccinated)"]
            female =cv_df.loc[990]["Female(Individuals Vaccinated)"]
            trans = cv_df.loc[990]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names = ["Male (Individual Vaccinated)" , "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)","Population"] , values =[male,female,trans,c_pop],title = "Male female Vaccinated ratio",width=700,height=300))
    if selected == "Rajasthan":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown("<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",unsafe_allow_html=True)
            r_df = cases_df[cases_df["State/UnionTerritory"] == "Rajasthan"]
            rv_df = vaccine_df[vaccine_df["State"]=="Rajasthan"]
            rt_df = test_df[test_df["State"]=="Rajasthan"]
            st.plotly_chart(px.line(r_df , x = "Date" , y="Confirmed" , title = "Cases In Rajasthan",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(r_df , x = "Date" , y= "Deaths" , title = "Deaths in Rajasthan",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(rt_df , x = "Date" , y="TotalSamples"  , title ="Tests in Rajasthan",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(rv_df , x = "Updated On" , y="Total Individuals Vaccinated" , title = "Vaccination in Rajasthan",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Rajasthan </p></h1>",
                unsafe_allow_html=True)
            st.image("rajasthan.jpg")
            r_pop = 68548437
            total_cases = r_df.loc[14646]["Confirmed"]
            st.plotly_chart(px.pie(names =["Total Population" , "Cases"] , values =[r_pop,total_cases],title ="Infected people in Rajasthan"))
            male  = rv_df.loc[3718]["Male(Individuals Vaccinated)"]
            female =rv_df.loc[3718]["Female(Individuals Vaccinated)"]
            trans = rv_df.loc[3718]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names = ["Male (Individual Vaccinated)" , "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)","Population"] , values =[male,female,trans,r_pop],title = "Male female Vaccinated Ratio In Rajasthan"))
    if selected == "Gujarat":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            g_df = cases_df[cases_df["State/UnionTerritory"] == "Gujarat"]
            gv_df = vaccine_df[vaccine_df["State"] == "Gujarat"]
            gt_df = test_df[test_df["State"] == "Gujarat"]
            st.plotly_chart(px.line(g_df, x="Date", y="Confirmed", title="Cases In Gujarat",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(g_df, x="Date", y="Deaths", title="Deaths in Gujarat",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(gt_df, x="Date", y="TotalSamples", title="Tests in Gujarat",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(gv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Gujarat",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Gujarat </p></h1>",
                unsafe_allow_html=True)
            st.image("gujrat.jpg")
            g_pop = 68548437
            total_cases = g_df.loc[15060]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[g_pop, total_cases],title="Infected people in Gujarat",width=700,height=300))
            male = gv_df.loc[1486]["Male(Individuals Vaccinated)"]
            female = gv_df.loc[1486]["Female(Individuals Vaccinated)"]
            trans = gv_df.loc[1486]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)","Population"],values =[male,female,trans,g_pop],title = "Male female Vaccinated Ratio",width=700,height=300))
    if selected == "Madhya Pradesh":
         col1,col2=st.beta_columns(2)
         with col2:
             st.markdown(
                 "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                 unsafe_allow_html=True)
             mp_df = cases_df[cases_df["State/UnionTerritory"] == "Madhya Pradesh"]
             mpv_df = vaccine_df[vaccine_df["State"] == "Madhya Pradesh"]
             mpt_df = test_df[test_df["State"] == "Madhya Pradesh"]
             st.plotly_chart(px.line(mp_df, x="Date", y="Confirmed", title="Cases In Madhya Pradesh",width=700,height=300,template="ggplot2"))
             st.plotly_chart(px.line(mp_df, x="Date", y="Deaths", title="Deaths in Madhya Pradesh",width=700,height=300,template="ggplot2"))
             st.plotly_chart(px.line(mpt_df, x="Date", y="TotalSamples", title="Tests in Madhya Pradesh",width=700,height=300,template="plotly"))
             st.plotly_chart(px.line(mpv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Madhya Pradesh",width=700,height=300,template="plotly"))
         with col1:
             st.markdown(
                 "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Madhya Pradesh </p></h1>",
                 unsafe_allow_html=True)
             mp_pop = 72597565
             st.image("madhya.png")
             total_cases = mp_df.loc[15069]["Confirmed"]
             st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[mp_pop, total_cases],title="Infected people in Madhya Pradesh",width=700,height=300))
             male = mpv_df.loc[2602]["Male(Individuals Vaccinated)"]
             female = mpv_df.loc[2602]["Female(Individuals Vaccinated)"]
             trans = mpv_df.loc[2602]["Transgender(Individuals Vaccinated)"]
             st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, mp_pop], title="Male female Vaccinated Ratio",width=700,height=300))
    if selected == "Haryana":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)

            h_df = cases_df[cases_df["State/UnionTerritory"] == "Haryana"]
            hv_df = vaccine_df[vaccine_df["State"] == "Haryana"]
            ht_df = test_df[test_df["State"] == "Haryana"]
            st.plotly_chart(px.line(h_df, x="Date", y="Confirmed", title="Cases In Haryana",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(h_df, x="Date", y="Deaths", title="Deaths in Haryana",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(ht_df, x="Date", y="TotalSamples", title="Tests in Haryana",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(hv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Haryana",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'> Haryana </p></h1>",
                unsafe_allow_html=True)
            st.image("haryana.png")
            h_pop = 25350000
            total_cases = h_df.loc[15061]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[h_pop, total_cases], title="Infected people in Haryana",width=700,height=300))
            male = hv_df.loc[1610]["Male(Individuals Vaccinated)"]
            female = hv_df.loc[1610]["Female(Individuals Vaccinated)"]
            trans = hv_df.loc[1610]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, h_pop], title="Male female Vaccinated Ratio",width=700,height=300))
    if selected == "Odisha":
        col1,col2 =st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            o_df = cases_df[cases_df["State/UnionTerritory"] == "Odisha"]
            ov_df = vaccine_df[vaccine_df["State"] == "Odisha"]
            ot_df = test_df[test_df["State"] == "Odisha"]
            st.plotly_chart(px.line(o_df, x="Date", y="Confirmed", title="Cases In Odisha",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(o_df, x="Date", y="Deaths", title="Deaths in Odisha",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(ot_df, x="Date", y="TotalSamples", title="Tests in Odisha",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(ov_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Odisha",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Odisha </p></h1>",
                unsafe_allow_html=True)
            st.image("odisha.png")
            o_pop = 43700000
            total_cases = o_df.loc[15075]["Confirmed"]
            st.plotly_chart( px.pie(names=["Total Population", "Cases"], values=[o_pop, total_cases], title="Infected people in Odisha",width=700,height=300))
            male = ov_df.loc[3346]["Male(Individuals Vaccinated)"]
            female = ov_df.loc[3346]["Female(Individuals Vaccinated)"]
            trans = ov_df.loc[3346]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, o_pop], title="Male female Vaccinated Ratio",width=700,height=300))
    if selected =="Bihar":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            b_df = cases_df[cases_df["State/UnionTerritory"] == "Bihar"]
            bv_df = vaccine_df[vaccine_df["State"] == "Bihar"]
            bt_df = test_df[test_df["State"] == "Bihar"]
            st.plotly_chart(px.line(b_df, x="Date", y="Confirmed", title="Cases In Bihar",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(b_df, x="Date", y="Deaths", title="Deaths in Bihar",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(bt_df, x="Date", y="TotalSamples", title="Tests in Bihar",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(bv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Bihar",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Bihar</p></h1>",
                unsafe_allow_html=True)
            st.image("bihar.jpg")
            b_pop = 128458570
            total_cases = b_df.loc[15054]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[b_pop, total_cases], title="Infected people in Bihar",width=700,height=300))
            male = bv_df.loc[742]["Male(Individuals Vaccinated)"]
            female = bv_df.loc[742]["Female(Individuals Vaccinated)"]
            trans = bv_df.loc[742]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, b_pop], title="Male female Vaccinated Ratio",width=700,height=300))
    if selected == "Telangana":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            t_df = cases_df[cases_df["State/UnionTerritory"] == "Telangana"]
            tv_df = vaccine_df[vaccine_df["State"] == "Telangana"]
            tt_df = test_df[test_df["State"] == "Telangana"]
            st.plotly_chart(px.line(t_df, x="Date", y="Confirmed", title="Cases In Telangana",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(t_df, x="Date", y="Deaths", title="Deaths in Telangana",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(tt_df, x="Date", y="TotalSamples", title="Tests in Telangana",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(tv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Telangana",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Telangana</p></h1>",
                unsafe_allow_html=True)
            st.image("Telangana.png")
            t_pop = 35200000
            total_cases = t_df.loc[15081]["Confirmed"]
            st.plotly_chart(
            px.pie(names=["Total Population", "Cases"], values=[t_pop, total_cases], title="Infected people in Telangana",width=700,height=300))
            male = tv_df.loc[4091]["Male(Individuals Vaccinated)"]
            female = tv_df.loc[4091]["Female(Individuals Vaccinated)"]
            trans = tv_df.loc[4091]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, t_pop], title="Male female Vaccinated Ratio",width=700,height=300))
    if selected == "Punjab":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            p_df = cases_df[cases_df["State/UnionTerritory"] == "Punjab"]
            pv_df = vaccine_df[vaccine_df["State"] == "Punjab"]
            pt_df = test_df[test_df["State"] == "Punjab"]
            st.plotly_chart(px.line(p_df, x="Date", y="Confirmed", title="Cases In Punjab"))
            st.plotly_chart(px.line(p_df, x="Date", y="Deaths", title="Deaths in Punjab"))
            st.plotly_chart(px.line(pt_df, x="Date", y="TotalSamples", title="Tests in Punjab"))
            st.plotly_chart(px.line(pv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Punjab"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Punjab</p></h1>",
                unsafe_allow_html=True)
            st.image("punjab.png")
            p_pop = 28000000
            total_cases = p_df.loc[15077]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[p_pop, total_cases], title="Infected people in Punjab",height=300,width=700))
            male = pv_df.loc[3594]["Male(Individuals Vaccinated)"]
            female = pv_df.loc[3594]["Female(Individuals Vaccinated)"]
            trans = pv_df.loc[3594]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, p_pop], title="Male female Vaccinated Ratio",height=300,width=700))

    if selected == "Assam":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            A_df = cases_df[cases_df["State/UnionTerritory"] == "Assam"]
            Av_df = vaccine_df[vaccine_df["State"] == "Assam"]
            At_df = test_df[test_df["State"] == "Assam"]
            st.plotly_chart(px.line(A_df, x="Date", y="Confirmed", title="Cases In Assam",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(A_df, x="Date", y="Deaths", title="Deaths in Assam",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(At_df, x="Date", y="TotalSamples", title="Tests in Assam",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(Av_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Assam",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Assam</p></h1>",
                unsafe_allow_html=True)
            st.image("assam.png")
            a_pop = 30900000
            total_cases = A_df.loc[15053]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[a_pop, total_cases], title="Infected people in Assam",height=300,width=700))
            male = Av_df.loc[618]["Male(Individuals Vaccinated)"]
            female = Av_df.loc[618]["Female(Individuals Vaccinated)"]
            trans = Av_df.loc[618]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],
                               values=[male, female, trans, a_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected == "Jharkhand":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            Jh_df = cases_df[cases_df["State/UnionTerritory"] == "Jharkhand"]
            Jhv_df = vaccine_df[vaccine_df["State"] == "Jharkhand"]
            Jht_df = test_df[test_df["State"] == "Jharkhand"]
            st.plotly_chart(px.line(Jh_df, x="Date", y="Confirmed", title="Cases In Jharkhand",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(Jh_df, x="Date", y="Deaths", title="Deaths in Jharkhand",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(Jht_df, x="Date", y="TotalSamples", title="Tests in Jharkhand",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(Jhv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Jharkhand",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'> Jharkhand</p></h1>",
                unsafe_allow_html=True)
            st.image("jharkhand.png")
            jh_pop = 31900000
            total_cases = Jh_df.loc[15064]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[jh_pop, total_cases],title="Infected people in Jharkhand",height=300,width=700))
            male = Jhv_df.loc[1982]["Male(Individuals Vaccinated)"]
            female = Jhv_df.loc[1982]["Female(Individuals Vaccinated)"]
            trans = Jhv_df.loc[1982]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, jh_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected == "Uttarakhand":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            U_df = cases_df[cases_df["State/UnionTerritory"] == "Uttarakhand"]
            Uv_df = vaccine_df[vaccine_df["State"] == "Uttarakhand"]
            Ut_df = test_df[test_df["State"] == "Uttarakhand"]
            st.plotly_chart(px.line(U_df, x="Date", y="Confirmed", title="Cases In Uttarakhand",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(U_df, x="Date", y="Deaths", title="Deaths in Uttarakhand",width=700,height=300,template="ggplot2"))
            st.plotly_chart(px.line(Ut_df, x="Date", y="TotalSamples", title="Tests in Uttarakhand",width=700,height=300,template="plotly"))
            st.plotly_chart(px.line(Uv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Uttarakhand",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Uttarakhand</p></h1>",
                unsafe_allow_html=True)
            st.image("uttrakhand.png")
            U_pop = 10100000
            total_cases = U_df.loc[15083]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[U_pop, total_cases],title="Infected people in Uttarakhand",height=300,width=700))
            male = Uv_df.loc[4463]["Male(Individuals Vaccinated)"]
            female = Uv_df.loc[4463]["Female(Individuals Vaccinated)"]
            trans = Uv_df.loc[4463]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, U_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected == "Jammu and Kashmir":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend </p></h1>",
                unsafe_allow_html=True)
            Jk_df = cases_df[cases_df["State/UnionTerritory"] == "Jammu and Kashmir"]
            Jkv_df = vaccine_df[vaccine_df["State"] == "Jammu and Kashmir"]
            Jkt_df = test_df[test_df["State"] == "Jammu and Kashmir"]
            st.plotly_chart(px.line(Jk_df, x="Date", y="Confirmed", title="Cases In Jammu and Kashmir",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Jk_df, x="Date", y="Deaths", title="Deaths in Jammu and Kashmir",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Jkt_df, x="Date", y="TotalSamples", title="Tests in Jammu and Kashmir",height=300,width=700,template="plotly"))
            st.plotly_chart(px.line(Jkv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Jammu And Kashmir",height=300,))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'> Jammu And Kashmir </p></h1>",
                unsafe_allow_html=True)
            st.image("jk.jpg")
            Jk_pop = 12500000
            total_cases = Jk_df.loc[15063]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[Jk_pop, total_cases],title="Infected people in Jammu And Kashmir",height=300,width=700))
            male = Jkv_df.loc[1858]["Male(Individuals Vaccinated)"]
            female = Jkv_df.loc[1858]["Female(Individuals Vaccinated)"]
            trans = Jkv_df.loc[1858]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)", "Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, Jk_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected == "Himachal Pradesh":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            Hp_df = cases_df[cases_df["State/UnionTerritory"] == "Himachal Pradesh"]
            Hpv_df = vaccine_df[vaccine_df["State"] == "Himachal Pradesh"]
            Hpt_df = test_df[test_df["State"] == "Himachal Pradesh"]
            st.plotly_chart(px.line(Hp_df, x="Date", y="Confirmed", title="Cases In Himachal Pradesh",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Hp_df, x="Date", y="Deaths", title="Deaths in Himachal Pradesh",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Hpt_df, x="Date", y="TotalSamples", title="Tests in Himachal Pradesh",height=300,width=700,template="plotly"))
            st.plotly_chart(px.line(Hpv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Himachal Pradesh",height=300,width=700,template="seaborn"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Himachal Pradesh</p></h1>",
                unsafe_allow_html=True)
            st.image("hp.jpg")
            Hp_pop = 6860000
            total_cases = Hp_df.loc[15062]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[Hp_pop, total_cases],title="Infected people in Himachal Pradesh",height=300,width=700))
            male = Hpv_df.loc[1734]["Male(Individuals Vaccinated)"]
            female = Hpv_df.loc[1734]["Female(Individuals Vaccinated)"]
            trans = Hpv_df.loc[1734]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, Hp_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected == "Goa":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            G_df = cases_df[cases_df["State/UnionTerritory"] == "Goa"]
            Gv_df = vaccine_df[vaccine_df["State"] == "Goa"]
            Gt_df = test_df[test_df["State"] == "Goa"]
            st.plotly_chart(px.line(G_df, x="Date", y="Confirmed", title="Cases In Goa",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(G_df, x="Date", y="Deaths", title="Deaths in Goa",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Gt_df, x="Date", y="TotalSamples", title="Tests in Goa",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Gv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Goa",height=300,width=700,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Goa</p></h1>",
                unsafe_allow_html=True)
            st.image("goa.png")
            G_pop = 1820000
            total_cases = G_df.loc[15059]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[G_pop, total_cases], title="Infected people in Goa",height=300,width=700))
            male = Gv_df.loc[1362]["Male(Individuals Vaccinated)"]
            female = Gv_df.loc[1362]["Female(Individuals Vaccinated)"]
            trans = Gv_df.loc[1362]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, G_pop], title="Male female Vaccinated Ratio",height=300,width=700))

    if selected == "Puducherry":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            P_df = cases_df[cases_df["State/UnionTerritory"] == "Puducherry"]
            Pv_df = vaccine_df[vaccine_df["State"] == "Puducherry"]
            Pt_df = test_df[test_df["State"] == "Puducherry"]
            st.plotly_chart(px.line(P_df, x="Date", y="Confirmed", title="Cases In Puducherry",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(P_df, x="Date", y="Deaths", title="Deaths in Puducherry",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Pt_df, x="Date", y="TotalSamples", title="Tests in Puducherry",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Pv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Puducherry",height=300,width=700,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Puducherry</p></h1>",
                unsafe_allow_html=True)
            st.image("pud.jpg")
            P_pop = 856000
            total_cases = P_df.loc[15076]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[P_pop, total_cases],title="Infected people in Puducherry",height=300,width=700))
            male = Pv_df.loc[3470]["Male(Individuals Vaccinated)"]
            female = Pv_df.loc[3470]["Female(Individuals Vaccinated)"]
            trans = Pv_df.loc[3470]["Transgender(Individuals Vaccinated)"]
        st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, P_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected == "Chandigarh":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            C_df = cases_df[cases_df["State/UnionTerritory"] == "Chandigarh"]
            Cv_df = vaccine_df[vaccine_df["State"] == "Chandigarh"]
            Ct_df = test_df[test_df["State"] == "Chandigarh"]
            st.plotly_chart(px.line(C_df, x="Date", y="Confirmed", title="Cases In Chandigarh",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(C_df, x="Date", y="Deaths", title="Deaths in Chandigarh",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Ct_df, x="Date", y="TotalSamples", title="Tests in Chandigarh",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Cv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Chandigarh",width=700,height=300,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Chandigarh</p></h1>",
                unsafe_allow_html=True)
            st.image("chandi.jpg")
            C_pop = 1060000
            total_cases = C_df.loc[15055]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[C_pop, total_cases],title="Infected people in Chandigarh",height=300,width=700))
            male = Cv_df.loc[866]["Male(Individuals Vaccinated)"]
            female = Cv_df.loc[866]["Female(Individuals Vaccinated)"]
            trans = Cv_df.loc[866]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, C_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected == "Tripura":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            T_df = cases_df[cases_df["State/UnionTerritory"] == "Tripura"]
            Tv_df = vaccine_df[vaccine_df["State"] == "Tripura"]
            Tt_df = test_df[test_df["State"] == "Tripura"]
            st.plotly_chart(px.line(T_df, x="Date", y="Confirmed", title="Cases In Tripura",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(T_df, x="Date", y="Deaths", title="Deaths in Tripura",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Tt_df, x="Date", y="TotalSamples", title="Tests in Tripura",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Tv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Tripura",height=300,width=700,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Tripura</p></h1>",
                unsafe_allow_html=True)
            T_pop =3660000
            st.image("tri.jpg")
            total_cases = T_df.loc[15082]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[T_pop, total_cases],title="Infected people in Tripura",height=300,width=700))
            male = Tv_df.loc[4215]["Male(Individuals Vaccinated)"]
            female = Tv_df.loc[4215]["Female(Individuals Vaccinated)"]
            trans = Tv_df.loc[4215]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, T_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected == "Manipur":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            M_df = cases_df[cases_df["State/UnionTerritory"] == "Manipur"]
            Mv_df = vaccine_df[vaccine_df["State"] == "Manipur"]
            Mt_df = test_df[test_df["State"] == "Manipur"]
            st.plotly_chart(px.line(M_df, x="Date", y="Confirmed", title="Cases In Manipur",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(M_df, x="Date", y="Deaths", title="Deaths in Manipur",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Mt_df, x="Date", y="TotalSamples", title="Tests in Manipur",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Mv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Manipur",template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Manipur</p></h1>",
                unsafe_allow_html=True)
            st.image("manipur.jpg")
            M_pop = 2720000
            total_cases = M_df.loc[15071]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[M_pop, total_cases],title="Infected people in Manipur"))
            male = Mv_df.loc[2850]["Male(Individuals Vaccinated)"]
            female = Mv_df.loc[2850]["Female(Individuals Vaccinated)"]
            trans = Mv_df.loc[2850]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, M_pop], title="Male female Vaccinated Ratio"))
    if selected == "Meghalaya":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            T_df = cases_df[cases_df["State/UnionTerritory"] == "Meghalaya"]
            Tv_df = vaccine_df[vaccine_df["State"] == "Meghalaya"]
            Tt_df = test_df[test_df["State"] == "Meghalaya"]
            st.plotly_chart(px.line(T_df, x="Date", y="Confirmed", title="Cases In Meghalaya",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(T_df, x="Date", y="Deaths", title="Deaths in Meghalaya",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Tt_df, x="Date", y="TotalSamples", title="Tests in Meghalaya",height=300,width=700,template="seabron"))
            st.plotly_chart(px.line(Tv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Meghalaya",height=300,width=700,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Meghalaya</p></h1>",
                unsafe_allow_html=True)
            st.image("megha.jpg")
            T_pop =2650000
            total_cases = T_df.loc[15072]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[T_pop, total_cases],title="Infected people in Meghalaya",height=300,width=700))
            male = Tv_df.loc[2974]["Male(Individuals Vaccinated)"]
            female = Tv_df.loc[2974]["Female(Individuals Vaccinated)"]
            trans = Tv_df.loc[2974]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, T_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected == "Arunachal Pradesh":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            T_df = cases_df[cases_df["State/UnionTerritory"] == "Arunachal Pradesh"]
            Tv_df = vaccine_df[vaccine_df["State"] == "Arunachal Pradesh"]
            Tt_df = test_df[test_df["State"] == "Arunachal Pradesh"]
            st.plotly_chart(px.line(T_df, x="Date", y="Confirmed", title="Cases In Arunachal Pradesh",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(T_df, x="Date", y="Deaths", title="Deaths in Arunachal Pradesh",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Tt_df, x="Date", y="TotalSamples", title="Tests in Arunachal Pradesh",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Tv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Arunachal Pradesh",height=300,width=700,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Arunachal Pradesh </p></h1>",
                unsafe_allow_html=True)
            st.image("arun.png")
            T_pop = 1260000
            total_cases = T_df.loc[15052]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[T_pop, total_cases],title="Infected people in Arunachal Pradesh",height=300,width=700))
            male = Tv_df.loc[494]["Male(Individuals Vaccinated)"]
            female = Tv_df.loc[494]["Female(Individuals Vaccinated)"]
            trans = Tv_df.loc[494]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, T_pop], title="Male female Vaccinated Ratio"))
    if selected == "Nagaland":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            T_df = cases_df[cases_df["State/UnionTerritory"] == "Nagaland"]
            Tv_df = vaccine_df[vaccine_df["State"] == "Nagaland"]
            Tt_df = test_df[test_df["State"] == "Nagaland"]
            st.plotly_chart(px.line(T_df, x="Date", y="Confirmed", title="Cases In Nagaland",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(T_df, x="Date", y="Deaths", title="Deaths in Nagaland",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Tt_df, x="Date", y="TotalSamples", title="Tests in Nagaland",height=300,width=700,template="plotly"))
            st.plotly_chart(px.line(Tv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Nagaland",height=300,width=700,template="seaborn"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Nagaland</p></h1>",
                unsafe_allow_html=True)
            st.image("nagaland.png")
            T_pop = 2280000
            total_cases = T_df.loc[15074]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[T_pop, total_cases],title="Infected people in Nagaland",height=300,width=700))
            male = Tv_df.loc[3223]["Male(Individuals Vaccinated)"]
            female = Tv_df.loc[3223]["Female(Individuals Vaccinated)"]
            trans = Tv_df.loc[3223]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, T_pop], title="Male female Vaccinated Ratio",height=300,width=700))

    if selected == "Ladakh":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            T_df = cases_df[cases_df["State/UnionTerritory"] == "Ladakh"]
            Tv_df = vaccine_df[vaccine_df["State"] == "Ladakh"]
            Tt_df = test_df[test_df["State"] == "Ladakh"]
            st.plotly_chart(px.line(T_df, x="Date", y="Confirmed", title="Cases In Ladakh",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(T_df, x="Date", y="Deaths", title="Deaths in Ladakh",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Tt_df, x="Date", y="TotalSamples", title="Tests in Ladakh",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Tv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Ladakh",height=300,width=700,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Ladakh</p></h1>",
                unsafe_allow_html=True)
            st.image("ladakh.png")
            T_pop = 2740000
            total_cases = T_df.loc[15067]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[T_pop, total_cases],title="Infected people in Ladakh",height=300,width=700))
            male = Tv_df.loc[2354]["Male(Individuals Vaccinated)"]
            female = Tv_df.loc[2354]["Female(Individuals Vaccinated)"]
            trans = Tv_df.loc[2354]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, T_pop], title="Male female Vaccinated Ratio",height=300,width=700))

    if selected == "Sikkim":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            T_df = cases_df[cases_df["State/UnionTerritory"] == "Sikkim"]
            Tv_df = vaccine_df[vaccine_df["State"] == "Sikkim"]
            Tt_df = test_df[test_df["State"] == "Sikkim"]
            st.plotly_chart(px.line(T_df, x="Date", y="Confirmed", title="Cases In Sikkim",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(T_df, x="Date", y="Deaths", title="Deaths in Sikkim",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Tt_df, x="Date", y="TotalSamples", title="Tests in Sikkim",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Tv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Sikkim",height=300,width=700,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Sikkim</p></h1>",
                unsafe_allow_html=True)
            st.image("sikkim.jpg")
            T_pop = 619000
            total_cases = T_df.loc[15079]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[T_pop, total_cases],title="Infected people in Sikkim",height=300,width=700))
            male = Tv_df.loc[3844]["Male(Individuals Vaccinated)"]
            female = Tv_df.loc[3844]["Female(Individuals Vaccinated)"]
            trans = Tv_df.loc[3844]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, T_pop], title="Male female Vaccinated Ratio"))

    if selected == "Mizoram":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            T_df = cases_df[cases_df["State/UnionTerritory"] == "Mizoram"]
            Tv_df = vaccine_df[vaccine_df["State"] == "Mizoram"]
            Tt_df = test_df[test_df["State"] == "Mizoram"]
            st.plotly_chart(px.line(T_df, x="Date", y="Confirmed", title="Cases In Mizoram",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(T_df, x="Date", y="Deaths", title="Deaths in Mizoram",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Tt_df, x="Date", y="TotalSamples", title="Tests in Mizoram",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Tv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Mizoram",height=300,width=700,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Mizoram</p></h1>",
                unsafe_allow_html=True)
            T_pop = 1120000
            st.image("mizoram.png")
            total_cases = T_df.loc[15073]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[T_pop, total_cases],title="Infected people in Mizoram",height=300,width=700))
            male = Tv_df.loc[3098]["Male(Individuals Vaccinated)"]
            female = Tv_df.loc[3098]["Female(Individuals Vaccinated)"]
            trans = Tv_df.loc[3098]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, T_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected =="Dadra and Nagar Haveli and Daman And Diu":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            T_df = cases_df[cases_df["State/UnionTerritory"] == "Dadra and Nagar Haveli and Daman and Diu"]
            Tv_df = vaccine_df[vaccine_df["State"] == "Dadra and Nagar Haveli and Daman and Diu"]
            Tt_df = test_df[test_df["State"] == "Dadra and Nagar Haveli and Daman and Diu"]
            st.plotly_chart(px.line(T_df, x="Date", y="Confirmed", title="Cases In Dadra And Nagar Haveli And Daman And Diu",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(T_df, x="Date", y="Deaths", title="Deaths in Dadra And Nagar Haveli And Daman And Diu",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Tt_df, x="Date", y="TotalSamples", title="Tests in Dadra And Nagar Haveli And Daman And Diu",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Tv_df, x="Updated On", y="Total Individuals Vaccinated",title="Vaccination in Dadra And Nagar Haveli And Daman And Diu",height=300,width=700,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Dadra and Nagar Haveli and Daman and Diu</p></h1>",unsafe_allow_html=True)
            T_pop = 344000
            st.image("dd.jpg")
            total_cases = T_df.loc[15057]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[T_pop, total_cases],title="Infected people in Dadra And Nagar Haveli And Daman And Diu",height=300,width=700))
            male = Tv_df.loc[1114]["Male(Individuals Vaccinated)"]
            female = Tv_df.loc[1114]["Female(Individuals Vaccinated)"]
            trans = Tv_df.loc[1114]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, T_pop], title="Male female Vaccinated Ratio",height=300,width=700))
    if selected == "Andaman and Nicobar Islands":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            T_df = cases_df[cases_df["State/UnionTerritory"] == "Andaman and Nicobar Islands"]
            Tv_df = vaccine_df[vaccine_df["State"] == "Andaman and Nicobar Islands"]
            Tt_df = test_df[test_df["State"] == "Andaman and Nicobar Islands"]
            st.plotly_chart(px.line(T_df, x="Date", y="Confirmed", title="Cases In Andaman And Nicobar Islands",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(T_df, x="Date", y="Deaths", title="Deaths in Andaman And Nicobar Islands",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Tt_df, x="Date", y="TotalSamples", title="Tests in Andaman And Nicobar Islands",height=300,width=700,template="plotly"))
            st.plotly_chart(px.line(Tv_df, x="Updated On", y="Total Individuals Vaccinated",title="Vaccination in Andaman And Nicobar Islands",height=300,width=700,template="seaborn"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Andaman and Nicobar Islands </p></h1>",
                unsafe_allow_html=True)
            st.image("an.jpg")
            T_pop = 434000
            total_cases = T_df.loc[15050]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[T_pop, total_cases],title="Infected people in Andaman And Nicobar Islands",height=300,width=700))
            male = Tv_df.loc[246]["Male(Individuals Vaccinated)"]
            female = Tv_df.loc[246]["Female(Individuals Vaccinated)"]
            trans = Tv_df.loc[246]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, T_pop], title="Male female Vaccinated Ratio",height=300,width=700))

    if selected =="Lakshadweep":
        col1,col2=st.beta_columns(2)
        with col2:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Spread Trend</p></h1>",
                unsafe_allow_html=True)
            T_df = cases_df[cases_df["State/UnionTerritory"] == "Lakshadweep"]
            Tv_df = vaccine_df[vaccine_df["State"] == "Lakshadweep"]
            Tt_df = test_df[test_df["State"] == "Lakshadweep"]
            st.plotly_chart(px.line(T_df, x="Date", y="Confirmed", title="Cases In Lakshadweep",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(T_df, x="Date", y="Deaths", title="Deaths in Lakshadweep",height=300,width=700,template="ggplot2"))
            st.plotly_chart(px.line(Tt_df, x="Date", y="TotalSamples", title="Tests in Lakshadweep",height=300,width=700,template="seaborn"))
            st.plotly_chart(px.line(Tv_df, x="Updated On", y="Total Individuals Vaccinated", title="Vaccination in Lakshadweep",height=300,width=700,template="plotly"))
        with col1:
            st.markdown(
                "<h1 <p style ='font-family:archia' style='text-align: center; color: black;'>Lakshadweep</p></h1>",
                unsafe_allow_html=True)
            T_pop = 64429
            total_cases = T_df.loc[15068]["Confirmed"]
            st.plotly_chart(px.pie(names=["Total Population", "Cases"], values=[T_pop, total_cases],title="Infected people in Lakshadweep",height=300,width=700))
            male = Tv_df.loc[2478]["Male(Individuals Vaccinated)"]
            female = Tv_df.loc[2478]["Female(Individuals Vaccinated)"]
            trans = Tv_df.loc[2478]["Transgender(Individuals Vaccinated)"]
            st.plotly_chart(px.pie(names=["Male (Individual Vaccinated)", "Female (Individual Vaccinated)","Transgender (Individual Vaccinated)", "Population"],values=[male, female, trans, T_pop], title="Male female Vaccinated Ratio",height=300,width=700))

    df=cases_df.groupby("State/UnionTerritory").sum()
    df = df.drop(["Cases being reassigned to states"],axis=0)
    df = df.drop(["Daman & Diu"], axis=0)
    df = df.drop(["Unassigned"], axis=0)
    df = df.drop(["Sno"], axis=1)
    st.table(df)
    st.video("Preventing.mp4")
    img=Image.open(("Capture.png"))
    buff,col,buff=st.beta_columns([4.5,3,4.5])
    col.image(img)
    buff,col4,buff=st.beta_columns(3)
    col.markdown(
        "<h5 <p style ='font-family:archia; text-align: center; color: grey;'>We stand with everyone fighting on the frontlines</p></h5>",unsafe_allow_html=True)
