import streamlit as st
from connect_data_warehouse import query_job_listings

def layout():

    df = query_job_listings()
    st.markdown("## Find advertisement")

    cols = st.columns(2)
    with cols[0]:
        selected_company = st.selectbox(
            "Select a company:", df["EMPLOYER_NAME"].unique()
        )

    with cols[1]:
        selected_headline = st.selectbox(
            "Select an advertisement:",
            df.query("EMPLOYER_NAME == @selected_company")["HEADLINE"],
        )

    st.markdown("### Job ad")
    st.markdown(
        df.query(
            "HEADLINE == @selected_headline and EMPLOYER_NAME == @selected_company"
        )["DESCRIPTION_FORMATTED"].values[0],
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    layout()