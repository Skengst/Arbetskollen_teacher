import streamlit as st
import plotly.express as px
import pandas as pd
import altair as alt
from connect_data_warehouse import query_job_listings
from datetime import datetime, timedelta

st.set_page_config(layout="wide")

def layout():
    df = query_job_listings("""
        SELECT * FROM mart_job_listings
    """)
    df.fillna('Not Specified', inplace=True)
    df.columns = df.columns.str.upper()

    total_vacancies = df['VACANCIES'].sum()
    total_employers = df['EMPLOYER_NAME'].nunique()
    most_common_occupation = df['OCCUPATION'].mode()[0]
    
    st.title('Job Listings Dashboard')
    st.write("Denna dashboard ger en översikt över information för lediga lärartjänster från Arbetsförmedlingens API.")

    st.write("### KPI:er")
    col1, col2, col3 = st.columns(3)
    col1.metric("Totala lediga platser", total_vacancies)
    col2.metric("Totalt antal arbetsgivare", total_employers)
    col3.metric("Vanligaste yrket", most_common_occupation)

    st.markdown("### Lediga tjänster per yrke")
    df_vacancies_per_occupation = df.groupby('OCCUPATION').agg(total_vacancies=('VACANCIES', 'sum')).reset_index()
    df_vacancies_per_occupation = df_vacancies_per_occupation.sort_values(by='total_vacancies', ascending=False)
    st.dataframe(df_vacancies_per_occupation)

    st.markdown("### Vanligaste jobbannonserna")
    df_frequent_ads = df.groupby('HEADLINE').size().reset_index(name='headline_count')
    df_frequent_ads = df_frequent_ads.sort_values(by='headline_count', ascending=False).head(10)
    fig_frequent_ads = px.pie(df_frequent_ads, names='HEADLINE', values='headline_count')
    st.plotly_chart(fig_frequent_ads)

    st.markdown("### Fördelning av anställningens varaktighet")
    df_duration = df.groupby('DURATION').size().reset_index(name='job_count')
    fig_duration = px.bar(df_duration, x="DURATION", y="job_count")
    st.plotly_chart(fig_duration)

    today = datetime.now()
    two_months_later = today + timedelta(days=60)
    df['APPLICATION_DEADLINE'] = pd.to_datetime(df['APPLICATION_DEADLINE'], errors='coerce')
    df_filtered_deadlines = df[
        (df['APPLICATION_DEADLINE'] >= today) & 
        (df['APPLICATION_DEADLINE'] <= two_months_later)
    ]
    st.markdown("### Lediga tjänster efter ansökningsdeadline (nästa 2 månader)")
    df_deadlines = df_filtered_deadlines.groupby('APPLICATION_DEADLINE').size().reset_index(name='job_count')
    fig_deadlines = px.line(df_deadlines, x="APPLICATION_DEADLINE", y="job_count")
    st.plotly_chart(fig_deadlines)

    st.markdown("### Topp 5 arbetsgivare efter lediga tjänster")
    df_top5 = df.groupby('EMPLOYER_NAME').agg(vacancies=('VACANCIES', 'sum')).reset_index()
    df_top5 = df_top5.sort_values(by='vacancies', ascending=False).head(5)
    fig_top5 = px.bar(df_top5, x="EMPLOYER_NAME", y="vacancies", orientation='v')
    st.plotly_chart(fig_top5)

    st.markdown("## Hitta annons")
    cols = st.columns(2)
    with cols[0]:
        selected_company = st.selectbox(
            "Välj ett företag:", df["EMPLOYER_NAME"].unique()
        )
    with cols[1]:
        selected_headline = st.selectbox(
            "Välj en annons:",
            df[df["EMPLOYER_NAME"] == selected_company]["HEADLINE"].unique(),
        )

    st.markdown("### Jobbannons")
    job_description = df.query(
        "HEADLINE == @selected_headline and EMPLOYER_NAME == @selected_company"
    )["DESCRIPTION_FORMATTED"]
    
    if not job_description.empty:
        st.markdown(job_description.values[0], unsafe_allow_html=True)
    else:
        st.write("Ingen beskrivning tillgänglig för den valda annonsen.")

    with st.expander("Se fullständiga jobbannonser"):
        st.dataframe(df)

if __name__ == "__main__":
    layout()
