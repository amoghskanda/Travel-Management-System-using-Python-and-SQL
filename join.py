import streamlit as st
import pandas as pd
from database import joind2
from database import joind

def join():

    if st.button('show'):
        df=pd.DataFrame(joind(),columns=['pid','pname','pcity','pdescription','cost'])
        st.dataframe(df)

def join2():
    if st.button('show'):
        df=pd.DataFrame(joind2(),columns=['bid','lname','fdesti','afname','aphone'])
        st.dataframe(df)


