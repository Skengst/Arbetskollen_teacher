import streamlit as st
from connect_data_warehouse import query_job_listings

def layout():
    df = query_job_listings()
    st.title('Job Listings Dashboard')
    st.write("This dashboard provides an overview of information for teaching job listings from Arbetsförmedlinges API")

# Bestämmer column space för de KPI nedan
    st.markdown("## Vacancies")
    cols = st.columns(2)

# Visar antal lediga platser
    with cols[0]:
        st.metric(label="Total",
        value=df["VACANCIES"].sum())

# Visar antal lediga tills vidare platser
    with cols[1]:
        st.metric(label="Tills vidare positions",
        value=df.query("DURATION == 'Tills vidare'")['VACANCIES'].sum())
        
# Bestämmer column space för de KPI nedan
    cols = st.columns(2)

# Visar i tabell lediga platser per titel
    with cols[0]:
        st.markdown("### Vacancies by Occupation")
        st.dataframe(
            query_job_listings(
                """
                    SELECT
                        SUM(vacancies) as total_vacancies,
                        OCCUPATION
                        
                    FROM 
                        mart_job_listings
                    GROUP BY 
                        OCCUPATION
                    ORDER BY total_vacancies DESC;
                    """
            )
        )
# Display top 5 employer name in bar chart
    with cols[1]:
        st.markdown("### Per company (top 5)")
        st.bar_chart(
            query_job_listings(
                """
                    SELECT 
                        SUM(vacancies) as vacancies,
                        employer_name
                    FROM 
                        mart_job_listings
                    GROUP BY 
                        employer_name
                    ORDER BY vacancies DESC LIMIT 5;
                    """
            ),
            x="EMPLOYER_NAME",
            y="VACANCIES",
        )
    
# Adds title
    st.markdown("## Find advertisement")

# Adds dtop down meny to filter by employer 
    cols = st.columns(2)
    with cols[0]:
        selected_company = st.selectbox(
            "Select a company:", df["EMPLOYER_NAME"].unique()
        )

# Adds another drop down menu to filter
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

    st.markdown("## Job listings data")
    st.dataframe(df)
    
if __name__ == "__main__":
    layout()