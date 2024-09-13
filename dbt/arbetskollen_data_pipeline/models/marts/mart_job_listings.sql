WITH fct_job_ads AS (
    SELECT * FROM {{ ref('fct_job_ads') }}
),

job_details AS (SELECT * FROM {{ ref('dim_job_details') }}),

employer AS (SELECT * FROM {{ ref('dim_employer') }})

SELECT
    e.employer_id,
    jd.occupation,
    jd.headline,
    jd.salary_description,
    jd.duration,
    e.employer_name,
    e.employer_workplace,
    f.relevance
FROM fct_job_ads AS f
LEFT JOIN job_details AS jd
    ON f.job_details_key = jd.job_details_id
LEFT JOIN employer AS e
    ON f.employer_key = e.employer_id



   