import streamlit as st
from database import add_data_booking
from database import add_data_customer
from database import add_data_feedback
from database import add_data_places
from database import add_data_information
from database import add_data_travel_agent




def create(table):
    if table=='booking':
        col1, col2 = st.columns(2)
        with col1:
            bid = st.text_input("bid:")
            aid = st.text_input("aid:")
            fname =  st.text_input("fname:")
            lname =  st.text_input("lname:")

        with col2:
            email = st.text_input("email:")
            city = st.text_input("city:")
            fphone = st.text_input("fphone:")
            fdesti = st.text_input("fdesti:")
            cost = st.text_input("cost:")


        if st.button("Add data"):
            add_data_booking(bid, aid, fname, lname, email,city,fphone,fdesti,cost)
            st.success("Successfully booked : {}".format(fname))

    elif table=='customer':
        col1, col2 = st.columns(2)
        with col1:
            cid = st.text_input("cid:")
            fname = st.text_input("fname:")
            lname =  st.text_input("lname:")

        with col2:
            email = st.text_input("email:")
            city = st.text_input("city:")
            phone = st.text_input("phone:")


        if st.button("Add data"):
            add_data_customer(cid,fname, lname, email,city,phone)
            st.success("Successfully added : {}".format(cid))
    elif table == 'feedback':
        col1, col2 = st.columns(2)
        with col1:
            id = st.text_input("id:")
            name = st.text_input("name:")
        with col2:
            email = st.text_input("email:")
            feedbk = st.text_input("feedbk:")

        if st.button("Add data"):
            add_data_feedback(id, name,email, feedbk)
            st.success("Successfully added : {}".format(id))

    elif table == 'places':
        col1, col2 = st.columns(2)
        with col1:
            pid = st.text_input("pid:")
            pname = st.text_input("pname:")
        with col2:
            pcity = st.text_input("pcity:")

        if st.button("Add data"):
            add_data_places(pid, pname, pcity)
            st.success("Successfully added : {}".format(pid))
    elif table == 'information':
        col1, col2 = st.columns(2)
        with col1:
            pname = st.text_input("pname:")
            pid = st.text_input("pid:")
            cost = st.text_input("cost:")
        pdescription = st.text_input("pdescription:")

        if st.button("Add data"):
            add_data_information(pname, pid, cost, pdescription)
            st.success("Successfully added : {}".format(pid))
    elif table == 'travel_agent':
        col1, col2 = st.columns(2)
        with col1:
            aid = st.text_input("aid:")
            afname = st.text_input("afname:")
            alname = st.text_input("alname:")

        with col2:
            aemail = st.text_input("aemail:")
            acity = st.text_input("acity:")
            aphone = st.text_input("aphone:")

        if st.button("Add data"):
            add_data_travel_agent(aid, afname, alname, aemail, acity, aphone)
            st.success("Successfully added : {}".format(aid))
