import streamlit as st
import pandas as pd
import altair as alt
from connect_data_warehouse import query_job_listings

def layout():
    st.set_page_config(layout="wide")
    st.subheader('Job Listings Dashboard')

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
    df['APPLICATION_DEADLINE'] = pd.to_datetime(df['APPLICATION_DEADLINE'], errors='coerce')
    relevance_over_time = df.groupby('APPLICATION_DEADLINE')['RELEVANCE'].mean().reset_index()
    common_jobs = df['OCCUPATION'].value_counts().head(3).reset_index(name='OCCUPATION_COUNT')
    common_jobs.rename(columns={'index': 'OCCUPATION'}, inplace=True)
    # Uppdaterade KPI:er
    permanent_jobs = df[df['DURATION'].str.contains('tills vidare', case=False, na=False)].shape[0]
    temporary_jobs = df[~df['DURATION'].str.contains('tills vidare', case=False, na=False)].shape[0]
    high_relevance_jobs = df[df['RELEVANCE'] > 0.9].shape[0]
    relevance_percentage = (high_relevance_jobs / total_jobs) * 100
    upcoming_deadlines = df[df['APPLICATION_DEADLINE'] <= pd.Timestamp.today() + pd.Timedelta(weeks=1)].shape[0]
    jobs_per_city = df.groupby('WORKPLACE_CITY').size().reset_index(name='ANTAL_JOBB').sort_values(by='ANTAL_JOBB', ascending=False)

    # KPI-sektion
    st.write("### KPI:er")
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Totala jobb", total_jobs)
    col2.metric("Totala lediga platser", total_vacancies)
    col3.metric("Vanligaste yrket", most_common_occupation)

    col1, col2, col3 = st.columns(3)

    col1.metric("Jobb med fast anställning", permanent_jobs)
    col2.metric("Jobb med tidsbegränsad anställning", temporary_jobs)
    col3.metric("Jobb med hög relevans", f"{relevance_percentage:.2f}%")

    # Data för topp 3 vanligaste yrken

    col1, = st.columns(1)

    # Visa en KPI för snart utgående ansökningstider i col1
    col1.metric("Snart utgående ansökningstider (inom 1 vecka)", upcoming_deadlines)

    # Skapa ett stapeldiagram för topp 3 vanligaste yrken i col2

    st.write("### Topp 3 vanligaste yrken")
    bar_chart = alt.Chart(common_jobs).mark_bar().encode(
        x=alt.X('OCCUPATION:N', title='Yrke'),
        y=alt.Y('OCCUPATION_COUNT:Q', title='Antal Lediga Jobb'),
        color='OCCUPATION:N',
        tooltip=['OCCUPATION', 'OCCUPATION_COUNT']
    ).properties(title="Antal Lediga Jobb per Yrke (Topp 3)")
    
    st.altair_chart(bar_chart, use_container_width=True)

    # Diagramsektion
    st.write("### Diagram")

    # 1. Diagram över antal jobb per yrke
    job_chart = alt.Chart(job_per_occupation).mark_bar().encode(
        x=alt.X('TOTAL_VACANCIES:Q', title='Antal Lediga Platser'),
        y=alt.Y('OCCUPATION:N', sort='-x', title='Yrke'),
        color='TOTAL_VACANCIES:Q',
        tooltip=['OCCUPATION', 'TOTAL_VACANCIES']
    ).properties(title="Antal Jobb per Yrke")
    st.altair_chart(job_chart, use_container_width=True)

    # 2. Diagram över antal jobb per arbetsgivare
    top_10_employers = job_per_employer.sort_values(by='ANTAL_JOBB', ascending=False).head(10)

    # Skapa diagrammet med topp 10 arbetsgivare
    employer_chart = alt.Chart(top_10_employers).mark_bar().encode(
        x=alt.X('ANTAL_JOBB:Q', title='Antal Jobb'),
        y=alt.Y('EMPLOYER_NAME:N', sort='-x', title='Arbetsgivare'),
        color='ANTAL_JOBB:Q',
        tooltip=['EMPLOYER_NAME', 'ANTAL_JOBB']
    ).properties(title="Antal Jobb per Arbetsgivare (Topp 10)")
    st.altair_chart(employer_chart, use_container_width=True)

    # 3. Diagram över relevans över tid
    relevance_chart = alt.Chart(relevance_over_time).mark_line().encode(
        x=alt.X('APPLICATION_DEADLINE:T', title='Ansökningsdeadline'),
        y=alt.Y('RELEVANCE:Q', title='Relevans'),
        tooltip=['APPLICATION_DEADLINE', 'RELEVANCE']
    ).properties(title="Relevans över Tid")
    st.altair_chart(relevance_chart, use_container_width=True)

    # 4. Stapeldiagram över jobb per stad
# Filtrera bort poster där WORKPLACE_CITY är "Ej specificerat" eller NaN
    jobs_per_city_filtered = jobs_per_city[(jobs_per_city['WORKPLACE_CITY'] != 'Ej specificerat') & (jobs_per_city['WORKPLACE_CITY'].notna())]

    # Skapa diagrammet med filtrerade städer
    city_chart = alt.Chart(jobs_per_city_filtered).mark_bar().encode(
        x=alt.X('ANTAL_JOBB:Q', title='Antal Jobb'),
        y=alt.Y('WORKPLACE_CITY:N', sort='-x', title='Stad'),
        color='ANTAL_JOBB:Q',
        tooltip=['WORKPLACE_CITY', 'ANTAL_JOBB']
    ).properties(title="Antal Jobb per Stad")
    st.altair_chart(city_chart, use_container_width=True)



    # Tabell med detaljerad data
    st.write("### Detaljerad Jobbdata")
    st.dataframe(df)

if __name__ == "__main__":
    layout()
