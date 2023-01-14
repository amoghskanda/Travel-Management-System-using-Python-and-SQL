import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data_booking
from database import view_all_data_customer
from database import view_all_data_feedback
from database import view_all_data_places
from database import view_all_data_information
from database import view_all_data_travel_agent



def read(table):
    if table=='booking':
        result = view_all_data_booking()
        # st.write(result)
        df = pd.DataFrame(result, columns=['bid', 'aid', 'fname', 'lname', 'email','city','fphone','fdesti','cost'])
        with st.expander("View all bookings"):
            st.dataframe(df)
        with st.expander("user Location"):
            task_df = df['city'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            #p1 = px.pie(task_df, names='index', values='city')
            #st.plotly_chart(p1)
    elif table=='customer':
        result = view_all_data_customer()
        # st.write(result)
        df = pd.DataFrame(result, columns=['cid','fname', 'lname', 'email','city','phone'])
        with st.expander("View all bookings"):
            st.dataframe(df)
        with st.expander("user Location"):
            task_df = df['city'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='city')
            st.plotly_chart(p1)
    elif table=='feedback':
        result = view_all_data_feedback()
        # st.write(result)
        df = pd.DataFrame(result, columns=['id', 'name', 'email','feedbk'])
        with st.expander("View all bookings"):
            st.dataframe(df)
    elif table=='places':
        result = view_all_data_places()
        # st.write(result)
        df = pd.DataFrame(result, columns=['pid', 'pname', 'pcity'])
        with st.expander("View all bookings"):
            st.dataframe(df)
    elif table=='information':
        result = view_all_data_information()
        # st.write(result)
        df = pd.DataFrame(result, columns=['pname', 'pid', 'pdescription', 'cost'])
        with st.expander("View all bookings"):
            st.dataframe(df)
    elif table=='travel_agent':
        result = view_all_data_travel_agent()
        # st.write(result)
        df = pd.DataFrame(result, columns=['aid', 'afname', 'alname', 'aemail', 'acity', 'aphone'])
        with st.expander("View all bookings"):
            st.dataframe(df)
        with st.expander("user Location"):
            task_df = df['acity'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='acity')
            st.plotly_chart(p1)

