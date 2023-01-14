# Importing pakages
import streamlit as st
import mysql.connector
from create import create
from database import create_table
from delete import delete
from read import read
from update import update
from func import func
from join import join
from join import join2
from front_query import front_query
from count import count

mydb = mysql.connector.connect(
host="127.0.0.1",
user="root",
password="suyog1131",
port="3306",
database="TMS_PROJECT_PES1UG20CS036",
auth_plugin='mysql_native_password'
)
c = mydb.cursor()

#c.execute("CREATE DATABASE PES1UG20CS036_PROJECT")
c.execute("use TMS_PROJECT_PES1UG20CS036")

def main():
    st.title("TRIP IT")
    menu = ["Add", "View", "Edit", "Remove","return_due","join","join2","count_customers","front_end_query"]
    he=["booking","places","information","customer","feedback","travel_agent"]
    choice = st.sidebar.selectbox("action", menu)
    table=st.sidebar.selectbox("table", he)
    create_table(table)
    if choice == "Add":
        if table=='booking':
            st.subheader("Enter booking Details:")
            create(table)
        elif table=='customer':
            st.subheader("Enter  Details:")
            create(table)
        elif table=='feedback':
            st.subheader("Enter  Details:")
            create(table)
        elif table=='places':
            st.subheader("Enter  Details:")
            create(table)
        elif table=='information':
            st.subheader("Enter  Details:")
            create(table)
        elif table=='travel_agent':
            st.subheader("Enter  Details:")
            create(table)
    elif choice == "View":
        if table=='booking':
            st.subheader("View created tasks")
            read(table)
        elif table=='customer':
            st.subheader("View booking Details:")
            read(table)
        elif table=='feedback':
            st.subheader("View booking Details:")
            read(table)
        elif table=='places':
            st.subheader("View booking Details:")
            read(table)
        elif table=='information':
            st.subheader("View booking Details:")
            read(table)
        elif table=='travel_agent':
            st.subheader("View booking Details:")
            read(table)

    elif choice == "Edit":
        if table=='booking':
            st.subheader("Update created tasks")
            update(table)
        elif table=='customer':
            st.subheader("Update created tasks:")
            update(table)
        elif table=='feedback':
            st.subheader("Update created tasks:")
            update(table)
        elif table=='places':
            st.subheader("Update created tasks:")
            update(table)
        elif table=='information':
            st.subheader("Update created tasks:")
            update(table)
        elif table=='travel_agent':
            st.subheader("Update created tasks:")
            update(table)

    elif choice == "Remove":
        if table=='booking':
            st.subheader("Delete created tasks")
            delete(table)
        elif table=='customer':
            st.subheader("Delete created tasks:")
            delete(table)
        elif table=='feedback':
            st.subheader("Delete created tasks:")
            delete(table)
        elif table=='places':
            st.subheader("Delete created tasks:")
            delete(table)
        elif table=='information':
            st.subheader("Delete created tasks:")
            delete(table)
        elif table=='travel_agent':
            st.subheader("Delete created tasks:")
            delete(table)
    elif choice=='return_due':
        st.subheader("calculate:")
        func()
    elif choice=='join':
        st.subheader("join table places and information:")
        join()

    elif choice=='join2':
        st.subheader("agent & booking :")
        join2()

    elif choice=='count_customers':
        st.subheader("count:")
        count()
    # elif choice=='email_list_curs':
    #     st.subheader("list of emails:")
    #     cursor()
    elif choice=='front_end_query':
        st.subheader("enter query")
        front_query()
    # elif choice=="bookedpackages":
    #     st.subheader("bookedpackages")
    #     bookedpackages()
    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()