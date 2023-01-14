import streamlit as st
import pandas as pd
from database import calc_due_price


def func():
    x=st.text_input('enter id')
    y=st.text_input('enter price')
    if st.button('calc'):
        df=pd.DataFrame(calc_due_price(int(y),int(x)),columns=['due'])
        st.dataframe(df)

