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
    employer__name AS employer_name,
    employer__workplace AS workplace,
    employer__organization_number AS organization_number,
    employer__url AS url,
    workplace_address__street_address AS street_address,
    workplace_address__municipality AS municipality,
    workplace_address__region AS region,
    workplace_address__postcode AS postcode,
    workplace_address__city AS workplace_city,
    workplace_address__country AS country
FROM stg_job_ads
