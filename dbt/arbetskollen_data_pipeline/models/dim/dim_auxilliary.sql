WITH src_auxilliary AS (SELECT * FROM {{ref('src_auxilliary')}})

SELECT 
    {{ dbt_utils.generate_surrogate_key(['id','experience_required'])}} AS auxilliary_attributes_id,
    experience_required,
    driving_license_required,
    car_required,

FROM src_auxilliary