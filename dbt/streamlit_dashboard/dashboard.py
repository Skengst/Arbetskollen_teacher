import streamlit as st
from connect_data_warehouse import query_job_listings

def layout():
    st.set_page_config(
    page_title="NAME OF THE COMPANY",
    page_icon="🧊",
    layout="wide")
    st.title('Job Listings Dashboard')
    df = query_job_listings()
    st.text("Placeholder of number of ads ")
    st.write(df)
    
if __name__ == "__main__":
    layout()
    
