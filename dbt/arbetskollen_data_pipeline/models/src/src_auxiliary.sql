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
    experience_required,
    driving_license_required,
    access_to_own_car as car_required,

FROM stg_job_ads