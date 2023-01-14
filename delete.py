import pandas as pd
import streamlit as st
from database import view_only_booked_bid
from database import view_only_customer_cid
from database import view_only_feedback_id
from database import view_only_places_pid
from database import view_only_information_pid
from database import view_only_travel_agent_aid

from database import view_all_data_booking
from database import view_all_data_customer
from database import view_all_data_feedback
from database import view_all_data_places
from database import view_all_data_information
from database import view_all_data_travel_agent

from database import delete_data_booking
from database import delete_data_customer
from database import delete_data_feedback
from database import delete_data_places
from database import delete_data_information
from database import delete_data_travel_agent

def delete(table):
    if table=='booking':
        result = view_all_data_booking()
        df = pd.DataFrame(result, columns=['bid', 'aid', 'fname', 'lname', 'email','city','fphone','fdesti','cost','reward'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealers = [i[0] for i in view_only_booked_bid()]
        selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data_booking(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_all_data_booking()
        df2 = pd.DataFrame(new_result, columns=['bid', 'aid', 'fname', 'lname', 'email','city','fphone','fdesti','cost','reward'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='customer':
        result = view_all_data_customer()
        df = pd.DataFrame(result, columns=['cid','fname', 'lname', 'email','city','phone'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealers = [i[0] for i in view_only_customer_cid()]
        selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data_customer(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_all_data_customer()
        df2 = pd.DataFrame(new_result, columns=['cid','fname', 'lname', 'email','city','phone'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='feedback':
        result = view_all_data_feedback()
        df = pd.DataFrame(result, columns=['id', 'name', 'email','feedbk'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealers = [i[0] for i in view_only_feedback_id()]
        selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data_feedback(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_all_data_feedback()
        df2 = pd.DataFrame(new_result, columns=['id', 'name', 'email','feedbk'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='places':
        result = view_all_data_places()
        df = pd.DataFrame(result, columns=['pid', 'pname', 'pcity'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealers = [i[0] for i in view_only_places_pid()]
        selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data_places(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_all_data_places()
        df2 = pd.DataFrame(new_result, columns=['pid', 'pname', 'pcity'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='information':
        result = view_all_data_information()
        df = pd.DataFrame(result, columns=['pname', 'pid', 'cost', 'pdescription'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealers = [i[0] for i in view_only_information_pid()]
        selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data_information(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_all_data_information()
        df2 = pd.DataFrame(new_result, columns=['pname', 'pid', 'cost', 'pdescription'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='travel_agent':
        result = view_all_data_travel_agent()
        df = pd.DataFrame(result, columns=['aid', 'afname', 'alname', 'aemail', 'acity', 'aphone'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealers = [i[0] for i in view_only_travel_agent_aid()]
        selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data_travel_agent(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_all_data_travel_agent()
        df2 = pd.DataFrame(new_result, columns=['aid', 'afname', 'alname', 'aemail', 'acity', 'aphone'])
        with st.expander("Updated data"):
            st.dataframe(df2)



