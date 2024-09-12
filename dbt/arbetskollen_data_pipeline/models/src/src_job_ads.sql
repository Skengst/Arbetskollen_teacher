{{
  config(
    materialized = 'ephemeral',
    )
}}

WITH stg_job_ads AS (
  SELECT * 
  FROM {{ source('job_ads_db', 'stg_teacher_ads') }}
)

SELECT 
    id,
    relevance,
    number_of_vacancies AS vacancies,
    publication_date,
    last_publication_date
FROM stg_job_ads