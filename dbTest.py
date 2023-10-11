import sqlite3
import pandas as pd
import streamlit as st

# conn = sqlite3.connect('my_data.db')
# # c = conn.cursor()

# a = pd.read_sql("Select * From categories", conn)
# print(a)

conn = st.experimental_connection('my_data', type='sql')
categories = conn.query('SELECt * FROM categories')
st.dataframe(categories)