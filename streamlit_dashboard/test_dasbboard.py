import streamlit as st
import pandas as pd
import altair as alt
from connect_data_warehouse import query_job_listings

st.set_page_config(layout="wide")

def layout():
    st.title('Job Listings Dashboard')

    # Hämta data
    df = query_job_listings()

    # Konvertera alla kolumnnamn till versaler
    df.columns = df.columns.str.upper()

    # KPI cards
    total_jobs = df.shape[0]
    total_vacancies = df['VACANCIES'].sum()
    most_common_occupation = df['OCCUPATION'].mode()[0]
    job_per_occupation = df.groupby('OCCUPATION')['VACANCIES'].sum().reset_index(name='TOTAL_VACANCIES')
    job_per_occupation = job_per_occupation.sort_values(by='TOTAL_VACANCIES', ascending=False)
    job_per_employer = df.groupby('EMPLOYER_NAME').size().reset_index(name='ANTAL_JOBB')
    
    st.write("### KPI:er")
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Totala jobb", total_jobs)
    col2.metric("Totala lediga platser", total_vacancies)
    col3.metric("Vanligaste yrket", most_common_occupation)

    col1, col2 = st.columns([2,1])

    with col1:
        st.write("### Lista över tjänster/yrke")
        st.dataframe(job_per_occupation)

    with col2:
        st.write("### Antal jobb")
        st.dataframe(job_per_employer)

    # Line chart för relevans över tid
    st.write("### Relevans över tid")
    df['APPLICATION_DEADLINE'] = pd.to_datetime(df['APPLICATION_DEADLINE'], errors='coerce')
    relevance_over_time = df.groupby('APPLICATION_DEADLINE')['RELEVANCE'].mean().reset_index()

    line_chart = alt.Chart(relevance_over_time).mark_line().encode(
        x='APPLICATION_DEADLINE:T',  # Time data
        y='RELEVANCE:Q'  # Quantitative data
    ).properties(width=600)
    st.altair_chart(line_chart)

    # Text om de mest frekventa yrkena
    st.write("### Mest förekommande yrken")
    common_jobs = df['OCCUPATION'].value_counts().head(5).reset_index(name='OCCUPATION_COUNT')
    st.write(f"De vanligaste jobben är: {', '.join(common_jobs['OCCUPATION'])}")
    
    # Tabell med detaljerad data
    st.write("### Detaljerad Jobbdata")
    st.dataframe(df)

if __name__ == "__main__":
    layout()