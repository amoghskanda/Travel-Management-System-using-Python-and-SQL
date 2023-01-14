import datetime

import pandas as pd
import streamlit as st
from database import view_all_data_booking, view_only_booked_bid, get_book_id, edit_booking_data
from database import view_all_data_customer, view_only_customer_cid, get_customer_id, edit_customer_data
from database import view_all_data_feedback, view_only_feedback_id, get_feed_id, edit_feedback_data
from database import view_all_data_places, view_only_places_pid, get_place_pid, edit_places_data
from database import view_all_data_information, view_only_information_pid, get_info_pid, edit_info_data
from database import view_all_data_travel_agent, view_only_travel_agent_aid, get_agent_aid, edit_agent_data




def update(table):
    if table=='booking':
        result = view_all_data_booking()
        # st.write(result)
        df = pd.DataFrame(result, columns=['bid', 'aid', 'fname', 'lname', 'email','city','fphone','fdesti','cost'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_booked_bid()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_book_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            bid = selected_result[0][0]
            aid = selected_result[0][1]
            fname = selected_result[0][2]
            lname = selected_result[0][3]
            email = selected_result[0][4]
            city = selected_result[0][5]
            fphone = selected_result[0][6]
            fdesti = selected_result[0][7]
            cost=selected_result[0][8]
            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_bid = st.text_input("bid:",bid)
                new_aid = st.text_input("aid:", aid)
                new_fname = st.text_input("fname:", fname)
                new_lname = st.text_input("lname:", lname)
            with col2:
                new_email = st.text_input("email:",email)
                new_city = st.text_input("city:",city)
                new_fphone = st.text_input("fphone:",fphone)
                new_fdesti = st.text_input("fdesti:",fdesti)
                new_cost=st.text_input("cost:",cost)
            if st.button("Update book"):
                edit_booking_data(new_bid, new_aid, new_fname, new_lname, new_email, new_city,new_fphone,new_fdesti,new_cost,bid, aid, fname, lname, email,city,fphone,fdesti,cost)
                st.success("Successfully updated:: {} to ::{}".format(bid, new_bid))

        result2 = view_all_data_booking()
        df2 = pd.DataFrame(result2, columns=['bid', 'aid', 'fname', 'lname', 'email','city','fphone','fdesti','cost'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='customer':
        result = view_all_data_customer()
        # st.write(result)
        df = pd.DataFrame(result, columns=['cid','fname', 'lname', 'email','city','phone'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_customer_cid()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_customer_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            cid = selected_result[0][0]
            fname = selected_result[0][1]
            lname = selected_result[0][2]
            email = selected_result[0][3]
            city = selected_result[0][4]
            phone = selected_result[0][5]

            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_cid = st.text_input("cid:", cid)
                new_fname = st.text_input("fname:", fname)
                new_lname = st.text_input("lname:", lname)

            with col2:
                new_email = st.text_input("email:", email)
                new_city = st.text_input("city:", city)
                new_phone = st.text_input("phone:", phone)
            if st.button("Update book"):
                edit_customer_data(new_cid,new_fname, new_lname, new_email,new_city,new_phone,cid,fname, lname, email,city,phone)
                st.success("Successfully updated:: {} to ::{}".format(cid, new_cid))

        result2 = view_all_data_customer()
        df2 = pd.DataFrame(result2, columns=['cid','fname', 'lname', 'email','city','phone'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='feedback':
        result = view_all_data_feedback()
        # st.write(result)
        df = pd.DataFrame(result, columns=['id', 'name', 'email','feedbk'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_feedback_id()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_feed_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            id = selected_result[0][0]
            name = selected_result[0][1]
            email = selected_result[0][2]
            feedbk = selected_result[0][3]

            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_id = st.text_input("id:", id)
                new_name = st.text_input("name:", name)
            with col2:
                new_email = st.text_input("email:", email)
                new_feedbk = st.text_input("feedbk:", feedbk)

            if st.button("Update book"):
                edit_feedback_data(new_id, new_name,new_email, new_feedbk,id, name,email, feedbk)
                st.success("Successfully updated:: {} to ::{}".format(id, new_id))

        result2 = view_all_data_feedback()
        df2 = pd.DataFrame(result2, columns=['id', 'name', 'email','feedbk'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='places':
        result = view_all_data_places()
        # st.write(result)
        df = pd.DataFrame(result, columns=['pid', 'pname', 'pcity'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_places_pid()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_place_pid(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            pid = selected_result[0][0]
            pname = selected_result[0][1]
            pcity = selected_result[0][2]


            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_pid = st.text_input("pid:", pid)
                new_pname = st.text_input("pname:", pname)
            with col2:
                new_pcity = st.text_input("pcity:", pcity)

            if st.button("Update book"):
                edit_places_data(new_pid, new_pname, new_pcity,pid, pname, pcity)
                st.success("Successfully updated:: {} to ::{}".format(pid, new_pid))

        result2 = view_all_data_places()
        df2 = pd.DataFrame(result2, columns=['pid', 'pname', 'pcity'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='information':
        result = view_all_data_information()
        # st.write(result)
        df = pd.DataFrame(result, columns=['pname', 'pid', 'pdescription', 'cost'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_information_pid()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_info_pid(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            pname = selected_result[0][0]
            pid = selected_result[0][1]
            cost = selected_result[0][3]
            pdescription = selected_result[0][2]


            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_pname = st.text_input("pname:",pname)
                new_pid = st.text_input("pid:",pid)
                new_pdescription = st.text_input("pdescription:", pdescription)
            new_cost = st.text_input("cost:", cost)

            if st.button("Update book"):
                edit_info_data(new_pname, new_pid, new_cost, new_pdescription,pname, pid, cost, pdescription)
                st.success("Successfully updated:: {} to ::{}".format(pid, new_pid))

        result2 = view_all_data_information()
        df2 = pd.DataFrame(result2, columns=['pname', 'pid', 'pdescription', 'cost'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='travel_agent':
        result = view_all_data_travel_agent()
        # st.write(result)
        df = pd.DataFrame(result, columns=['aid', 'afname', 'alname', 'aemail', 'acity', 'aphone'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_travel_agent_aid()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_agent_aid(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            aid = selected_result[0][0]
            afname = selected_result[0][1]
            alname = selected_result[0][2]
            aemail = selected_result[0][3]
            acity = selected_result[0][4]
            aphone = selected_result[0][5]

            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_aid = st.text_input("aid:",aid)
                new_afname = st.text_input("afname:",afname)
                new_alname = st.text_input("alname:",alname)

            with col2:
                new_aemail = st.text_input("aemail:",aemail)
                new_acity = st.text_input("acity:",acity)
                new_aphone = st.text_input("aphone:",aphone)

        if st.button("Update book"):
                edit_agent_data(new_aid, new_afname, new_alname, new_aemail, new_acity, new_aphone,aid, afname, alname, aemail, acity, aphone)
                st.success("Successfully updated:: {} to ::{}".format(aid, new_aid))

        result2 = view_all_data_travel_agent()
        df2 = pd.DataFrame(result2, columns=['aid', 'afname', 'alname', 'aemail', 'acity', 'aphone'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='information':
        result = view_all_data_information()
        # st.write(result)
        df = pd.DataFrame(result, columns=['pname', 'pid', 'pdescription', 'cost'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_information_pid()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_info_pid(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            pname = selected_result[0][0]
            pid = selected_result[0][1]
            cost = selected_result[0][3]
            pdescription = selected_result[0][2]


            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_pname = st.text_input("pname:",pname)
                new_pid = st.text_input("pid:",pid)
                new_pdescription = st.text_input("pdescription:", pdescription)
            new_cost = st.text_input("cost:", cost)

            if st.button("Update book"):
                edit_info_data(new_pname, new_pid, new_cost, new_pdescription,pname, pid, cost, pdescription)
                st.success("Successfully updated:: {} to ::{}".format(pid, new_pid))

        result2 = view_all_data_information()
        df2 = pd.DataFrame(result2, columns=['pname', 'pid', 'pdescription', 'cost'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='travel_agent':
        result = view_all_data_travel_agent()
        # st.write(result)
        df = pd.DataFrame(result, columns=['aid', 'afname', 'alname', 'aemail', 'acity', 'aphone'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_travel_agent_aid()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_agent_aid(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            aid = selected_result[0][0]
            afname = selected_result[0][1]
            alname = selected_result[0][2]
            aemail = selected_result[0][3]
            acity = selected_result[0][4]
            aphone = selected_result[0][5]

            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_aid = st.text_input("aid:",aid)
                new_afname = st.text_input("afname:",afname)
                new_alname = st.text_input("alname:",alname)

            with col2:
                new_aemail = st.text_input("aemail:",aemail)
                new_acity = st.text_input("acity:",acity)
                new_aphone = st.text_input("aphone:",aphone)

        if st.button("Update book"):
                edit_agent_data(new_aid, new_afname, new_alname, new_aemail, new_acity, new_aphone,aid, afname, alname, aemail, acity, aphone)
                st.success("Successfully updated:: {} to ::{}".format(aid, new_aid))

        result2 = view_all_data_travel_agent()
        df2 = pd.DataFrame(result2, columns=['aid', 'afname', 'alname', 'aemail', 'acity', 'aphone'])
        with st.expander("Updated data"):
            st.dataframe(df2)