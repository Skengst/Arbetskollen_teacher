{{
  config(
    materialized = 'ephemeral',
    )
}}

WITH stg_job_details AS (
  SELECT * 
  FROM {{ source('job_ads_db', 'stg_teacher_ads') }}
)

SELECT
    id,
    occupation__label AS occupation,
    headline,
    description__text AS description,
    description__text_formatted AS description_formatted,
    employment_type__label AS employment_type,
    duration__label AS duration,
    working_hours_type__label AS working_hours_type,
    salary_type__label AS salary_type,
    SALARY_DESCRIPTION AS salary_description,
    scope_of_work__min AS scope_of_work_min,
    scope_of_work__max AS scope_of_work_max
FROM stg_job_details