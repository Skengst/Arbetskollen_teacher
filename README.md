# Arbetskollen Data Pipeline Project

https://qe50964.west-europe.azure.snowflakecomputing.com/

## Project Description
This project aims to implement a modern data stack to support the visualization of job listings through a dashboard. The system is designed to help students and job seekers find relevant occupations and study fields based on the current job market.

## Technologies and Tools
- **Snowflake**: Used for data storage and management.
- **dlt**: 
- **dbt**: Used for data transformations.
- **Git and GitHub**: Version control and collaboration within the team.
- **Streamlit**: Used to create the dashboard.
- **Jobtech API**: Source of job listings data.

## Project Structure
- **data_pipeline/**: Contains scripts to extract, load, and transform data from the Jobtech API into Snowflake.
- **dlt_project/**:
- **dbt_project/**: Contains data models and transformations.
- **dashboard/**: Code for data visualization using Streamlit.
- **tests/**: Contains tests for data transformations and modeling.

## Installation
1. Clone this repository:
```bash
git clone https://github.com/Skengst/Arbetskollen_teacher.git
```
   
2. Install the necessary packages:
```bash
pip install -r requirements.txt
```

3. Set up connections to Snowflake,dlt and dbt by configuring profiles.yml and secrets.toml.

## Usage
Run the data extraction from Jobtech API and load it into Snowflake:
```bash
python dlt/arbetskollen_stagin.py
```
Go into the dbt folder: cd dbt/arbetskollen_data_pipeline
```bash
cd dbt/arbetskollen_data_pipeline
```
```bash
dbt deps
```
```bash
dbt run
```
You can then try the tests:
```bash
dbt tests
```
You can then look into the documentation:
```bash
dbt docs generate
```
```bash
dbt docs serve
```

Start the dashboard using Streamlit:
You have to set up youre .env file.
then run:
```bash
python streamlit_dashboard/run_dashboard.py
```

## Agile Workflow
This project follows a Kanban methodology using GitHub Projects. Tasks are managed in smaller iterations, and we use pull requests to review and merge code.