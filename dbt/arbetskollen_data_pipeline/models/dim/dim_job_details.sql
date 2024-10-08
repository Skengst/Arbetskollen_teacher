WITH src_job_details AS (SELECT * FROM {{ ref('src_job_details') }}) -- it is the upstream for dimention job details.

{# TODO: fill nulls #}

SELECT 
   {{ dbt_utils.generate_surrogate_key(['id','headline']) }} AS job_details_id,
    occupation,
    headline,
    description,
    description_formatted,
    employment_type,
    coalesce(duration, 'No duration') as duration,
    coalesce(working_hours_type, 'Not specified') as working_hours_type,
    salary_type,
    coalesce(salary_description, 'No salary description') as salary_description,
    scope_of_work_min,
    scope_of_work_max

FROM SRC_JOB_DETAILS

