# Arbetskollen Data Pipeline Project

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

3. Set up connections to Snowflake and dbt by configuring profiles.yml and secrets.toml.

## Usage
Run the data extraction from Jobtech API and load it into Snowflake:
```bash
python data_pipeline/load_data.py
```
```bash
Run the dbt models:
```
```bash
dbt run
```
Start the dashboard using Streamlit:
```bash
streamlit run dashboard/app.py
```

## Agile Workflow
This project follows a Kanban methodology using GitHub Projects. Tasks are managed in smaller iterations, and we use pull requests to review and merge code.

## Contributing
Create a new branch for your feature:
```bash
git checkout -b feature/new-feature
```
Make frequent commits and create a pull request when you're done.
