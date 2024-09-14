import streamlit as st
import plotly.express as px
from connect_data_warehouse import query_job_listings

def layout():
    df = query_job_listings()
    df.fillna('Not Specified', inplace=True)  # Fyller 'none' med 'Not Specified'

    st.title('Job Listings Dashboard')
    st.write("This dashboard provides an overview of information for teaching job listings from Arbetsförmedlinges API")

    # Vacancies KPI
    st.markdown("## Vacancies")
    cols = st.columns(2)
    with cols[0]:
        st.metric(label="Total Vacancies", value=df["VACANCIES"].sum())
    with cols[1]:
        st.metric(label="Tills vidare positions", value=df.query("DURATION == 'Tills vidare'")['VACANCIES'].sum())

    # Vacancies by Occupation
    cols = st.columns(2)
    with cols[0]:
        st.markdown("### Vacancies by Occupation")
        st.dataframe(query_job_listings("""
            SELECT SUM(vacancies) AS total_vacancies, OCCUPATION
            FROM mart_job_listings
            GROUP BY OCCUPATION
            ORDER BY total_vacancies DESC;
        """))

    # Salary Description per Occupation
    with cols[1]:
        st.markdown("### Salary Description per Occupation")
        st.dataframe(query_job_listings("""
            SELECT OCCUPATION, SALARY_DESCRIPTION, SALARY_TYPE
            FROM mart_job_listings;
        """))

    # Employment Duration Distribution
    cols = st.columns(2)
    with cols[0]:
        st.markdown("### Employment Duration Distribution")
        df_duration = query_job_listings("""
            SELECT DURATION, COUNT(*) AS job_count
            FROM mart_job_listings
            GROUP BY DURATION;
        """)
        fig_duration = px.bar(df_duration, x="DURATION", y="JOB_COUNT", title="Employment Duration Distribution")
        st.plotly_chart(fig_duration)

    # Scope of Work per Occupation
    with cols[1]:
        st.markdown("### Scope of Work per Occupation")
        st.dataframe(query_job_listings("""
            SELECT OCCUPATION, AVG(SCOPE_OF_WORK_MIN) AS min_work_hours, AVG(SCOPE_OF_WORK_MAX) AS max_work_hours
            FROM mart_job_listings
            GROUP BY OCCUPATION;
        """))

    # Job Listings by Application Deadline
    st.markdown("### Job Listings by Application Deadline")
    df_deadlines = query_job_listings("""
        SELECT APPLICATION_DEADLINE, COUNT(*) AS job_count
        FROM mart_job_listings
        GROUP BY APPLICATION_DEADLINE
        ORDER BY APPLICATION_DEADLINE ASC;
    """)
    fig_deadlines = px.line(df_deadlines, x="APPLICATION_DEADLINE", y="JOB_COUNT", title="Job Listings by Application Deadline")
    st.plotly_chart(fig_deadlines)

    # Relevance by Occupation
    cols = st.columns(2)
    with cols[0]:
        st.markdown("### Relevance by Occupation")
        df_relevance = query_job_listings("""
            SELECT OCCUPATION, AVG(RELEVANCE) AS avg_relevance
            FROM mart_job_listings
            GROUP BY OCCUPATION
            ORDER BY avg_relevance DESC;
        """)
        fig_relevance = px.bar(df_relevance, x="OCCUPATION", y="AVG_RELEVANCE", title="Relevance by Occupation")
        st.plotly_chart(fig_relevance)

    # Vacancies per Employer and Occupation
    with cols[1]:
        st.markdown("### Vacancies per Employer and Occupation")
        st.dataframe(query_job_listings("""
            SELECT EMPLOYER_NAME, OCCUPATION, SUM(VACANCIES) AS total_vacancies
            FROM mart_job_listings
            GROUP BY EMPLOYER_NAME, OCCUPATION
            ORDER BY total_vacancies DESC;
        """))

    # Most Frequent Job Ads (using treemap for top 10)
    st.markdown("### Most Frequent Job Ads")
    df_frequent_ads = query_job_listings("""
        SELECT HEADLINE, COUNT(*) AS headline_count
        FROM mart_job_listings
        GROUP BY HEADLINE
        ORDER BY headline_count DESC
        LIMIT 10;
    """)
    df_frequent_ads.columns = ['HEADLINE', 'headline_count']  # Explicitly rename columns to match
    fig_frequent_ads = px.treemap(df_frequent_ads, path=['HEADLINE'], values='headline_count', title="Most Frequent Job Ads")
    st.plotly_chart(fig_frequent_ads)

    # Per company (top 5)
    st.markdown("### Per company (top 5)")
    df_top5 = query_job_listings("""
        SELECT SUM(vacancies) AS vacancies, employer_name
        FROM mart_job_listings
        GROUP BY employer_name
        ORDER BY vacancies DESC
        LIMIT 5;
    """)
    df_top5.columns = ['vacancies', 'employer_name']  # Explicitly rename columns to match
    fig_top5 = px.bar(df_top5, x="employer_name", y="vacancies", title="Top 5 Employers by Vacancies", orientation='v')
    st.plotly_chart(fig_top5)

    # Find advertisement
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
    job_description = df.query(
        "HEADLINE == @selected_headline and EMPLOYER_NAME == @selected_company"
    )["DESCRIPTION_FORMATTED"]
    
    if not job_description.empty:
        st.markdown(job_description.values[0], unsafe_allow_html=True)
    else:
        st.write("No description available for the selected job ad.")

    # Full job listings data (optional collapsible section)
    with st.expander("See full job listings data"):
        st.dataframe(df)

if __name__ == "__main__":
    layout()
