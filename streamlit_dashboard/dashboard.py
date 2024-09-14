import streamlit as st
from connect_data_warehouse import query_job_listings

def layout():
    st.title('Job Listings Dashboard')
    df = query_job_listings()
    st.write(df)
    
if __name__ == "__main__":
    layout()