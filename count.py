import streamlit as st
import pandas as pd
from database import counter

def count():

    if st.button('show'):
        df=pd.DataFrame(counter(),columns=['number of customers'])
        st.dataframe(df)

