import streamlit as st
from connect_data_warehouse import query_job_listings

def layout():
    df = query_job_listings()
    st.title('Job Listings Dashboard')
    st.write("## Detaljerad Jobbdata")
    st.dataframe(df)


if __name__ == "__main__":
    layout()