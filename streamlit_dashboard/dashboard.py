import streamlit as st
import plotly.express as px
import pandas as pd
import altair as alt
from connect_data_warehouse import query_job_listings
from datetime import datetime, timedelta

# Set page configuration to wide mode
st.set_page_config(layout="wide")

def layout():
    df = query_job_listings()
    df.fillna('Not Specified', inplace=True)  # Fyller 'none' med 'Not Specified'
    
    # Konvertera alla kolumnnamn till versaler för enhetlighet
    df.columns = df.columns.str.upper()

    st.title('Job Listings Dashboard')
    st.write("Denna dashboard ger en översikt över information för lediga lärartjänster från Arbetsförmedlingens API.")

    # KPI cards
    total_vacancies = df['VACANCIES'].sum()
    total_employers = df['EMPLOYER_NAME'].nunique()
    most_common_occupation = df['OCCUPATION'].mode()[0]
    
    st.write("### KPI:er")
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Totala lediga platser", total_vacancies)
    col2.metric("Totalt antal arbetsgivare", total_employers)
    col3.metric("Vanligaste yrket", most_common_occupation)

    # Lediga tjänster per yrke
    cols = st.columns(2)
    with cols[0]:
        st.markdown("### Lediga tjänster per yrke")
        st.dataframe(query_job_listings("""  
            SELECT SUM(vacancies) AS total_vacancies, OCCUPATION
            FROM mart_job_listings
            GROUP BY OCCUPATION
            ORDER BY total_vacancies DESC;
        """))

    # Vanligaste jobbannonserna (Pie chart)
    st.markdown("### Vanligaste jobbannonserna")
    df_frequent_ads = query_job_listings("""  
        SELECT HEADLINE, COUNT(*) AS headline_count
        FROM mart_job_listings
        GROUP BY HEADLINE
        ORDER BY headline_count DESC
        LIMIT 10;
    """)
    df_frequent_ads.columns = ['HEADLINE', 'headline_count']  # Explicitly rename columns to match
    fig_frequent_ads = px.pie(df_frequent_ads, names='HEADLINE', values='headline_count')
    st.plotly_chart(fig_frequent_ads)

    # Employment Duration Distribution
    with cols[1]:
        st.markdown("### Fördelning av anställningens varaktighet")
        df_duration = query_job_listings("""  
            SELECT DURATION, COUNT(*) AS job_count
            FROM mart_job_listings
            GROUP BY DURATION;
        """)
        fig_duration = px.bar(df_duration, x="DURATION", y="JOB_COUNT")
        st.plotly_chart(fig_duration)

    # Filtrera för ansökningsdeadlines inom de kommande 2 månaderna
    today = datetime.now()
    two_months_later = today + timedelta(days=60)  # Ungefär 2 månader

    df['APPLICATION_DEADLINE'] = pd.to_datetime(df['APPLICATION_DEADLINE'], errors='coerce')
    df_filtered_deadlines = df[
        (df['APPLICATION_DEADLINE'] >= today) & 
        (df['APPLICATION_DEADLINE'] <= two_months_later)
    ]

    st.markdown("### Lediga tjänster efter ansökningsdeadline (nästa 2 månader)")
    df_deadlines = df_filtered_deadlines.groupby('APPLICATION_DEADLINE').size().reset_index(name='job_count')
    fig_deadlines = px.line(df_deadlines, x="APPLICATION_DEADLINE", y="job_count")
    st.plotly_chart(fig_deadlines)

    # Per company (top 5)
    st.markdown("### Topp 5 arbetsgivare efter lediga tjänster")
    df_top5 = query_job_listings("""  
        SELECT SUM(vacancies) AS vacancies, employer_name
        FROM mart_job_listings
        GROUP BY employer_name
        ORDER BY vacancies DESC
        LIMIT 5;
    """)
    df_top5.columns = ['vacancies', 'employer_name']  # Explicitly rename columns to match
    fig_top5 = px.bar(df_top5, x="employer_name", y="vacancies", orientation='v')
    st.plotly_chart(fig_top5)

    # Find advertisement
    st.markdown("## Hitta annons")
    cols = st.columns(2)
    with cols[0]:
        selected_company = st.selectbox(
            "Välj ett företag:", df["EMPLOYER_NAME"].unique()
        )

    with cols[1]:
        selected_headline = st.selectbox(
            "Välj en annons:",
            df.query("EMPLOYER_NAME == @selected_company")["HEADLINE"],
        )

    st.markdown("### Jobbannons")
    job_description = df.query(
        "HEADLINE == @selected_headline and EMPLOYER_NAME == @selected_company"
    )["DESCRIPTION_FORMATTED"]
    
    if not job_description.empty:
        st.markdown(job_description.values[0], unsafe_allow_html=True)
    else:
        st.write("Ingen beskrivning tillgänglig för den valda annonsen.")

    # Full job listings data (optional collapsible section)
    with st.expander("Se fullständiga jobbannonser"):
        st.dataframe(df)

if __name__ == "__main__":
    layout()
