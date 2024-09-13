WITH ja AS (SELECT * FROM {{ ref('src_job_ads') }}),

jd AS (SELECT * FROM {{ ref('src_job_details') }}),

e AS (SELECT * FROM {{ ref('src_employer') }}),

a AS (SELECT * FROM {{ ref('src_auxiliary') }})

SELECT 
    ja.id as job_id,
    {{dbt_utils.generate_surrogate_key(['jd.id', 'jd.headline'])}} as job_details_key,
    {{dbt_utils.generate_surrogate_key(['e.id', 'e.employer_name'])}} as employer_key,
    {{dbt_utils.generate_surrogate_key(['a.id', 'a.experience_required'])}} as auxiliary_attributes_key,
    {# TODO: key to junk dimension #}
    relevance,
    coalesce(vacancies, 1) as vacancies,
    publication_date,
    last_publication_date
FROM 
    ja 
LEFT JOIN 
    jd ON ja.id = jd.id
LEFT JOIN 
    e ON ja.id = e.id
LEFT JOIN
    a ON ja.id = a.id