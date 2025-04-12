import streamlit as st
import pandas as pd
import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="melt250143",
        user="root",
        password="Kishore@9729",
        database="ExpensesDB"
    )
@st.cache
def load_data(month):
    conn = create_connection()
    query = f"SELECT * FROM month_{month}_expenses"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title('Monthly Expenses Dashboard')

month = st.selectbox('Select Month', range(1, 13))

df = load_data(month)
st.write(f'Expenses for Month {month}')
st.write(df)

st.bar_chart(df.groupby('category')['amount'].sum())

query = st.text_input('Enter SQL query')
if query:
    conn = create_connection()
    df_query = pd.read_sql(query, conn)
    conn.close()
    st.write(df_query)
