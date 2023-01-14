import streamlit as st
import mysql.connector

mydb = mysql.connector.connect(
host="127.0.0.1",
user="root",
password="suyog1131",
database="TMS_PROJECT_PES1UG20CS036",
port="3306"


)
c = mydb.cursor()
c.execute("use TMS_PROJECT_PES1UG20CS036")

#MYSQL WORKBENCH