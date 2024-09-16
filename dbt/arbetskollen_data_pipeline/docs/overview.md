{% docs __overview__ %}

# Job Ad Project

This project is part of the Arbetskollen initiative, which aims to build a data pipeline for visualizing job ad statistics. The main purpose is to help students and job seekers navigate the job market and make informed decisions about education and career paths.

> [!NOTE]
> The project employs the modern data stack and involves the entire process of setting up a pipeline, transforming data, and visualizing it on a dashboard.

## Project Objective

The aim of the project is to implement a modern data pipeline using various technologies to solve a real-world problem. It includes setting up Snowflake as a data warehouse, applying dimensional modeling, and creating a dashboard to visualize job ad data.

## Key Features

- **Data Extraction**: Extract data from jobtech's API and load it into Snowflake.
- **Dimensional Modeling**: Improve on an initial dimensional model created by a previous data engineer. The model includes tables such as `dim_employer`, `dim_job_details`, and `dim_auxiliary`.
- **Data Transformation**: Use dbt to apply transformations according to the dimensions model.
- **Testing**: Implement thorough data tests in dbt to ensure data quality.
- **Visualization**: Create a user-friendly dashboard that provides insights into job statistics for various occupations.
  
## Dimensional Model 

![dimensional model](assets/dimension_model.png)

![Assignment](assets/projectpm.pdf)

## What is dbt?
[What is dbt?](what_is_dbt.md)

This diagram represents the star schema for the job ad data model. It includes dimensions like `employer`, `job_details`, and `auxiliary` with a fact table for `job_ads`.

## Agile Methodology

We follow a Kanban approach with continuous refinement of the backlog. The team works on one task at a time, ensuring smooth collaboration and incremental progress.

## Technologies Used

- **DLT**: For loading all raw data into our warehouse
- **Snowflake**: For storing and managing data.
- **DBT**: For transformations and data testing.
- **Git & GitHub**: For version control and team collaboration.
- **Streamlit**: For building the final dashboard to display job statistics.

{% enddocs %}